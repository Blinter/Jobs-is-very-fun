"""
API Endpoint Type
IntEnum
"""
from enum import IntEnum, Enum


class APIEndpointTypes(IntEnum):
    """
    Enum representing various Endpoint Types mapped to integers.

    Attributes:
        NONE = 0
        CLASSIFY_JOB = 1
        EMPLOYEE_SEARCH = 2
        RECRUITER_SEARCH = 3
        JOB_DETAILS = 4
        JOB_TITLE_SEARCH = 5
        JOB_SKILLS_SEARCH = 6
        JOB_SALARY_MISC = 7
        JOB_YEARS_EXP_MISC = 8
        JOBS_SEARCH = 9
        JOBS_FEED = 10
        JOB_MISC = 11
        LOCATIONS_SEARCH = 12
        LOCATIONS_QUERY = 13
        INDUSTRY_QUERY = 14
        WORKERS_SEARCH = 15
        COMPANY_SEARCH = 16
        COMPANY_DETAILS = 17
        COMPANY_REVIEWS = 18
        COMPANY_POSTS = 19
        COMPANY_MISC = 20
        X_MISC = 21
        PROFILE_SEARCH = 22
        PROFILE_SCRAPE = 23
        PROFILE_POSTS_SEARCH = 24
        PROFILE_MISC = 25
        POSTS_SEARCH = 26
        MISC_CREATE_TOKEN = 27
        MISC_GENERAL = 28
    """
    NONE = 0
    CLASSIFY_JOB = 1
    EMPLOYEE_SEARCH = 2
    RECRUITER_SEARCH = 3
    JOB_DETAILS = 4
    JOB_TITLE_SEARCH = 5
    JOB_SKILLS_SEARCH = 6
    JOB_SALARY_MISC = 7
    JOB_YEARS_EXP_MISC = 8
    JOBS_SEARCH = 9
    JOBS_FEED = 10
    JOB_MISC = 11
    LOCATIONS_SEARCH = 12
    LOCATIONS_QUERY = 13
    INDUSTRY_QUERY = 14
    WORKERS_SEARCH = 15
    COMPANY_SEARCH = 16
    COMPANY_DETAILS = 17
    COMPANY_REVIEWS = 18
    COMPANY_POSTS = 19
    COMPANY_MISC = 20
    X_MISC = 21
    PROFILE_SEARCH = 22
    PROFILE_SCRAPE = 23
    PROFILE_POSTS_SEARCH = 24
    PROFILE_MISC = 25
    POSTS_SEARCH = 26
    MISC_CREATE_TOKEN = 27
    MISC_GENERAL = 28


class APIEndpointTypesDescription(Enum):
    """
    Enum representing various Endpoint Types mapped to integers.

    Attributes:
        NONE = "None"
        CLASSIFY_JOB = "Classify Job"
        EMPLOYEE_SEARCH = "Employee Search"
        RECRUITER_SEARCH = "Recruiter Search"
        JOB_DETAILS = "Job Details"
        JOB_TITLE_SEARCH = "Job Title Search"
        JOB_SKILLS_SEARCH = "Job Skills Search"
        JOB_SALARY_MISC = "Job Salary (Misc.)"
        JOB_YEARS_EXP_MISC = "Job Years Experience (Misc.)"
        JOBS_SEARCH = "Jobs Search"
        JOBS_FEED = "Jobs Feed"
        JOB_MISC = "Job (Misc.)"
        LOCATIONS_SEARCH = "Locations Search"
        LOCATIONS_QUERY = "Locations Query"
        INDUSTRY_QUERY = "Industry Query"
        WORKERS_SEARCH = "Workers Search"
        COMPANY_SEARCH = "Company Search"
        COMPANY_DETAILS = "Company Details"
        COMPANY_REVIEWS = "Company Reviews"
        COMPANY_POSTS = "Company Posts"
        COMPANY_MISC = "Company (Misc.)"
        X_MISC = "X (Misc.)"
        PROFILE_SEARCH = "Profile Search"
        PROFILE_SCRAPE = "Profile Scrape"
        PROFILE_POSTS_SEARCH = "Profile Posts Search"
        PROFILE_MISC = "Profile (Misc.)"
        POSTS_SEARCH = "Posts Search"
        MISC_CREATE_TOKEN = "Create Token (Misc.)"
        MISC_GENERAL = "General (Misc.)"
    """
    NONE = "None (Misc.)"
    CLASSIFY_JOB = "Classify Job"
    EMPLOYEE_SEARCH = "Employee Search"
    RECRUITER_SEARCH = "Recruiter Search"
    JOB_DETAILS = "Job Details"
    JOB_TITLE_SEARCH = "Job Title Search"
    JOB_SKILLS_SEARCH = "Job Skills Search"
    JOB_SALARY_MISC = "Job Salary (Misc.)"
    JOB_YEARS_EXP_MISC = "Job Years Experience (Misc.)"
    JOBS_SEARCH = "Jobs Search"
    JOBS_FEED = "Jobs Feed"
    JOB_MISC = "Job (Misc.)"
    LOCATIONS_SEARCH = "Locations Search"
    LOCATIONS_QUERY = "Locations Query"
    INDUSTRY_QUERY = "Industry Query"
    WORKERS_SEARCH = "Workers Search"
    COMPANY_SEARCH = "Company Search"
    COMPANY_DETAILS = "Company Details"
    COMPANY_REVIEWS = "Company Reviews"
    COMPANY_POSTS = "Company Posts"
    COMPANY_MISC = "Company (Misc.)"
    X_MISC = "X (Misc.)"
    PROFILE_SEARCH = "Profile Search"
    PROFILE_SCRAPE = "Profile Scrape"
    PROFILE_POSTS_SEARCH = "Profile Posts Search"
    PROFILE_MISC = "Profile (Misc.)"
    POSTS_SEARCH = "Posts Search"
    MISC_CREATE_TOKEN = "Create Token (Misc.)"
    MISC_GENERAL = "General (Misc.)"


def api_endpoint_type_to_description(endpoint_type: int):
    """Converts an API Endpoint Type to its description"""
    match endpoint_type:
        case APIEndpointTypes.NONE:
            return APIEndpointTypesDescription.NONE.value
        case APIEndpointTypes.CLASSIFY_JOB:
            return APIEndpointTypesDescription.CLASSIFY_JOB.value
        case APIEndpointTypes.EMPLOYEE_SEARCH:
            return APIEndpointTypesDescription.EMPLOYEE_SEARCH.value
        case APIEndpointTypes.RECRUITER_SEARCH:
            return APIEndpointTypesDescription.RECRUITER_SEARCH.value
        case APIEndpointTypes.JOB_DETAILS:
            return APIEndpointTypesDescription.JOB_DETAILS.value
        case APIEndpointTypes.JOB_TITLE_SEARCH:
            return APIEndpointTypesDescription.JOB_TITLE_SEARCH.value
        case APIEndpointTypes.JOB_SKILLS_SEARCH:
            return APIEndpointTypesDescription.JOB_SKILLS_SEARCH.value
        case APIEndpointTypes.JOB_SALARY_MISC:
            return APIEndpointTypesDescription.JOB_SALARY_MISC.value
        case APIEndpointTypes.JOB_YEARS_EXP_MISC:
            return APIEndpointTypesDescription.JOB_YEARS_EXP_MISC.value
        case APIEndpointTypes.JOBS_SEARCH:
            return APIEndpointTypesDescription.JOBS_SEARCH.value
        case APIEndpointTypes.JOBS_FEED:
            return APIEndpointTypesDescription.JOBS_FEED.value
        case APIEndpointTypes.JOB_MISC:
            return APIEndpointTypesDescription.JOB_MISC.value
        case APIEndpointTypes.LOCATIONS_SEARCH:
            return APIEndpointTypesDescription.LOCATIONS_SEARCH.value
        case APIEndpointTypes.LOCATIONS_QUERY:
            return APIEndpointTypesDescription.LOCATIONS_QUERY.value
        case APIEndpointTypes.INDUSTRY_QUERY:
            return APIEndpointTypesDescription.INDUSTRY_QUERY.value
        case APIEndpointTypes.WORKERS_SEARCH:
            return APIEndpointTypesDescription.WORKERS_SEARCH.value
        case APIEndpointTypes.COMPANY_SEARCH:
            return APIEndpointTypesDescription.COMPANY_SEARCH.value
        case APIEndpointTypes.COMPANY_DETAILS:
            return APIEndpointTypesDescription.COMPANY_DETAILS.value
        case APIEndpointTypes.COMPANY_REVIEWS:
            return APIEndpointTypesDescription.COMPANY_REVIEWS.value
        case APIEndpointTypes.COMPANY_POSTS:
            return APIEndpointTypesDescription.COMPANY_POSTS.value
        case APIEndpointTypes.COMPANY_MISC:
            return APIEndpointTypesDescription.COMPANY_MISC.value
        case APIEndpointTypes.X_MISC:
            return APIEndpointTypesDescription.X_MISC.value
        case APIEndpointTypes.PROFILE_SEARCH:
            return APIEndpointTypesDescription.PROFILE_SEARCH.value
        case APIEndpointTypes.PROFILE_SCRAPE:
            return APIEndpointTypesDescription.PROFILE_SCRAPE.value
        case APIEndpointTypes.PROFILE_POSTS_SEARCH:
            return APIEndpointTypesDescription.PROFILE_POSTS_SEARCH.value
        case APIEndpointTypes.PROFILE_MISC:
            return APIEndpointTypesDescription.PROFILE_MISC.value
        case APIEndpointTypes.POSTS_SEARCH:
            return APIEndpointTypesDescription.POSTS_SEARCH.value
        case APIEndpointTypes.MISC_CREATE_TOKEN:
            return APIEndpointTypesDescription.MISC_CREATE_TOKEN.value
        case APIEndpointTypes.MISC_GENERAL:
            return APIEndpointTypesDescription.MISC_GENERAL.value
