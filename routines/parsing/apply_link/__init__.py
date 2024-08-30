"""
Get Apply Link
main function that parses API data and retrieves the apply link.
"""
import ast
from routines import (
    extract_value_from_dict,
    extract_value_from_dict_nested,
)


def get_apply_link(
        api_url: str,
        nice_name: str,
        dict_new: dict,
        input_json: dict):
    """
    Converts a jobs dictionary to a parsed Apply Link dictionary
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
                result = (
                    extract_value_from_dict(
                        key_name='url',
                        dict_new=dict_new
                    )
                )
                return result

        # APIJobs | Job Searching API
        # Search organization
        case ("https://apijob-job-searching-api.p.rapidapi.com"
              "/v1/organization/search"):
            if nice_name == "Search organization":
                return (
                    {
                        "error":
                            "Data from API does not include URL link. "
                    }
                )

        # APIJobs | Job Searching API
        # Get job by id
        case ("https://apijob-job-searching-api.p.rapidapi.com"
              "/v1/job/"):
            if nice_name == "Get job by id":
                return (
                    extract_value_from_dict(
                        key_name='url',
                        dict_new=dict_new
                    )
                )

        # avadataservices | Job Postings
        # /api/v2/Jobs/{slug}
        case ("https://job-postings1.p.rapidapi.com"
              "/api/v2/Jobs/"):
            if nice_name == "/api/v2/Jobs/{slug}":
                return (
                    extract_value_from_dict(
                        key_name='url',
                        dict_new=dict_new
                    )
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
                result = (
                    extract_value_from_dict(
                        key_name='url',
                        dict_new=dict_new
                    )
                )
                for i in [i for i in result.keys()]:
                    if i == "N/A":
                        result.pop(i)
                    else:
                        new_link = result[i]
                        if new_link.find('?utm_source=') != -1:
                            new_link = (
                                new_link[:new_link.find('?utm_source=')])
                        if new_link.find('&utm_source=') != -1:
                            new_link = (
                                new_link[:new_link.find('&utm_source=')])
                        result[i] = new_link

                return result

        # bareq | Remote Jobs API
        # Get job by id
        # List jobs free
        case ("https://remote-jobs-api1.p.rapidapi.com"
              "/jobs/free"):
            if (nice_name == "Get job by id" or
                    nice_name == "List jobs free"):
                return (
                    extract_value_from_dict(
                        key_name='url',
                        dict_new=dict_new
                    )
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
                        key_name='jobUrl',
                        dict_new=dict_new
                    )
                )
                for i in result.keys():
                    result[i] = result[i].replace(
                        '?trk=public_jobs_topcard-title', ''
                    )
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
            result = (
                extract_value_from_dict(
                    key_name='url',
                    dict_new=dict_new
                )
            )

            for i in result.keys():
                new_link = result[i]
                if new_link.find('?position=') != -1:
                    new_link = (
                        new_link[:new_link.find('?position=')])
                    result[i] = new_link

            return result

        # Dodocr7 | Google Jobs
        # OfferInfo
        # SearchOffers
        case ("https://google-jobs.p.rapidapi.com/"):
            if nice_name == "OfferInfo":
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
                return (
                    extract_value_from_dict(
                        key_name='googleUrl',
                        dict_new=dict_new
                    )
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
                return (
                    extract_value_from_dict(
                        key_name='url',
                        dict_new=dict_new
                    )
                )

        # Flatroy | Jobs from Remoteok
        # Get list
        case ("https://jobs-from-remoteok.p.rapidapi.com/"):
            if nice_name == "Get list":
                return (
                    extract_value_from_dict(
                        key_name='apply_url',
                        dict_new=dict_new
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

                result = (
                    extract_value_from_dict(
                        key_name='job_url',
                        dict_new=dict_new)
                )

                return result

        # Freshdata | Fresh Linkedin Profile Data
        # Freshdata | Linkedin Jobs
        # Search Jobs
        case ("https://fresh-linkedin-profile-data.p.rapidapi.com"
              "/search-jobs" |
              "https://linkedin-jobs4.p.rapidapi.com"
              "/search-jobs"):
            if nice_name == "Search Jobs":
                if (dict_new.get('message', None) is not None and
                        dict_new['message'] ==
                        "Endpoint '/search-jobs' does not exist"):
                    return (
                        {
                            "error":
                                "Search query failed"
                        }
                    )
                try:
                    result = (
                        extract_value_from_dict(
                            key_name='job_url',
                            dict_new=dict_new
                        )
                    )
                except Exception as e:
                    print(e, flush=True)
                    return (
                        {
                            "error":
                                "Search query failed"
                        }
                    )

                return result

        # jaypat87 | Indeed
        # Search
        case ("https://indeed11.p.rapidapi.com"
              "/"):
            if nice_name == "Search":
                result = (
                    extract_value_from_dict(
                        key_name='url',
                        dict_new=dict_new
                    )
                )
                for i in result.keys():
                    result[i] = result[i][:result[i].find('&bb=')]

                return result

        # jaypat87 | Job Search
        # Jobs Search
        # Job Description Full-Text
        case ("https://job-search15.p.rapidapi.com"
              "/"):
            if (nice_name == "Jobs Search" or
                    nice_name == "Job Description Full-Text"):
                return (
                    extract_value_from_dict(
                        key_name='job_url',
                        dict_new=dict_new
                    )
                )

        # jaypat87 | Linkedin Jobs Search
        # Search
        case ("https://linkedin-jobs-search.p.rapidapi.com"
              "/"):
            if nice_name == "Search":
                result = (
                    extract_value_from_dict(
                        key_name='job_url',
                        dict_new=dict_new
                    )
                )
                for i in result.keys():
                    new_link = result[i]
                    if new_link.find('?position=') != -1:
                        new_link = (
                            new_link[:new_link.find('?position=')])
                    result[i] = new_link

                return result

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

                return (
                    extract_value_from_dict(
                        key_name='url',
                        dict_new=dict_new
                    )
                )

        # jobisite | Job Search
        # Search Jobs
        case ("https://job-search38.p.rapidapi.com"
              "/my/searchJobs"):
            if nice_name == "Search Jobs":
                return (
                    extract_value_from_dict(
                        key_name='ApplyLink',
                        dict_new=dict_new
                    )
                )

        # JobsAPI2020 | Zambian Jobs API
        # httpsJobapiCoUkGet
        case ("https://zambian-jobs-api1.p.rapidapi.com"
              "/getdataNew.php"):
            if nice_name == "httpsJobapiCoUkGet":
                result = (
                    extract_value_from_dict(
                        key_name="application_email",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if (result[i] is not None and
                            result[i] != ''):
                        result[i] = "mailto:" + result[i]
                    else:
                        result[i] = None

                return result

        # Jobwiz | Job Search API
        # searchJob
        case ("https://job-search-api1.p.rapidapi.com"
              "/v1/job-description-search"):
            if nice_name == "searchJob":
                result = (
                    extract_value_from_dict(
                        key_name="application_url",
                        dict_new=dict_new
                    )
                )
                for i in result.keys():
                    result[i] = result[i].replace('''\
?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=\
organic''',  '').replace('''\
?lang=en-us&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&\
utm_medium=organic''',  '').replace('''\
&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium\
=organic''',  '')
                return result

        # letscrape | Job Salary Data
        # Job Salary
        case ("https://job-salary-data.p.rapidapi.com"
              "/job-salary"):
            if nice_name == "Job Salary":
                return (
                    {
                        "error":
                            "Data does not include any Apply Links."
                    }
                )

        # letscrape | JSearch
        # Search
        case ("https://jsearch.p.rapidapi.com"
              "/search"):
            if nice_name == "Search":
                result = (
                    extract_value_from_dict(
                        key_name="job_apply_link",
                        dict_new=dict_new
                    )
                )
                for i in result.keys():
                    new_link = result[i]
                    if new_link.find('?utm_medium=') != -1:
                        new_link = (
                            new_link[:new_link.find('?utm_medium=')])
                    if new_link.find('?domain=') != -1:
                        new_link = (
                            new_link[:new_link.find('?domain=')])
                    if new_link.find('?sortBy=') != -1:
                        new_link = (
                            new_link[:new_link.find('?sortBy=')])
                    if new_link.find('?lastSelectedFacet=') != -1:
                        new_link = (
                            new_link[:new_link.find('?lastSelectedFacet=')])
                    if new_link.find('?ltclid') != -1:
                        new_link = (
                            new_link[:new_link.find('?ltclid')])
                    result[i] = new_link

                return result

        # letscrape | JSearch
        # Search Filters
        case ("https://jsearch.p.rapidapi.com"
              "/search-filters"):
            if nice_name == "Search Filters":
                return (
                    {
                        "error":
                            "Data does not include any job Apply Links."
                    }
                )

        # letscrape | JSearch
        # Job Details
        case ("https://jsearch.p.rapidapi.com"
              "/job-details"):
            if nice_name == "Job Details":
                return (
                    extract_value_from_dict(
                        key_name="job_apply_link",
                        dict_new=dict_new
                    )
                )

        # letscrape | Real-Time Glassdoor Data
        # Company Search
        case ("https://real-time-glassdoor-data.p.rapidapi.com"
              "/company-search"):
            if nice_name == "Company Search":
                return (
                    extract_value_from_dict(
                        key_name="company_link",
                        dict_new=dict_new
                    )
                )

        # letscrape | Real-Time Glassdoor Data
        # Company Reviews
        case ("https://real-time-glassdoor-data.p.rapidapi.com"
              "/company-reviews"):
            if nice_name == "Company Reviews":
                return (
                    {
                        "error":
                            "Apply Links not listed in review details."
                    }
                )

        # letscrape | Real-Time Glassdoor Data
        # Company Overview
        case ("https://real-time-glassdoor-data.p.rapidapi.com"
              "/company-overview"):
            if nice_name == "Company Overview":
                return (
                    extract_value_from_dict(
                        key_name="jobs_link",
                        dict_new=dict_new
                    )
                )

        # Lundehund | Twitter X Job API
        # Get Job Detail
        case ("https://twitter-x-api.p.rapidapi.com"
              "/api/job/detail"):
            if nice_name == "Get Job Detail":
                result = (
                    extract_value_from_dict(
                        key_name="job_page_url",
                        dict_new=dict_new
                    )
                )
                for i in result.keys():
                    new_link = result[i]
                    if new_link[-1] == '?':
                        new_link = new_link[:len(new_link)-1]
                    result[i] = new_link

                return result

        # Lundehund | Twitter X Job API
        # Search Job
        case ("https://twitter-x-api.p.rapidapi.com"
              "/api/job/search"):
            if nice_name == "Search Job":
                result = (
                    extract_value_from_dict(
                        key_name="redirect_url",
                        dict_new=dict_new
                    )
                )
                for i in result.keys():
                    new_link = result[i]
                    if new_link.find('?utm_medium=') != -1:
                        new_link = (
                            new_link[:new_link.find('?utm_medium=')])
                    if new_link.find('?domain=') != -1:
                        new_link = (
                            new_link[:new_link.find('?domain=')])
                    if new_link.find('?sortBy=') != -1:
                        new_link = (
                            new_link[:new_link.find('?sortBy=')])
                    if new_link.find('?lastSelectedFacet=') != -1:
                        new_link = (
                            new_link[:new_link.find('?lastSelectedFacet=')])
                    if new_link.find('?ltclid') != -1:
                        new_link = (
                            new_link[:new_link.find('?ltclid')])
                    if new_link.find('?utm_campaign=') != -1:
                        new_link = (
                            new_link[:new_link.find('?utm_campaign=')])
                    if new_link.find('?lever-source=') != -1:
                        new_link = (
                            new_link[:new_link.find('lever-source=')])
                    if new_link[-1] == '?':
                        new_link = new_link[:len(new_link)-1]
                    result[i] = new_link

                return result

        # Lundehund | Twitter X Job API
        # Search Location
        case ("https://twitter-x-api.p.rapidapi.com"
              "/api/job/search/location"):
            if nice_name == "Search Location":
                return (
                    {
                        "error":
                            "Apply Links not in Search location "
                            "queries."
                    }
                )

        # mantiks | Glassdoor
        # Companies Search
        case ("https://glassdoor.p.rapidapi.com"
              "/companies/search"):
            if nice_name == "Companies Search":
                return (
                    extract_value_from_dict(
                        key_name="final_url",
                        dict_new=dict_new
                    )
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
                # URL only links to company
                # derive Glassdoor ID from job ID query
                # result = dict_new.get('company', None)
                return (
                    {
                        input_json.get('job_id'):
                            ('https://www.glassdoor.com/Job/index.htm?jl=' +
                             input_json.get('job_id'))
                    }
                )

        # mantiks | Glassdoor
        # Jobs Search
        case ("https://glassdoor.p.rapidapi.com"
              "/jobs/search"):
            if nice_name == "Jobs Search":
                # Extra parsing required to retrieve job links
                result = (
                    extract_value_from_dict(
                        key_name="link",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    result[i] = ('https://www.glassdoor.com/Job/index.htm'
                                 '?jl=' + result[i].replace('/job/', ""))

                return result

        # mantiks | Glassdoor
        # Locations Search
        case ("https://glassdoor.p.rapidapi.com"
              "/locations/search"):
            if nice_name == "Locations Search":
                return (
                    {
                        "error":
                            "Apply Links not listed in Search location "
                            "queries."
                    }
                )

        # mantiks | Indeed
        # Job details
        case ("https://indeed12.p.rapidapi.com"
              "/job/"):
            if nice_name == "Job details":
                result = (
                    extract_value_from_dict(
                        key_name='indeed_final_url',
                        dict_new=dict_new
                    )
                )
                for i in result.keys():
                    result[i] = result[i].replace('&vjs=3', '')

                return result

        # mantiks | Indeed
        # Jobs Search
        case ("https://indeed12.p.rapidapi.com"
              "/jobs/search"):
            if nice_name == "Jobs Search":
                result = (
                    extract_value_from_dict(
                        key_name='link',
                        dict_new=dict_new
                    )
                )
                for i in result.keys():
                    result[i] = ('https://www.indeed.com/viewjob?jk=' +
                                 result[i]
                                 .replace('?locality=us', '')
                                 .replace('/job/', '')
                                 )

                return result

        # mantiks | Indeed
        # Company Search
        case ("https://indeed12.p.rapidapi.com"
              "/companies/search"):
            if nice_name == "Company Search":
                return extract_value_from_dict(
                    key_name="indeed_absolute_url",
                    dict_new=dict_new
                )

        # mantiks | Indeed
        # Company details
        # Company jobs
        case ("https://indeed12.p.rapidapi.com"
              "/company/"):
            if nice_name == "Company details":
                result = (
                    extract_value_from_dict(
                        key_name='indeed_final_url',
                        dict_new=dict_new
                    )
                )

                return result

            elif nice_name == "Company jobs":
                result = extract_value_from_dict(
                    key_name="link",
                    dict_new=dict_new
                )

                for i in result.keys():
                    result[i] = ('https://www.indeed.com/viewjob?jk=' +
                                 result[i]
                                 .replace('?locality=us', '')
                                 .replace('/job/', '')
                                 )

                return result

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
                            "Apply Links not listed in data from API."
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
                            "Apply Links not listed in data from API."
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

                return extract_value_from_dict(
                    key_name="url",
                    dict_new=dict_new
                )

        # mgujjargamingm | LinkedIn Data Scraper
        # Company Jobs
        case ("https://linkedin-data-scraper.p.rapidapi.com"
              "/company_jobs" |
              "https://linkedin-bulk-data-scraper.p.rapidapi.com"
              "/company_jobs"):
            if nice_name == "Company Jobs":
                result = (
                    extract_value_from_dict(
                        key_name="companyApplyUrl",
                        dict_new=dict_new
                    )
                )
                for i in result.keys():
                    new_link = result[i]
                    if new_link.find('/?src=Online') != -1:
                        new_link = (
                            new_link[:new_link.find('/?src=Online')])
                    result[i] = new_link

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
                        key_name="jobPostingUrl",
                        dict_new=dict_new
                    )
                )
                for i in result.keys():
                    if result[i] is None:
                        continue
                    result[i] = result[i].replace(
                        '/?trk=jobs_biz_prem_srch', '')

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
                result = {}
                for i in dict_new.keys():
                    if dict_new[i].get('jobPostingUrl') is not None:
                        result[i] = (
                            dict_new[i]
                            .get('jobPostingUrl')
                            .replace('/?trk=jobs_biz_prem_srch', '')
                        )
                    else:
                        result[i] = (
                            "https://www.linkedin.com/jobs/view/" +
                            dict_new[i]
                            .get('jobPostingUrn')
                            .replace('/?trk=jobs_biz_prem_srch', '')
                        )

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
                    extract_value_from_dict(
                        key_name="navigationUrl",
                        dict_new=dict_new
                    )
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
        # All remote (Freelance jobs)
        case ("https://freelancer-api.p.rapidapi.com"
              "/api/find-freelancers" |
              "https://freelancer-api.p.rapidapi.com"
              "/api/find-freelancers/"):
            if (nice_name == "Get all freelancers" or
                    nice_name == "Get all freelancers in specific page"):
                return (
                    extract_value_from_dict(
                        key_name="freelancerProfile",
                        dict_new=dict_new
                    )
                )

        # omarmohamed0 | Jobs API
        # All remote (Freelance jobs)
        case ("https://freelancer-api.p.rapidapi.com"
              "/api/find-job" |
              "https://freelancer-api.p.rapidapi.com"
              "/api/find-job/"):
            if (nice_name == "Get All Jobs" or
                    nice_name == "Get all jobs in specific page"):
                result = (
                    extract_value_from_dict(
                        key_name="project-link",
                        dict_new=dict_new
                    )
                )
                for i in [i for i in result.keys()]:
                    if result[i].find(
                            'https://www.freelancer.com/login') != -1:
                        result.pop(i)

                return result

        # Pat92 | Jobs API
        # List Jobs
        case ("https://jobs-api14.p.rapidapi.com"
              "/list"):
            if nice_name == "List Jobs":
                # Apply links are provided by jobProviders only.
                # jobProviders[List] { jobProvider, url} (Keys)
                # Multiple links are listed. when checking links, expand the
                # list.
                result = (
                    extract_value_from_dict(
                        key_name="jobProviders",
                        dict_new=dict_new
                    )
                )
                for i in result.keys():
                    result[i] = ast.literal_eval(result[i])
                    new_list = []
                    for j in range(len(result[i])):
                        new_link = result[i][j].get('url')
                        if new_link.find('?utm_campaign=') != -1:
                            new_link = (
                                new_link[:new_link.find('?utm_campaign=')])
                        if new_link.find('&utm_campaign=') != -1:
                            new_link = (
                                new_link[:new_link.find('&utm_campaign=')])
                        if new_link.find('?utm_source=') != -1:
                            new_link = (
                                new_link[:new_link.find('?utm_source=')])
                        if new_link.find('?lastSelectedFacet=') != -1:
                            new_link = (
                                new_link[:new_link.find(
                                    '?lastSelectedFacet=')])
                        if new_link.find('?domain=') != -1:
                            new_link = (
                                new_link[:new_link.find('?domain=')])
                        new_list.append(new_link)
                    result[i] = new_list

                return result

        # Pat92 | Jobs API
        # Get salary range
        case ("https://jobs-api14.p.rapidapi.com"
              "/salary/getSalaryRange"):
            if nice_name == "Get salary range":
                return (
                    {
                        "error":
                            "Apply Links not listed in salary data."
                    }
                )

        # Pat92 | Jobs API
        # Get job titles
        case ("https://jobs-api14.p.rapidapi.com"
              "/salary/getJobTitles"):
            if nice_name == "Get job titles":
                # print("Data from API does not include Apply Links.",
                #       flush=True)
                return (
                    {
                        "error":
                            "Data from API does not "
                            "include Apply Links."
                    }
                )

        # qurazor1 | Remoote Job Search
        # list_skills_skills_get
        case ("https://remoote-job-search1.p.rapidapi.com"
              "/remoote/skills"):
            if nice_name == "list_skills_skills_get":
                # print("Data from API does not include Apply Link data.",
                #       flush=True)
                return (
                    {
                        "error":
                            "Data from API does not "
                            "include Apply Link data."
                    }
                )

        # qurazor1 | Remoote Job Search
        # list_jobs_jobs_get
        case ("https://remoote-job-search1.p.rapidapi.com"
              "/remoote/jobs"):
            if nice_name == "list_jobs_jobs_get":
                result = (
                    extract_value_from_dict(
                        key_name='url',
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    new_link = result[i]
                    if new_link.find('?utm_campaign=') != -1:
                        new_link = (
                            new_link[:new_link.find('?utm_campaign=')])
                    result[i] = new_link

                return result

        # qurazor1 | Remoote Job Search
        # get_related_jobs_jobs__int_id___related_post
        case ("https://remoote-job-search1.p.rapidapi.com"
              "/remoote/jobs/"):
            if nice_name == "get_related_jobs_jobs__int_id___related_post":
                result = (
                    extract_value_from_dict(
                        key_name='url',
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    new_link = result[i]
                    if new_link.find('?utm_campaign=') != -1:
                        new_link = (
                            new_link[:new_link.find('?utm_campaign=')])
                    result[i] = new_link

                return result

        # qurazor1 | Remoote Job Search
        # list_countries_countries_get
        case ("https://remoote-job-search1.p.rapidapi.com"
              "/remoote/countries"):
            if nice_name == "list_countries_countries_get":
                # print("Data from API does not include Apply Links.",
                #       flush=True)

                return (
                    {
                        "error":
                            "Data from API does not "
                            "include Apply Links."
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

                result = (
                    extract_value_from_dict(
                        key_name='externeUrl',
                        dict_new=dict_new
                    )
                )
                new_dict = {}
                for i in result.keys():
                    if result[i] is None:
                        continue

                    new_link = result[i]

                    if new_link.find('?utm_source=') != -1:
                        new_link = result[i][:result[i].find('?utm_source=')]

                    if new_link.find('?utm_id=') != -1:
                        new_link = result[i][:result[i].find('?utm_id=')]

                    if new_link.find('?hp_source=') != -1:
                        new_link = result[i][:result[i].find('?hp_source=')]

                    if new_link.find('?jw_chl_seg=') != -1:
                        new_link = result[i][:result[i].find('?jw_chl_seg=')]

                    if new_link.find('&bb=') != -1:
                        new_link = result[i][:result[i].find('&bb=')]

                    new_dict[i] = new_link

                return new_dict

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

                result = (
                    extract_value_from_dict(
                        key_name='jobLink',
                        dict_new=dict_new
                    )
                )
                new_dict = {}

                for i in result.keys():
                    if result[i] is None:
                        continue

                    new_link = result[i]

                    if new_link.find('?utm_source=') != -1:
                        new_link = result[i][:result[i].find('?utm_source=')]

                    if new_link.find('?utm_id=') != -1:
                        new_link = result[i][:result[i].find('?utm_id=')]

                    if new_link.find('?hp_source=') != -1:
                        new_link = result[i][:result[i].find('?hp_source=')]

                    if new_link.find('?jw_chl_seg=') != -1:
                        new_link = result[i][:result[i].find('?jw_chl_seg=')]

                    if new_link.find('&bb=') != -1:
                        new_link = result[i][:result[i].find('&bb=')]

                    new_dict[i] = new_link

                return new_dict

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

                result = (
                    extract_value_from_dict(
                        key_name='jobLink',
                        dict_new=dict_new
                    )
                )

                return result

        # RockAPIs | Linkedin API
        # Search Employees
        case ("https://linkedin-api8.p.rapidapi.com"
              "/search-employees"):
            # This API Provider doesn't like multiple free accounts
            if nice_name == "Search Employees":
                result = (
                    extract_value_from_dict(
                        key_name='profile',
                        dict_new=dict_new
                    )
                )

                return result

        # RockAPIs | Linkedin API
        # Get Company Details
        case ("https://linkedin-api8.p.rapidapi.com"
              "/get-company-details"):
            # This API Provider doesn't like multiple free accounts
            if nice_name == "Get Company Details":
                result = (
                    extract_value_from_dict(
                        key_name='linkedinUrl',
                        dict_new=dict_new
                    )
                )

                return result

        # RockAPIs | Linkedin API
        # Get Company By Domain (BETA)
        case ("https://linkedin-api8.p.rapidapi.com"
              "/get-company-by-domain"):
            if nice_name == "Get Company By Domain (BETA)":
                return (
                    extract_value_from_dict(
                        key_name="linkedinUrl",
                        dict_new=dict_new
                    )
                )

        # RockAPIs | Linkedin API
        # Get Company Insights [PREMIUM] (Beta)
        case ("https://linkedin-api8.p.rapidapi.com"
              "/get-company-insights"):
            if nice_name == "Get Company Insights [PREMIUM] (Beta)":
                # print("Data from API cannot be used to find apply links.",
                #       flush=True)

                return (
                    {
                        "error":
                            "Data from API is not used for apply links."
                    }
                )

        # RockAPIs | Linkedin API
        # Get Company Employees Count
        case ("https://linkedin-api8.p.rapidapi.com"
              "/get-company-employees-count"):
            if nice_name == "Get Company Employees Count":
                # print("Data from API cannot be used to find apply links.",
                #       flush=True)

                return (
                    {
                        "error":
                            "Data from API is not used for apply links."
                    }
                )

        # RockAPIs | Linkedin API
        # Get Company Jobs Count
        case ("https://linkedin-api8.p.rapidapi.com"
              "/get-company-jobs-count"):
            if nice_name == "Get Company Jobs Count":
                # print("Data from API cannot be used to find apply links.",
                #       flush=True)

                return (
                    {
                        "error":
                            "Data from API is not used for apply links."
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

                result = (
                    extract_value_from_dict(
                        key_name='url',
                        dict_new=dict_new
                    )
                )

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
                result = (
                    extract_value_from_dict(
                        key_name='linkedin_url',
                        dict_new=dict_new
                    )
                )
                return result

        # sohailglt | Linkedin Live Data
        # People Search
        case ("https://linkedin-live-data.p.rapidapi.com"
              "/people-search"):
            if nice_name == "People Search":
                return (
                    {
                        "error":
                            "Unclear data returned from API/Endpoint "
                            "is broken."
                    }
                )

        # sohailglt | Linkedin Live Data
        # Get Profile Details
        # Get Company Details
        case ("https://linkedin-live-data.p.rapidapi.com"
              "/profile-details"):
            if nice_name == "Get Company Details":
                result = (
                    extract_value_from_dict_nested(
                        key_name='urls',
                        key_name_nested='li_url',
                        dict_new=dict_new
                    )
                )

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
                # print("Data from API is used for Company Types DB "
                #       "generation only", flush=True)

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
                result = (
                    extract_value_from_dict(
                        key_name='job_url',
                        dict_new=dict_new
                    )
                )
                for i in result.keys():
                    result[i] = result[i][:result[i].find('&from=vjs')]

                return result

        case _:
            print("Unknown API\n"
                  "Debug Info\n"
                  "API URL: " + str(api_url) + "\n"
                  "Name: " + str(nice_name), flush=True)
            raise KeyError("Unknown API: " + api_url + " - " + nice_name)


"""

        # TODO
        case (""
              ""):
            if nice_name == "":
                return None
"""
