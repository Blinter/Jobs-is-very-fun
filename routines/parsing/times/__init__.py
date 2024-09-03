"""
Get Times
main function that parses API Job times.
"""
import ast
from datetime import datetime, timedelta, UTC

import pytz

from routines import (
    extract_value_from_dict,
    # extract_value_from_dict_list,
    extract_from_list_dict,
    convert_str_to_datetime_y_m_d_h_m_s_z,
    convert_str_to_datetime_y_m_d_h_m_s_f,
    convert_str_to_datetime_gmt_default,
    convert_str_to_datetime_date,
    convert_str_to_datetime_date_time_only,
    convert_str_to_datetime_from_iso,
    convert_str_to_datetime_date_time2,
    # convert_str_to_datetime_utc_default,
    convert_str_to_datetime_non_us,
    convert_str_to_datetime_utc_extra
)


def get_times(
        api_url: str,
        nice_name: str,
        dict_new: dict,
        input_json: dict,
        query_time: datetime):
    """
    Converts a jobs dictionary to a parsed Time dictionary

    posted_time_utc: Posted Time
    expiration_time_utc: Expiration Time (or 1 Month ahead)

    """
    query_time = query_time.replace(tzinfo=pytz.UTC)
    match api_url:

        # APIJobs | Job Searching API
        # APIJobs.dev | API Jobs
        # Search jobs
        # Search Jobs
        case ("https://apijob-job-searching-api.p.rapidapi.com"
              "/v1/job/search" |
              "https://api.apijobs.dev"
              "/v1/job/search"):
            if (nice_name == "Search jobs" or
                    nice_name == "Search Jobs"):
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = (
                    extract_value_from_dict(
                        key_name='created_at',
                        dict_new=dict_new
                    )
                )

                for i in dict_new.keys():
                    result[i] = convert_str_to_datetime_y_m_d_h_m_s_z(result[i])

                    result[i] = ({
                        'posted_time_utc': result[i]
                        if result[i] is not None else
                        query_time,

                        'expiration_time_utc': result[i] + timedelta(days=30)
                        if result[i] is not None else
                        query_time + timedelta(days=30),
                    })

                return result

        # APIJobs | Job Searching API
        # Search organization
        case ("https://apijob-job-searching-api.p.rapidapi.com"
              "/v1/organization/search"):
            if nice_name == "Search organization":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                # Fix filter to show domain name instead.
                # derive from query time
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # APIJobs | Job Searching API
        # Get job by id
        case ("https://apijob-job-searching-api.p.rapidapi.com"
              "/v1/job/"):
            if nice_name == "Get job by id":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = (
                    extract_value_from_dict(
                        key_name='created_at',
                        dict_new=dict_new
                    )
                )
                for i in dict_new.keys():
                    new_time = convert_str_to_datetime_y_m_d_h_m_s_z(result[i])

                    result[i] = ({
                        'posted_time_utc': new_time
                        if new_time is not None else
                        query_time,

                        'expiration_time_utc': new_time + timedelta(days=30)
                        if new_time is not None else
                        query_time + timedelta(days=30),
                    })

                return result

        # avadataservices | Job Postings
        # /api/v2/Jobs/{slug}
        case ("https://job-postings1.p.rapidapi.com"
              "/api/v2/Jobs/"):
            if nice_name == "/api/v2/Jobs/{slug}":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = (
                    extract_value_from_dict(
                        key_name='dateAdded',
                        dict_new=dict_new
                    )
                )

                for i in dict_new.keys():
                    result[i] = convert_str_to_datetime_y_m_d_h_m_s_f(
                        result[i][:-1]
                    )

                    result[i] = ({
                        'posted_time_utc': result[i]
                        if result[i] is not None else
                        query_time,

                        'expiration_time_utc': result[i] + timedelta(days=30)
                        if result[i] is not None else
                        query_time + timedelta(days=30),
                    })

                return result

        # avadataservices | Job Postings
        # /api/v2/Jobs/Latest
        case ("https://job-postings1.p.rapidapi.com/"):
            if nice_name == "/api/v2/Jobs/Latest":
                return (
                    {
                        "error":
                            "Data from API does not provide JSON data. "
                            "HTML must be interpreted."
                    }
                )

        # avadataservices | Job Postings
        # /api/v2/Jobs/Search
        case ("https://job-postings1.p.rapidapi.com"
              "/api/v2/Jobs/Search"):
            if nice_name == "/api/v2/Jobs/Search":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = (
                    extract_value_from_dict(
                        key_name='dateAdded',
                        dict_new=dict_new
                    )
                )

                for i in dict_new.keys():
                    try:
                        result[i] = convert_str_to_datetime_y_m_d_h_m_s_f(
                            result[i][:-2])
                    except ValueError:
                        print("Could not parse " + str(result[i][:-2]) +
                              "from default (y_m_d_h_m_s_f) "
                              "defaulting to query time")
                        result[i] = None

                    result[i] = ({
                        'posted_time_utc': result[i]
                        if result[i] is not None else
                        query_time,

                        'expiration_time_utc': result[i] + timedelta(days=30)
                        if result[i] is not None else
                        query_time + timedelta(days=30),
                    })

                return result

        # bareq | Remote Jobs API
        # List jobs free
        case ("https://remote-jobs-api1.p.rapidapi.com"
              "/jobs/free"):
            if nice_name == "List jobs free":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = (
                    extract_value_from_dict(
                        key_name='publishDate',
                        dict_new=dict_new
                    )
                )

                for i in dict_new.keys():
                    result[i] = (convert_str_to_datetime_gmt_default(result[i]))

                    result[i] = ({
                        'posted_time_utc': result[i]
                        if result[i] is not None else
                        query_time,

                        'expiration_time_utc': result[i] + timedelta(days=30)
                        if result[i] is not None else
                        query_time + timedelta(days=30),
                    })

                return result

        # Bebity | Linkedin Jobs Scraper API
        # Get jobs (JSON)
        case ("https://linkedin-jobs-scraper-api.p.rapidapi.com"
              "/jobs" |
              "https://linkedin-jobs-scraper-api.p.rapidapi.com"
              "/jobs/trial"):
            if (nice_name == "Get jobs (JSON)" or
                    nice_name == "Get jobs trial (JSON)"):
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = (
                    extract_value_from_dict(
                        key_name='postedTime',
                        dict_new=dict_new
                    )
                )

                new_dict = {}
                # Get date difference
                for i in dict_new.keys():
                    if result[i].lower().find(' seconds ago') != -1:
                        time_diff = result[i].lower().replace(
                            ' seconds ago', '').strip()
                        result[i] = query_time - timedelta(seconds=int(
                            time_diff))

                    elif result[i].lower().find(' minutes ago') != -1:
                        time_diff = result[i].lower().replace(
                            ' minutes ago', '').strip()
                        result[i] = query_time - timedelta(minutes=int(
                            time_diff))

                    elif result[i].lower().find(' hours ago') != -1:
                        time_diff = result[i].lower().replace(
                            ' hours ago', '').strip()
                        result[i] = query_time - timedelta(hours=int(
                            time_diff))

                    elif result[i].lower().find(' days ago') != -1:
                        time_diff = result[i].lower().replace(
                            ' days ago', '').strip()
                        result[i] = query_time - timedelta(days=int(
                            time_diff))

                    elif result[i].lower().find(' weeks ago') != -1:
                        time_diff = result[i].lower().replace(
                            ' weeks ago', '').strip()
                        result[i] = query_time - timedelta(weeks=int(
                            time_diff))
                    else:
                        result[i] = query_time

                    new_dict[i] = ({
                        'posted_time_utc': result[i]
                        if result[i] is not None else
                        query_time,

                        'expiration_time_utc': result[i] + timedelta(days=30)
                        if result[i] is not None else
                        query_time + timedelta(days=30),
                    })

                return new_dict

        # Betoalien | USA Jobs for IT
        # All Endpoints
        case ("https://usa-jobs-for-it.p.rapidapi.com"
              "/DataEngineer" |
              "https://usa-jobs-for-it.p.rapidapi.com"
              "/DataAnalyst" |
              "https://usa-jobs-for-it.p.rapidapi.com"
              "/Angular" |
              "https://usa-jobs-for-it.p.rapidapi.com"
              "/Java" |
              "https://usa-jobs-for-it.p.rapidapi.com"
              "/Python" |
              "https://usa-jobs-for-it.p.rapidapi.com"
              "/React" |
              "https://usa-jobs-for-it.p.rapidapi.com"
              "/BusinessIntelligence" |
              "https://usa-jobs-for-it.p.rapidapi.com"
              "/Laravel" |
              "https://usa-jobs-for-it.p.rapidapi.com"
              "/NodeJs" |
              "https://usa-jobs-for-it.p.rapidapi.com"
              "/FullStack" |
              "https://usa-jobs-for-it.p.rapidapi.com"
              "/JavaScript"
              ):
            if (not isinstance(dict_new, dict) or
                    dict_new.get('error') is not None):
                return {}
            result = {}

            for i in dict_new.keys():
                result[i] = ({
                    'posted_time_utc': query_time,
                    'expiration_time_utc': query_time + timedelta(days=30)
                })

            return result

        # Dodocr7 | Google Jobs
        # OfferInfo
        # SearchOffers
        case ("https://google-jobs.p.rapidapi.com/"):
            if nice_name == "OfferInfo":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                if ((dict_new.get('status', None) is not None and
                        dict_new.get('status') == 404 or
                        dict_new.get('status') == 500) or
                        dict_new.get('error') is not None):
                    return (
                        {
                            'error':
                                'Error with query.'
                        }
                    )
                result = (
                    extract_value_from_dict(
                        key_name='scrapedDate',
                        dict_new=dict_new
                    )
                )

                posted_date = (
                    extract_value_from_dict(
                        key_name='postedDate',
                        dict_new=dict_new
                    )
                )

                for i in dict_new.keys():
                    result[i] = convert_str_to_datetime_date_time_only(
                        result[i]
                    )

                    if posted_date[i].lower().find(' seconds ago') != -1:
                        time_diff = posted_date[i].lower().replace(
                            ' seconds ago', '').strip()
                        result[i] -= timedelta(seconds=int(
                            time_diff))

                    elif posted_date[i].lower().find(' minutes ago') != -1:
                        time_diff = posted_date[i].lower().replace(
                            ' minutes ago', '').strip()
                        result[i] -= timedelta(minutes=int(
                            time_diff))

                    elif posted_date[i].lower().find(' hours ago') != -1:
                        time_diff = posted_date[i].lower().replace(
                            ' hours ago', '').strip()
                        result[i] -= timedelta(hours=int(
                            time_diff))

                    elif posted_date[i].lower().find(' days ago') != -1:
                        time_diff = posted_date[i].lower().replace(
                            ' days ago', '').strip()
                        result[i] -= timedelta(days=int(
                            time_diff))

                    elif posted_date[i].lower().find(' weeks ago') != -1:
                        time_diff = posted_date[i].lower().replace(
                            ' weeks ago', '').strip()
                        result[i] -= timedelta(weeks=int(
                            time_diff))

                    result[i] = ({
                        'posted_time_utc': result[i]
                        if result[i] is not None else
                        query_time,


                        'expiration_time_utc': result[i] + timedelta(days=30)
                        if result[i] is not None else
                        query_time + timedelta(days=30),
                    })

                return result

            elif nice_name == "SearchOffers":
                # print("Data from API does not include appropriate data. "
                #       "Each job query page must be queried individually.",
                #       flush=True)

                return (
                    {
                        "error":
                            "Data from API does not include "
                            "appropriate data. Each page must "
                            "be queried individually."
                    }
                )

        # Fantastic Jobs | Active Jobs DB
        # Get Jobs
        # Get Jobs - (Text Description)
        case ("https://active-jobs-db.p.rapidapi.com"
              "/active-ats" |
              "https://active-jobs-db.p.rapidapi.com"
              "/rest/v1/active_ats_textdescription_v1"):
            if (nice_name == "Get Jobs" or
                    nice_name == "Get Jobs - (Text Description"):
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = (
                    extract_value_from_dict(
                        key_name='dateposted',
                        dict_new=dict_new
                    )
                )

                for i in dict_new.keys():
                    try:
                        result[i] = convert_str_to_datetime_from_iso(result[i])
                    except ValueError as e:
                        print(str(e) + " - defaulting to query time")
                        result[i] = None

                    result[i] = ({
                        'posted_time_utc': result[i]
                        if result[i] is not None else
                        query_time,

                        'expiration_time_utc': result[i] + timedelta(days=30)
                        if result[i] is not None else
                        query_time + timedelta(days=30),
                    })

                return result

        # Flatroy | Jobs from Remoteok
        # Get list
        case ("https://jobs-from-remoteok.p.rapidapi.com/"):
            if nice_name == "Get list":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = (
                    extract_value_from_dict(
                        key_name='date',
                        dict_new=dict_new
                    )
                )

                for i in dict_new.keys():
                    result[i] = convert_str_to_datetime_from_iso(result[i])

                    result[i] = ({
                        'posted_time_utc': result[i]
                        if result[i] is not None else
                        query_time,

                        'expiration_time_utc': result[i] + timedelta(days=30)
                        if result[i] is not None else
                        query_time + timedelta(days=30),
                    })

                return result

        # Freshdata | Fresh Linkedin Profile Data
        # Freshdata | Linkedin Jobs
        # Get Job Details
        case ("https://linkedin-jobs4.p.rapidapi.com"
              "/get-job-details" |
              "https://fresh-linkedin-profile-data.p.rapidapi.com"
              "/get-job-details"):
            if nice_name == "Get Job Details":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # Freshdata | Fresh Linkedin Profile Data
        # Freshdata | Linkedin Jobs
        # Search Jobs
        case ("https://fresh-linkedin-profile-data.p.rapidapi.com"
              "/search-jobs" |
              "https://linkedin-jobs4.p.rapidapi.com"
              "/search-jobs"):
            if nice_name == "Search Jobs":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = (
                    extract_value_from_dict(
                        key_name='posted_time',
                        dict_new=dict_new
                    )
                )

                for i in dict_new.keys():
                    result[i] = convert_str_to_datetime_date_time_only(
                        result[i]
                    )

                    result[i] = ({
                        'posted_time_utc': result[i]
                        if result[i] is not None else
                        query_time,

                        'expiration_time_utc': result[i] + timedelta(days=30)
                        if result[i] is not None else
                        query_time + timedelta(days=30),
                    })

                return result

        # jaypat87 | Indeed
        # Search
        case ("https://indeed11.p.rapidapi.com"
              "/"):
            if nice_name == "Search":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # jaypat87 | Job Search
        # Jobs Search
        # Job Description Full-Text
        case ("https://job-search15.p.rapidapi.com"
              "/"):
            if nice_name == "Jobs Search":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = (
                    extract_value_from_dict(
                        key_name='posted_date',
                        dict_new=dict_new
                    )
                )

                for i in dict_new.keys():
                    result[i] = convert_str_to_datetime_date(
                        result[i]
                    )

                    result[i] = ({
                        'posted_time_utc': result[i]
                        if result[i] is not None else
                        query_time,

                        'expiration_time_utc': result[i] + timedelta(days=30)
                        if result[i] is not None else
                        query_time + timedelta(days=30),
                    })

                return result

            elif nice_name == "Job Description Full-Text":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                # This should be derived from the Jobs Search endpoint while
                # retrieving the ID.
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # jaypat87 | Linkedin Jobs Search
        # Search
        case ("https://linkedin-jobs-search.p.rapidapi.com"
              "/"):
            if nice_name == "Search":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = (
                    extract_value_from_dict(
                        key_name='posted_date',
                        dict_new=dict_new
                    )
                )

                for i in dict_new.keys():
                    result[i] = convert_str_to_datetime_date(
                        result[i]
                    )

                    result[i] = ({
                        'posted_time_utc': result[i]
                        if result[i] is not None else
                        query_time,

                        'expiration_time_utc': result[i] + timedelta(days=30)
                        if result[i] is not None else
                        query_time + timedelta(days=30),
                    })

                return result

        # jobicy | Remote Jobs API
        # Remote Jobs API
        case ("https://jobicy.p.rapidapi.com"
              "/api/v2/remote-jobs"):
            if nice_name == "Remote Jobs API":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                if (dict_new.get('success', None) is not None and
                        dict_new.get('success', False) is False):
                    return (
                        {
                            "error":
                                "Query was not processed"
                        }
                    )

                result = (
                    extract_value_from_dict(
                        key_name='pubDate',
                        dict_new=dict_new
                    )
                )

                for i in dict_new.keys():
                    result[i] = convert_str_to_datetime_date_time_only(
                        result[i]
                    )

                    result[i] = ({
                        'posted_time_utc': result[i]
                        if result[i] is not None else
                        query_time,

                        'expiration_time_utc': result[i] + timedelta(days=30)
                        if result[i] is not None else
                        query_time + timedelta(days=30),
                    })

                return result

        # jobisite | Job Search
        # Search Jobs
        case ("https://job-search38.p.rapidapi.com"
              "/my/searchJobs"):
            if nice_name == "Search Jobs":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # JobsAPI2020 | Zambian Jobs API
        # httpsJobapiCoUkGet
        case ("https://zambian-jobs-api1.p.rapidapi.com"
              "/getdataNew.php"):
            if nice_name == "httpsJobapiCoUkGet":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # Jobwiz | Job Search API
        # searchJob
        case ("https://job-search-api1.p.rapidapi.com"
              "/v1/job-description-search"):
            if nice_name == "searchJob":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = (
                    extract_value_from_dict(
                        key_name='publication_time',
                        dict_new=dict_new
                    )
                )

                for i in dict_new.keys():
                    result[i] = convert_str_to_datetime_y_m_d_h_m_s_z(
                        result[i]
                    )

                    result[i] = ({
                        'posted_time_utc': result[i]
                        if result[i] is not None else
                        query_time,

                        'expiration_time_utc': result[i] + timedelta(days=30)
                        if result[i] is not None else
                        query_time + timedelta(days=30),
                    })

                return result

        # letscrape | Job Salary Data
        # Job Salary
        case ("https://job-salary-data.p.rapidapi.com"
              "/job-salary"):
            if nice_name == "Job Salary":
                return (
                    {
                        "error":
                            "Data does not include any specific job titles."
                    }
                )

        # letscrape | JSearch
        # Search
        case ("https://jsearch.p.rapidapi.com"
              "/search"):
            if nice_name == "Search":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                # job_offer_expiration_datetime_utc
                # job_offer_expiration_timestamp

                # job_posted_at_datetime_utc
                # job_posted_at_timestamp
                result = (
                    extract_value_from_dict(
                        key_name='job_offer_expiration_datetime_utc',
                        dict_new=dict_new
                    )
                )

                result2 = (
                    extract_value_from_dict(
                        key_name='job_posted_at_datetime_utc',
                        dict_new=dict_new
                    )
                )

                for i in dict_new.keys():
                    result[i] = [
                        convert_str_to_datetime_y_m_d_h_m_s_z(
                            result2[i]
                        ) if result2[i] is not None else None,
                        convert_str_to_datetime_y_m_d_h_m_s_z(
                            result[i]
                        ) if result[i] is not None else None,
                    ]

                    result[i] = ({
                        'posted_time_utc':
                            result[i][0]
                            if result[i][0] is not None
                            else query_time,

                        'expiration_time_utc':
                            result[i][1]
                            if result[i][1] is not None
                            else result[i][0] + timedelta(days=30)
                            if result[i][0] is not None
                            else query_time + timedelta(days=30)
                    })

                return result

        # letscrape | JSearch
        # Search Filters
        case ("https://jsearch.p.rapidapi.com"
              "/search-filters"):
            if nice_name == "Search Filters":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = (
                    extract_from_list_dict(
                        key_name='name',
                        list_new=dict_new.get('date_posted')
                    )
                )

                for i in result.keys():
                    result[i] = ({
                        'posted_time_utc': result[i]
                        if result[i] is not None else
                        query_time,
                        'expiration_time_utc': result[i] + timedelta(days=30)
                        if result[i] is not None else
                        query_time + timedelta(days=30),
                    })

                return result

        # letscrape | JSearch
        # Job Details
        case ("https://jsearch.p.rapidapi.com"
              "/job-details"):
            if nice_name == "Job Details":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                # job_offer_expiration_datetime_utc
                # job_offer_expiration_timestamp

                # job_posted_at_datetime_utc
                # job_posted_at_timestamp
                result = (
                    extract_value_from_dict(
                        key_name='job_offer_expiration_datetime_utc',
                        dict_new=dict_new
                    )
                )

                result2 = (
                    extract_value_from_dict(
                        key_name='job_posted_at_datetime_utc',
                        dict_new=dict_new
                    )
                )

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc':
                            convert_str_to_datetime_y_m_d_h_m_s_z(
                                result2[i]
                            ) if result2[i] is not None else query_time,
                        'expiration_time_utc':
                            convert_str_to_datetime_y_m_d_h_m_s_z(
                                result[i]
                            ) if result[i] is not None else
                            result2[i] + timedelta(days=30)
                            if result2[i] is not None else
                            query_time + timedelta(days=30),
                    })

                return result

        # letscrape | Real-Time Glassdoor Data
        # Company Search
        case ("https://real-time-glassdoor-data.p.rapidapi.com"
              "/company-search"):
            if nice_name == "Company Search":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # letscrape | Real-Time Glassdoor Data
        # Company Reviews
        case ("https://real-time-glassdoor-data.p.rapidapi.com"
              "/company-reviews"):
            if nice_name == "Company Reviews":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = (
                    extract_from_list_dict(
                        key_name='review_datetime',
                        list_new=dict_new.get('reviews')
                    )
                )

                result2 = (
                    extract_from_list_dict(
                        key_name='review_id',
                        list_new=dict_new.get('reviews')
                    )
                )

                new_dict = {}

                for i in range(len(result)):
                    result[i] = ({
                        'posted_time_utc': query_time,
                    })
                    new_dict[str(result2[i])] = result[i]

                return (
                    {
                        input_json.get('company_id', '0'):
                            new_dict
                    }
                )

        # letscrape | Real-Time Glassdoor Data
        # Company Overview
        case ("https://real-time-glassdoor-data.p.rapidapi.com"
              "/company-overview"):
            if nice_name == "Company Overview":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # Lundehund | Twitter X Job API
        # Get Job Detail
        case ("https://twitter-x-api.p.rapidapi.com"
              "/api/job/detail"):
            if nice_name == "Get Job Detail":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # Lundehund | Twitter X Job API
        case ("https://twitter-x-api.p.rapidapi.com"
              "/api/job/search"):
            if nice_name == "Search Job":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # Lundehund | Twitter X Job API
        # Search Location
        case ("https://twitter-x-api.p.rapidapi.com"
              "/api/job/search/location"):
            if nice_name == "Search Location":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # mantiks | Glassdoor
        # Companies Search
        case ("https://glassdoor.p.rapidapi.com"
              "/companies/search"):
            if nice_name == "Companies Search":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # mantiks | Glassdoor
        # Company details
        case ("https://glassdoor.p.rapidapi.com"
              "/company/"):
            if nice_name == "Company Details":
                return (
                    {
                        "error":
                            "Endpoint is disabled."
                    }
                )

        # mantiks | Glassdoor
        # Job details
        case ("https://glassdoor.p.rapidapi.com"
              "/job/"):
            if nice_name == "Job details":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                dict_new = {
                    input_json.get('job_id'):
                        dict_new
                }

                result = {}

                for i in dict_new.keys():
                    if dict_new[i].get('creation_date', None) is not None:
                        result[i] = convert_str_to_datetime_date_time2(
                            dict_new[i].get('creation_date')
                        )

                        result[i] = ({
                            'posted_time_utc': result[i]
                            if result[i] is not None else
                            query_time,
                            'expiration_time_utc':
                                result[i] + timedelta(days=30)
                                if result[i] is not None else
                                query_time + timedelta(days=30),
                        })

                    else:
                        result[i] = {}

                return result

        # mantiks | Glassdoor
        # Jobs Search
        case ("https://glassdoor.p.rapidapi.com"
              "/jobs/search"):
            if nice_name == "Jobs Search":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # mantiks | Glassdoor
        # Locations Search
        case ("https://glassdoor.p.rapidapi.com"
              "/locations/search"):
            if nice_name == "Locations Search":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # mantiks | Indeed
        # Job details
        case ("https://indeed12.p.rapidapi.com"
              "/job/"):
            if nice_name == "Job details":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = (
                    extract_value_from_dict(
                        key_name='creation_date',
                        dict_new=dict_new
                    )
                )

                new_dict = {}
                # Get date difference
                for i in dict_new.keys():
                    if result[i].lower().find(' seconds ago') != -1:
                        time_diff = result[i].lower().replace(
                            ' seconds ago', '').strip()
                        new_dict[i] = query_time - timedelta(seconds=int(
                            time_diff))

                    elif result[i].lower().find(' minutes ago') != -1:
                        time_diff = result[i].lower().replace(
                            ' minutes ago', '').strip()
                        new_dict[i] = query_time - timedelta(minutes=int(
                            time_diff))

                    elif result[i].lower().find(' hours ago') != -1:
                        time_diff = result[i].lower().replace(
                            ' hours ago', '').strip()
                        new_dict[i] = query_time - timedelta(hours=int(
                            time_diff))

                    elif result[i].lower().find(' days ago') != -1:
                        time_diff = result[i].lower().replace(
                            ' days ago', '').strip()
                        new_dict[i] = query_time - timedelta(days=int(
                            time_diff))

                    elif result[i].lower().find(' weeks ago') != -1:
                        time_diff = result[i].lower().replace(
                            ' weeks ago', '').strip()
                        new_dict[i] = query_time - timedelta(weeks=int(
                            time_diff))
                    else:
                        new_dict[i] = query_time

                    new_dict[i] = ({
                        'posted_time_utc': new_dict[i]
                        if new_dict[i] is not None else
                        query_time,
                        'expiration_time_utc': new_dict[i] + timedelta(days=30)
                        if new_dict[i] is not None else
                        query_time + timedelta(days=30),
                    })

                return new_dict

        # mantiks | Indeed
        # Jobs Search
        case ("https://indeed12.p.rapidapi.com"
              "/jobs/search"):
            if nice_name == "Jobs Search":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = (
                    extract_value_from_dict(
                        key_name='formatted_relative_time',
                        dict_new=dict_new
                    )
                )

                new_dict = {}
                # Get date difference
                for i in dict_new.keys():
                    if result[i].lower().find(' seconds ago') != -1:
                        time_diff = result[i].lower().replace(
                            ' seconds ago', '').strip()

                        if time_diff.find('+') != -1:
                            time_diff = (time_diff
                                         .replace('+', '')
                                         .strip())
                            new_dict[i] = query_time - timedelta(seconds=int(
                                time_diff)+1)
                        else:
                            new_dict[i] = query_time - timedelta(seconds=int(
                                time_diff))

                    elif result[i].lower().find(' minutes ago') != -1:
                        time_diff = result[i].lower().replace(
                            ' minutes ago', '').strip()

                        if time_diff.find('+') != -1:
                            time_diff = (time_diff
                                         .replace('+', '')
                                         .strip())
                            new_dict[i] = query_time - timedelta(minutes=int(
                                time_diff)+1)
                        else:
                            new_dict[i] = query_time - timedelta(minutes=int(
                                time_diff))

                    elif result[i].lower().find(' hours ago') != -1:
                        time_diff = result[i].lower().replace(
                            ' hours ago', '').strip()

                        if time_diff.find('+') != -1:
                            time_diff = (time_diff
                                         .replace('+', '')
                                         .strip())
                            new_dict[i] = query_time - timedelta(hours=int(
                                time_diff)+1)
                        else:
                            new_dict[i] = query_time - timedelta(hours=int(
                                time_diff))

                    elif result[i].lower().find(' days ago') != -1:
                        time_diff = result[i].lower().replace(
                            ' days ago', '').strip()

                        if time_diff.find('+') != -1:
                            time_diff = (time_diff
                                         .replace('+', '')
                                         .strip())
                            new_dict[i] = query_time - timedelta(days=int(
                                time_diff)+1)
                        else:
                            new_dict[i] = query_time - timedelta(days=int(
                                time_diff))

                    elif result[i].lower().find(' weeks ago') != -1:
                        time_diff = result[i].lower().replace(
                            ' weeks ago', '').strip()

                        if time_diff.find('+') != -1:
                            time_diff = (time_diff
                                         .replace('+', '')
                                         .strip())
                            new_dict[i] = query_time - timedelta(weeks=int(
                                time_diff)+1)
                        else:
                            new_dict[i] = query_time - timedelta(weeks=int(
                                time_diff))

                    elif result[i].lower().find(' months ago') != -1:
                        time_diff = result[i].lower().replace(
                            ' months ago', '').strip()

                        if time_diff.find('+') != -1:
                            time_diff = (time_diff
                                         .replace('+', '')
                                         .strip())
                            new_dict[i] = query_time - timedelta(weeks=int(
                                time_diff)+4.33)
                        else:
                            new_dict[i] = query_time - timedelta(weeks=int(
                                time_diff) * 4.33)
                    else:
                        new_dict[i] = query_time

                    new_dict[i] = ({
                        'posted_time_utc': new_dict[i]
                        if new_dict[i] is not None else
                        query_time,
                        'expiration_time_utc': new_dict[i] + timedelta(days=30)
                        if new_dict[i] is not None else
                        query_time + timedelta(days=30),
                    })

                return new_dict

        # mantiks | Indeed
        # Company Search
        case ("https://indeed12.p.rapidapi.com"
              "/companies/search"):
            if nice_name == "Company Search":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # mantiks | Indeed
        # Company details
        # Company jobs
        case ("https://indeed12.p.rapidapi.com"
              "/company/"):
            if nice_name == "Company details":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

            elif nice_name == "Company jobs":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # mgujjargamingm | LinkedIn Data Scraper
        # Company Data
        case ("https://linkedin-data-scraper.p.rapidapi.com"
              "/company" |
              "https://linkedin-bulk-data-scraper.p.rapidapi.com"
              "/company"):
            if nice_name == "Company Data":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # mgujjargamingm | LinkedIn Data Scraper
        # Company Data (Premium)
        case ("https://linkedin-data-scraper.p.rapidapi.com"
              "/company_pro" |
              "https://linkedin-bulk-data-scraper.p.rapidapi.com"
              "/company_pro"):
            if nice_name == "Company Data (Premium)":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # mgujjargamingm | LinkedIn Data Scraper
        # Company data from web-domain /web-domain
        case ("https://linkedin-data-scraper.p.rapidapi.com"
              "/web-domain" |
              "https://linkedin-bulk-data-scraper.p.rapidapi.com"
              "/web-domain"):
            if nice_name == "Company data from web-domain /web-domain":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                if ((dict_new.get('status', None) is not None and
                        dict_new.get('status') == 404) or
                        (dict_new.get('error', None) is not None and
                         dict_new.get('error') == '404 - Company not found')):
                    return (
                        {
                            'error':
                                'Error with query.'
                        }
                    )

                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # mgujjargamingm | LinkedIn Data Scraper
        # Company Jobs
        case ("https://linkedin-data-scraper.p.rapidapi.com"
              "/company_jobs" |
              "https://linkedin-bulk-data-scraper.p.rapidapi.com"
              "/company_jobs"):
            if nice_name == "Company Jobs":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # mgujjargamingm | LinkedIn Data Scraper
        # Search Company
        case ("https://linkedin-data-scraper.p.rapidapi.com"
              "/search_company" |
              "https://linkedin-bulk-data-scraper.p.rapidapi.com"
              "/search_company"):
            if nice_name == "Search Company":
                return (
                    {
                        "error":
                            "Endpoint is broken on API."
                    }
                )

        # mgujjargamingm | LinkedIn Data Scraper
        # Search Jobs
        # Search Jobs ( with filters )
        case ("https://linkedin-data-scraper.p.rapidapi.com"
              "/search_jobs"):
            if (nice_name == "Search Jobs ( with filters )" or
                    nice_name == "Search Jobs"):
                if dict_new.get('error', None) is not None:
                    return (
                        {
                            "error":
                                "Search query failed"
                        }
                    )
                result = (
                    extract_value_from_dict(
                        key_name="listedAt",
                        dict_new=dict_new
                    )
                )

                for i in dict_new.keys():
                    result[i] = convert_str_to_datetime_y_m_d_h_m_s_z(
                        result[i])

                    result[i] = ({
                        'posted_time_utc': result[i]
                        if result[i] is not None else
                        query_time,
                        'expiration_time_utc': result[i] + timedelta(days=30)
                        if result[i] is not None else
                        query_time + timedelta(days=30),
                    })

                return result

        # mgujjargamingm | LinkedIn Bulk Data Scraper
        # Search Jobs
        # Search Jobs ( with filters )
        case ("https://linkedin-bulk-data-scraper.p.rapidapi.com"
              "/search_jobs"):
            if (nice_name == "Search Jobs ( with filters )" or
                    nice_name == "Search Jobs"):
                if dict_new.get('error', None) is not None:
                    return (
                        {
                            "error":
                                "Search query failed"
                        }
                    )
                result = (
                    extract_value_from_dict(
                        key_name="footerItems",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    try:
                        result[i] = (ast.literal_eval(result[i])[0]
                                     .get('timeAt'))
                    except (ValueError, SyntaxError) as _:
                        result[i] = None

                    if result[i] is not None:
                        try:
                            result[i] = datetime.fromtimestamp(
                                int(result[i]) / 1000, UTC)
                        except ValueError as _:
                            result[i] = None

                for i in result.keys():
                    if result[i] is None:
                        result[i] = dict_new[i].get('listedAt')
                        if result[i] is not None:
                            result[i] = convert_str_to_datetime_y_m_d_h_m_s_z(
                                result[i])

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': result[i]
                        if result[i] is not None else
                        query_time,
                        'expiration_time_utc': result[i] + timedelta(days=30)
                        if result[i] is not None else
                        query_time + timedelta(days=30),
                    })
                    # print(str(result[i]), flush=True)

                return result

        # mgujjargamingm | LinkedIn Data Scraper
        # Search GeoUrns
        case ("https://linkedin-data-scraper.p.rapidapi.com"
              "/search_geourns" |
              "https://linkedin-bulk-data-scraper.p.rapidapi.com"
              "/search_geourns"):
            if nice_name == "Search GeoUrns":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # mgujjargamingm | LinkedIn Data Scraper
        # Suggestion Company Size
        case ("https://linkedin-data-scraper.p.rapidapi.com"
              "/suggestion_company_size" |
              "https://linkedin-bulk-data-scraper.p.rapidapi.com"
              "/suggestion_company_size"):
            if nice_name == "Suggestion Company Size":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # mgujjargamingm | LinkedIn Data Scraper
        # Search Companies With Filters
        case ("https://linkedin-data-scraper.p.rapidapi.com"
              "/search_company_with_filters" |
              "https://linkedin-bulk-data-scraper.p.rapidapi.com"
              "/search_company_with_filters"):
            if nice_name == "Search Companies With Filters":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # mgujjargamingm | LinkedIn Data Scraper
        # Companies
        case ("https://linkedin-data-scraper.p.rapidapi.com"
              "/bulk_companies" |
              "https://linkedin-bulk-data-scraper.p.rapidapi.com"
              "/bulk_companies"):
            if nice_name == "Companies":
                # print("Endpoint is disabled on API.", flush=True)

                return (
                    {
                        "error":
                            "Endpoint has been moved to a different API."
                    }
                )

        # omarmohamed0 | Jobs API
        # All remote (Freelance profiles)
        case ("https://freelancer-api.p.rapidapi.com"
              "/api/find-freelancers" |
              "https://freelancer-api.p.rapidapi.com"
              "/api/find-freelancers/"):
            if (nice_name == "Get all freelancers" or
                    nice_name == "Get all freelancers in specific page"):
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # omarmohamed0 | Jobs API
        # All remote (Freelance jobs)
        case ("https://freelancer-api.p.rapidapi.com"
              "/api/find-job" |
              "https://freelancer-api.p.rapidapi.com"
              "/api/find-job/"):
            if (nice_name == "Get All Jobs" or
                    nice_name == "Get all jobs in specific page"):
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}

                ends_in_value = (
                    extract_value_from_dict(
                        key_name="ends in",
                        dict_new=dict_new
                    )
                )

                ends_in_dict = {}
                # Get date difference
                for i in dict_new.keys():
                    if ends_in_value[i].lower().find(' seconds left') != -1:
                        time_diff = ends_in_value[i].lower().replace(
                            ' seconds left', '').strip()
                        ends_in_dict[i] = query_time + timedelta(seconds=int(
                            time_diff))

                    elif ends_in_value[i].lower().find(' minutes left') != -1:
                        time_diff = ends_in_value[i].lower().replace(
                            ' minutes left', '').strip()
                        ends_in_dict[i] = query_time + timedelta(minutes=int(
                            time_diff))

                    elif ends_in_value[i].lower().find(' hours left') != -1:
                        time_diff = ends_in_value[i].lower().replace(
                            ' hours left', '').strip()
                        ends_in_dict[i] = query_time + timedelta(hours=int(
                            time_diff))

                    elif ends_in_value[i].lower().find(' days left') != -1:
                        time_diff = ends_in_value[i].lower().replace(
                            ' days left', '').strip()
                        ends_in_dict[i] = query_time + timedelta(days=int(
                            time_diff))

                    elif ends_in_value[i].lower().find(' weeks left') != -1:
                        time_diff = ends_in_value[i].lower().replace(
                            ' weeks left', '').strip()
                        ends_in_dict[i] = query_time + timedelta(weeks=int(
                            time_diff))
                    else:
                        ends_in_dict[i] = query_time

                query_time_dict = {}

                for i in dict_new.keys():
                    query_time_dict[i] = query_time

                result = {}

                for i in dict_new.keys():
                    result[i] = {
                        'posted_time_utc':
                            query_time_dict[i]
                            if query_time_dict[i] is not None
                            else query_time,
                        'expiration_time_utc':
                            ends_in_dict[i]
                            if ends_in_dict[i] is not None
                            else query_time_dict[i] + timedelta(days=30)
                            if query_time_dict[i] is not None
                            else query_time + timedelta(days=30),
                    }

                return result

        # Pat92 | Jobs API
        # List Jobs
        case ("https://jobs-api14.p.rapidapi.com"
              "/list"):
            if nice_name == "List Jobs":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = (
                    extract_value_from_dict(
                        key_name='datePosted',
                        dict_new=dict_new
                    )
                )

                new_dict = {}

                # Get date difference
                for i in dict_new.keys():
                    if result[i].lower().find(' seconds ago') != -1:
                        time_diff = result[i].lower().replace(
                            ' seconds ago', '').strip()
                        new_dict[i] = query_time - timedelta(seconds=int(
                            time_diff))

                    elif result[i].lower().find(' minutes ago') != -1:
                        time_diff = result[i].lower().replace(
                            ' minutes ago', '').strip()
                        new_dict[i] = query_time - timedelta(minutes=int(
                            time_diff))

                    elif result[i].lower().find(' hours ago') != -1:
                        time_diff = result[i].lower().replace(
                            ' hours ago', '').strip()
                        new_dict[i] = query_time - timedelta(hours=int(
                            time_diff))

                    elif result[i].lower().find(' days ago') != -1:
                        time_diff = result[i].lower().replace(
                            ' days ago', '').strip()
                        new_dict[i] = query_time - timedelta(days=int(
                            time_diff))

                    elif result[i].lower().find(' weeks ago') != -1:
                        time_diff = result[i].lower().replace(
                            ' weeks ago', '').strip()
                        new_dict[i] = query_time - timedelta(weeks=int(
                            time_diff))
                    else:
                        new_dict[i] = query_time

                for i in dict_new.keys():
                    new_dict[i] = {
                        'posted_time_utc':
                            new_dict[i]
                            if new_dict[i] is not None
                            else query_time,
                        'expiration_time_utc':
                            new_dict[i] + timedelta(days=30)
                            if new_dict[i] is not None
                            else query_time + timedelta(days=30),
                    }

                return new_dict

        # Pat92 | Jobs API
        # Get salary range
        case ("https://jobs-api14.p.rapidapi.com"
              "/salary/getSalaryRange"):
            if nice_name == "Get salary range":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # Pat92 | Jobs API
        # Get job titles
        case ("https://jobs-api14.p.rapidapi.com"
              "/salary/getJobTitles"):
            if nice_name == "Get job titles":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # qurazor1 | Remoote Job Search
        # list_skills_skills_get
        case ("https://remoote-job-search1.p.rapidapi.com"
              "/remoote/skills"):
            if nice_name == "list_skills_skills_get":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # qurazor1 | Remoote Job Search
        # list_jobs_jobs_get
        case ("https://remoote-job-search1.p.rapidapi.com"
              "/remoote/jobs"):
            if nice_name == "list_jobs_jobs_get":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = (
                    extract_value_from_dict(
                        key_name='created_at',
                        dict_new=dict_new
                    )
                )

                for i in dict_new.keys():
                    if (result[i] is not None and
                            isinstance(result[i], str) and
                            len(result[i]) != 0):
                        result[i] = convert_str_to_datetime_y_m_d_h_m_s_f(
                            result[i])

                    result[i] = ({
                        'posted_time_utc': result[i]
                        if result[i] is not None else
                        query_time,
                        'expiration_time_utc': result[i] + timedelta(days=30)
                        if result[i] is not None else
                        query_time + timedelta(days=30),
                    })

                return result

        # qurazor1 | Remoote Job Search
        # get_related_jobs_jobs__int_id___related_post
        case ("https://remoote-job-search1.p.rapidapi.com"
              "/remoote/jobs/"):
            if nice_name == "get_related_jobs_jobs__int_id___related_post":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = (
                    extract_value_from_dict(
                        key_name='created_at',
                        dict_new=dict_new
                    )
                )

                for i in dict_new.keys():
                    result[i] = convert_str_to_datetime_y_m_d_h_m_s_f(
                        result[i])

                    result[i] = ({
                        'posted_time_utc': result[i]
                        if result[i] is not None else
                        query_time,
                        'expiration_time_utc': result[i] + timedelta(days=30)
                        if result[i] is not None else
                        query_time + timedelta(days=30),
                    })

                return result

        # qurazor1 | Remoote Job Search
        # list_countries_countries_get
        case ("https://remoote-job-search1.p.rapidapi.com"
              "/remoote/countries"):
            if nice_name == "list_countries_countries_get":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # qurazor1 | Remoote Job Search
        # list_titles_titles_get
        case ("https://remoote-job-search1.p.rapidapi.com"
              "/remoote/titles"):
            if nice_name == "list_titles_titles_get":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # Relu Consultancy | Arbeitsagentur
        # Get Token
        case ("https://arbeitsagentur-employement-agency.p.rapidapi.com"
              "/get-token"):
            if nice_name == "Get Token":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # Relu Consultancy | Arbeitsagentur
        # Search Jobs
        case ("https://arbeitsagentur-employement-agency.p.rapidapi.com"
              "/search"):
            if nice_name == "Search Jobs":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                if (dict_new.get('message', None) is not None and
                        dict_new.get('message') == "No job found"):
                    return (
                        {
                            "error":
                                "Search query failed"
                        }
                    )

                result = (
                    extract_value_from_dict(
                        key_name='modifikationsTimestamp',
                        dict_new=dict_new
                    )
                )

                for i in dict_new.keys():
                    result[i] = convert_str_to_datetime_y_m_d_h_m_s_f(
                        result[i])

                    result[i] = ({
                        'posted_time_utc': result[i]
                        if result[i] is not None else
                        query_time,
                        'expiration_time_utc': result[i] + timedelta(days=30)
                        if result[i] is not None else
                        query_time + timedelta(days=30),
                    })

                return result

        # Relu Consultancy | Arbeitsagentur
        # Get Token
        case ("https://indeed-scraper-api-germany.p.rapidapi.com"
              "/get-token"):
            if nice_name == "Get Token":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # Relu Consultancy | Indeed Scraper API - Germany
        # Search Jobs
        case ("https://indeed-scraper-api-germany.p.rapidapi.com"
              "/search"):
            if nice_name == "Search Jobs":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                if (dict_new.get('message', None) is not None and
                        dict_new.get('message') == "No job found"):
                    return (
                        {
                            "error":
                                "Search query failed"
                        }
                    )

                result = (
                    extract_value_from_dict(
                        key_name='publishedDate',
                        dict_new=dict_new
                    )
                )

                for i in dict_new.keys():
                    result[i] = convert_str_to_datetime_date(result[i])

                    result[i] = ({
                        'posted_time_utc': result[i]
                        if result[i] is not None else
                        query_time,
                        'expiration_time_utc': result[i] + timedelta(days=30)
                        if result[i] is not None else
                        query_time + timedelta(days=30),
                    })

                return result

        # Relu Consultancy | Indeed Scraper API - Germany
        # Job View
        case ("https://indeed-scraper-api-germany.p.rapidapi.com"
              "/jobview"):
            if nice_name == "Job View":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                if (dict_new.get('message', None) is not None and
                        (dict_new.get('message') == "No job found" or
                         dict_new.get('message') ==
                         "Parameters validation error")):
                    return (
                        {
                            "error":
                                "Search query failed"
                        }
                    )

                result = {}
                for i in dict_new.keys():
                    result[i] = dict_new[i].get('publishAge')

                    plus_found = False

                    # Seconds (German)
                    if (result[i].lower().find('vor ') != -1 and
                            result[i].lower().find(' sekunden') != -1):
                        time_diff = (result[i].lower()
                                     .replace('vor ', '')
                                     .replace(' sekunden', '')
                                     .strip())

                        if time_diff.find('+') != -1:
                            time_diff = (time_diff
                                         .replace('+', '')
                                         .strip())
                            plus_found = True

                        result[i] = query_time - timedelta(
                            seconds=int(time_diff)
                        )

                        if plus_found:
                            result[i] -= timedelta(seconds=1)

                    # Minutes (German)
                    elif (result[i].lower().find('vor ') != -1 and
                          result[i].lower().find(' minuten') != -1):
                        time_diff = (result[i].lower()
                                     .replace('vor ', '')
                                     .replace(' minuten', '')
                                     .strip())

                        if time_diff.find('+') != -1:
                            time_diff = (time_diff
                                         .replace('+', '')
                                         .strip())
                            plus_found = True

                        result[i] = query_time - timedelta(
                            minutes=int(time_diff)
                        )

                        if plus_found:
                            result[i] -= timedelta(minutes=1)

                    # Hours (German)
                    elif (result[i].lower().find('vor ') != -1 and
                          result[i].lower().find(' stunden') != -1):
                        time_diff = (result[i].lower()
                                     .replace('vor ', '')
                                     .replace(' stunden', '')
                                     .strip()
                                     )

                        if time_diff.find('+') != -1:
                            time_diff = (time_diff
                                         .replace('+', '')
                                         .strip())
                            plus_found = True

                        result[i] = query_time - timedelta(
                            hours=int(time_diff)
                        )

                        if plus_found:
                            result[i] -= timedelta(hours=1)

                    # Days (German)
                    elif (result[i].lower().find('vor ') != -1 and
                          result[i].lower().find(' tagen') != -1):
                        time_diff = (result[i].lower()
                                     .replace('vor ', '')
                                     .replace(' tagen', '')
                                     .strip())

                        if time_diff.find('+') != -1:
                            time_diff = (time_diff
                                         .replace('+', '')
                                         .strip())
                            plus_found = True

                        result[i] = query_time - timedelta(days=int(time_diff))

                        if plus_found:
                            result[i] -= timedelta(days=1)
                    # Weeks (German)
                    elif (result[i].lower().find('vor ') != -1 and
                          result[i].lower().find(' wochen') != -1):
                        time_diff = (result[i].lower()
                                     .replace('vor ', '')
                                     .replace(' wochen', '')
                                     .strip())

                        if time_diff.find('+') != -1:
                            time_diff = (time_diff
                                         .replace('+', '')
                                         .strip())
                            plus_found = True

                        result[i] = query_time - timedelta(weeks=int(
                            time_diff))

                        if plus_found:
                            result[i] -= timedelta(weeks=1)

                    # Months (German)
                    elif (result[i].lower().find('vor ') != -1 and
                          result[i].lower().find('monaten') != -1):
                        time_diff = (result[i].lower()
                                     .replace('monaten', '')
                                     .strip())

                        if time_diff.find('+') != -1:
                            time_diff = (time_diff
                                         .replace('+', '')
                                         .strip())
                            plus_found = True

                        result[i] = query_time - timedelta(
                            weeks=4.33*int(time_diff)
                        )

                        if plus_found:
                            result[i] -= timedelta(weeks=4.33)

                    else:
                        result[i] = query_time

                    result[i] = ({
                        'posted_time_utc': result[i]
                        if result[i] is not None else
                        query_time,
                        'expiration_time_utc': result[i] + timedelta(days=30)
                        if result[i] is not None else
                        query_time + timedelta(days=30),
                    })

                return result

        # RockAPIs | Linkedin API
        # Search Employees
        case ("https://linkedin-api8.p.rapidapi.com"
              "/search-employees"):
            # This API Provider doesn't like multiple free accounts
            if nice_name == "Search Employees":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                # currentPositions -> List of Dicts -> title (Key)
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # RockAPIs | Linkedin API
        # Get Company Details
        case ("https://linkedin-api8.p.rapidapi.com"
              "/get-company-details"):
            # This API Provider doesn't like multiple free accounts
            if nice_name == "Get Company Details":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # RockAPIs | Linkedin API
        # Get Company By Domain (BETA)
        case ("https://linkedin-api8.p.rapidapi.com"
              "/get-company-by-domain"):
            if nice_name == "Get Company By Domain (BETA)":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # RockAPIs | Linkedin API
        # Get Company Insights [PREMIUM] (Beta)
        case ("https://linkedin-api8.p.rapidapi.com"
              "/get-company-insights"):
            if nice_name == "Get Company Insights [PREMIUM] (Beta)":
                return (
                    {
                        "error":
                            "API keys unavailable to query API."
                    }
                )

        # RockAPIs | Linkedin API
        # Get Company Employees Count
        case ("https://linkedin-api8.p.rapidapi.com"
              "/get-company-employees-count"):
            if nice_name == "Get Company Employees Count":
                return (
                    {
                        "error":
                            "API keys unavailable to query API."
                    }
                )

        # RockAPIs | Linkedin API
        # Get Company Jobs Count
        case ("https://linkedin-api8.p.rapidapi.com"
              "/get-company-jobs-count"):
            if nice_name == "Get Company Jobs Count":
                return (
                    {
                        "error":
                            "API keys unavailable to query API."
                    }
                )

        # RockAPIs | Linkedin API
        # Get Job Details
        case ("https://linkedin-api8.p.rapidapi.com"
              "/get-job-details"):
            if nice_name == "Get Job Details":
                return (
                    {
                        "error":
                            "API keys unavailable to query API."
                    }
                )

        # RockAPIs | Linkedin API
        # RockAPIs | Rapid LinkedIn Data API
        # RockAPIs | Rapid Linkedin Jobs API
        case ("https://rapid-linkedin-jobs-api.p.rapidapi.com"
              "/search-jobs-v2" |
              "https://rapid-linkedin-jobs-api.p.rapidapi.com"
              "/search-jobs" |

              "https://linkedin-api8.p.rapidapi.com"
              "/search-jobs" |
              "https://linkedin-api8.p.rapidapi.com"
              "/search-jobs-v2" |

              "https://linkedin-data-api.p.rapidapi.com"
              "/search-jobs" |
              "https://linkedin-data-api.p.rapidapi.com"
              "/search-jobs-v2"):
            # This API Provider doesn't like multiple free accounts
            if (nice_name == "Search Jobs V2" or
                    nice_name == "Search Jobs"):
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                if (str(dict_new) == '''{'message': 'Blocked User. Please \
contact your API provider.'}'''):
                    return (
                        {
                            "error":
                                "Search query failed"
                        }
                    )
                result = (
                    extract_value_from_dict(
                        key_name="postAt",
                        dict_new=dict_new
                    )
                )

                for i in dict_new.keys():
                    # Defaults to +0000 UTC
                    result[i] = convert_str_to_datetime_utc_extra(result[i])

                    result[i] = ({
                        'posted_time_utc': result[i]
                        if result[i] is not None else
                        query_time,

                        'expiration_time_utc': result[i] + timedelta(days=30)
                        if result[i] is not None else
                        query_time + timedelta(days=30),
                    })

                return result

        # RockAPIs | Linkedin API
        # Get Hiring Team
        case ("https://linkedin-api8.p.rapidapi.com"
              "/get-hiring-team"):
            if nice_name == "Get Hiring Team":
                return (
                    {
                        "error":
                            "API keys unavailable to query API."
                    }
                )

        # RockAPIs | Linkedin API
        # Search Locations
        case ("https://linkedin-api8.p.rapidapi.com"
              "/search-locations"):
            if nice_name == "Search Locations":
                return (
                    {
                        "error":
                            "API keys unavailable to query API."
                    }
                )

        # sohailglt | Linkedin Live Data
        # Company Search
        case ("https://linkedin-live-data.p.rapidapi.com"
              "/company-search"):
            if nice_name == "Company Search":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

        # sohailglt | Linkedin Live Data
        # People Search
        case ("https://linkedin-live-data.p.rapidapi.com"
              "/people-search"):
            if nice_name == "People Search":
                return (
                    {
                        "error":
                            "Unclear data returned from API"
                    }
                )

        # sohailglt | Linkedin Live Data
        # Get Profile Details
        # Get Company Details
        case ("https://linkedin-live-data.p.rapidapi.com"
              "/profile-details"):
            if nice_name == "Get Company Details":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = {}

                for i in dict_new.keys():
                    result[i] = ({
                        'posted_time_utc': query_time,
                        'expiration_time_utc': query_time + timedelta(days=30)
                    })

                return result

            elif nice_name == "Get Profile Details":
                return (
                    {
                        "error":
                            "Unclear data returned from API"
                    }
                )

        # sohailglt | Linkedin Live Data
        # Industries List
        case ("https://linkedin-live-data.p.rapidapi.com"
              "/company-industries"):
            if nice_name == "Industries List":
                # print("Data from API is used for Industries List"
                #       " DB generation only", flush=True)

                return (
                    {
                        "error":
                            "Data from API is used for "
                            "Industries List DB generation "
                            "only"
                    }
                )

        # sohailglt | Linkedin Live Data
        # Industries List
        case ("https://linkedin-live-data.p.rapidapi.com"
              "/company-types"):
            if nice_name == "Company Types":
                # print("Data from API is used for Company Types "
                #       "DB generation only", flush=True)

                return (
                    {
                        "error":
                            "Data from API is used for "
                            "Company Types DB generation "
                            "only"
                    }
                )

        # vuesdata | Indeed Jobs API
        # vuesdata | Indeed Jobs - Sweden
        # vuesdata | Indeed Jobs API - Finland
        # vuesdata | Indeed Jobs API - Denmark
        case ("https://indeed-jobs-api.p.rapidapi.com"
              "/indeed-us/" |
              "https://indeed-jobs-api-finland.p.rapidapi.com"
              "/indeed-fi/" |
              "https://indeed-jobs-api-sweden.p.rapidapi.com"
              "/indeed-se/" |
              "https://indeed-jobs-api-denmark.p.rapidapi.com"
              "/indeed-dk/"):
            if nice_name == "SearchJobs":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                error_keyword = '''\
{'Error': "Jobs API returned no data, You have entered'''

                if error_keyword in str(dict_new)[:len(error_keyword)]:
                    return (
                        {
                            "error":
                                "Search query failed"
                        }
                    )

                result = (
                    extract_value_from_dict(
                        key_name="date",
                        dict_new=dict_new
                    )
                )

                for i in dict_new.keys():
                    result[i] = convert_str_to_datetime_non_us(result[i])

                    result[i] = ({
                        'posted_time_utc': result[i]
                        if result[i] is not None
                        else query_time,
                        'expiration_time_utc': result[i] + timedelta(days=30)
                        if result[i] is not None else
                        query_time + timedelta(days=30),
                    })

                return result

        case _:
            print("Unknown API"
                  "\nDebug Info"
                  "\nAPI URL: " + str(api_url) +
                  "\nName: " + str(nice_name), flush=True)
            raise KeyError("Unknown API: " + api_url + " - " + nice_name)


"""

        # TODO
        case (""
              ""):
            if nice_name == "":
                return None
"""
