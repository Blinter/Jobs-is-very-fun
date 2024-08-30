"""
get_locations
main function that converts a location string to a parsed location dictionary.
"""

from routines import (
    extract_value_from_dict,
    extract_value_from_dict_list, extract_values_from_dict_list
)
from routines.parsing.location.apijobs import api_jobs_search_jobs
from routines.parsing.location.avadataservices_job_postings import\
    ava_data_services_job_postings_job_slug
from routines.parsing.location.dodocr7_google_jobs import \
    dodocr7_google_jobs_offer_info
from routines.parsing.location.fantastic_jobs_active_jobs_db import \
    fantastic_jobs_active_jobs_db_get_jobs_text
from routines.parsing.location.flatroy_jobs_from_remoteok import \
    flatroy_jobs_from_remoteok_get_list
from routines.parsing.location.bebity_linkedin_jobs_scraper import \
    bebity_linkedin_jobs_scraper_get_jobs_json
from routines.parsing.location.freshdata_linkedin_jobs import (
    freshdata_search_jobs,
    freshdata_get_job_details,
    freshdata_get_company
)
from routines.parsing.location.jaypat87_indeed import jaypat87_indeed_search
from routines.parsing.location.jaypat87_linkedin import (
    jaypat87_linkedin_search
)
from routines.parsing.location.jobicy_remote_jobs import \
    jobicy_remote_jobs_remote_jobs
from routines.parsing.location.jobisite_job_search import jobisite_job_search
from routines.parsing.location.jobsapi2020_zambian_jobs import \
    jobs_2020_zambian_jobs_https_job_co_uk_get
from routines.parsing.location.jobwiz_job_search import \
    jobwiz_job_search_search_job
from routines.parsing.location.letscrape_real_time_glassdoor_data import\
    letscrape_real_time_glassdoor_data
from routines.parsing.location.letscrape_search import letscrape_jsearch
from routines.parsing.location.lundehund_twitter_x_job import \
    (lundehund_twitter_x_job_search_job,
     lundehund_twitter_x_job_search_location)
from routines.parsing.location.mantiks_glassdoor import\
    (mantiks_glassdoor_jobs_search, mantiks_glassdoor_locations_search,
     mantiks_glassdoor_job_details)
from routines.parsing.location.mantiks_indeed import (
    mantiks_indeed_jobs_search,
    mantiks_indeed_job_details, mantiks_indeed_company_jobs)
from routines.parsing.location.mgujjargamingm_linkedin import\
    mgujjargamingm_linkedin_search_jobs
from routines.parsing.location.pat92_jobs import pat92_jobs_list_jobs
from routines.parsing.location.qurazor1_remoote_job_search import \
    qurazor1_remoote_job_search_list_jobs_jobs_get
from routines.parsing.location.relu_consultancy_arbeitsagentur import\
    relu_consultancy_arbeitsagentur
from routines.parsing.location.relu_consultancy_indeed_scraper_germany import\
    (relu_consultancy_indeed_scraper_germany_search_jobs,
     relu_consultancy_indeed_scraper_germany_job_view)
from routines.parsing.location.rockapis_rapid_linkedin_jobs import \
    rockapis_rapid_linkedin_jobs_search_jobs_v2
from routines.parsing.location.sohailglt_linkedin_live_data import\
    (sohailglt_linkedin_live_data_company_search,
     sohailglt_linkedin_live_data_company_details)
from routines.parsing.location.vuesdata_indeed_jobs import \
    vuesdata_indeed_jobs_search_jobs


def get_locations(
        api_url: str,
        nice_name: str,
        dict_new: dict,
        input_json: dict):
    """
    Converts a jobs dictionary to a parsed location dictionary
    """
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
                # print("Data from API does not include locations. Each job "
                #       "listing must be queried individually.", flush=True)

                return api_jobs_search_jobs(dict_new)

        # APIJobs | Job Searching API
        # Search organization
        case ("https://apijob-job-searching-api.p.rapidapi.com"
              "/v1/organization/search"):
            if nice_name == "Search organization":
                return (
                    {
                        "error":
                            "Data from API does not include location data."
                    }
                )

        # APIJobs | Job Searching API
        # Get job by id
        case ("https://apijob-job-searching-api.p.rapidapi.com"
              "/v1/job/"):
            if nice_name == "Get job by id":
                # print("Data from API does not include location data. "
                #       "The job must be scraped manually from the URL.",
                #       flush=True)

                return (
                    {
                        "error":
                            "Data from API does not include location data."
                            "The job must be scraped manually from the "
                            "URL."
                    }
                )

        # avadataservices | Job Postings
        # /api/v2/Jobs/{slug}
        case ("https://job-postings1.p.rapidapi.com"
              "/api/v2/Jobs/"):
            if nice_name == "/api/v2/Jobs/{slug}":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                return (
                    ava_data_services_job_postings_job_slug(
                        dict_new=dict_new
                    )
                )

        # avadataservices | Job Postings
        # /api/v2/Jobs/Latest
        case ("https://job-postings1.p.rapidapi.com"
              "/"):
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
                # print("Data from API does not include location data. "
                #       "The job must be scraped manually from the URL key.",
                #       flush=True)

                return (
                    {
                        "error":
                            "Data from API does not include "
                            "location data. The job must be "
                            "scraped manually from the URL "
                            "key."
                    }
                )

        # bareq | Remote Jobs API
        # List jobs free
        case ("https://remote-jobs-api1.p.rapidapi.com"
              "/jobs/free"):
            if nice_name == "List jobs free":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                temp_dict_new = {}

                for i in dict_new.keys():
                    temp_dict_new[str(i)] = {
                        'source__jobs': "bareq | Remote Jobs API",
                        'remote__jobs': True
                    }

                return temp_dict_new

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
                return (
                    bebity_linkedin_jobs_scraper_get_jobs_json(
                        dict_new=dict_new,
                        input_json=input_json
                    )
                )

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
            # print("Data from API does not include locations. Each job "
            #       "listing must be queried individually.", flush=True)

            return (
                {
                    "error":
                        "Data from API does not include "
                        "locations. Each job listing must be "
                        "queried individually."
                }
            )

        # Dodocr7 | Google Jobs
        # SearchOffers
        case ("https://google-jobs.p.rapidapi.com"
              "/"):
            if nice_name == "OfferInfo":
                if ((dict_new.get('status', None) is not None and
                        dict_new.get('status') == 404 or
                        dict_new.get('status') == 500) or
                        dict_new.get('error') is not None):

                    if (not isinstance(dict_new, dict) or
                            dict_new.get('error') is not None):
                        return {}
                    return (
                        {
                            'error':
                                'Error with query.'
                        }
                    )
                return dodocr7_google_jobs_offer_info(
                    job_info=dict_new
                )
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
                # todo locations parsing refinement
                return (
                    fantastic_jobs_active_jobs_db_get_jobs_text(
                        dict_new=dict_new
                    )
                )

        # Flatroy | Jobs from Remoteok
        # Get list
        case ("https://jobs-from-remoteok.p.rapidapi.com/"):
            if nice_name == "Get list":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                return (
                    flatroy_jobs_from_remoteok_get_list(
                        dict_new=dict_new,
                        input_json=input_json
                    )
                )

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
                return (
                    freshdata_get_job_details(
                        dict_new=dict_new,
                    )
                )

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
                return (
                    freshdata_search_jobs(
                        dict_new=dict_new,
                        input_json=input_json
                    )
                )

        # jaypat87 | Indeed
        # jaypat87 | Job Search
        # Search
        # Jobs Search
        case ("https://indeed11.p.rapidapi.com"
              "/" |
              "https://job-search15.p.rapidapi.com"
              "/"):
            if (nice_name == "Search" or
                    nice_name == "Jobs Search"):
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                return (
                    jaypat87_indeed_search(
                        dict_new=dict_new,
                        input_json=input_json
                    )
                )

            elif nice_name == "Job Description Full-Text":
                # print("Data from API does not include company name. "
                #       "Each job listing must be queried individually.",
                #       flush=True)

                return (
                    {
                        "error":
                            "Data from API does not include "
                            "appropriate data. Each job listing must "
                            "be queried individually."
                    }
                )

        # jaypat87 | Linkedin Jobs Search
        # Search
        case ("https://linkedin-jobs-search.p.rapidapi.com"
              "/"):
            if nice_name == "Search":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                return (
                    jaypat87_linkedin_search(
                        dict_new=dict_new,
                        input_json=input_json
                    )
                )

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
                return (
                    jobicy_remote_jobs_remote_jobs(
                        dict_new=dict_new,
                        input_json=input_json
                    )
                )

        # jobisite | Job Search
        # Search Jobs
        case ("https://job-search38.p.rapidapi.com"
              "/my/searchJobs"):
            if nice_name == "Search Jobs":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                return (
                    jobisite_job_search(
                        dict_new=dict_new,
                        input_json=input_json
                    )
                )

        # JobsAPI2020 | Zambian Jobs API
        # httpsJobapiCoUkGet
        case ("https://zambian-jobs-api1.p.rapidapi.com"
              "/getdataNew.php"):
            if nice_name == "httpsJobapiCoUkGet":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                return (
                    jobs_2020_zambian_jobs_https_job_co_uk_get(
                        dict_new=dict_new
                    )
                )

        # Jobwiz | Job Search API
        # searchJob
        case ("https://job-search-api1.p.rapidapi.com"
              "/v1/job-description-search"):
            if nice_name == "searchJob":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                return (
                    jobwiz_job_search_search_job(
                        dict_new=dict_new,
                        input_json=input_json
                    )
                )

        # letscrape | Job Salary Data
        # Job Salary
        case ("https://job-salary-data.p.rapidapi.com"
              "/job-salary"):
            if nice_name == "Job Salary":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                return (
                    {
                        "error":
                            "Data does not include any locations."
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
                return (
                    letscrape_jsearch(
                        dict_new=dict_new,
                        input_json=input_json,
                    )
                )

        # letscrape | JSearch
        # Search Filters
        case ("https://jsearch.p.rapidapi.com"
              "/search-filters"):
            if nice_name == "Search Filters":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                return (
                    {
                        "error":
                            "Data does not include any locations."
                    }
                )

        # letscrape | JSearch
        # Job Details
        case ("https://jsearch.p.rapidapi.com"
              "/job-details"):
            if nice_name == "Job Details":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                return (
                    letscrape_jsearch(
                        dict_new=dict_new,
                        input_json=input_json,
                    )
                )

        # letscrape | Real-Time Glassdoor Data
        # Company Search
        case ("https://real-time-glassdoor-data.p.rapidapi.com"
              "/company-search"):
            if nice_name == "Company Search":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                return (
                    letscrape_real_time_glassdoor_data(
                        dict_new=dict_new
                    )
                )

        # letscrape | Real-Time Glassdoor Data
        # Company Reviews
        case ("https://real-time-glassdoor-data.p.rapidapi.com"
              "/company-reviews"):
            if nice_name == "Company Reviews":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = dict_new.get('reviews')
                new_dict = {}

                for i in range(len(result)):
                    if (result[i].get('location') is not None and
                            result[i].get('review_id') is not None):
                        new_dict[result[i].get('review_id')] = (
                            result[i].get('location')
                        )

                return new_dict

        # letscrape | Real-Time Glassdoor Data
        # Company Overview
        case ("https://real-time-glassdoor-data.p.rapidapi.com"
              "/company-overview"):
            if nice_name == "Company Overview":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                return (
                    letscrape_real_time_glassdoor_data(
                        dict_new=dict_new
                    )
                )

        # Lundehund | Twitter X Job API
        # Search Job
        # Get Job Detail
        # Order of locations are inconsistent
        # So rely on Location ID only
        case ("https://twitter-x-api.p.rapidapi.com"
              "/api/job/search" |
              "https://twitter-x-api.p.rapidapi.com"
              "/api/job/detail"):
            if (nice_name == "Search Job" or
                    nice_name == "Get Job Detail"):
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                return (
                    lundehund_twitter_x_job_search_job(
                        dict_new=dict_new,
                        input_json=input_json,
                    )
                )

        # Lundehund | Twitter X Job API
        # Search Location
        case ("https://twitter-x-api.p.rapidapi.com"
              "/api/job/search/location"):
            if nice_name == "Search Location":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                return (
                    lundehund_twitter_x_job_search_location(
                        dict_new=dict_new,
                    )
                )

        # mantiks | Glassdoor
        # Companies Search
        case ("https://glassdoor.p.rapidapi.com"
              "/companies/search"):
            if nice_name == "Companies Search":
                # print("Company data from API does not include locations.",
                #       flush=True)

                return (
                    {
                        "error":
                            "Company data from API does not "
                            "include locations."
                    }
                )

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
                return (
                    mantiks_glassdoor_job_details(
                        dict_new=dict_new
                    )
                )

        # mantiks | Glassdoor
        # Jobs Search
        case ("https://glassdoor.p.rapidapi.com"
              "/jobs/search"):
            if nice_name == "Jobs Search":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                return (
                    mantiks_glassdoor_jobs_search(
                        dict_new=dict_new,
                        input_json=input_json,
                    )
                )

        # mantiks | Glassdoor
        # Locations Search
        case ("https://glassdoor.p.rapidapi.com"
              "/locations/search"):
            if nice_name == "Locations Search":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                return (
                    mantiks_glassdoor_locations_search(
                        dict_new=dict_new,
                    )
                )

        # mantiks | Indeed
        # Job details
        case ("https://indeed12.p.rapidapi.com"
              "/job/"):
            if nice_name == "Job details":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                return (
                    mantiks_indeed_job_details(
                        dict_new=dict_new
                    )
                )

        # mantiks | Indeed
        # Jobs Search
        case ("https://indeed12.p.rapidapi.com"
              "/jobs/search"):
            if nice_name == "Jobs Search":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                return (
                    mantiks_indeed_jobs_search(
                        dict_new=dict_new,
                        input_json=input_json,
                    )
                )

        # mantiks | Indeed
        # Company Search
        case ("https://indeed12.p.rapidapi.com"
              "/companies/search"):
            if nice_name == "Company Search":
                # print("Company data from API does not include locations. "
                #       "Use company details to get hq_location", flush=True)

                return (
                    {
                        "error":
                            "Company data from API does not "
                            "include locations. only hq_location is "
                            "defined from company details endpoint."
                    }
                )

        # mantiks | Indeed
        # Company details
        # Company jobs
        case ("https://indeed12.p.rapidapi.com"
              "/company/"):
            if (not isinstance(dict_new, dict) or
                    dict_new.get('error') is not None):
                return {}

            if nice_name == "Company details":
                # print("Company data includes HQ Location only (hq_location)",
                #       flush=True)

                return (
                    extract_value_from_dict(
                        key_name="hq_location",
                        dict_new=dict_new
                    )
                )

            elif nice_name == "Company jobs":
                return (
                    mantiks_indeed_company_jobs(
                        dict_new=dict_new,
                        input_json=input_json
                    )
                )

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
                # Grab HQ location if needed
                # This is usually included in the first location in locations
                # list.
                # headquarters_location = extract_value_from_dict_nested(
                #     key_name="headquarters",
                #     key_name_nested="city__State_PostalCode_Country",
                #     dict_new=dict_new
                # )
                list_new_dict = extract_value_from_dict(
                    key_name="locations",
                    dict_new=dict_new
                )

                # print(str(list_new_dict), flush=True)
                return (
                    extract_value_from_dict_list(
                        key_name='city_State_PostalCode_Country',
                        list_new_dict=list_new_dict
                    )
                )

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
                # Grab HQ location if needed

                # This is usually included in the headquarter key in the
                # location list.
                # i.e. "headquarter": false

                # Example: extract city, geographicArea, country
                #  for location parsing
                #  "headquarter": {
                #       "city": "Mountain View",
                #       "country": "US",
                #       "description": null,
                #       "geographicArea": "CA",
                #       "line1": "1600 Amphitheatre Parkway",
                #       "line2": null,
                #       "postalCode": "94043"
                #     },
                list_new_dict = extract_value_from_dict(
                    key_name="locations",
                    dict_new=dict_new
                )
                # print(str(list_new_dict), flush=True)
                # returned data is a dictionary with Company ID
                # containing a list of locations.
                #
                # Example: extract city, geographicArea, country
                #  for location parsing
                return (
                    list_new_dict
                )

        # mgujjargamingm | LinkedIn Data Scraper
        # Company data from web-domain /web-domain
        case ("https://linkedin-data-scraper.p.rapidapi.com"
              "/web-domain" |
              "https://linkedin-bulk-data-scraper.p.rapidapi.com"
              "/web-domain"):
            if nice_name == "Company data from web-domain /web-domain":
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

                # Grab HQ location if needed
                # This is usually included in the first location in locations
                # list.
                # headquarters_location = extract_value_from_dict_nested(
                #     key_name="headquarters",
                #     key_name_nested="city__State_PostalCode_Country",
                #     dict_new=dict_new
                # )
                list_new_dict = extract_value_from_dict(
                    key_name="locations",
                    dict_new=dict_new
                )

                # print(str(list_new_dict), flush=True)
                return (
                    extract_values_from_dict_list(
                        key_name='city_State_PostalCode_Country',
                        list_new_dict=list_new_dict
                    )
                )

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
                return (
                    mgujjargamingm_linkedin_search_jobs(
                        dict_new=dict_new
                    )
                )

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
        # mgujjargamingm | LinkedIn Bulk Data Scraper
        # Search Jobs
        # Search Jobs ( with filters )
        case ("https://linkedin-data-scraper.p.rapidapi.com"
              "/search_jobs" |
              "https://linkedin-bulk-data-scraper.p.rapidapi.com"
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
                return (
                    mgujjargamingm_linkedin_search_jobs(
                        dict_new=dict_new,
                        input_json=input_json
                    )
                )

        # mgujjargamingm | LinkedIn Data Scraper
        # Search GeoUrns
        case ("https://linkedin-data-scraper.p.rapidapi.com"
              "/search_geourns" |
              "https://linkedin-bulk-data-scraper.p.rapidapi.com"
              "/search_geourns"):
            if nice_name == "Search GeoUrns":
                # print("Data from API only gives Geo Urns for DB population.",
                #       flush=True)
                return (
                    {
                        "error":
                            "Data from API only gives "
                            "LinkedIn GeoUrns for DB population."
                    }
                )

        # mgujjargamingm | LinkedIn Data Scraper
        # Suggestion Company Size
        case ("https://linkedin-data-scraper.p.rapidapi.com"
              "/suggestion_company_size" |
              "https://linkedin-bulk-data-scraper.p.rapidapi.com"
              "/suggestion_company_size"):
            if nice_name == "Suggestion Company Size":
                # print("Data from API only gives company sizes for "
                #       "DB population.", flush=True)

                return (
                    {
                        "error":
                            "Data from API only gives "
                            "LinkedIn Company Size codes for DB population."
                    }
                )

        # mgujjargamingm | LinkedIn Data Scraper
        # Search Companies With Filters
        case ("https://linkedin-data-scraper.p.rapidapi.com"
              "/search_company_with_filters" |
              "https://linkedin-bulk-data-scraper.p.rapidapi.com"
              "/search_company_with_filters"):
            if nice_name == "Search Companies With Filters":
                # print("Data from API only gives company summaries.",
                #       flush=True)

                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = (
                    extract_value_from_dict(
                        key_name="primarySubtitle",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    result[i] = result[i][(result[i].find('•'))+1:].strip()

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
                temp_dict_new = {}

                for i in dict_new.keys():
                    temp_dict_new[str(i)] = {
                        'source__jobs': "omarmohamed0 | Jobs API",
                        'remote__jobs': True
                    }

                return temp_dict_new

        # omarmohamed0 | Jobs API
        # All remote (Freelance jobs)
        case ("https://freelancer-api.p.rapidapi.com"
              "/api/find-job/" |
              "https://freelancer-api.p.rapidapi.com"
              "/api/find-job"):
            if (nice_name == "Get All Jobs" or
                    nice_name == "Get all jobs in specific page"):
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                # All remote jobs
                temp_dict_new = {}

                for i in dict_new.keys():
                    temp_dict_new[str(i)] = {
                        'source__jobs': "omarmohamed0 | Jobs API",
                        'remote__jobs': True
                    }

                return temp_dict_new

        # Pat92 | Jobs API
        # List Jobs
        case ("https://jobs-api14.p.rapidapi.com"
              "/list"):
            if nice_name == "List Jobs":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                return (
                    pat92_jobs_list_jobs(
                        dict_new=dict_new,
                        input_json=input_json
                    )
                )

        # Pat92 | Jobs API
        # Get salary range
        case ("https://jobs-api14.p.rapidapi.com"
              "/salary/getSalaryRange"):
            if nice_name == "Get salary range":
                # print("Data from API does not include locations.", flush=True)

                return (
                    {
                        "error":
                            "Data from API does not "
                            "include locations."
                    }
                )

        # Pat92 | Jobs API
        # Get job titles
        case ("https://jobs-api14.p.rapidapi.com"
              "/salary/getJobTitles"):
            if nice_name == "Get job titles":
                # print("Data from API does not include locations.", flush=True)

                return (
                    {
                        "error":
                            "Data from API does not "
                            "include locations."
                    }
                )

        # qurazor1 | Remoote Job Search
        # list_skills_skills_get
        case ("https://remoote-job-search1.p.rapidapi.com"
              "/remoote/skills"):
            if nice_name == "list_skills_skills_get":
                # print("Data from API does not include locations.", flush=True)

                return (
                    {
                        "error":
                            "Data from API does not "
                            "include locations."
                    }
                )

        # qurazor1 | Remoote Job Search
        # list_jobs_jobs_get
        case ("https://remoote-job-search1.p.rapidapi.com"
              "/remoote/jobs"):
            if nice_name == "list_jobs_jobs_get":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                # todo: extra parsing refinement
                return (
                    qurazor1_remoote_job_search_list_jobs_jobs_get(
                        dict_new=dict_new,
                        input_json=input_json
                    )
                )

        # qurazor1 | Remoote Job Search
        # get_related_jobs_jobs__int_id___related_post
        case ("https://remoote-job-search1.p.rapidapi.com"
              "/remoote/jobs/"):
            if nice_name == "get_related_jobs_jobs__int_id___related_post":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                return (
                    qurazor1_remoote_job_search_list_jobs_jobs_get(
                        dict_new=dict_new,
                        input_json=input_json
                    )
                )

        # qurazor1 | Remoote Job Search
        # list_countries_countries_get
        case ("https://remoote-job-search1.p.rapidapi.com"
              "/remoote/countries"):
            if nice_name == "list_countries_countries_get":
                # print("Data from API only gives countries for "
                #       "DB population.", flush=True)

                return (
                    {
                        "error":
                            "Data from API only gives "
                            "countries for DB population."
                    }
                )

        # qurazor1 | Remoote Job Search
        # list_titles_titles_get
        case ("https://remoote-job-search1.p.rapidapi.com"
              "/remoote/titles"):
            if nice_name == "list_titles_titles_get":
                # print("Data from API only gives titles for DB population.",
                #       flush=True)

                return (
                    {
                        "error":
                            "Data from API only gives "
                            "titles for DB population."
                    }
                )

        # Relu Consultancy | Arbeitsagentur
        # Get Token
        case ("https://arbeitsagentur-employement-agency.p.rapidapi.com"
              "/get-token"):
            if nice_name == "Get Token":
                # print("Data from API is used for token generation only",
                #       flush=True)

                return (
                    {
                        "error":
                            "Data from API is used for token "
                            "generation only"
                    }
                )

        # Relu Consultancy | Arbeitsagentur
        # Search Jobs
        case ("https://arbeitsagentur-employement-agency.p.rapidapi.com"
              "/search"):
            if nice_name == "Search Jobs":
                if (dict_new.get('message', None) is not None and
                        dict_new.get('message') == "No job found"):
                    return (
                        {
                            "error":
                                "Search query failed"
                        }
                    )

                return (
                    relu_consultancy_arbeitsagentur(
                        dict_new=dict_new,
                        input_json=input_json
                    )
                )

        # Relu Consultancy | Indeed Scraper API - Germany
        # Get Token
        case ("https://indeed-scraper-api-germany.p.rapidapi.com"
              "/get-token"):
            if nice_name == "Get Token":
                # print("Data from API is used for token generation only",
                #       flush=True)

                return (
                    {
                        "error":
                            "Data from API is used for token "
                            "generation only"
                    }
                )

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

                # German Location parsing
                return (
                    relu_consultancy_indeed_scraper_germany_search_jobs(
                        dict_new,
                        input_json
                    )
                )

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
                # German Location parsing
                return (
                    relu_consultancy_indeed_scraper_germany_job_view(
                        dict_new
                    )
                )

        # RockAPIs | Linkedin API
        # Search Employees
        case ("https://linkedin-api8.p.rapidapi.com"
              "/search-employees"):
            # This API Provider doesn't like multiple free accounts
            if nice_name == "Search Employees":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                result = (
                    extract_value_from_dict(
                        key_name='geoRegion',
                        dict_new=dict_new
                    )
                )

                return (
                    result
                )

        # RockAPIs | Linkedin API
        # Get Company Details
        case ("https://linkedin-api8.p.rapidapi.com"
              "/get-company-details"):
            # This API Provider doesn't like multiple free accounts
            if nice_name == "Get Company Details":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                # Grab HQ location if needed

                # This is usually included in the headquarter key in the
                # location list.
                # i.e. "headquarter": false

                # Example: extract city, geographicArea, country
                #  for location parsing
                #  "headquarter": {
                #       "city": "Mountain View",
                #       "country": "US",
                #       "description": null,
                #       "geographicArea": "CA",
                #       "line1": "1600 Amphitheatre Parkway",
                #       "line2": null,
                #       "postalCode": "94043"
                #     },
                list_new_dict = extract_value_from_dict(
                    key_name="locations",
                    dict_new=dict_new
                )
                # print(str(list_new_dict), flush=True)
                # returned data is a dictionary with Company ID
                # containing a list of locations.
                #
                # Example: extract city, geographicArea, country
                #  for location parsing
                return (
                    list_new_dict
                )

        # RockAPIs | Linkedin API
        # Get Company By Domain (BETA)
        case ("https://linkedin-api8.p.rapidapi.com"
              "/get-company-by-domain"):
            if nice_name == "Get Company By Domain (BETA)":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                return freshdata_get_company(dict_new)

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
        # Search Jobs
        # Search Jobs V2
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

                return (
                    rockapis_rapid_linkedin_jobs_search_jobs_v2(
                        dict_new=dict_new,
                        input_json=input_json
                    )
                )

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
                return (
                    sohailglt_linkedin_live_data_company_search(
                        dict_new=dict_new
                    )
                )

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

            if (not isinstance(dict_new, dict) or
                    dict_new.get('error') is not None):
                return {}
            if nice_name == "Get Company Details":
                return (
                    sohailglt_linkedin_live_data_company_details(
                        dict_new=dict_new
                    )
                )

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
                # print("Data from API is used for Industries List DB
                # generation only", flush=True)

                return (
                    {
                        "error":
                            "Data from API is used for "
                            "Industries List DB generation "
                            "only"
                    }
                )

        # sohailglt | Linkedin Live Data
        # Company Types
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
        # SearchJobs
        case ("https://indeed-jobs-api.p.rapidapi.com"
              "/indeed-us/"):
            if nice_name == "SearchJobs":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                error_keyword = '''\
{'Error': "Jobs API returned no data, You have entered'''
                if error_keyword in str(dict_new)[:len(error_keyword)]:
                    return {"error": "Search query failed"}
                return (
                    vuesdata_indeed_jobs_search_jobs(
                        # country="United States",
                        dict_new=dict_new,
                        input_json=input_json
                    )
                )

        # vuesdata | Indeed Jobs - Sweden
        # SearchJobs
        case ("https://indeed-jobs-api-sweden.p.rapidapi.com"
              "/indeed-se/"):
            if nice_name == "SearchJobs":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                error_keyword = '''\
{'Error': "Jobs API returned no data, You have entered'''
                if error_keyword in str(dict_new)[:len(error_keyword)]:
                    return {"error": "Search query failed"}
                return (
                    vuesdata_indeed_jobs_search_jobs(
                        country="Sweden",
                        dict_new=dict_new,
                        input_json=input_json
                    )
                )

        # vuesdata | Indeed Jobs API - Finland
        # SearchJobs
        case ("https://indeed-jobs-api-finland.p.rapidapi.com"
              "/indeed-fi/"):
            if nice_name == "SearchJobs":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                error_keyword = '''\
{'Error': "Jobs API returned no data, You have entered'''
                if error_keyword in str(dict_new)[:len(error_keyword)]:
                    return {"error": "Search query failed"}
                return (
                    vuesdata_indeed_jobs_search_jobs(
                        country="Finland",
                        dict_new=dict_new,
                        input_json=input_json
                    )
                )

        # vuesdata | Indeed Jobs API - Denmark
        # SearchJobs
        case ("https://indeed-jobs-api-denmark.p.rapidapi.com"
              "/indeed-dk/"):
            if nice_name == "SearchJobs":
                if (not isinstance(dict_new, dict) or
                        dict_new.get('error') is not None):
                    return {}
                error_keyword = '''\
{'Error': "Jobs API returned no data, You have entered'''
                if error_keyword in str(dict_new)[:len(error_keyword)]:
                    return {"error": "Search query failed"}
                return (
                    vuesdata_indeed_jobs_search_jobs(
                        country="Denmark",
                        dict_new=dict_new,
                        input_json=input_json
                    )
                )

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
