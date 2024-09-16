"""
This file can be run
cd <this directory>
PYTHONPATH=<base_dir> python3 <file_name>.py
"""
from datetime import datetime
import argparse
from zoneinfo import ZoneInfo

import pytz
from bson import ObjectId
from pytz import utc
from sqlalchemy import and_, asc, or_
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError
from sqlalchemy.orm import load_only

from app import create_app, db
from enums.api_endpoint_types import APIEndpointTypes
from extensions_mongo import fs_mongo
from extensions_proxies import http_pass_codes
from extensions_string import clean_unknown_characters
from models.mariadb.api_endpoints import APIEndpoint
from models.mariadb.database_timegraph import DatabaseTimegraph
from models.mariadb.mongo_storage import MongoStorage
from routines.parsing.apply_link import get_apply_link
from routines.parsing.conversions import convert_bytes_to_dict_raw
from routines.parsing.job_title import get_job_titles
from routines.parsing.times import get_times

scrape_endpoints_type_list = [
    db.cast(APIEndpointTypes.JOBS_SEARCH.value, TINYINT()),
    db.cast(APIEndpointTypes.JOBS_FEED.value, TINYINT()),
    db.cast(APIEndpointTypes.JOB_DETAILS.value, TINYINT()),
]

endpoints_id_broken_list = []

days_to_process = 31

app = create_app()


def populate_broken_endpoint_list(database_app):
    return [broken_endpoint[0] for broken_endpoint in (
        database_app.session.query(APIEndpoint.id)
        .filter(
            or_(
                and_(
                    APIEndpoint.nice_name == "/api/v2/Jobs/Latest",
                    APIEndpoint.http_path ==
                    "https://job-postings1.p.rapidapi.com/",
                ),
                and_(
                    APIEndpoint.nice_name == "httpsJobapiCoUkGet",
                    APIEndpoint.http_path ==
                    "https://zambian-jobs-api1.p.rapidapi.com/getdataNew.php",
                )
            )
        ).all()
    )]


def get_processed_query_list(
        endpoint_types_list: list,
        database_app,
        date_filter: datetime = None):
    """
    Refreshes Processed Query List
     matching allowed scrape endpoints only

     mongo storage columns: endpoint_nice_name, url
     endpoint columns: nice_name, http_path
    """
    result = (
        database_app.session.query(MongoStorage)
        .filter(
            and_(
                MongoStorage.code.in_(http_pass_codes),
                MongoStorage.object_id.is_not(None),
                MongoStorage.query_time.is_not(None),
                MongoStorage.length.is_not(None),
                MongoStorage.data_truncated.is_not(None),
                (MongoStorage.query_time > date_filter
                 if date_filter is not None else True),
            )
        )
        .order_by(asc(MongoStorage.query_time))
        .options(
            load_only(
                MongoStorage.id,
                MongoStorage.object_id,
                MongoStorage.endpoint_nice_name,
                MongoStorage.input_json,
                MongoStorage.url,
            )
        )
        .all()
    )

    final_list = []

    for mongo_stor in result:
        for endpoint_ in endpoint_types_list:
            if (endpoint_.nice_name == mongo_stor.endpoint_nice_name and
                    endpoint_.http_path == mongo_stor.url):
                # print("adding " + endpoint_.nice_name +
                #       "(" + endpoint_.http_path + ")", flush=True)

                final_list.append(mongo_stor)

    return final_list


def get_scrape_endpoint_filtered_types(database_app):
    """
    Retrieve full APIEndpoint List to pull
    URL and Nice_Name details for jobs that can be scraped.
    """
    return (
        database_app.session.query(APIEndpoint)
        .filter(
            and_(
                APIEndpoint.type__.in_(scrape_endpoints_type_list),
                APIEndpoint.id.not_in(endpoints_id_broken_list),
                APIEndpoint.disabled == 0
            )
        )
        .all()
    )


def utc_midnight_x_days_ago(x):
    target_date = datetime.datetime.now(pytz.utc) - datetime.timedelta(days=x)
    return datetime.datetime(year=target_date.year, month=target_date.month,
                             day=target_date.day, tzinfo=pytz.utc).date()


# Parse Arguments
parser = argparse.ArgumentParser(
    description="Accept DateTime String as format "
                "(%a, %d %b %Y %H:%M:%S.%f %Z)")

parser.add_argument(
    '--date',
    type=str,
    help="Datetime of query time to start scan from"
)

args = parser.parse_args()
# print("Original: " +
#       progress_timestamp)
# print("Date Argument: " +
#       (args.date if args.date is not None else 'None'))

progress_timestamp = "earliest"

if (args.date is not None and
        isinstance(args.date, str) and
        len(args.date) > 0):
    if args.date == "earliest":
        progress_timestamp = ""
        latest_date_time = datetime.min

    else:
        progress_timestamp = args.date
        latest_date_time = datetime.strptime(
            args.date,
            "%a, %d %b %Y %H:%M:%S.%f %Z"
        )
else:
    if progress_timestamp == "earliest":
        progress_timestamp = ""
        from datetime import datetime
        latest_date_time = datetime.min
    else:
        latest_date_time = datetime.strptime(
            progress_timestamp,
            "%a, %d %b %Y %H:%M:%S.%f %Z"
        )
# raise ValueError(progress_timestamp)


with (app.app_context()):
    # Performance check
    import time
    start_time = time.time()
    try:
        # populate ID's for broken endpoints
        endpoints_id_broken_list: list = populate_broken_endpoint_list(db)

        # Grab all queries
        processed_queries: list = get_processed_query_list(
            endpoint_types_list=(
                get_scrape_endpoint_filtered_types(database_app=db)),
            # date_filter=None,
            database_app=db
        )

        # Enable debug parse for an ID
        # debug_test_parse_id = 2385
        debug_test_parse_id = -1

        if debug_test_parse_id != -1:
            print("Debugging specified ID and stopping. " +
                  str(debug_test_parse_id))

        new_new_jobs = {}
        earliest_day = datetime.min
        for query in processed_queries:
            # Debug Test Parsing
            if (debug_test_parse_id != -1 and
                    query.id != debug_test_parse_id):
                continue

            print("ID: " + str(query.id) + " " +
                  "URL: " + query.url + " (" +
                  query.endpoint_nice_name +
                  ")", flush=True)

            import datetime
            new_jobs = {}
            if earliest_day == datetime.datetime.min:
                earliest_day = query.query_time.replace(tzinfo=pytz.UTC).date()

            elif (query.query_time.replace(tzinfo=pytz.UTC).date() <
                  earliest_day):
                earliest_day = query.query_time.replace(tzinfo=pytz.UTC).date()
            # Process based on scrape time
            # Check per day which jobs have expired

            # if (latest_date_time.replace(tzinfo=pytz.UTC) <
            #         query.query_time.replace(tzinfo=pytz.UTC)):
            #     test_string = (
            #         query.query_time
            #         .replace(tzinfo=pytz.UTC)
            #         .strftime("%a, %d %b %Y %H:%M:%S.%f %Z"))
            #     if not test_string.endswith("UTC"):
            #         test_string += "UTC"
            #     # print("Reset current timestamp to " +
            #     #       test_string,
            #     #       flush=True)
            #     latest_date_time = query.query_time.replace(tzinfo=pytz.UTC)

            new_dict: dict = convert_bytes_to_dict_raw(
                fs_mongo.get(file_id=ObjectId(query.object_id))
                .read().decode()
            )

            # Fix for special error code
            if ('code' in new_dict.keys() and
                    'message' in new_dict.keys() and
                    new_dict.get('code') == "57014"):
                continue

            if not new_dict:
                continue

            names: dict = get_job_titles(
                api_url=query.url,
                nice_name=query.endpoint_nice_name,
                dict_new=new_dict,
                input_json=query.input_json,
            )
            if not names:
                print("Empty Job Titles")

            apply_links: dict = get_apply_link(
                api_url=query.url,
                nice_name=query.endpoint_nice_name,
                dict_new=new_dict,
                input_json=query.input_json,
            )
            if not apply_links:
                print("Empty Apply Links")

            times: dict = get_times(
                api_url=query.url,
                nice_name=query.endpoint_nice_name,
                dict_new=new_dict,
                input_json=query.input_json,
                query_time=query.query_time
            )
            if not times:
                print("Empty Times")

            # Add names to dictionary
            for i in names.keys():
                if "error" in i.lower():
                    # print("No names for ID: " + str(query.id) + " " +
                    #       query.endpoint_nice_name, flush=True)
                    for j in new_dict.keys():
                        if "error" in str(j).lower():
                            break
                        # new_jobs[j + query.api]['name'] = None
                    break

                # Initialize
                if i + query.api not in new_jobs.keys():
                    new_jobs[i + query.api] = {}

                names[i] = clean_unknown_characters(names[i])

                if (isinstance(names[i], str) and
                        len(names[i]) > 2):
                    new_jobs[i + query.api]['name'] = " "
                else:
                    new_jobs[i + query.api]['name'] = None

            for i in apply_links.keys():
                if "error" in i.lower():
                    # print("No apply links for ID: " + str(query.id) + " " +
                    #       str(query.endpoint_nice_name), flush=True)
                    for j in new_dict.keys():
                        if "error" in str(j).lower():
                            new_jobs.pop(i + query.api, None)
                            break
                        # new_jobs[str(j)]['apply_links'] = None
                    break

                if isinstance(apply_links[i], str):
                    apply_links[i] = [apply_links[i]]

                test_apply_link = None
                if len(apply_links[i]) != 0:
                    test_apply_link = clean_unknown_characters(
                        apply_links[i][0])

                    if (isinstance(test_apply_link, str) and
                            len(test_apply_link) > 2):
                        new_jobs[i + query.api]['apply_links'] = " "
                else:
                    new_jobs[i + query.api]['apply_links'] = None

            # print("ID: " + str(query.id) + " " +
            #       "URL: " + query.url + " (" +
            #       query.endpoint_nice_name +
            #       ")", flush=True)

            for i in times.keys():
                if "error" in i.lower():
                    # print("No times for ID: " + str(query.id) + " " +
                    #       str(query.endpoint_nice_name), flush=True)
                    for j in new_dict.keys():
                        if "error" in str(j).lower():
                            new_jobs.pop(i + query.api, None)
                            break
                    break

                if not isinstance(times[i], dict):
                    print("times[i] = " + str(times[i]) +
                          " key: " + i, flush=True)
                    raise ValueError("Fix this")

                # Compare
                if i + query.api in new_jobs.keys():
                    if (new_jobs[i + query.api].get('times') is None or
                            new_jobs[i + query.api]['times']
                            .get('expiration_time_utc') <
                            times[i].get('expiration_time_utc')):
                        new_jobs[i + query.api]['times'] = times[i]
                else:
                    pass

            for i in new_jobs.keys():
                if (new_jobs[i].get('name') != " " or
                    new_jobs[i].get('apply_links') != " " or
                    not isinstance(new_jobs[i].get('times'), dict) or
                        'expiration_time_utc' not in new_jobs[i].get('times')):
                    continue
                # 0 - query_time, 1 - expiration_time_utc
                new_new_jobs[i] = (
                    (query.query_time.replace(tzinfo=pytz.UTC).date(),
                     new_jobs[i].get('times').get('expiration_time_utc')
                     .replace(tzinfo=pytz.UTC).date())
                )

            if (debug_test_parse_id != -1 and
                    query.id == debug_test_parse_id):
                raise ReferenceError("Debug Test Parse")

        counted_jobs = []

        # print("Count unique key jobs: " + str(len(new_new_jobs)))

        # Removed duplicates
        for i in new_new_jobs.keys():
            if not isinstance(new_new_jobs[i], tuple):
                continue
            # 0 - query time, 1 - expiration time
            counted_jobs.append(
                (new_new_jobs[i][0],
                 new_new_jobs[i][1])
            )

        # counted_accumulative = {}
        # last_index = -1
        # for i in range(len(counted_jobs)):
        #     if i <= last_index:
        #         continue
        #
        #     index = i + 1
        #     current_day = counted_jobs[i][0]
        #     counted = 0
        #     while (index < len(counted_jobs) and
        #            counted_jobs[i][0] == counted_jobs[index][0]):
        #         counted += 1
        #         index += 1
        #     last_index = index - 1
        #     if current_day in counted_accumulative:
        #         counted_accumulative[current_day] += counted
        #     else:
        #         counted_accumulative[current_day] = counted
        import datetime
        if earliest_day == datetime.datetime.min:
            earliest_day = min(j[0] for j in counted_jobs)

        tracked_dates = [
            utc_midnight_x_days_ago(i)
            for i in range(
                min(
                    days_to_process,
                    (datetime.datetime.now().replace(tzinfo=pytz.UTC).date() -
                     earliest_day).days + 1)
            )
        ]

        # print("Tracked Dates")
        # for i in tracked_dates:
        #     print(str(i))

        # print(str(tracked_dates))

        counted_expired = {}
        counted_active = {}
        counted_total = {}
        for i in tracked_dates:
            counted_expired[i] = 0
            counted_active[i] = 0
            counted_total[i] = 0
            # Count sum for current query day
            # Job was queried on or before query day
            # Job[1] is expired

            # j[1]: Expiration Date
            # i: tracked day - j[0] must be less than or equal to i
            # j[0]: Query Date
            # j[0] >= i
            for j in [k for k in counted_jobs if k[0] <= i]:
                counted_total[i] += 1
                if i >= j[1]:
                    counted_expired[i] += 1
                else:
                    counted_active[i] += 1

            print("Expired: " + str(counted_expired[i]))
            print("Active: " + str(counted_active[i]))
            print("Total: " + str(counted_active[i] + counted_expired[i]))

        final = {
            i: {
                'active': counted_active[i],
                'expired': counted_expired[i],
                'total': counted_active[i] + counted_expired[i],
            } for i in set(counted_active.keys())
        }

        print("-- Total --")
        for i in sorted(final.keys()):
            print(str(i) + ": " + str(final[i]))
        #
        # print("-- Active --")
        # for i in sorted(counted_active.keys()):
        #     print(str(counted_active[i]) + ",")
        #
        # print("-- Expired --")
        # for i in sorted(counted_expired.keys()):
        #     print(str(counted_expired[i]) + ",")
        #
        # print("-- Keys --")
        # for i in sorted(counted_expired.keys()):
        #     print('"' + str(i) + '",')

        # print(str(final))
        database_timegraph = db.session.query(DatabaseTimegraph).all()
        for i in final.keys():
            if not any(j.time.date() == i for j in database_timegraph):
                db.session.add(
                    DatabaseTimegraph(
                        time=i,
                        total=final[i]['total'],
                        active=final[i]['active'],
                        expired=final[i]['expired'],
                    )
                )
                db.session.commit()
                print("Added Time: " + str(i))
            else:
                current_timegraph = [j for j in database_timegraph
                                     if j.time.date() == i][0]

                if (int(current_timegraph.total) !=
                        int(final[i].get('expired')) or
                        int(current_timegraph.total) !=
                        int(final[i].get('active')) or
                        int(current_timegraph.total) !=
                        int(final[i].get('total'))):
                    current_timegraph.verified = True

                if int(current_timegraph.total) != int(final[i].get('total')):
                    current_timegraph.total = int(final[i].get('total'))

                if int(current_timegraph.total) != int(final[i].get('active')):
                    current_timegraph.active = int(final[i].get('active'))

                if int(current_timegraph.total) != int(final[i].get('expired')):
                    current_timegraph.expired = int(final[i].get('expired'))

                db.session.commit()
                print("Updated Time: " + str(i))

        print("Processed "
              f"({((time.time() - start_time) * 1000):.6g} ms)",
              flush=True)

        # if (latest_date_time
        #         .replace(tzinfo=pytz.UTC)
        #         .strftime("%a, %d %b %Y %H:%M:%S.%f %Z") !=
        #         progress_timestamp):
        #
        #     print("Reset current timestamp to " +
        #           latest_date_time
        #           .replace(tzinfo=pytz.UTC)
        #           .strftime("%a, %d %b %Y %H:%M:%S.%f %Z"),
        #           flush=True)
        #
        #     print(progress_timestamp + " vs. " +
        #           latest_date_time
        #           .replace(tzinfo=pytz.UTC)
        #           .strftime("%a, %d %b %Y %H:%M:%S.%f %Z"),
        #           flush=True)
        #     raise ChildProcessError(
        #         "Completed"
        #         ". Latest DateTime: [[" +
        #         latest_date_time
        #         .replace(tzinfo=pytz.UTC)
        #         .strftime("%a, %d %b %Y %H:%M:%S.%f %Z") + "]]"
        #     )

        raise ChildProcessError("Count Completed")

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.rollback()
        db.session.close()
        print(f"IntegrityError: {e}", flush=True)
        raise e

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.rollback()
        db.session.close()
        print(f"OperationalError: {e}", flush=True)
        raise e

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.rollback()
        db.session.close()
        print(f"SQLAlchemyError: {e}", flush=True)
        raise e

    # Handler Process error for jobs processed successfully.
    except ChildProcessError as e:
        if 'Count Completed' not in str(e):
            db.session.rollback()
        db.session.close()
        raise e

    # Other Errors
    except Exception as e:
        db.session.rollback()
        db.session.close()
        print(f"Error: {e}", flush=True)
        raise e
