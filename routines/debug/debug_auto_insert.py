from datetime import datetime
import random

from routines.auto.main_job_list import main_job_titles
from routines.auto.qurazor_remoote_job_info import (
    qurazor_remote_skill_keys,
    qurazor_remote_title_keys
)
from routines.auto.top_company_list import company_list
from routines.auto.top_job_list import top_job_titles
from routines.auto.top_locations_list import top_location_list
from routines.auto.row_location_list import row_location_list


def clean_query(input_str):
    """Cleans an input JSON column value and adds a backward slash before any
    escape character used in the statement."""
    return input_str.replace("'", '''\\\'''')


# avadataservices | Job Postings | /api/v2/Jobs/Search
# 1000 per month
def avadataservices_job_postings_api_auto_insert(start, pages):
    for i in top_job_titles:
        clean_job_str = clean_query(i)
        for j in range(start, start + pages):
            print('''\
INSERT INTO `jobs`.`MongoStorage` (\
`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (NOW(), \
'https://rapidapi.com/avadataservices-avadataservices-default/\
api/job-postings1/', b'1', \
'https://job-postings1.p.rapidapi.com/api/v2/Jobs/Search', \
'/api/v2/Jobs/Search', \
'{\\\"searchQuery\\\": \\\"''' + clean_job_str + '''\\\", \
\\\"PageSize\\\": \\\"12\\\", \
\\\"PageNumber\\\": \\\"''' + str(j) + '''\\\"}');\
''')


# avadataservices_job_postings_api_auto_insert(start=1, pages=20)


# avadataservices | Job Postings | /api/v2/Jobs/Search
# 1000 per month
def avadataservices_job_postings_api_auto_insert_additional(start, pages):
    import os
    file_path = "avadataservices_job_postings_main_large.txt"
    if os.path.exists(file_path):
        os.remove(file_path)
    f = open(file_path, "a")
    for i in main_job_titles:
        clean_job_str = clean_query(i)
        for j in range(start, start + pages):
            f.write('''\
INSERT INTO `jobs`.`MongoStorage` (\
`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (NOW(), \
'https://rapidapi.com/avadataservices-avadataservices-default/\
api/job-postings1/', b'1', \
'https://job-postings1.p.rapidapi.com/api/v2/Jobs/Search', \
'/api/v2/Jobs/Search', \
'{\\\"searchQuery\\\": \\\"''' + clean_job_str + '''\\\", \
\\\"PageSize\\\": \\\"12\\\", \
\\\"PageNumber\\\": \\\"''' + str(j) + '''\\\"}');\n\
''')
    f.close()


# avadataservices_job_postings_api_auto_insert_additional(start=1, pages=5)


# Bebity | Linkedin Jobs Scraper API | Get jobs trial (JSON)
# 25 per month
def bebity_linked_in_jobs_scraper_api_auto_insert():
    for i in top_job_titles:
        clean_job_str = clean_query(i)
        print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES \
(NOW(), \
'https://rapidapi.com/bebity-bebity-default/api/linkedin-jobs-scraper-api/', \
b'1', 'https://linkedin-jobs-scraper-api.p.rapidapi.com/jobs/trial', \
'Get jobs trial (JSON)', \
'{\\\"companyIds\\\": \\\"\\\", \
\\\"companyNames\\\": \\\"\\\", \
\\\"contractType\\\": \\\"\\\", \
\\\"experienceLevel\\\": \\\"\\\", \
\\\"location\\\": \\\"United States\\\", \
\\\"publishedAt\\\": \\\"PastMonth\\\", \
\\\"rows\\\": \\\"100\\\", \
\\\"title\\\": \\\"''' + clean_job_str + '''\\\", \
\\\"workType\\\": \\\"\\\"}');\
''')


# bebity_linked_in_jobs_scraper_api_auto_insert()


# Fantastic Jobs | Active Jobs DB
# 30 per month
def fantastic_jobs_get_jobs_auto_insert():
    for i in top_job_titles:
        clean_job_str = clean_query(i)
        print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/\
fantastic-jobs-fantastic-jobs-default/api/active-jobs-db/', \
b'1', \
'https://active-jobs-db.p.rapidapi.com/active-ats', \
'Get Jobs', \
'{\
\\\"title\\\": \\\"''' + clean_job_str + '''\\\", \
\\\"location\\\": \\\"United States\\\", \
\\\"organization\\\": \\\"\\\", \
\\\"offset\\\": \\\"\\\", \
\\\"description\\\": \\\"text\\\"}');\
''')


# fantastic_jobs_get_jobs_auto_insert()


# Fantastic Jobs | Active Jobs DB
# 30 per month
def fantastic_jobs_get_jobs_auto_insert_additional():
    for i in main_job_titles:
        clean_job_str = clean_query(i)
        print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/\
fantastic-jobs-fantastic-jobs-default/api/active-jobs-db/', \
b'1', \
'https://active-jobs-db.p.rapidapi.com/active-ats', \
'Get Jobs', \
'{\
\\\"title\\\": \\\"''' + clean_job_str + '''\\\", \
\\\"location\\\": \\\"United States\\\", \
\\\"organization\\\": \\\"\\\", \
\\\"offset\\\": \\\"\\\", \
\\\"description\\\": \\\"text\\\"}');\
''')


# fantastic_jobs_get_jobs_auto_insert_additional()


# Freshdata | Fresh Linkedin Profile Data
# 30 per month
def freshdata_linkedin_profile_data_auto_insert(pages):
    if pages < 1:
        pages = 1
    for i in top_job_titles:
        clean_job_str = clean_query(i)
        for j in range(0, pages + 1):
            print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/freshdata-freshdata-default/\
api/fresh-linkedin-profile-data/', \
b'1', \
'https://fresh-linkedin-profile-data.p.rapidapi.com/search-jobs', \
'Search Jobs', \
'{\\\"company_ids\\\": \\\"\\\", \
\\\"date_posted\\\": \\\"Past month\\\", \
\\\"easy_apply\": \\\"\\\", \
\\\"experience_levels\\\": \\\"\\\", \
\\\"functions\\\": \\\"\\\", \
\\\"geo_code\\\": \\\"103644278\\\", \
\\\"industries\": \\\"\\\", \
\\\"job_types\": \\\"\\\", \
\\\"keywords\": \\\"''' + clean_job_str + '''\\\", \
\\\"onsite_remotes\": \\\"\\\", \
\\\"sort_by\": \\\"Most recent\\\", \
\\\"start\": \\\"''' + str(j * 25) + '''\\\", \
\\\"title_ids\": \\\"\\\", \
\\\"under_10_applicants\\\": \\\"\\\"}');''')


# freshdata_linkedin_profile_data_auto_insert(4)


# Freshdata | Linkedin Jobs
# 30 per month
def freshdata_linkedin_jobs_auto_insert(pages):
    for i in top_job_titles:
        clean_job_str = clean_query(i)
        for j in range(0, pages + 1):
            print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (NOW(), 'https://rapidapi.com/freshdata-freshdata-default/\
api/linkedin-jobs4/', b'1', \
'https://linkedin-jobs4.p.rapidapi.com/search-jobs', 'Search Jobs', \
'{\\\"keywords\\\": \\\"''' + clean_job_str + '''\\\", \
\\\"geo_code\\\": \\\"103644278\\\", \
\\\"date_posted\\\": \\\"Past month\\\", \
\\\"experience_levels\\\": \\\"\\\", \
\\\"company_ids\\\": \\\"\\\", \
\\\"title_ids\\\": \\\"\\\", \
\\\"onsite_remotes\\\": \\\"\\\", \
\\\"functions\\\": \\\"\\\", \
\\\"industries\\\": \\\"\\\", \
\\\"job_types\\\": \\\"\\\", \
\\\"sort_by\\\": \\\"Most recent\\\", \
\\\"easy_apply\\\": \\\"\\\", \
\\\"under_10_applicants\\\": \\\"false\\\", \
\\\"start\\\": \\\"''' + str(j * 25) + '''\\\"}');''')


# freshdata_linkedin_jobs_auto_insert(0)


# Freshdata | Linkedin Jobs
# 30 per month
def freshdata_linkedin_jobs_auto_insert_additional(pages):
    if pages < 1:
        pages = 1
    for i in main_job_titles:
        clean_job_str = clean_query(i)
        for j in range(0, pages + 1):
            print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (NOW(), 'https://rapidapi.com/freshdata-freshdata-default/\
api/linkedin-jobs4/', b'1', \
'https://linkedin-jobs4.p.rapidapi.com/search-jobs', 'Search Jobs', \
'{\\\"keywords\\\": \\\"''' + clean_job_str + '''\\\", \
\\\"geo_code\\\": \\\"103644278\\\", \
\\\"date_posted\\\": \\\"Past month\\\", \
\\\"experience_levels\\\": \\\"\\\", \
\\\"company_ids\\\": \\\"\\\", \
\\\"title_ids\\\": \\\"\\\", \
\\\"onsite_remotes\\\": \\\"\\\", \
\\\"functions\\\": \\\"\\\", \
\\\"industries\\\": \\\"\\\", \
\\\"job_types\\\": \\\"\\\", \
\\\"sort_by\\\": \\\"Most recent\\\", \
\\\"easy_apply\\\": \\\"\\\", \
\\\"under_10_applicants\\\": \\\"false\\\", \
\\\"start\\\": \\\"''' + str(j * 25) + '''\\\"}');''')


# freshdata_linkedin_jobs_auto_insert_additional(1)


# Jaypay87 | Indeed Job Search
# 15 per month
def jaypat87_indeed_job_search_auto_insert():
    for i in top_job_titles:
        clean_job_str = clean_query(i)
        print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/jaypat87/api/indeed11/', \
b'1', 'https://indeed11.p.rapidapi.com/', 'Search', \
'{\\\"search_terms\\\": \\\"''' + clean_job_str + '''\\\", \
\\\"location\\\": \\\"United States\\\", \
\\\"page\\\": \\\"1\\\"}');''')


# jaypat87_indeed_job_search_auto_insert()


# Jaypay87 | Indeed Job Search
# 15 per month
def jaypat87_indeed_job_search_auto_insert_additional():
    for i in main_job_titles:
        clean_job_str = clean_query(i)
        print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/jaypat87/api/indeed11/', \
b'1', 'https://indeed11.p.rapidapi.com/', 'Search', \
'{\\\"search_terms\\\": \\\"''' + clean_job_str + '''\\\", \
\\\"location\\\": \\\"United States\\\", \
\\\"page\\\": \\\"1\\\"}');''')


# jaypat87_indeed_job_search_auto_insert_additional()


# jaypay87 | Job Search
# 50 per month
def jaypat87_job_search_auto_insert():
    for i in top_job_titles:
        clean_job_str = clean_query(i)
        print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/jaypat87/api/job-search15', \
b'1', 'https://job-search15.p.rapidapi.com/', 'Jobs Search', \
'{\\\"api_type\\\": \\\"fetch_jobs\\\", \
\\\"search_terms\\\": \\\"''' + clean_job_str + '''\\\", \
\\\"location\\\": \\\"United States\\\", \
\\\"page\\\": \\\"1\\\"}');''')


# jaypat87_job_search_auto_insert()


# jaypay87 | Job Search
# 50 per month
def jaypat87_job_search_auto_insert_additional():
    for i in main_job_titles:
        clean_job_str = clean_query(i)
        print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/jaypat87/api/job-search15', \
b'1', 'https://job-search15.p.rapidapi.com/', 'Jobs Search', \
'{\\\"api_type\\\": \\\"fetch_jobs\\\", \
\\\"search_terms\\\": \\\"''' + clean_job_str + '''\\\", \
\\\"location\\\": \\\"United States\\\", \
\\\"page\\\": \\\"1\\\"}');''')


# jaypat87_job_search_auto_insert_additional()


# jaypat87 | Linkedin Jobs Search
# 100 per month
def jaypat87_linkedin_job_search_auto_insert():
    for i in top_job_titles:
        clean_job_str = clean_query(i)
        print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/jaypat87/api/linkedin-jobs-search/', \
b'1', 'https://linkedin-jobs-search.p.rapidapi.com/', 'Search', \
'{\\\"search_terms\\\": \\\"''' + clean_job_str + '''\\\", \
\\\"location\\\": \\\"United States\\\", \
\\\"page\\\": \\\"1\\\", \
\\\"fetch_full_text\\\": \\\"True\\\"}');''')


# jaypat87_linkedin_job_search_auto_insert()


# jaypat87 | Linkedin Jobs Search
# 100 per month
def jaypat87_linkedin_job_search_auto_insert_additional():
    for i in main_job_titles:
        clean_job_str = clean_query(i)
        print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/jaypat87/api/linkedin-jobs-search/', \
b'1', 'https://linkedin-jobs-search.p.rapidapi.com/', 'Search', \
'{\\\"search_terms\\\": \\\"''' + clean_job_str + '''\\\", \
\\\"location\\\": \\\"United States\\\", \
\\\"page\\\": \\\"1\\\", \
\\\"fetch_full_text\\\": \\\"True\\\"}');''')


# jaypat87_linkedin_job_search_auto_insert_additional()


# jobicy | Remote Jobs API
# 1000 per hour
def jobicy_remote_jobs_api_auto_insert():
    for i in top_job_titles:
        clean_job_str = clean_query(i)
        print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/jobicy-jobicy-default/api/jobicy/', b'1', \
'https://jobicy.p.rapidapi.com/api/v2/remote-jobs', \
'Remote Jobs API', '{\\\"count\\\": \\\"\\\", \
\\\"geo\\\": \\\"\\\", \
\\\"tag\\\": \\\"''' + clean_job_str + '''\\\"}');\
''')


# jobicy_remote_jobs_api_auto_insert()


# jobicy | Remote Jobs API
# 1000 per hour
def jobicy_remote_jobs_api_auto_insert_additional():
    for i in main_job_titles:
        clean_job_str = clean_query(i)
        print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/jobicy-jobicy-default/api/jobicy/', b'1', \
'https://jobicy.p.rapidapi.com/api/v2/remote-jobs', \
'Remote Jobs API', '{\\\"count\\\": \\\"\\\", \
\\\"geo\\\": \\\"\\\", \
\\\"tag\\\": \\\"''' + clean_job_str + '''\\\"}');\
''')


# jobicy_remote_jobs_api_auto_insert_additional()


# jobwiz | Job Search API
# 20 per month
def jobwiz_job_search_api_auto_insert():
    for i in top_job_titles:
        clean_job_str = clean_query(i)
        print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/jobwiz-jobwiz-default/api/job-search-api1/', b'1', \
'https://job-search-api1.p.rapidapi.com/v1/job-description-search', \
'searchJob', \
'{\\\"q\\\": \\\"''' + clean_job_str + '''\\\", \
\\\"page\\\": \\\"1\\\", \
\\\"country\\\": \\\"us\\\", \
\\\"city\\\": \\\"\\\"}');\
''')


# jobwiz_job_search_api_auto_insert()


# jobwiz | Job Search API
# 20 per month
def jobwiz_job_search_api_auto_insert_additional():
    for i in main_job_titles:
        clean_job_str = clean_query(i)
        print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/jobwiz-jobwiz-default/api/job-search-api1/', b'1', \
'https://job-search-api1.p.rapidapi.com/v1/job-description-search', \
'searchJob', \
'{\\\"q\\\": \\\"''' + clean_job_str + '''\\\", \
\\\"page\\\": \\\"1\\\", \
\\\"country\\\": \\\"us\\\", \
\\\"city\\\": \\\"\\\"}');\
''')


# jobwiz_job_search_api_auto_insert_additional()


# letscrape | JSearch
# 200 per month
# 3x request for 20 pages = 66
def letscrape_j_search_auto_insert():
    for i in top_job_titles:
        clean_job_str = clean_query(i)
        print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch/', \
b'1', 'https://jsearch.p.rapidapi.com/search', 'Search', \
'{\\\"query\\\": \\\"''' + clean_job_str + ''' in USA\\\", \
\\\"page\\\": \\\"1\\\", \
\\\"num_pages\\\": \\\"20\\\", \
\\\"date_posted\\\": \\\"month\\\", \
\\\"remote_jobs_only\\\": \\\"\\\", \
\\\"employment_types\\\": \\\"\\\", \
\\\"job_requirements\\\": \\\"\\\", \
\\\"job_titles\\\": \\\"\\\", \
\\\"company_types\\\": \\\"\\\", \
\\\"employer\\\": \\\"\\\", \
\\\"actively_hiring\\\": \\\"\\\", \
\\\"radius\\\": \\\"\\\", \
\\\"exclude_job_publishers\\\": \\\"\\\", \
\\\"categories\\\": \\\"\\\"}');''')


# letscrape_j_search_auto_insert()


# letscrape | JSearch
# 200 per month
# 3x request for 20 pages = 66
def letscrape_j_search_auto_insert_additional():
    for i in main_job_titles:
        clean_job_str = clean_query(i)
        print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch/', \
b'1', 'https://jsearch.p.rapidapi.com/search', 'Search', \
'{\\\"query\\\": \\\"''' + clean_job_str + ''' in USA\\\", \
\\\"page\\\": \\\"1\\\", \
\\\"num_pages\\\": \\\"20\\\", \
\\\"date_posted\\\": \\\"month\\\", \
\\\"remote_jobs_only\\\": \\\"\\\", \
\\\"employment_types\\\": \\\"\\\", \
\\\"job_requirements\\\": \\\"\\\", \
\\\"job_titles\\\": \\\"\\\", \
\\\"company_types\\\": \\\"\\\", \
\\\"employer\\\": \\\"\\\", \
\\\"actively_hiring\\\": \\\"\\\", \
\\\"radius\\\": \\\"\\\", \
\\\"exclude_job_publishers\\\": \\\"\\\", \
\\\"categories\\\": \\\"\\\"}');''')


# letscrape_j_search_auto_insert_additional()


# letscrape | Real-Time Glassdoor Data
# 50 per month
def letscrape_real_time_glassdoor_data_auto_insert():
    for i in company_list:
        clean_company_str = clean_query(i)
        print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/letscrape-6bRBa3QguO5/api/real-time-glassdoor-data/', \
b'1', 'https://real-time-glassdoor-data.p.rapidapi.com/company-search', \
'Company Search', \
'{\\\"query\\\": \\\"''' + clean_company_str + '''\\\", \
\\\"limit\\\": \\\"100\\\"}');''')


# letscrape_real_time_glassdoor_data_auto_insert()


# mantiks | Glassdoor
# 25 per month
def mantiks_glassdoor_jobs_auto_insert():
    for i in top_job_titles:
        clean_job_str = clean_query(i)
        print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/mantiks-mantiks-default/api/glassdoor/', b'1', \
'https://glassdoor.p.rapidapi.com/jobs/search', 'Jobs Search', \
'{\\\"keyword\\\": \\\"''' + clean_job_str + '''\\\", \
\\\"location_id\\\": \\\"1\\\", \
\\\"location_type\\\": \\\"N\\\", \
\\\"page_id\\\": \\\"0\\\", \
\\\"page_cursor\\\": \\\"\\\"}');\
''')


# mantiks_glassdoor_jobs_auto_insert()


# mantiks | Glassdoor
# 25 per month
def mantiks_glassdoor_jobs_auto_insert_additional():
    for i in main_job_titles:
        clean_job_str = clean_query(i)
        print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/mantiks-mantiks-default/api/glassdoor/', b'1', \
'https://glassdoor.p.rapidapi.com/jobs/search', 'Jobs Search', \
'{\\\"keyword\\\": \\\"''' + clean_job_str + '''\\\", \
\\\"location_id\\\": \\\"1\\\", \
\\\"location_type\\\": \\\"N\\\", \
\\\"page_id\\\": \\\"0\\\", \
\\\"page_cursor\\\": \\\"\\\"}');\
''')


# mantiks_glassdoor_jobs_auto_insert_additional()


# mantiks | Glassdoor
# 25 per month
def mantiks_glassdoor_companies_auto_insert():
    for i in company_list:
        clean_company_str = clean_query(i)
        print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/mantiks-mantiks-default/api/glassdoor/', b'1', \
'https://glassdoor.p.rapidapi.com/companies/search', 'Companies Search', \
'{\\\"company_name\\\": \\\"''' + clean_company_str + '''\\\"}');\
''')


# mantiks_glassdoor_companies_auto_insert()


# mantiks | Indeed
# 25 per month
def mantiks_indeed_auto_insert():
    for i in top_job_titles:
        clean_job_str = clean_query(i)
        print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/mantiks-mantiks-default/api/indeed12/', b'1', \
'https://indeed12.p.rapidapi.com/jobs/search', 'Jobs Search', \
'{\\\"query\\\": \\\"''' + clean_job_str + '''\\\", \
\\\"location\\\": \\\"\\\", \\\"page_id\\\": \\\"1\\\", \
\\\"locality\\\": \\\"us\\\", \\\"fromage\\\": \\\"\\\", \
\\\"radius\\\": \\\"\\\", \\\"sort\\\": \\\"date\\\"}');\
''')


# mantiks_indeed_auto_insert()


# mantiks | Indeed | Company Search
# 25 per month
def mantiks_indeed_companies_auto_insert():
    for i in company_list:
        clean_str = clean_query(i)
        print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/mantiks-mantiks-default/api/indeed12/', b'1', \
'https://indeed12.p.rapidapi.com/companies/search', 'Company Search', \
'{\\\"company_name\\\": \\\"''' + clean_str + '''\\\", \
\\\"locality\\\": \\\"us\\\"}');\
''')


# mantiks_indeed_companies_auto_insert()


# mantiks | Indeed
# 25 per month
def mantiks_indeed_auto_insert_additional():
    for i in main_job_titles:
        clean_job_str = clean_query(i)
        print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/mantiks-mantiks-default/api/indeed12/', b'1', \
'https://indeed12.p.rapidapi.com/jobs/search', 'Jobs Search', \
'{\\\"query\\\": \\\"''' + clean_job_str + '''\\\", \
\\\"location\\\": \\\"\\\", \\\"page_id\\\": \\\"1\\\", \
\\\"locality\\\": \\\"us\\\", \\\"fromage\\\": \\\"\\\", \
\\\"radius\\\": \\\"\\\", \\\"sort\\\": \\\"date\\\"}');\
''')


# mantiks_indeed_auto_insert_additional()


# mgujjargamingm | LinkedIn Data Scraper
# 50 per month
def mgujjargamingm_search_jobs_auto_insert():
    for i in top_job_titles:
        # No responses
        if i == "C# Developer":
            continue
        clean_job_str = clean_query(i)
        print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/mgujjargamingm/api/linkedin-data-scraper/', b'1', \
'https://linkedin-data-scraper.p.rapidapi.com/search_jobs', 'Search Jobs', \
'{\\\"keywords\\\": \\\"''' + clean_job_str + '''\\\", \
\\\"location\\\": \\\"United States\\\", \
\\\"count\\\": \\\"10\\\"}');\
''')


# mgujjargamingm_search_jobs_auto_insert()


# mgujjargamingm | LinkedIn Data Scraper
# 50 per month
def mgujjargamingm_search_jobs_auto_insert_additional():
    for i in main_job_titles:
        clean_job_str = clean_query(i)
        print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/mgujjargamingm/api/linkedin-data-scraper/', b'1', \
'https://linkedin-data-scraper.p.rapidapi.com/search_jobs', 'Search Jobs', \
'{\\\"keywords\\\": \\\"''' + clean_job_str + '''\\\", \
\\\"location\\\": \\\"United States\\\", \
\\\"count\\\": \\\"10\\\"}');\
''')


# mgujjargamingm_search_jobs_auto_insert_additional()


# mgujjargamingm | Linkedin BULK data scraper
# 150 per month
def mgujjargamingm_bulk_search_jobs_auto_insert():
    for i in top_job_titles:
        clean_job_str = clean_query(i)
        print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/mgujjargamingm/api/linkedin-bulk-data-scraper', b'1', \
'https://linkedin-bulk-data-scraper.p.rapidapi.com/search_jobs', \
'Search Jobs', \
'{\\\"companyIdsList\\\": \\\"\\\", \
\\\"easyApply\\\": \\\"\\\", \
\\\"experience\\\": \\\"\\\", \
\\\"functionIdsList\\\": \\\"\\\", \
\\\"industryIdsList\\\": \\\"\\\", \
\\\"jobType\\\": \\\"\\\", \
\\\"locationIdsList\\\": \\\"\\\", \
\\\"page\\\": \\\"1\\\", \
\\\"postedAgo\\\": \\\"2629746\\\", \
\\\"query\\\": \\\"''' + clean_job_str + '''\\\", \
\\\"searchLocationId\\\": \\\"103644278\\\", \
\\\"sortBy\\\": \\\"\\\", \
\\\"titleIdsList\\\": \\\"\\\", \
\\\"workplaceType\\\": \\\"\\\"}');\
''')


# mgujjargamingm_bulk_search_jobs_auto_insert()


# mgujjargamingm | Linkedin BULK data scraper
# 150 per month
def mgujjargamingm_bulk_search_jobs_auto_insert_additional():
    for i in main_job_titles:
        clean_job_str = clean_query(i)
        print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/mgujjargamingm/api/linkedin-bulk-data-scraper', b'1', \
'https://linkedin-bulk-data-scraper.p.rapidapi.com/search_jobs', \
'Search Jobs', \
'{\\\"companyIdsList\\\": \\\"\\\", \
\\\"easyApply\\\": \\\"\\\", \
\\\"experience\\\": \\\"\\\", \
\\\"functionIdsList\\\": \\\"\\\", \
\\\"industryIdsList\\\": \\\"\\\", \
\\\"jobType\\\": \\\"\\\", \
\\\"locationIdsList\\\": \\\"\\\", \
\\\"page\\\": \\\"1\\\", \
\\\"postedAgo\\\": \\\"2629746\\\", \
\\\"query\\\": \\\"''' + clean_job_str + '''\\\", \
\\\"searchLocationId\\\": \\\"103644278\\\", \
\\\"sortBy\\\": \\\"\\\", \
\\\"titleIdsList\\\": \\\"\\\", \
\\\"workplaceType\\\": \\\"\\\"}');\
''')


# mgujjargamingm_bulk_search_jobs_auto_insert_additional()


# Pat92 | Jobs API
# 50 per month
def pat92_jobs_api_auto_insert():
    for i in top_job_titles:
        clean_job_str = clean_query(i)
        print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/Pat92/api/jobs-api14/', \
b'1', 'https://jobs-api14.p.rapidapi.com/list', 'List Jobs', \
'{\\\"query\\\": \\\"''' + clean_job_str + '''\\\", \
\\\"location\\\": \\\"United States\\\", \
\\\"distance\\\": \\\"\\\", \
\\\"language\\\": \\\"\\\", \
\\\"remoteOnly\\\": \\\"\\\", \
\\\"datePosted\\\": \\\"month\\\", \
\\\"employmentTypes\\\": \\\"\\\", \
\\\"allowedJobProviders\\\": \\\"\\\", \
\\\"index\\\": \\\"0\\\"}');\
''')


# pat92_jobs_api_auto_insert()


# Pat92 | Jobs API
# 50 per month
def pat92_jobs_api_auto_insert_additional():
    for i in main_job_titles:
        clean_job_str = clean_query(i)
        print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/Pat92/api/jobs-api14/', \
b'1', 'https://jobs-api14.p.rapidapi.com/list', 'List Jobs', \
'{\\\"query\\\": \\\"''' + clean_job_str + '''\\\", \
\\\"location\\\": \\\"United States\\\", \
\\\"distance\\\": \\\"\\\", \
\\\"language\\\": \\\"\\\", \
\\\"remoteOnly\\\": \\\"\\\", \
\\\"datePosted\\\": \\\"month\\\", \
\\\"employmentTypes\\\": \\\"\\\", \
\\\"allowedJobProviders\\\": \\\"\\\", \
\\\"index\\\": \\\"0\\\"}');\
''')


# pat92_jobs_api_auto_insert_additional()


# qurazor1 | Remoote Job Search
# 50 per month
def qurazor1_remoote_job_search_auto_insert():
    for i in qurazor_remote_title_keys.get('titles'):
        clean_skill_str = clean_query(i.get('name'))
        print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/qurazor1/api/remoote-job-search1/', b'1', \
'https://remoote-job-search1.p.rapidapi.com/remoote/jobs', \
'list_jobs_jobs_get', \
'{\\\"country_id\\\": \\\"236\\\", \
\\\"exclude_skill_ids\\\": \\\"\\\", \
\\\"limit\\\": \\\"10\\\", \
\\\"search_id\\\": \\\"\\\", \
\\\"skill_ids\\\": \\\"\\\", \
\\\"titles\\\": \\\"[\\\\"''' + clean_skill_str + '''\\\\"]\\\"}');\
''')


# qurazor1_remoote_job_search_auto_insert()


# vuesdata | Indeed Jobs API
# 20 per month
# Actual location must be searched
def vuesdata_indeed_jobs_auto_insert():
    for i in top_job_titles:
        clean_job_str = clean_query(i)
        for j in top_location_list["United States"]:
            print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/vuesdata/api/indeed-jobs-api/', \
b'1', 'https://indeed-jobs-api.p.rapidapi.com/indeed-us/', 'SearchJobs', \
'{\\\"keyword\\\": \\\"''' + clean_job_str + '''\\\", \
\\\"location\\\": \\\"''' + j.replace(", United States", "") + '''\\\", \
\\\"offset\\\": \\\"0\\\"}');\
''')


# vuesdata_indeed_jobs_auto_insert()


# vuesdata | Finland | Indeed Jobs API
# 20 per month
# Actual location must be searched
def vuesdata_finland_indeed_jobs_auto_insert(start, pages):
    for i in top_job_titles:
        clean_job_str = clean_query(i)
        for j in row_location_list["Finland"]:
            for k in range(start, start + pages):
                print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/vuesdata/api/indeed-jobs-api-finland/', \
b'1', \
'https://indeed-jobs-api-finland.p.rapidapi.com/indeed-fi/', \
'SearchJobs', \
'{\\\"keyword\\\": \\\"''' + clean_job_str + '''\\\", \
\\\"location\\\": \\\"''' + str(j.replace(", Finland", "")) + '''\\\", \
\\\"offset\\\": \\\"''' + str(k * 10) + '''\\\"}');\
''')


# vuesdata_finland_indeed_jobs_auto_insert(start=0, pages=5)


# vuesdata | Sweden | Indeed Jobs API
# 10 per month
# Actual location must be searched
def vuesdata_sweden_indeed_jobs_auto_insert(start, pages):
    for i in top_job_titles:
        clean_job_str = clean_query(i)
        for j in row_location_list["Sweden"]:
            for k in range(start, start + pages):
                print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/vuesdata/api/indeed-jobs-api-sweden/', \
b'1', \
'https://indeed-jobs-api-sweden.p.rapidapi.com/indeed-se/', \
'SearchJobs', \
'{\\\"keyword\\\": \\\"''' + clean_job_str + '''\\\", \
\\\"location\\\": \\\"''' + str(j.replace(", Sweden", "")) + '''\\\", \
\\\"offset\\\": \\\"''' + str(k * 10) + '''\\\"}');\
''')


# vuesdata_sweden_indeed_jobs_auto_insert(start=0, pages=2)


# vuesdata | Denmark | Indeed Jobs API
# 10 per month
# Actual location must be searched
def vuesdata_denmark_indeed_jobs_auto_insert(start, pages):
    for i in top_job_titles:
        clean_job_str = clean_query(i)
        for j in row_location_list["Denmark"]:
            for k in range(start, start + pages):
                print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/vuesdata/api/indeed-jobs-api-denmark/', \
b'1', \
'https://indeed-jobs-api-denmark.p.rapidapi.com/indeed-dk/', \
'SearchJobs', \
'{\\\"keyword\\\": \\\"''' + clean_job_str + '''\\\", \
\\\"location\\\": \\\"''' + str(j.replace(", Denmark", "")) + '''\\\", \
\\\"offset\\\": \\\"''' + str(k * 10) + '''\\\"}');\
''')


# vuesdata_denmark_indeed_jobs_auto_insert(start=0, pages=2)


# apijobs | apijobs
# 250 per month
def api_jobs_direct_auto_insert():
    for i in top_job_titles:
        clean_job_str = clean_query(i)
        print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://app.apijobs.dev/', b'1', \
'https://api.apijobs.dev/v1/job/search', 'Search Jobs', \
'{\\\"country\\\": \\\"\\\", \
\\\"domains\\\": \\\"\\\", \
\\\"employment_type\\\": \\\"\\\", \
\\\"hiringOrganizationName\\\": \\\"\\\", \
\\\"language\\\": \\\"\\\", \
\\\"published_since\\\": \\\"\\\", \
\\\"published_until\\\": \\\"\\\", \
\\\"q\\\": \\\"''' + clean_job_str + '''\\\"}');\
''')


# api_jobs_direct_auto_insert()


# apijobs
# 250 per month
def generate_direct_api_jobs_search_query(search_query):
    return '''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://app.apijobs.dev/', b'1', \
'https://api.apijobs.dev/v1/job/search', 'Search Jobs', \
'{\\\"country\\\": \\\"\\\", \
\\\"domains\\\": \\\"\\\", \
\\\"employment_type\\\": \\\"\\\", \
\\\"hiringOrganizationName\\\": \\\"\\\", \
\\\"language\\\": \\\"\\\", \
\\\"published_since\\\": \\\"\\\", \
\\\"published_until\\\": \\\"\\\", \
\\\"q\\\": \\\"''' + clean_query(search_query) + '''\\\"}');\
'''


# apijobs
# 100 per day
def generate_rapid_api_jobs_search_query(search_query):
    return '''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/apijobs-apijobs-default/api/apijob-job-searching-api/', \
b'1', \
'https://apijob-job-searching-api.p.rapidapi.com/v1/job/search', \
'Search jobs',\
'{\\\"country\\\": \\\"\\\", \
\\\"domains\\\": \\\"\\\", \
\\\"employment_type\\\": \\\"\\\", \
\\\"hiringOrganizationName\\\": \\\"\\\", \
\\\"language\\\": \\\"\\\", \
\\\"published_since\\\": \\\"\\\", \
\\\"published_until\\\": \\\"\\\", \
\\\"q\\\": \\\"''' + clean_query(search_query) + '''\\\"}');\
'''


# apijobs | apijobs + API Jobs | Job Searching API
# 100 per day

# 250 per month
def api_jobs_rapid_api_direct_dual_auto_insert():
    # get total count
    # every 13 direct api queries, send 1 query using the direct API
    for (count, i) in enumerate(top_job_titles + main_job_titles):
        if count % 13 == 1:
            print(generate_rapid_api_jobs_search_query(i))
        else:
            print(generate_direct_api_jobs_search_query(i))


# api_jobs_rapid_api_direct_dual_auto_insert()


# API Jobs | Job Searching API | Company Search
# 100 per day
def api_jobs_search_organizations_auto_insert():
    for i in company_list:
        clean_company_str = clean_query(i)
        print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`input_json`, `time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`) \
VALUES \
('{\"q\": \"''' + clean_company_str + '''\"}', \
NOW(), \
'https://rapidapi.com/apijobs-apijobs-default/api/apijob-job-searching-api/', \
b'1', \
'https://apijob-job-searching-api.p.rapidapi.com/v1/organization/search', \
'Search organization');''')

# api_jobs_search_organizations_auto_insert()


# API Jobs | Job Searching API
# 100 per day
def api_jobs_search_jobs_auto_insert():
    for i in top_job_titles:
        clean_job_str = clean_query(i)
        print('''\
INSERT INTO `jobs`.`MongoStorage` \
(`time`, `api`, `api_key_auto`, `url`, `endpoint_nice_name`, `input_json`) \
VALUES (\
NOW(), \
'https://rapidapi.com/apijobs-apijobs-default/api/apijob-job-searching-api/', \
b'1', \
'https://apijob-job-searching-api.p.rapidapi.com/v1/job/search', \
'Search jobs',\
'{\\\"country\\\": \\\"\\\", \
\\\"domains\\\": \\\"\\\", \
\\\"employment_type\\\": \\\"\\\", \
\\\"hiringOrganizationName\\\": \\\"\\\", \
\\\"language\\\": \\\"\\\", \
\\\"published_since\\\": \\\"\\\", \
\\\"published_until\\\": \\\"\\\", \
\\\"q\\\": \\\"''' + clean_job_str + '''\\\"}');\
''')


# api_jobs_search_jobs_auto_insert()


# NEWAPI
#  per hour
def new_api_name():
    for i in top_job_titles:
        clean_job_str = clean_query(i)
        print('''\
''')


# new_api_name()
