"""
Get Experience Levels
main function that parses API data and retrieves experience levels in a job
description.
"""

from routines import (
    extract_value_from_dict,
)


def get_experience_levels(
        api_url: str,
        nice_name: str,
        dict_new: dict):
    """
    Converts a jobs dictionary to a parsed experience levels dictionary
    """
    if (not isinstance(dict_new, dict) or
            dict_new.get('error') is not None):
        return {}
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
                # Attempt to from description keywords
                # Preferred Skills:
                # keyword 'years'
                # Look for skill keywords
                return (
                    {
                        "error":
                            "Data from API does not include Experience Levels"
                    }
                )

        # APIJobs | Job Searching API
        # Search organization
        case ("https://apijob-job-searching-api.p.rapidapi.com"
              "/v1/organization/search"):
            if nice_name == "Search organization":
                return (
                    {
                        "error":
                            "Data from API does not include Experience Levels"
                    }
                )

        # APIJobs | Job Searching API
        # Get job by id
        case ("https://apijob-job-searching-api.p.rapidapi.com"
              "/v1/job/"):
            if nice_name == "Get job by id":
                # Attempt to from description keywords
                # Preferred Skills:
                # keyword 'years'
                # Look for skill keywords
                return (
                    {
                        "error":
                            "Data from API does not include Experience Levels"
                    }
                )

        # avadataservices | Job Postings
        # /api/v2/Jobs/{slug}
        case ("https://job-postings1.p.rapidapi.com"
              "/api/v2/Jobs/"):
            if nice_name == "/api/v2/Jobs/{slug}":
                # Attempt to from description keywords
                # Qualifications
                # Requirements
                # Academic Courses
                return (
                    {
                        "error":
                            "Data from API does not include Experience Levels"
                    }
                )

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
                return (
                    {
                        "error":
                            "Data from API does not provide Experience Levels."
                    }
                )

        # bareq | Remote Jobs API
        # List jobs free
        case ("https://remote-jobs-api1.p.rapidapi.com"
              "/jobs/free"):
            if nice_name == "List jobs free":
                return (
                    {
                        "error":
                            "Data from API does not provide Experience Levels."
                    }
                )

        # Bebity | Linkedin Jobs Scraper API
        # Get jobs (JSON)
        case ("https://linkedin-jobs-scraper-api.p.rapidapi.com"
              "/jobs" |
              "https://linkedin-jobs-scraper-api.p.rapidapi.com"
              "/jobs/trial"):
            if (nice_name == "Get jobs (JSON)" or
                    nice_name == "Get jobs trial (JSON)"):
                result = (
                    extract_value_from_dict(
                        key_name='experienceLevel',
                        dict_new=dict_new
                    )
                )
                for i in result.keys():
                    if result[i] == "Not Applicable":
                        result[i] = None
                return result

        # Betoalien | USA Jobs for IT
        # All endpoints
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
            # print("Each job listing must be queried individually from job"
            #       "URL.", flush=True)
            return (
                {
                    "error":
                        "Data from API does not include "
                        "appropriate data. Each job listing must "
                        "be queried individually from job URL."
                }
            )

        # Dodocr7 | Google Jobs
        # OfferInfo
        # SearchOffers
        case ("https://google-jobs.p.rapidapi.com/"):
            if nice_name == "OfferInfo":
                # Experience levels can be parsed from description
                # description (str)
                # result = extract_value_from_dict(
                #         key_name='description',
                #         dict_new=dict_new
                #     )
                # print("Data from API does not include experience levels. "
                #       "Each job listing must be scraped individually.",
                #       flush=True)
                return (
                    {
                        "error":
                            "Data from API does not include "
                            "appropriate data. Each job listing must "
                            "be queried individually."
                    }
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
                # Experience levels can be parsed from descriptiontext
                # descriptiontext (str)
                # result = extract_value_from_dict(
                #         key_name='descriptiontext',
                #         dict_new=dict_new
                #     )
                return (
                    {
                        "error":
                            "Experience Levels not listed in data from API."
                    }
                )

        # Flatroy | Jobs from Remoteok
        # Get list
        case ("https://jobs-from-remoteok.p.rapidapi.com/"):
            if nice_name == "Get list":
                # Experience levels can only be parsed from description/tags
                # description (str)
                # result = extract_value_from_dict(
                #         key_name='description',
                #         dict_new=dict_new
                #     )
                # tags (List)
                # result2 = extract_value_from_dict(
                #         key_name='tags',
                #         dict_new=dict_new
                #     )
                return (
                    {
                        "error":
                            "Experience Levels not listed in data from API."
                    }
                )

        # Freshdata | Fresh Linkedin Profile Data
        # Freshdata | Linkedin Jobs
        # Get Job Details
        case ("https://linkedin-jobs4.p.rapidapi.com"
              "/get-job-details" |
              "https://fresh-linkedin-profile-data.p.rapidapi.com"
              "/get-job-details"):
            if nice_name == "Get Job Details":
                # Experience levels can be parsed from job_description value
                return (
                    {
                        "error":
                            "Experience Levels not listed in data from API."
                    }
                )

        # Freshdata | Fresh Linkedin Profile Data
        # Freshdata | Linkedin Jobs
        # Search Jobs
        case ("https://fresh-linkedin-profile-data.p.rapidapi.com"
              "/search-jobs" |
              "https://linkedin-jobs4.p.rapidapi.com"
              "/search-jobs"):
            if nice_name == "Search Jobs":
                # Experience levels can only be parsed from Job Details
                return (
                    {
                        "error":
                            "Experience Levels not listed in data from API."
                    }
                )

        # jaypat87 | Indeed
        # Search
        case ("https://indeed11.p.rapidapi.com"
              "/"):
            if nice_name == "Search":
                # Experience levels can be parsed from summary
                return (
                    {
                        "error":
                            "Experience Levels not listed in data from API."
                    }
                )

        # jaypat87 | Job Search
        # Jobs Search
        # Job Description Full-Text
        case ("https://job-search15.p.rapidapi.com"
              "/"):
            if (nice_name == "Jobs Search" or
                    nice_name == "Job Description Full-Text"):

                # Experience levels can be parsed from full_text
                return (
                    {
                        "error":
                            "Experience Levels not listed in data from API."
                    }
                )

        # jaypat87 | Linkedin Jobs Search
        # Search
        case ("https://linkedin-jobs-search.p.rapidapi.com"
              "/"):
            if nice_name == "Search":

                # Experience levels can only be parsed from job Details
                return (
                    {
                        "error":
                            "Experience Levels not listed in data from API."
                    }
                )

        # jobicy | Remote Jobs API
        # Remote Jobs API
        case ("https://jobicy.p.rapidapi.com"
              "/api/v2/remote-jobs"):
            if nice_name == "Remote Jobs API":
                if (dict_new.get('success', None) is not None and
                        dict_new.get('success', False) is False):
                    return (
                        {
                            "error":
                                "Query was not processed"
                        }
                    )

                # Experience levels can be parsed from jobDescription
                return (
                    {
                        "error":
                            "Experience Levels not listed in data from API."
                    }
                )

        # jobisite | Job Search
        # Search Jobs
        case ("https://job-search38.p.rapidapi.com"
              "/my/searchJobs"):
            if nice_name == "Search Jobs":
                # Experience levels can be parsed from description
                return (
                    {
                        "error":
                            "Experience Levels not listed in data from API."
                    }
                )

        # JobsAPI2020 | Zambian Jobs API
        # httpsJobapiCoUkGet
        case ("https://zambian-jobs-api1.p.rapidapi.com"
              "/getdataNew.php"):
            if nice_name == "httpsJobapiCoUkGet":
                return (
                    {
                        "error":
                            "Experience Levels not listed in data from API."
                    }
                )

        # Jobwiz | Job Search API
        # searchJob
        case ("https://job-search-api1.p.rapidapi.com"
              "/v1/job-description-search"):
            if nice_name == "searchJob":
                # Experience levels can be parsed from plain_text_description
                return (
                    {
                        "error":
                            "Experience Levels not listed in data from API."
                    }
                )

        # letscrape | Job Salary Data
        # Job Salary
        case ("https://job-salary-data.p.rapidapi.com"
              "/job-salary"):
            if nice_name == "Job Salary":
                return (
                    {
                        "error":
                            "Data does not include any Experience Levels."
                    }
                )

        # letscrape | JSearch
        # Search
        case ("https://jsearch.p.rapidapi.com"
              "/search"):
            if nice_name == "Search":
                # Search includes usable data
                # job_highlights -> Qualifications (List)
                # other keys:
                # job_required_experience key
                # job_required_education key

                # return (
                #     extract_value_from_dict_nested(
                #         key_name="job_highlights",
                #         key_name_nested="Qualifications",
                #         dict_new=dict_new
                #     )
                # )

                return (
                    {
                        "error":
                            "Data does not include any Experience Levels."
                    }
                )

        # letscrape | JSearch
        # Search Filters
        case ("https://jsearch.p.rapidapi.com"
              "/search-filters"):
            if nice_name == "Search Filters":
                # result = (
                #     extract_from_list_dict(
                #         key_name='name',
                #         list_new=dict_new.get('job_requirements')
                #     )
                # )
                #
                # return result

                return (
                    {
                        "error":
                            "Data does not include any Experience Levels."
                    }
                )

        # letscrape | JSearch
        # Job Details
        case ("https://jsearch.p.rapidapi.com"
              "/job-details"):
            if nice_name == "Job Details":
                # Job details include usable data
                # job_highlights -> Qualifications (List)
                # other keys:
                # job_required_experience key
                # job_required_education key

                # return (
                #     extract_value_from_dict_nested(
                #         key_name="job_highlights",
                #         key_name_nested="Qualifications",
                #         dict_new=dict_new
                #     )
                # )

                return (
                    {
                        "error":
                            "Data does not include any Experience Levels."
                    }
                )

        # letscrape | Real-Time Glassdoor Data
        # Company Search
        case ("https://real-time-glassdoor-data.p.rapidapi.com"
              "/company-search"):
            if nice_name == "Company Search":
                return (
                    {
                        "error":
                            "Data does not include any job Experience Levels."
                    }
                )

        # letscrape | Real-Time Glassdoor Data
        # Company Reviews
        case ("https://real-time-glassdoor-data.p.rapidapi.com"
              "/company-reviews"):
            if nice_name == "Company Reviews":
                return (
                    {
                        "error":
                            "Experience Levels not listed in review details."
                    }
                )

        # letscrape | Real-Time Glassdoor Data
        # Company Overview
        case ("https://real-time-glassdoor-data.p.rapidapi.com"
              "/company-overview"):
            if nice_name == "Company Overview":
                return (
                    {
                        "error":
                            "Experience Levels not listed in review details."
                    }
                )

        # Lundehund | Twitter X Job API
        # Get Job Detail
        case ("https://twitter-x-api.p.rapidapi.com"
              "/api/job/detail"):
            if nice_name == "Get Job Detail":
                # Experience levels can be parsed from job_description value
                return (
                    {
                        "error":
                            "Experience Levels not listed in data from API."
                    }
                )

        # Lundehund | Twitter X Job API
        # Search Job
        case ("https://twitter-x-api.p.rapidapi.com"
              "/api/job/search"):
            if nice_name == "Search Job":
                return (
                    {
                        "error":
                            "Experience Levels not listed in data from API."
                    }
                )

        # Lundehund | Twitter X Job API
        # Search Location
        case ("https://twitter-x-api.p.rapidapi.com"
              "/api/job/search/location"):
            if nice_name == "Search Location":
                return (
                    {
                        "error":
                            "Experience Levels not in Search location "
                            "queries."
                    }
                )

        # mantiks | Glassdoor
        # Companies Search
        case ("https://glassdoor.p.rapidapi.com"
              "/companies/search"):
            if nice_name == "Companies Search":
                # print("Company data from API does not include Experience "
                #       "Levels.", flush=True)

                return (
                    {
                        "error":
                            "Data from API does not "
                            "include Experience Levels."
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
                # Experience levels can be parsed from description data
                return (
                    {
                        "error":
                            "Experience Levels not listed in data from API."
                    }
                )

        # mantiks | Glassdoor
        # Jobs Search
        case ("https://glassdoor.p.rapidapi.com"
              "/jobs/search"):
            if nice_name == "Jobs Search":
                # Experience levels can be parsed from Job details endpoint.
                return (
                    {
                        "error":
                            "Experience Levels not listed in data from API."
                    }
                )

        # mantiks | Glassdoor
        # Locations Search
        case ("https://glassdoor.p.rapidapi.com"
              "/locations/search"):
            if nice_name == "Locations Search":
                return (
                    {
                        "error":
                            "Experience Levels not listed in Search location "
                            "queries."
                    }
                )

        # mantiks | Indeed
        # Job details
        case ("https://indeed12.p.rapidapi.com"
              "/job/"):
            if nice_name == "Job details":
                # Experience levels can be parsed from description
                return (
                    {
                        "error":
                            "Experience Levels not listed in data from API."
                    }
                )

        # mantiks | Indeed
        # Jobs Search
        case ("https://indeed12.p.rapidapi.com"
              "/jobs/search"):
            if nice_name == "Jobs Search":
                return (
                    {
                        "error":
                            "Experience Levels not listed in data from API."
                    }
                )

        # mantiks | Indeed
        # Company Search
        case ("https://indeed12.p.rapidapi.com"
              "/companies/search"):
            if nice_name == "Company Search":
                return (
                    {
                        "error":
                            "Experience Levels not listed in data from API."
                    }
                )

        # mantiks | Indeed
        # Company details
        # Company jobs
        case ("https://indeed12.p.rapidapi.com"
              "/company/"):
            if nice_name == "Company details":
                return (
                    {
                        "error":
                            "Experience Levels not listed in data from API."
                    }
                )

            elif nice_name == "Company jobs":
                # must be parsed from job details using ID

                return (
                    {
                        "error":
                            "Experience Levels not listed "
                            "specifically in data."
                    }
                )

        # mgujjargamingm | LinkedIn Data Scraper
        # Company Data
        case ("https://linkedin-data-scraper.p.rapidapi.com"
              "/company" |
              "https://linkedin-bulk-data-scraper.p.rapidapi.com"
              "/company"):
            if nice_name == "Company Data":
                return (
                    {
                        "error":
                            "Experience Levels not listed in data from API."
                    }
                )

        # mgujjargamingm | LinkedIn Data Scraper
        # Company Data (Premium)
        case ("https://linkedin-data-scraper.p.rapidapi.com"
              "/company_pro" |
              "https://linkedin-bulk-data-scraper.p.rapidapi.com"
              "/company_pro"):
            if nice_name == "Company Data (Premium)":
                return (
                    {
                        "error":
                            "Experience Levels not listed in data from API."
                    }
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

                return (
                    {
                        "error":
                            "Experience Levels not listed in data from API."
                    }
                )

        # mgujjargamingm | LinkedIn Data Scraper
        # Company Jobs
        case ("https://linkedin-data-scraper.p.rapidapi.com"
              "/company_jobs" |
              "https://linkedin-bulk-data-scraper.p.rapidapi.com"
              "/company_jobs"):
            if nice_name == "Company Jobs":
                # can be parsed from 'jobDescription'

                return (
                    {
                        "error":
                            "Experience Levels not listed "
                            "specifically in data."
                    }
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
                return (
                    extract_value_from_dict(
                        key_name="formattedExperienceLevel",
                        dict_new=dict_new
                    )
                )

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
                result = {}
                for i in dict_new.keys():
                    if dict_new[i].get('formattedExperienceLevel') is not None:
                        result[i] = dict_new[i].get('formattedExperienceLevel')
                    else:
                        return {
                            "error":
                                "Data from API does not provide appropriate "
                                "data."
                        }

                return result

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

                return (
                    {
                        "error":
                            "Experience Levels not listed "
                            "specifically in data."
                    }
                )

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
                # Experience Levels must be queried individually
                # or parsed from 'bio' key
                return (
                    {
                        "error":
                            "Experience Levels not listed "
                            "specifically in data."
                    }
                )

        # omarmohamed0 | Jobs API
        # All remote (Freelance jobs)
        case ("https://freelancer-api.p.rapidapi.com"
              "/api/find-job" |
              "https://freelancer-api.p.rapidapi.com"
              "/api/find-job/"):
            if (nice_name == "Get All Jobs" or
                    nice_name == "Get all jobs in specific page"):
                # Experience Levels must be queried individually
                # or parsed from 'project_description' key

                return (
                    {
                        "error":
                            "Experience Levels not listed "
                            "specifically in data."
                    }
                )

        # Pat92 | Jobs API
        # List Jobs
        case ("https://jobs-api14.p.rapidapi.com"
              "/list"):
            if nice_name == "List Jobs":
                # Experience Levels must be queried individually
                # or parsed from 'description' key

                return (
                    {
                        "error":
                            "Experience Levels not listed "
                            "specifically in data."
                    }
                )

        # Pat92 | Jobs API
        # Get salary range
        case ("https://jobs-api14.p.rapidapi.com"
              "/salary/getSalaryRange"):
            if nice_name == "Get salary range":
                return (
                    {
                        "error":
                            "Experience Levels not listed in salary data."
                    }
                )

        # Pat92 | Jobs API
        # Get job titles
        case ("https://jobs-api14.p.rapidapi.com"
              "/salary/getJobTitles"):
            if nice_name == "Get job titles":
                # print("Data from API does not include Experience Levels.",
                #       flush=True)
                return (
                    {
                        "error":
                            "Data from API does not "
                            "include Experience Levels."
                    }
                )

        # qurazor1 | Remoote Job Search
        # list_skills_skills_get
        case ("https://remoote-job-search1.p.rapidapi.com"
              "/remoote/skills"):
            if nice_name == "list_skills_skills_get":
                # print("Data from API does not include "
                #       "Experience Levels data.", flush=True)
                return (
                    {
                        "error":
                            "Data from API does not "
                            "include Experience Levels data."
                    }
                )

        # qurazor1 | Remoote Job Search
        # list_jobs_jobs_get
        case ("https://remoote-job-search1.p.rapidapi.com"
              "/remoote/jobs"):
            if nice_name == "list_jobs_jobs_get":
                # print("Data from API does not include Experience Levels.",
                #       flush=True)

                return (
                    {
                        "error":
                            "Data from API does not "
                            "include Experience Levels."
                    }
                )
                # result = (
                #     extract_value_from_dict(
                #         key_name='requirements_raw',
                #         dict_new=dict_new
                #     )
                # )
                # result2 = (
                #     extract_value_from_dict(
                #         key_name='skills',
                #         dict_new=dict_new
                #     )
                # )
                # return result

        # qurazor1 | Remoote Job Search
        # get_related_jobs_jobs__int_id___related_post
        case ("https://remoote-job-search1.p.rapidapi.com"
              "/remoote/jobs/"):
            if nice_name == "get_related_jobs_jobs__int_id___related_post":
                # print("Data from API does not include Experience Levels.",
                #       flush=True)

                return (
                    {
                        "error":
                            "Data from API does not "
                            "include Experience Levels."
                    }
                )

        # qurazor1 | Remoote Job Search
        # list_countries_countries_get
        case ("https://remoote-job-search1.p.rapidapi.com"
              "/remoote/countries"):
            if nice_name == "list_countries_countries_get":
                # print("Data from API does not include Experience Levels.",
                #       flush=True)

                return (
                    {
                        "error":
                            "Data from API does not "
                            "include Experience Levels."
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
                            "Data from API is used for token"
                            " generation only"
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
                    {
                        "error":
                            "Data from API is not used for Experience Levels."
                    }
                )

        # Relu Consultancy | Arbeitsagentur
        # Get Token
        case ("https://indeed-scraper-api-germany.p.rapidapi.com"
              "/get-token"):
            if nice_name == "Get Token":
                # print("Data from API is used for token generation only",
                #       flush=True)

                return (
                    {
                        "error":
                            "Data from API is used for token"
                            " generation only"
                    }
                )

        # Relu Consultancy | Indeed Scraper API - Germany
        # Search Jobs
        case ("https://indeed-scraper-api-germany.p.rapidapi.com"
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
                    {
                        "error":
                            "Data from API is not used for Experience Levels."
                    }
                )

        # Relu Consultancy | Indeed Scraper API - Germany
        # Job View
        case ("https://indeed-scraper-api-germany.p.rapidapi.com"
              "/jobview"):
            if nice_name == "Job View":
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

                return (
                    {
                        "error":
                            "Data from API is not used for Experience Levels."
                    }
                )

        # RockAPIs | Linkedin API
        # Search Employees
        case ("https://linkedin-api8.p.rapidapi.com"
              "/search-employees"):
            # This API Provider doesn't like multiple free accounts
            if nice_name == "Search Employees":
                return (
                    {
                        "error":
                            "Data from API is not used for Experience Levels."
                    }
                )

        # RockAPIs | Linkedin API
        # Get Company Details
        case ("https://linkedin-api8.p.rapidapi.com"
              "/get-company-details"):
            # This API Provider doesn't like multiple free accounts
            if nice_name == "Get Company Details":
                # print("Data from API cannot be used to "
                #       "find Experience Levels.", flush=True)

                return (
                    {
                        "error":
                            "Data from API is not used for Experience Levels."
                    }
                )

        # RockAPIs | Linkedin API
        # Get Company By Domain (BETA)
        case ("https://linkedin-api8.p.rapidapi.com"
              "/get-company-by-domain"):
            if nice_name == "Get Company By Domain (BETA)":
                # print("Data from API cannot be used to "
                #       "find Experience Levels.", flush=True)

                return (
                    {
                        "error":
                            "Data from API is not used for Experience Levels."
                    }
                )

        # RockAPIs | Linkedin API
        # Get Company Insights [PREMIUM] (Beta)
        case ("https://linkedin-api8.p.rapidapi.com"
              "/get-company-insights"):
            if nice_name == "Get Company Insights [PREMIUM] (Beta)":
                # print("Data from API cannot be used to find "
                #       "Experience Levels.", flush=True)

                return (
                    {
                        "error":
                            "Data from API is not used for Experience Levels."
                    }
                )

        # RockAPIs | Linkedin API
        # Get Company Employees Count
        case ("https://linkedin-api8.p.rapidapi.com"
              "/get-company-employees-count"):
            if nice_name == "Get Company Employees Count":
                # print("Data from API cannot be used to "
                #       "find Experience Levels.", flush=True)

                return (
                    {
                        "error":
                            "Data from API is not used for Experience Levels."
                    }
                )

        # RockAPIs | Linkedin API
        # Get Company Jobs Count
        case ("https://linkedin-api8.p.rapidapi.com"
              "/get-company-jobs-count"):
            if nice_name == "Get Company Jobs Count":
                # print("Data from API cannot be used to find "
                #       "Experience Levels.", flush=True)

                return (
                    {
                        "error":
                            "Data from API is not used for Experience Levels."
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
        # Search Jobs V2
        # Search Jobs
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
                if (str(dict_new) == '''{'message': 'Blocked User. Please \
contact your API provider.'}'''):
                    return (
                        {
                            "error":
                                "Search query failed"
                        }
                    )

                return (
                    {
                        "error":
                            "Data from API is not used for Experience Levels."
                    }
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
                # print("Data from API cannot be used to "
                #       "find Experience Levels.", flush=True)

                return (
                    {
                        "error":
                            "Data from API is not used for Experience Levels."
                    }
                )

        # sohailglt | Linkedin Live Data
        # People Search
        case ("https://linkedin-live-data.p.rapidapi.com"
              "/people-search"):
            if nice_name == "People Search":
                return (
                    {
                        "error":
                            "Unclear data returned from "
                            "API/Endpoint is broken."
                    }
                )

        # sohailglt | Linkedin Live Data
        # Get Profile Details
        # Get Company Details
        case ("https://linkedin-live-data.p.rapidapi.com"
              "/profile-details"):
            if nice_name == "Get Company Details":
                return (
                    {
                        "error":
                            "Data from API does not include a description or "
                            "experience level data."
                    }
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
                # print("Data from API is used for Industries List "
                #       "DB generation only", flush=True)

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
        # SearchJobs
        case ("https://indeed-jobs-api.p.rapidapi.com"
              "/indeed-us/" |
              "https://indeed-jobs-api-finland.p.rapidapi.com"
              "/indeed-fi/" |
              "https://indeed-jobs-api-sweden.p.rapidapi.com"
              "/indeed-se/" |
              "https://indeed-jobs-api-denmark.p.rapidapi.com"
              "/indeed-dk/"):
            if nice_name == "SearchJobs":
                error_keyword = '''\
{'Error': "Jobs API returned no data, You have entered'''
                if error_keyword in str(dict_new)[:len(error_keyword)]:
                    return (
                        {
                            "error":
                                "Search query failed"
                        }
                    )
                return (
                    {
                        "error":
                            "Data from API does not include a description or "
                            "experience level data."
                    }
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
