"""
Get Companies
main function that converts a company string to a parsed company dictionary.
"""
import ast
import re

from routines import (
    extract_value_from_dict,
    extract_value_from_dict_nested,
    extract_from_list_dict
)


def clean_extras_from_company(company_str: str):
    return re.compile(
        '|'.join(
            map(
                re.escape,
                [
                    "Incorporated",
                    "Corporation",
                    "Inc.",
                    "Inc",
                    "LLC",
                    "Corp.",
                    "Ltd.",
                    "LTD",
                    "Co."
                ]
            )
        ),
        re.IGNORECASE
    ).sub('', company_str) if (company_str is not None and
                               len(company_str) != 0) else None


def clean_company_str(company_str: str):
    """
    Cleans company string for proper parsing
    """
    if company_str is None or len(company_str) == 0:
        return None

    company_str = re.sub(
        r'[^\w\s.&\'\-/(),\[\]+@":;|]',
        '',
        clean_extras_from_company(company_str),
    ).strip()

    if company_str is None or len(company_str) == 0:
        return None

    if company_str[0] == '-':
        company_str = company_str[1:].strip()

    if company_str is None:
        return None

    if company_str[0] == '_':
        company_str = company_str[1:].strip()

    if company_str is None:
        return None

    if company_str.endswith(','):
        company_str = company_str.rstrip(",").strip()

    if company_str is None:
        return None

    if company_str.endswith('.'):
        company_str = company_str.rstrip(".").strip()

    if company_str is None:
        return None

    if company_str.find(', ,'):
        company_str = company_str.replace(', ,', ',').strip()

    if company_str is None:
        return None

    while 'GmbH' in company_str:
        company_str = company_str.replace("GmbH", "").strip()

    if company_str is None:
        return None

    if "Other Agencies and Independent Organizations -" in company_str:
        company_str = company_str.replace(
            "Other Agencies and Independent Organizations -",
            ''
        ).strip()

    if company_str is None:
        return None

    if "Other Agencies and Independent Organizations " in company_str:
        company_str = company_str.replace(
            "Other Agencies and Independent Organizations ",
            ''
        ).strip()

    if company_str is None:
        return None

    if "Department of the " in company_str:
        company_str = company_str.replace(
            "Department of the ",
            ''
        ).strip()

    if company_str is None:
        return None

    if "Department of " in company_str:
        company_str = company_str.replace(
            "Department of ",
            ''
        ).strip()

    if company_str is None:
        return None

    while '  ' in company_str:
        company_str = company_str.replace("  ", " ").strip()

    if company_str is None or len(company_str) == 0 or company_str == ' ':
        return None

    return company_str.strip()


def get_companies(
        api_url: str,
        nice_name: str,
        dict_new: dict,
        input_json: dict):
    """
    Converts a jobs dictionary to a parsed company dictionary
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
                        key_name='hiringOrganizationName',
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if (result[i] is None or
                            len(result[i]) == 0):
                        result[i] = dict_new[i].get('domain')

                        if (result[i] is not None and
                                len(result[i]) != 0):
                            result[i] = clean_company_str(result[i])

                return result

        # APIJobs | Job Searching API
        # Search organization
        case ("https://apijob-job-searching-api.p.rapidapi.com"
              "/v1/organization/search"):
            if nice_name == "Search organization":
                # Fix filter to show domain name instead.
                result = (
                    extract_value_from_dict(
                        key_name='domain',
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

        # APIJobs | Job Searching API
        # Get job by id
        case ("https://apijob-job-searching-api.p.rapidapi.com"
              "/v1/job/"):
            if nice_name == "Get job by id":
                result = (
                    extract_value_from_dict(
                        key_name='hiringOrganizationName',
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

        # avadataservices | Job Postings
        # /api/v2/Jobs/{slug}
        case ("https://job-postings1.p.rapidapi.com"
              "/api/v2/Jobs/"):
            if nice_name == "/api/v2/Jobs/{slug}":
                result = (
                    extract_value_from_dict(
                        key_name='company',
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

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
                result = (
                    extract_value_from_dict(
                        key_name='company',
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

        # bareq | Remote Jobs API
        # List jobs free
        case ("https://remote-jobs-api1.p.rapidapi.com"
              "/jobs/free"):
            if nice_name == "List jobs free":
                result = (
                    extract_value_from_dict(
                        key_name='companyName',
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

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
                        key_name='companyName',
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

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
            # print("Data from API does not include company_name. Each job "
            #       "listing must be queried individually.", flush=True)
            return (
                {
                    "error":
                        "Data from API does not include "
                        "company_name. Each job listing "
                        "must be queried individually."
                }
            )

        # Dodocr7 | Google Jobs
        # OfferInfo
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
                        key_name='company',
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
                result = (
                    extract_value_from_dict(
                        key_name='organization',
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

        # Flatroy | Jobs from Remoteok
        # Get list
        case ("https://jobs-from-remoteok.p.rapidapi.com/"):
            if nice_name == "Get list":
                # strip key 0 from list
                if '0' in dict_new.keys():
                    dict_new.pop('0', None)

                result = (
                    extract_value_from_dict(
                        key_name='company',
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

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
                        key_name='company_name',
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

        # Freshdata | Fresh Linkedin Profile Data
        # Freshdata | Linkedin Jobs
        # Search Jobs
        case ("https://fresh-linkedin-profile-data.p.rapidapi.com"
              "/search-jobs" |
              "https://linkedin-jobs4.p.rapidapi.com"
              "/search-jobs"):
            if nice_name == "Search Jobs":
                result = (
                    extract_value_from_dict(
                        key_name='company',
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

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
                result = (
                    extract_value_from_dict(
                        key_name='company_name',
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

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
                result = (
                    extract_value_from_dict(
                        key_name='company_name',
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

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
                result = (
                    extract_value_from_dict(
                        key_name='companyName',
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

        # jobisite | Job Search
        # Search Jobs
        case ("https://job-search38.p.rapidapi.com"
              "/my/searchJobs"):
            if nice_name == "Search Jobs":
                result = (
                    extract_value_from_dict(
                        key_name='companyName',
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] == "---":
                        result[i] = None
                    elif (result[i] is None or len(result[i]) == 0 or
                          len(result[i]) == 0):
                        result[i] = None

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

        # JobsAPI2020 | Zambian Jobs API
        # httpsJobapiCoUkGet
        case ("https://zambian-jobs-api1.p.rapidapi.com"
              "/getdataNew.php"):
            if nice_name == "httpsJobapiCoUkGet":
                result = (
                    extract_value_from_dict(
                        key_name='company',
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

        # Jobwiz | Job Search API
        # searchJob
        case ("https://job-search-api1.p.rapidapi.com"
              "/v1/job-description-search"):
            if nice_name == "searchJob":
                result = (
                    extract_value_from_dict(
                        key_name="company_name",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

        # letscrape | Job Salary Data
        # Job Salary
        case ("https://job-salary-data.p.rapidapi.com"
              "/job-salary"):
            if nice_name == "Job Salary":
                return (
                    {
                        "error":
                            "Data does not include any companies."
                    }
                )

        # letscrape | JSearch
        # Search
        case ("https://jsearch.p.rapidapi.com"
              "/search"):
            if nice_name == "Search":
                result = (
                    extract_value_from_dict(
                        key_name="employer_name",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

        # letscrape | JSearch
        # Search Filters
        case ("https://jsearch.p.rapidapi.com"
              "/search-filters"):
            if nice_name == "Search Filters":
                result = (
                    extract_from_list_dict(
                        key_name='name',
                        list_new=dict_new.get('employers')
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

        # letscrape | JSearch
        # Job Details
        case ("https://jsearch.p.rapidapi.com"
              "/job-details"):
            if nice_name == "Job Details":
                result = (
                    extract_value_from_dict(
                        key_name="employer_name",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

        # letscrape | Real-Time Glassdoor Data
        # Company Search
        case ("https://real-time-glassdoor-data.p.rapidapi.com"
              "/company-search"):
            if nice_name == "Company Search":
                result = (
                    extract_value_from_dict(
                        key_name="name",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

        # letscrape | Real-Time Glassdoor Data
        # Company Reviews
        case ("https://real-time-glassdoor-data.p.rapidapi.com"
              "/company-reviews"):
            if nice_name == "Company Reviews":
                return (
                    {
                        "error":
                            "Company names not listed in review details."
                    }
                )

        # letscrape | Real-Time Glassdoor Data
        # Company Overview
        case ("https://real-time-glassdoor-data.p.rapidapi.com"
              "/company-overview"):
            if nice_name == "Company Overview":
                result = (
                    extract_value_from_dict(
                        key_name="name",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

        # Lundehund | Twitter X Job API
        # Search Job
        # Get Job Detail
        case ("https://twitter-x-api.p.rapidapi.com"
              "/api/job/search" |
              "https://twitter-x-api.p.rapidapi.com"
              "/api/job/detail"):
            if (nice_name == "Search Job" or
                    nice_name == "Get Job Detail"):
                result = (
                    extract_value_from_dict(
                        key_name="company",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

        # Lundehund | Twitter X Job API
        # Search Location
        case ("https://twitter-x-api.p.rapidapi.com"
              "/api/job/search/location"):
            if nice_name == "Search Location":
                return (
                    {
                        "error":
                            "Company names not listed in Search location "
                            "queries."
                    }
                )

        # mantiks | Glassdoor
        # Companies Search
        case ("https://glassdoor.p.rapidapi.com"
              "/companies/search"):
            if nice_name == "Companies Search":
                result = (
                    extract_value_from_dict(
                        key_name="name",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

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
                # Dictionary fix for single item dict
                result = (
                    extract_value_from_dict_nested(
                        key_name="company",
                        key_name_nested="name",
                        dict_new={input_json.get('job_id'): dict_new}
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

        # mantiks | Glassdoor
        # Jobs Search
        case ("https://glassdoor.p.rapidapi.com"
              "/jobs/search"):
            if nice_name == "Jobs Search":
                result = (
                    extract_value_from_dict_nested(
                        key_name="company",
                        key_name_nested="name",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

        # mantiks | Glassdoor
        # Locations Search
        case ("https://glassdoor.p.rapidapi.com"
              "/locations/search"):
            if nice_name == "Locations Search":
                return (
                    {
                        "error":
                            "Company names not listed in Search location "
                            "queries."
                    }
                )

        # mantiks | Indeed
        # Job details
        case ("https://indeed12.p.rapidapi.com"
              "/job/"):
            if nice_name == "Job details":
                result = (
                    extract_value_from_dict_nested(
                        key_name="company",
                        key_name_nested="name",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

        # mantiks | Indeed
        # Jobs Search
        case ("https://indeed12.p.rapidapi.com"
              "/jobs/search"):
            if nice_name == "Jobs Search":
                result = (
                    extract_value_from_dict(
                        key_name="company_name",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

        # mantiks | Indeed
        # Company Search
        case ("https://indeed12.p.rapidapi.com"
              "/companies/search"):
            if nice_name == "Company Search":
                result = (
                    extract_value_from_dict(
                        key_name="name",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

        # mantiks | Indeed
        # Company details
        # Company jobs
        case ("https://indeed12.p.rapidapi.com"
              "/company/"):
            if nice_name == "Company details":
                # Dictionary fix for single item dict
                result = (
                    extract_value_from_dict(
                        key_name="name",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

            elif nice_name == "Company jobs":
                new_dict = {}
                company = input_json.get('company_id')
                for j in dict_new.keys():
                    new_dict[str(j)] = clean_company_str(str(company))

                return new_dict

        # mgujjargamingm | LinkedIn Data Scraper
        # Company Data
        case ("https://linkedin-data-scraper.p.rapidapi.com"
              "/company" |
              "https://linkedin-bulk-data-scraper.p.rapidapi.com"
              "/company"):
            if nice_name == "Company Data":
                result = (
                    extract_value_from_dict(
                        key_name="company_name",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

        # mgujjargamingm | LinkedIn Data Scraper
        # Company Data (Premium)
        case ("https://linkedin-data-scraper.p.rapidapi.com"
              "/company_pro" |
              "https://linkedin-bulk-data-scraper.p.rapidapi.com"
              "/company_pro"):
            if nice_name == "Company Data (Premium)":
                result = (
                    extract_value_from_dict(
                        key_name="companyName",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

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

                result = (
                    extract_value_from_dict(
                        key_name="company_name",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

        # mgujjargamingm | LinkedIn Data Scraper
        # Company Jobs
        case ("https://linkedin-data-scraper.p.rapidapi.com"
              "/company_jobs" |
              "https://linkedin-bulk-data-scraper.p.rapidapi.com"
              "/company_jobs"):
            if nice_name == "Company Jobs":
                result = (
                    extract_value_from_dict(
                        key_name="companyName",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

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
                        key_name="companyName",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

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
                    if dict_new[i].get('primaryDescription') is not None:
                        result[i] = clean_company_str(
                            dict_new[i].get('primaryDescription')
                        )
                    else:
                        result[i] = clean_company_str(
                            dict_new[i].get('companyName')
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
                result = (
                    extract_value_from_dict(
                        key_name="companyName",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

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
                result = (
                    extract_value_from_dict(
                        key_name="name",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

        # omarmohamed0 | Jobs API
        # All remote (Freelance jobs)
        case ("https://freelancer-api.p.rapidapi.com"
              "/api/find-job" |
              "https://freelancer-api.p.rapidapi.com"
              "/api/find-job/"):
            if (nice_name == "Get All Jobs" or
                    nice_name == "Get all jobs in specific page" or
                    nice_name == "Get all freelancers in specific page" or
                    nice_name == "Get all freelancers"):
                return (
                    {
                        "error":
                            "Company data not listed in freelancer-type "
                            "jobs"
                    }
                )

        # Pat92 | Jobs API
        # List Jobs
        case ("https://jobs-api14.p.rapidapi.com"
              "/list"):
            if nice_name == "List Jobs":
                result = (
                    extract_value_from_dict(
                        key_name="company",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

        # Pat92 | Jobs API
        # Get salary range
        case ("https://jobs-api14.p.rapidapi.com"
              "/salary/getSalaryRange"):
            if nice_name == "Get salary range":
                return (
                    {
                        "error":
                            "Company data not listed in salary data"
                    }
                )

        # Pat92 | Jobs API
        # Get job titles
        case ("https://jobs-api14.p.rapidapi.com"
              "/salary/getJobTitles"):
            if nice_name == "Get job titles":
                # print("Data from API does not include company names.",
                #       flush=True)
                return (
                    {
                        "error":
                            "Data from API does not include company names."
                    }
                )

        # qurazor1 | Remoote Job Search
        # list_skills_skills_get
        case ("https://remoote-job-search1.p.rapidapi.com"
              "/remoote/skills"):
            if nice_name == "list_skills_skills_get":
                # print("Data from API does not include company data.",
                #       flush=True)
                return (
                    {
                        "error":
                            "Data from API does not include company data."
                    }
                )

        # qurazor1 | Remoote Job Search
        # list_jobs_jobs_get
        case ("https://remoote-job-search1.p.rapidapi.com"
              "/remoote/jobs"):
            if nice_name == "list_jobs_jobs_get":
                # todo: company name can be parsed from scraping the job URL
                # print(str(dict_new), flush=True)
                if len(dict_new) == 0:
                    return {}

                result = (
                    extract_value_from_dict_nested(
                        key_name="company",
                        key_name_nested="title",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if (result[i] is None or
                            len(result[i]) == 0):
                        continue
                    result[i] = clean_company_str(result[i])

                return result

        # qurazor1 | Remoote Job Search
        # get_related_jobs_jobs__int_id___related_post
        case ("https://remoote-job-search1.p.rapidapi.com"
              "/remoote/jobs/"):
            if nice_name == "get_related_jobs_jobs__int_id___related_post":
                result = (
                    extract_value_from_dict_nested(
                        key_name="company",
                        key_name_nested="title",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

        # qurazor1 | Remoote Job Search
        # list_countries_countries_get
        case ("https://remoote-job-search1.p.rapidapi.com"
              "/remoote/countries"):
            if nice_name == "list_countries_countries_get":
                # print("Data from API does not include company data.",
                #       flush=True)
                return (
                    {
                        "error":
                            "Data from API does not include company data."
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
                            "Data from API only gives titles for DB "
                            "population."
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
                            "Data from API is used for token generation "
                            "only"
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
                        key_name="arbeitgeber",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

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
                            "Data from API is used for token "
                            "generation only."
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
                        key_name="companyName",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

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
                        key_name="companyName",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

        # RockAPIs | Linkedin API
        # Search Employees
        case ("https://linkedin-api8.p.rapidapi.com"
              "/search-employees"):
            # This API Provider doesn't like multiple free accounts
            if nice_name == "Search Employees":
                result = (
                    extract_value_from_dict(
                        key_name='currentPositions',
                        dict_new=dict_new
                    )
                )
                new_dict = {}
                for i in result.keys():
                    new_dict[i] = ast.literal_eval(result[i])[0]

                result = (
                    extract_value_from_dict(
                        key_name='companyName',
                        dict_new=new_dict
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

        # RockAPIs | Linkedin API
        # Get Company Details
        case ("https://linkedin-api8.p.rapidapi.com"
              "/get-company-details"):
            # This API Provider doesn't like multiple free accounts
            if nice_name == "Get Company Details":
                result = (
                    extract_value_from_dict(
                        key_name="universalName",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

                return result

        # RockAPIs | Linkedin API
        # Get Company By Domain (BETA)
        case ("https://linkedin-api8.p.rapidapi.com"
              "/get-company-by-domain"):
            if nice_name == "Get Company By Domain (BETA)":
                result = (
                    extract_value_from_dict(
                        key_name="name",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

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
                if (str(dict_new) == '''{'message': 'Blocked User. Please \
contact your API provider.'}'''):
                    return (
                        {
                            "error":
                                "Search query failed"
                        }
                    )
                result = (
                    extract_value_from_dict_nested(
                        key_name="company",
                        key_name_nested="name",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

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
                        key_name="name",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

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
                result = (
                    extract_value_from_dict(
                        key_name='name',
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

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
                # print("Data from API is used for Industries List DB "
                #       "generation only", flush=True)
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
                # print("Data from API is used for Company Types DB generation"
                #       "only", flush=True)
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
                        key_name='company_name',
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if result[i] is None or len(result[i]) == 0:
                        continue
                    result[i] = clean_company_str(result[i])

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
