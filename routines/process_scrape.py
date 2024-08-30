"""
This file can be run
cd <this directory>
PYTHONPATH=<base_dir> python3 <file_name>.py
"""
import argparse
import random
from datetime import datetime, UTC
import time
from time import sleep
from urllib.parse import urlparse

from bson import ObjectId
import requests
from requests.auth import HTTPBasicAuth
from sqlalchemy import and_, asc, or_, exists
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import load_only
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError

from app import create_app, db
from enums.api_endpoint_types import APIEndpointTypes
from extensions_mongo import fs_mongo, fs_upload
from extensions_sql import get_session
from extensions_proxies import (
    http_pass_codes,
    preferred_residential_proxy_type_list,
    proxy_type_prefix_dict
)
from extensions_scrape_rate_limits import calculate_next_scrape_rate_limit
from extensions_user_agents import user_agent_list
from models.mariadb.api_endpoints import APIEndpoint
from models.mariadb.mongo_scrape_storage import MongoScrapeStorage
from models.mariadb.mongo_storage import MongoStorage
from models.mariadb.proxies import Proxy
from models.mariadb.scrape_rate_limit import ScrapeRateLimits
from extensions_undetected_chromedriver import (
    uc_chromium_pull_page,
    destroy_chromium_process,
    cleanup_temp_profile_data,
    destroy_display
)
from routines.parsing.apply_link import get_apply_link
from routines.parsing.conversions import convert_bytes_to_dict_raw
from xvfbwrapper import Xvfb

zombie_process_limit: int = 150

scrape_endpoints_type_list: list = [
    db.cast(APIEndpointTypes.JOBS_SEARCH.value, TINYINT()),
    db.cast(APIEndpointTypes.JOBS_FEED.value, TINYINT()),
    db.cast(APIEndpointTypes.JOB_DETAILS.value, TINYINT()),
]


scrape_endpoints_id_broken_list: list = []

scrape_apply_link_fail_messages: list = [
    'Query was not processed',
    'Search query failed',
]

# Website list can be queried with higher quality residential proxies.
restricted_sites = [
    'geoffreypugen.com',
    'forensic.jobs',
    'aviation.careers',
    'mikegoldby.com',
    'darwinrecruitment.ch',
    'darwinrecruitment.de',
    'darwinrecruitment.com',
    'darwinrecruitment.us',
    'darwinrecruitment.org',
    'darwinrecruitment.no',
    'darwinrecruitment.se',
    'hospitalityjobs.com',

    # Site does not exist (404 page)
    'musictechart.com',

    # Site does not exist (404 page)
    'newyorkjobscentral.com',

    # Site does not exist (404 page)
    'hiringrecruits.com',

    # Site does not exist
    'texasjobsmarket.com',

    # Sites does not exist
    # subdomain (cs.lkqd.net)
    'lkqd.net',

    # Sites does not exist
    # subdomain (usermatch.krxd.net)
    'krxd.net',

    # Sites does not exist
    # subdomain (oasc14008.247realmedia.com)
    '247realmedia.com',

    # Sites does not exist
    'jobinny.com',

    # Site does not exist
    # Subdomain included
    #'dfyemio1vslq8.cloudfront.net',
]

faulty_sites = [
    # Points to PDF file which contains no JS
    "https://www.indeed.com/rc/clk?jk=719ffd89d1488184",
    # Empty 0 length web page
    "https://www.communitycollegejobs.com/jobdetail-243540-faculty-astronomy",
    # Site Error
    "https://jobstinger.com/Illinois/arlingtonheights/etc/"
    "vacancy-site_52082650.html",

    # 0 Length
    "https://skyebackpackers.com/job-listing/job/first-miami-presbyterian-"
    "church-minister-of-children-at-ministry-architects-florida-WStPbGhYbU01Rkd"
    "RQlJ3a0k3R3ZhTm5z",

    "https://www.communitycollegejobs.com/jobdetail-244745-library-assistant",

    "https://www.communitycollegejobs.com/jobdetail-261160-library-assistant",

    "https://skyebackpackers.com/job-listing/job/iacp-certified-auto-appraiser"
    "-insurance-adjuster-real-estate-property-appraiser-at-roy-bent-kingdom-inc"
    "-dba-houston-auto-appraisers-baytown-tx-Yk9hbWdIbU00RitVQlIwbklyK2piTjNtU2"
    "c9PQ==",

    # Refused to connect
    "https://campstreetclimbing.com/opportunity/job/search-engine-evaluator-at-"
    "appen-birmingham-al-ZHBpanVoSTRMelNXT3lMU0dPQlpkZU1ycEE9PQ==",

    # 0 Length
    "https://skyebackpackers.com/job-listing/job/search-engine-marketing-specia"
    "list-at-millers-inc-columbia-mo-WitXa2puNlA2MStVQnhrbExiS2phOXJsU1E9PQ==",

    # 0 Length
    "https://www.communitycollegejobs.com/jobdetail-219787-farm-business-manage"
    "ment-instructor",

    # 0 Length
    "https://skyebackpackers.com/job-listing/job/search-engine-evaluator-at-cen"
    "tific-ri-ben-Yk9haGhuaU81RmlRQmhrbExMV25hTlht",

    # 0 Length
    "https://skyebackpackers.com/job-listing/job/natural-gas-compressor-mechani"
    "c-delaware-basin-west-texas-and-se-new-mexico-at-knock-out-energy-llc-kerm"
    "it-tx-WWVHaGdIcU41VithQVI0aUlyNmphOVhnVHc9PQ==",

    # 0 Length
    "https://www.communitycollegejobs.com/jobdetail-276767-criminal-justice-ins"
    "tructor",

    # 0 Length
    "https://skyebackpackers.com/job-listing/job/front-desk-hotel-clerk-at-lead"
    "er-motel-leader-sk-WnVxaGozK040MW1XQlI4bElyU25idG5rU3c9PQ==",

    # 0 Length
    "https://skyebackpackers.com/job-listing/job/ecumenical-worship-musician-pi"
    "anist-keyboardist-at-music-ministry-international-chong-nawa-xian-chong-na"
    "wa-shi-WmVDc2puV0Q0VkNiQ0I4aUtyYWdaOW50",

    # 0 Length
    "https://skyebackpackers.com/job-listing/job/junior-graphic-designer-at-adj"
    "ust-your-set-toronto-on-WU9Hc2czNks0MWliQmg4akxiNmtaOVhtVHc9PQ==",

    "https://skyebackpackers.com/job-listing/job/doc-operator-i-at-maldonado-bu"
    "rkett-llp-thomaston-ga-WU9xbmdYeU00MTJiQWg4aElyQ2tiOS9tU2c9PQ==",

    # 0 Length
    "https://skyebackpackers.com/job-listing/job/set-designer-at-cornerstone-te"
    "chnologies-american-fork-ut-WmVha2huNkw2MTZYQnhnbktyV2hiTjdn",
]


def populate_broken_endpoint_list(database_app):
    return ([
        endpoint_id
        for (endpoint_id,) in database_app.session.query(APIEndpoint.id)
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
        )
        .all()
    ])


def get_base_domain(url_full: str):
    if (not isinstance(url_full, str) or
            len(url_full) == 0):
        return None

    if 'http' not in url_full:
        url_full = 'http://' + url_full

    domain_base: list = [
        *filter('www'.__ne__, urlparse(url_full).netloc.split('.'))
    ]

    return '.'.join(domain_base)


def get_proxy_list(database_app):
    """
    Refreshes Proxy List
    Loads only residential proxies
    Only loads enabled proxies.
    """
    return (
        database_app.session.query(Proxy)
        .filter(
            and_(
                Proxy.disabled.is_(False),
                Proxy.testing.is_(False),
                Proxy.proxy_type.in_(preferred_residential_proxy_type_list)
            )
        )
        .order_by(asc(Proxy.last_access))
        .all()
    )


def get_scrape_rate_limit_list(
        domain_name: str,
        database_app):
    """
    Loads rate limit settings for a specific domain name
    Returns list of ScrapeRateLimit Rows
    """
    if len(domain_name) == 0:
        return None

    return (
        database_app.session.query(ScrapeRateLimits)
        .filter(
            and_(
                ScrapeRateLimits.disabled.is_(False),
                ScrapeRateLimits.domain == domain_name,
                or_(
                    ScrapeRateLimits.next_access.is_(None),
                    ScrapeRateLimits.next_access <= datetime.now(UTC)
                )
            )
        )
        .order_by(asc(ScrapeRateLimits.next_access))
        .all()
    )


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
                APIEndpoint.id.not_in(scrape_endpoints_id_broken_list),
                APIEndpoint.disabled == 0
            )
        )
        .all()
    )


def get_proxies_in_rate_limit_list(
        check_domain: str,
        proxies: list,
        database_app):
    """
    Return strings that match the proxies list provided
    as a set of strings.

    Does not filter if next_access time is greater than current time.

    proxies input is a list of strings
    """
    return set([
        get_rate_limit.proxy for get_rate_limit in
        database_app.session.query(ScrapeRateLimits)
        .filter(
            and_(
                ScrapeRateLimits.domain == check_domain,
                ScrapeRateLimits.proxy.in_(proxies)
            )
        )
        .options(
            load_only(
                ScrapeRateLimits.proxy
            )
        )
        .all()
    ])


def get_processed_query_list(
        endpoint_types_list: list,
        database_app):
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
            )
        )
        .order_by(
            asc(
                MongoStorage.query_time
            )
        )
        .options(
            load_only(
                MongoStorage.id,
                MongoStorage.object_id,
                MongoStorage.endpoint_nice_name,
                MongoStorage.input_json,
                MongoStorage.url,
                MongoStorage.query_time,
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


def get_scrape_list(database_app):
    """
    Refreshes Current Scrape List
    """
    return (
        database_app.session.query(MongoScrapeStorage)
        .filter(
            or_(
                # Scrape list unprocessed
                and_(
                    MongoScrapeStorage.object_id.is_(None),
                    MongoScrapeStorage.query_time.is_(None),
                    MongoScrapeStorage.length.is_(None),
                    MongoScrapeStorage.data_truncated.is_(None),
                    MongoScrapeStorage.code.is_(None),
                ),

                # Scrape list that has not been successfully processed.
                and_(
                    MongoScrapeStorage.code.not_in(http_pass_codes),

                    MongoScrapeStorage.object_id.is_not(None),
                    MongoScrapeStorage.query_time.is_not(None),
                    MongoScrapeStorage.length.is_not(None),
                    MongoScrapeStorage.data_truncated.is_not(None),
                ),

                # Scrapes that have failed.
                and_(
                    or_(
                        MongoScrapeStorage.object_id.is_not(None),
                        MongoScrapeStorage.query_time.is_not(None),
                        MongoScrapeStorage.code.is_not(None),
                    ),
                    or_(MongoScrapeStorage.length.is_(None),
                        MongoScrapeStorage.length <= 3),
                ),
            )
        )
        .options(
            load_only(
                MongoScrapeStorage.id,
                MongoScrapeStorage.url,
            )
        )
        .order_by(asc(MongoScrapeStorage.time))
        # .limit(zombie_process_limit)
        .all()
    )


def get_scrape_duplicate_checker(database_app, current_list):
    """
    Checks URLS in the MongoScrapeStorage so as not to insert any duplicate
    URLs. On the database side, it will verify that the URL indicated is not
    currently in the scrape table.
    """
    return (
        database_app.session.query(MongoScrapeStorage)
        .filter(MongoScrapeStorage.url.in_(current_list))
        .options(load_only(MongoScrapeStorage.url))
        .all()
    )


def check_duplicate_urls(list_of_urls_to_check, limit):
    database_app_session = get_session(bind_key='mariadb')

    missing_urls = set()
    processed_urls = 0

    initial_start_duplicate_urls = time.time()
    start_time_duplicate_urls = time.time()

    # 15 million characters / 2048 URL string length = 7324.21875
    batch_size = 7324

    for index in range(0, len(list_of_urls_to_check), batch_size):
        # Query for the batch of URLs
        batch = set(
            s for s in list_of_urls_to_check[index: index + batch_size]
            if (s not in faulty_sites and
                get_base_domain(s) not in restricted_sites)
        )

        # Fetch existing URLs from the database for the current batch
        existing_urls = set(
            existing.url
            for existing in database_app_session.query(MongoScrapeStorage)
            .filter(MongoScrapeStorage.url.in_(batch))
            .options(load_only(MongoScrapeStorage.url))
            .all()
        )

        processed_urls += len(batch)
        # Calculate missing URLs in the current batch
        current_batch_missing_urls = set(batch) - existing_urls

        if current_batch_missing_urls:
            missing_urls.update(current_batch_missing_urls)

        print(f"Batch {processed_urls}/{len(list_of_urls_to_check)} " +
              f"Unique URL Count: {len(missing_urls)} " +
              f"({((time.time() - start_time_duplicate_urls) * 1000):.6g} ms)",
              flush=True)
        start_time_duplicate_urls = time.time()

        # If the number of missing URLs reaches the limit, return them
        if len(missing_urls) >= limit:
            print("Limit reached, found unique URLs")
            database_app_session.close()
            return missing_urls

    # Return the missing URLs found if the limit wasn't reached
    database_app_session.close()

    print(f"Batch Complete: {processed_urls} "
          f"({((time.time() - initial_start_duplicate_urls) * 1000):.6g} ms)",
          flush=True)


def get_apply_links(mongo_row: MongoStorage):
    """
    Pull data from Mongo Database Storage and parse apply links
    Returns a tuple list (Performance)
    0: URL Ref Key
    1: URL
    """
    if mongo_row is None:
        return {}

    result_apply_links: dict = get_apply_link(
        api_url=mongo_row.url,
        nice_name=mongo_row.endpoint_nice_name,
        dict_new=convert_bytes_to_dict_raw(
            fs_mongo.get(file_id=ObjectId(mongo_row.object_id))
            .read().decode()
        ),
        input_json=mongo_row.input_json,
    )

    if not isinstance(result_apply_links, dict):
        # print(result_apply_links, flush=True)
        # print(mongo_row, flush=True)
        raise ValueError("NOT A DICT")

    new_tuple_apply_links = []

    for mongo_key_apply_links in result_apply_links.keys():
        if (mongo_key_apply_links is None or
                mongo_key_apply_links.lower() == "error"):
            continue

        new_key_apply_link = mongo_key_apply_links
        new_value_apply_link = result_apply_links[mongo_key_apply_links]
        # print('new key: ' + mongo_key, flush=True)
        # print('new val: ' + str(result[mongo_key]), flush=True)

        if isinstance(new_value_apply_link, list):
            for index, nested in enumerate(new_value_apply_link):
                if (not isinstance(nested, str) or
                        len(nested) < 3 or
                        get_base_domain(nested) in restricted_sites or
                        nested in faulty_sites or
                        (len(new_tuple_apply_links) != 0 and
                         any(tup_apply_link[0] + str(index) ==
                             new_key_apply_link or
                             tup_apply_link[1] == nested
                             for tup_apply_link in new_tuple_apply_links))):
                    continue

                new_tuple_apply_links.append(
                    (new_key_apply_link + str(index), nested)
                )
        else:
            if (not isinstance(new_value_apply_link, str) or
                    len(new_value_apply_link) < 3 or
                    get_base_domain(new_value_apply_link) in restricted_sites or
                    new_value_apply_link in faulty_sites or

                    (len(new_tuple_apply_links) != 0 and
                     any(tup_apply_link[0] == new_key_apply_link or
                         tup_apply_link[1] == new_value_apply_link
                         for tup_apply_link in new_tuple_apply_links))):
                continue

            new_tuple_apply_links.append(
                (new_key_apply_link, new_value_apply_link)
            )

    return new_tuple_apply_links


app = create_app()

# Run cleanup if there are stale processes.
destroy_display()
destroy_chromium_process()
cleanup_temp_profile_data()
display = Xvfb()

with app.app_context():
    try:
        display.start()

        # Performance check
        start_time = time.time()

        # populate ID's for broken endpoints
        scrape_endpoints_id_broken_list: list = (
            populate_broken_endpoint_list(db)
        )

        # Refresh list
        scrapes: list = [
            s for s in get_scrape_list(database_app=db)
            if (isinstance(s.url, str) and
                len(s.url) != 0 and
                s.url not in faulty_sites and
                isinstance((domain := get_base_domain(s.url)), str) and
                domain not in restricted_sites)
        ]

        count_scrape_list = len(scrapes)

        if count_scrape_list < zombie_process_limit:
            print("Not enough scrapes to run a batch, processing more.")

            processed_queries: list = get_processed_query_list(
                get_scrape_endpoint_filtered_types(database_app=db),
                database_app=db,
            )

            # for i in processed_queries:
            #     print(str(i.id), flush=True)
            print("Processed Queries "
                  f"({((time.time() - start_time) * 1000):.6g} ms)",
                  flush=True)
            start_time = time.time()

            list_of_urls_temp = []
            for new_query in processed_queries:
                # Add filter here for limit of apply links
                new_tuple_list = get_apply_links(new_query)

                if not isinstance(new_tuple_list, list):
                    raise ValueError("NOT A LIST")

                list_of_urls_temp.extend(new_tuple_list)

            # list_of_urls: [0], [1]
            # Format: [ (url_key, url), ...]

            missing_urls_unique = check_duplicate_urls(
                list_of_urls_to_check=[
                    val[1] for val in list_of_urls_temp
                    if (val[1] not in faulty_sites and
                        get_base_domain(val[1]) not in restricted_sites)],
                limit=zombie_process_limit
            )

            # print("len missing: " + str(len(missing_urls_unique)))

            list_of_urls = []
            if (isinstance(missing_urls_unique, list)
                    and len(missing_urls_unique) != 0):
                seen = set()
                for tup in list_of_urls_temp:
                    if (tup[1] not in seen and
                            tup[1] in missing_urls_unique):
                        list_of_urls.append(tup)
                        seen.add(tup[1])

            # print("len urls: " + str(len(list_of_urls)))

            print(f"Get New Apply Links\n" +
                  "Length: " + str(len(list_of_urls)) + " "
                  f"({((time.time() - start_time) * 1000):.6g} ms)",
                  flush=True)
            start_time = time.time()

            # print("URL List", flush=True)
            # for j, new_url_ in enumerate(list_of_urls):
            #     print("ID: " + str(j) + " " + str(new_url_[1]), flush=True)

            if len(processed_queries) == 0:
                print("No processed_queries", flush=True)
                # raise ValueError("No new processed_queries length")

            if len(list_of_urls) == 0:
                print("Nothing new in URL List", flush=True)
                # raise ValueError("No list_of_urls length")

            # count_process_list: int = len(processed_queries)
            # count_unique_url_dict: int = len(dict_of_unique_urls)

            # print("Process Length: " + str(count_process_list), flush=True)
            # print("Unique URL Length: " + str(len(list_of_urls)), flush=True)

            if len(list_of_urls) != 0:
                unique_urls_to_add = [
                    MongoScrapeStorage(
                        url_ref_key=val[0],
                        url=val[1],
                        time=datetime.now(),
                    ) for val in list_of_urls
                ]

                try:
                    db.session.add_all(unique_urls_to_add)
                    db.session.commit()

                except Exception as e:
                    db.session.rollback()
                    db.session.close()
                    # print(e, flush=True)
                    raise e

                print(f"New Scrape Items: " +
                      str(len(unique_urls_to_add)) + " " +
                      f"({((time.time() - start_time) * 1000):.6g} ms)",
                      flush=True)
                start_time = time.time()

            if len(scrapes) == 0:
                print("Nothing new to process", flush=True)
                raise ValueError("Nothing to process.")

            # recount when done
            # count_scrape_list = len(
            #     1 for scrape in scrapes
            #     if scrape.url not in faulty_sites and
            #     get_base_domain(scrape.url) not in restricted_sites
            # )
            count_scrape_list = len(scrapes)

        else:
            print("Found " + str(count_scrape_list) + " scrapes to process")

        current_count_scrape_list: int = 0
        final_scrape_status = ""

        all_proxies: list = get_proxy_list(database_app=db)

        elapsed_time = (time.time() - start_time) * 1000
        start_time = time.time()

        print(f"Proxy Load " +
              f"({elapsed_time:.6g} ms)",
              flush=True)

        for scrape in scrapes:
            print("Process " + str(scrape.id))
            if scrape.url in faulty_sites:
                print(scrape.url + " in faulty sites")
                continue

            domain = get_base_domain(scrape.url)
            if (not isinstance(domain, str) or
                    domain in restricted_sites):
                print(scrape + " in restricted_sites")
                continue

            # Check rate limits if populated per scrape:
            set_existing_rate_limits = (
                get_proxies_in_rate_limit_list(
                    check_domain=domain,
                    proxies=[p.proxy_address for p in all_proxies],
                    database_app=db
                )
            )
            new_rate_limits = [
                ScrapeRateLimits(
                    domain=domain,
                    proxy=j
                ) for j in (set(p.proxy_address for p in all_proxies) -
                            set_existing_rate_limits
                            if set_existing_rate_limits is not None
                            else set())]

            if len(new_rate_limits) != 0:
                try:
                    db.session.add_all(new_rate_limits)
                    db.session.commit()
                    print(str(len(new_rate_limits)) +
                          " rate limit items added " +
                          "for " + domain)

                except Exception as e:
                    db.session.rollback()
                    db.session.close()
                    # print(e, flush=True)
                    raise e

            if (current_count_scrape_list > 0 and
                    current_count_scrape_list + 1 != count_scrape_list):

                if current_count_scrape_list >= zombie_process_limit:
                    print(f"{zombie_process_limit} zombie "
                          "processes. Restarting.",
                          flush=True)

                    destroy_chromium_process()
                    cleanup_temp_profile_data()
                    raise ChildProcessError("ZOMBIE PROCESS CLEANUP")

                # print("Scrape test finished", flush=True)
                # raise ValueError("Debug Finish")

            loaded_rate_limits = get_scrape_rate_limit_list(
                domain_name=domain,
                database_app=db
            )

            if len(loaded_rate_limits) == 0:
                print("No rate limits available for " + domain)
                continue

            # Check rate limit settings per proxy
            try:
                total_scrapes_remaining = (
                    zombie_process_limit
                    if count_scrape_list > zombie_process_limit
                    else (count_scrape_list
                          if count_scrape_list != 0 else '?'))
                print("Current: (" +
                      str(current_count_scrape_list + 1) +
                      "/" +
                      str(total_scrapes_remaining) +
                      ")", flush=True)

                # Set URL for query
                url: str = scrape.url
                # print("Fetch " + url, flush=True)
                # Refresh proxy list to update
                proxy: list = [p for p in get_proxy_list(database_app=db)
                               for r in loaded_rate_limits
                               if p.proxy_address == r.proxy]

                selected_rate_limit: None = None
                # Load next proxy
                # match rate limit to proxies available

                if (proxy is not None and
                        len(proxy) != 0):
                    proxy: Proxy = proxy[0]
                    selected_rate_limit: list = [
                        i for i in loaded_rate_limits
                        if i.proxy == proxy.proxy_address
                    ]

                    if (selected_rate_limit is None or
                            len(selected_rate_limit) == 0):
                        print("Could not find a rate limit object for proxy" +
                              proxy.proxy_address, flush=True)
                        continue

                    else:
                        selected_rate_limit: ScrapeRateLimits = (
                            selected_rate_limit[0])

                    print("Processing " + str(scrape.id) +
                          " [" + url + "] using Proxy (" +
                          proxy.proxy_address + ")",
                          flush=True)

                else:
                    print("No proxies found for " + url, flush=True)
                    continue

                response: None = None
                selected_proxy_prefix: str = ''

                for i in proxy_type_prefix_dict.keys():
                    for j in range(len(proxy_type_prefix_dict[i])):
                        if int(proxy_type_prefix_dict[i][j]) == int(
                                proxy.proxy_type):
                            selected_proxy_prefix = i

                if selected_proxy_prefix == '':
                    raise ValueError("Proxy Prefix Error. Not found in "
                                     "proxy_type_prefix_dict")

                # print("Adding " + selected_proxy_prefix +
                #       " to proxy as prefix", flush=True)

                proxy_settings: dict = {
                    'http': selected_proxy_prefix + proxy.proxy_address,
                    'https': selected_proxy_prefix + proxy.proxy_address
                }

                # print("URL: " + str(url), flush=True)

                user_agent: str = random.choice(user_agent_list)
                headers: dict = {'User-Agent': user_agent}
                # print("Adding Header: " + str(headers), flush=True)

                # finally, send the query.
                # use requests to retrieve the GET response

                # raise ValueError("Debug stop")

                if proxy.auth_required == 1:
                    raise ValueError("Chromium support for Authentication "
                                     "not implemented by driver")
                fail_count: int = 0
                while response is None:
                    try:
                        response: str = uc_chromium_pull_page(
                            user_agent=user_agent,
                            proxy_server=(selected_proxy_prefix +
                                          proxy.proxy_address),
                            url=url
                        )

                        # Run killall after response is retrieved
                        destroy_chromium_process()

                        if response is None:
                            raise EnvironmentError("Response returned nothing.")

                    except Exception as e:
                        # Log proxy failing request
                        if proxy.failed_requests is None:
                            proxy.failed_requests = 0

                        proxy.failed_requests += 1

                        if fail_count >= 1:
                            print(str(e))
                            print("Fail Count: " + str(fail_count), flush=True)
                            response: ValueError = (
                                ValueError("Failed attempts to scrape"))
                            fail_count = 0

                        else:
                            fail_count += 1

                            print("Fail Count: " + str(fail_count) +
                                  "/2)")
                            response: None = None
                            # Add sleep here to reduce overhead
                            sleep(5)

                # response = requests.get(
                #     url=url,
                #     headers=headers,
                #     proxies=proxy_settings,
                #     auth=(HTTPBasicAuth(
                #         proxy.proxy_username,
                #         proxy.proxy_password)
                #           if proxy.auth_required != 0 else None)
                # )

                if isinstance(response, ValueError):
                    print("Skipping (" + str(response))
                    continue

                current_time: datetime = datetime.now(UTC)

                if response is None:
                    raise ValueError("Response did not go through.")

                # print(str(response.headers), flush=True)
                print("Saved JS Text " + str(
                    len(response)), flush=True)

                print("======", flush=True)

                # Fill the Mongo_Storage with response
                # Insert response json into mongo_fs
                # scrape.object_id = fs_upload(response.text.encode(
                #     encoding='utf-8')).binary
                scrape.object_id = fs_upload(response.encode()).binary
                scrape.proxy = proxy.proxy_address
                scrape.headers = headers

                # Add query time
                scrape.query_time = current_time

                # scrape.length = len(response.text)
                scrape.length = len(response)

                # scrape.data_truncated = response.text[:255]
                scrape.data_truncated = response[:255]

                # scrape.code = response.status_code
                scrape.code = 200 if len(response) > 3 else 500
                scrape.verified = True

                if proxy.requests is None:
                    proxy.requests = 0

                proxy.requests += 1

                # if response.status_code not in http_pass_codes:
                if response is None:
                    if proxy.failed_requests is None:
                        proxy.failed_requests = 0

                    proxy.failed_requests += 1
                    final_scrape_status += ("Scrape " + str(scrape.id) +
                                            " not processed.\n")

                elif not isinstance(response, ValueError):

                    selected_rate_limit.next_access = (
                        calculate_next_scrape_rate_limit(
                            scrape_rate_limit_row=selected_rate_limit,
                            current_date_time_utc=current_time
                        )
                    )

                    selected_rate_limit.verified = True

                    final_scrape_status += ("Scrape " + str(scrape.id) +
                                            " processed.\n")

                proxy.last_access = current_time
                proxy.verified = True
                db.session.commit()
                current_count_scrape_list += 1

            except KeyError as e:
                final_scrape_status += (str(e) + " - Could not process "
                                        "scrape " + str(scrape.id) + ".\n")
                raise e

        if (final_scrape_status is not None and
                isinstance(final_scrape_status, str) and
                len(final_scrape_status) != 0):
            print(final_scrape_status, flush=True)
            db.session.commit()

        if (final_scrape_status is None or
                len(final_scrape_status) == 0):
            pass

        raise ChildProcessError("Completed")

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

    except ChildProcessError as e:
        e_str = str(e)
        if ("ZOMBIE PROCESS CLEANUP" not in e_str or
                "Completed" not in e_str):
            db.session.rollback()
        db.session.close()
        raise e

    # Other Errors
    except Exception as e:
        db.session.rollback()
        db.session.close()
        print(f"Error: {e}", flush=True)
        raise e

    finally:
        if display or 'display' in locals():
            display.stop()
        destroy_display()
        destroy_chromium_process()
        cleanup_temp_profile_data()
