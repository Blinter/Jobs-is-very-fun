"""
API Endpoint Bodies

Seed file can be run
cd <base_dir>
PYTHONPATH=<base_dir> python3 <base_dir>/<file_name>.py
"""
from sqlalchemy import inspect, text, MetaData
from sqlalchemy_utils import database_exists, create_database
from secrets_jobs.credentials import (maria_information_login_details,
                                      mariadb_database_name)
from models.mariadb.api_list_url import APIListURL
from models.mariadb.api_headers import APIHeader
from models.mariadb.api_endpoints import APIEndpoint
from models.mariadb.api_endpoint_params import APIEndpointParam
from models.mariadb.api_endpoint_bodies import APIEndpointBody
from models.mariadb.api_endpoint_headers import APIEndpointHeader
from models.mariadb.api_endpoint_extras import APIEndpointExtra
from app import create_app, db
import sqlalchemy as db2

engine = db2.create_engine(maria_information_login_details)
if not database_exists(engine.url):
    create_database(engine.url, encoding='UTF8')

app = create_app()


# Function to get the names of foreign key constraints
def get_foreign_key_constraint_names(temp_table, temp_connection):
    """
    Inspect table and get foreign key restraints.
    """
    inspector = inspect(temp_connection)
    fks = inspector.get_foreign_keys(temp_table.name, schema=temp_table.schema)
    return [fk['name'] for fk in fks]


def table_exists(temp_db, table_name, schema=mariadb_database_name):
    """
    Query information_schema and check if table exists.
    """
    query = text(f"""\
SELECT COUNT(*) FROM information_schema.TABLES \
WHERE TABLE_SCHEMA = '{schema}' AND TABLE_NAME = '{table_name}'\
""")
    result = temp_db.session.execute(query)
    return result.scalar() > 0


with app.app_context():
    try:
        metadata = MetaData()
        table = db.Table(
            APIEndpointBody.__tablename__,
            metadata=metadata,
            bind_key="mariadb",
            autoload_with=engine)
        if table_exists(db, table.name):
            fk_names = get_foreign_key_constraint_names(table, engine)
            for fk_name in fk_names:
                if fk_name:
                    sql_text = (f'ALTER TABLE {table.name} DROP FOREIGN KEY '
                                f'{fk_name}')
                    db.session.execute(text(sql_text))

        table.drop(engine, checkfirst=True)
        table.create(engine, checkfirst=True)

        # Retrieve API Endpoints in order to reference foreign keys.
        API_Endpoint_List = db.session.query(APIEndpoint).all()

        # Search Jobs
        # APIJobs | Job Searching API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://apijob-job-searching-api.p.rapidapi.com'
                '/v1/job/search') and
            i.nice_name == 'Search jobs')
        db.session.add_all([

            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='q',
                key_description='Search Keyword',
                value_hint_type='String',
                value_default='Full Stack Engineer',
                required=True
            ),

            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='published_since',
                key_description='Published since a specific date',
                value_hint_type='String',
                value_default='',
                required=False,
            ),

            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='published_until',
                key_description='Published until a specific date',
                value_hint_type='String',
                value_default='',
                required=False,
            ),

            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='country',
                key_description='''\
The country filter can be used in the POST /job/search endpoint to narrow down \
job listings to specific countries. Use the country codes from the /countries \
endpoint to specify which countries you want to include in your job search \
query. This allows for more targeted job searches based on the location of \
the job listings.''',
                value_hint_type='String',
                value_default='United States',
                required=False,
            ),

            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='employment_type',
                key_description='''\
Employment Type - The employment_types filter can be used in the  \
POST /job/search endpoint to narrow down job listings to specific \
types of employment. Use the employment type codes from the /employment_types\
 endpoint to specify which types of employment you want to include in your job\
 search query. This allows for more targeted job searches based on the nature\
 of employment, such as full-time, part-time, contract, etc. ("Contract", \
"Freelance", "Internship", "Temporary", "Part Time", "Full Time", "Other")\
''',
                value_hint_type='String',
                value_default='Full Time',
                required=False,
            ),

            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='language',
                key_description='''\
The languages filter can be used in the  POST job/search endpoint to narrow \
down job listings to specific languages. Use the language codes from the \
/languages endpoint to specify which languages you want to include in your \
job search query. This allows for more targeted job searches based on the \
preferred language of the job listings.''',
                value_hint_type='String',
                value_default='English',
                required=False,
            ),

            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='domains',
                key_description='''Domains where the job is present. Example : \
["boards.eu.greenhouse.io", "boards.greenhouse.io"]''',
                value_hint_type='Array String',
                value_default='',
                required=False,
            ),

            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='hiringOrganizationName',
                key_description='''\
filter by the organization Name. Organizations can be fetch using the \
organization route ''',
                value_hint_type='String',
                value_default='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Organization
        # APIJobs | Job Searching API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://apijob-job-searching-api.p.rapidapi.com'
                '/v1/organization/search') and
            i.nice_name == 'Search organization')
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='q',
                key_description='Search Organization - Company Name',
                value_hint_type='String',
                value_default='Google',
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Jobs
        # bareq | Remote Jobs API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://remote-jobs-api1.p.rapidapi.com'
                '/jobs/search') and
            i.nice_name == 'Search jobs')
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='search',
                key_description='Keyword Search',
                value_hint_type='String',
                value_default='Software Engineer',
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='country',
                key_description='Country',
                value_hint_type='String',
                value_default='usa',
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='max_results',
                key_description='Maximum Results',
                value_hint_type='Number',
                value_default='50',
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='after',
                key_description='After',
                value_hint_type='Number',
                value_default='0',
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Jobs (JSON)
        # Bebity | Linkedin Jobs Scraper API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-jobs-scraper-api.p.rapidapi.com'
                '/jobs') and
            i.nice_name == 'Get jobs (JSON)')
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='title',
                key_description='The Title of the Job',
                value_hint_type='String',
                value_default='Software Engineer',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='location',
                key_description='The Location of the Job',
                value_hint_type='String',
                value_default='United States',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='rows',
                key_description='The # of rows to return',
                value_hint_type='Number',
                value_default='100',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='workType',
                key_description='The Job Type '
                                '(i.e. OnSite, '
                                'Remote, '
                                'Hybrid)',
                value_hint_type='String',
                value_default='Remote',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='contractType',
                key_description='The Job Contract Type '
                                '(i.e. FullTime, '
                                'PartTime, '
                                'Contract, '
                                'Temporary, '
                                'Internship, '
                                'Volunteer)',
                value_hint_type='String',
                value_default='FullTime',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='experienceLevel',
                key_description='The Experience Level '
                                '(i.e. Internship, '
                                'EntryLevel, '
                                'Associate, '
                                'MidSeniorLevel, '
                                'Director)',
                value_hint_type='String',
                value_default='EntryLevel',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='companyNames',
                key_description='The Company Names '
                                '(Default: ["Google","Facebook"])',
                value_hint_type='Array String',
                value_default='',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='companyIds',
                key_description='The Company IDs '
                                '(Default: ["1","2"])',
                value_hint_type='Array String',
                value_default='',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='publishedAt',
                key_description='The date the job was published '
                                '(i.e. AnyTime, '
                                'Past24Hours, '
                                'PastWeek, '
                                'PastMonth)',
                value_hint_type='String',
                value_default='AnyTime',
                required=False
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get jobs trial (JSON)
        # Bebity | Linkedin Jobs Scraper API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-jobs-scraper-api.p.rapidapi.com'
                '/jobs/trial'
            ) and i.nice_name == 'Get jobs trial (JSON)')
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='title',
                key_description='The Title of the Job',
                value_hint_type='String',
                value_default='Software Engineer',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='location',
                key_description='The Location of the Job',
                value_hint_type='String',
                value_default='United States',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='rows',
                key_description='The # of rows to return',
                value_hint_type='Number',
                value_default='100',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='workType',
                key_description='The Job Type '
                                '(i.e. OnSite, '
                                'Remote, '
                                'Hybrid)',
                value_hint_type='String',
                value_default='Remote',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='contractType',
                key_description='The Job Contract Type '
                                '(i.e. FullTime, '
                                'PartTime, '
                                'Contract, '
                                'Temporary, '
                                'Internship, '
                                'Volunteer)',
                value_hint_type='String',
                value_default='FullTime',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='experienceLevel',
                key_description='The Experience Level '
                                '(i.e. Internship, '
                                'EntryLevel, '
                                'Associate, '
                                'MidSeniorLevel, '
                                'Director)',
                value_hint_type='String',
                value_default='EntryLevel',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='companyNames',
                key_description='The Company Names '
                                '(i.e. ["Google","Facebook"])',
                value_hint_type='Array String',
                value_default='',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='companyIds',
                key_description='The Company IDs '
                                '(i.e. ["1","2"])',
                value_hint_type='Array String',
                value_default='',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='publishedAt',
                key_description='The date the job was published '
                                '(i.e. AnyTime, '
                                'Past24Hours, '
                                'PastWeek, '
                                'PastMonth)',
                value_hint_type='String',
                value_default='AnyTime',
                required=False
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get jobs (CSV)
        # Bebity | Linkedin Jobs Scraper API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-jobs-scraper-api.p.rapidapi.com'
                '/jobs/csv') and
            i.nice_name == 'Get jobs (CSV)')
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='title',
                key_description='The Title of the Job',
                value_hint_type='String',
                value_default='Software Engineer',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='location',
                key_description='The Location of the Job',
                value_hint_type='String',
                value_default='United States',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='rows',
                key_description='The # of rows to return',
                value_hint_type='Number',
                value_default='100',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='workType',
                key_description='The Job Type '
                                '(i.e. OnSite, '
                                'Remote, '
                                'Hybrid)',
                value_hint_type='String',
                value_default='Remote',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='contractType',
                key_description='The Job Contract Type '
                                '(i.e. FullTime, '
                                'PartTime, '
                                'Contract, '
                                'Temporary, '
                                'Internship, '
                                'Volunteer)',
                value_hint_type='String',
                value_default='FullTime',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='experienceLevel',
                key_description='The Experience Level '
                                '(i.e. Internship, '
                                'EntryLevel, '
                                'Associate, '
                                'MidSeniorLevel, '
                                'Director)',
                value_hint_type='String',
                value_default='EntryLevel',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='companyNames',
                key_description='The Company Names '
                                '(i.e. ["Google","Facebook"])',
                value_hint_type='Array String',
                value_default='',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='companyIds',
                key_description='The Company IDs '
                                '(i.e. ["1","2"])',
                value_hint_type='Array String',
                value_default='',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='publishedAt',
                key_description='The Date the Job was published '
                                '(i.e. AnyTime, '
                                'Past24Hours, '
                                'PastWeek, '
                                'PastMonth)',
                value_hint_type='String',
                value_default='AnyTime',
                required=False
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Jobs (CSV File)
        # Bebity | Linkedin Jobs Scraper API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-jobs-scraper-api.p.rapidapi.com'
                '/jobs/csv/file') and
            i.nice_name == 'Get jobs (CSV File)')
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='title',
                key_description='The Title of the Job',
                value_hint_type='String',
                value_default='Software Engineer',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='location',
                key_description='The Location of the Job',
                value_hint_type='String',
                value_default='United States',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='rows',
                key_description='The # of rows to return',
                value_hint_type='Number',
                value_default='100',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='workType',
                key_description='The Job Type '
                                '(i.e. OnSite, '
                                'Remote, '
                                'Hybrid)',
                value_hint_type='String',
                value_default='Remote',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='contractType',
                key_description='The Job Contract Type '
                                '(i.e. FullTime, '
                                'PartTime, '
                                'Contract, '
                                'Temporary, '
                                'Internship, '
                                'Volunteer)',
                value_hint_type='String',
                value_default='FullTime',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='experienceLevel',
                key_description='The Experience Level '
                                '(i.e. Internship, '
                                'EntryLevel, '
                                'Associate, '
                                'MidSeniorLevel, '
                                'Director)',
                value_hint_type='String',
                value_default='EntryLevel',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='companyNames',
                key_description='The Company Name(s) '
                                '(i.e. ["Google","Facebook"])',
                value_hint_type='Array',
                value_default='',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='companyIds',
                key_description='The Company ID(s) '
                                '(i.e. ["1","2"])',
                value_hint_type='Array',
                value_default='',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='publishedAt',
                key_description='The date the job was published '
                                '(i.e. AnyTime, '
                                'Past24Hours, '
                                'PastWeek, '
                                'PastMonth)',
                value_hint_type='String',
                value_default='AnyTime',
                required=False
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Posts
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/search-posts') and
            i.nice_name == 'Search Posts')
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='search_keywords',
                key_description='Search Keywords',
                value_hint_type='String',
                value_default='Software Engineer',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='sort_by',
                key_description='Sort By',
                value_hint_type='String',
                value_default='Latest',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='date_posted',
                key_description='Date Posted',
                value_hint_type='String',
                value_default='',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='content_type',
                key_description='Content Type',
                value_hint_type='String',
                value_default='',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='from_member',
                key_description='From Member',
                value_hint_type='String',
                value_default='',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='from_company',
                key_description='From Company',
                value_hint_type='String',
                value_default='',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='mentioning_member',
                key_description='Mentioning Member',
                value_hint_type='String',
                value_default='',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='mentioning_company',
                key_description='Mentioning Company',
                value_hint_type='String',
                value_default='162479',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='author_company',
                key_description='Author Company',
                value_hint_type='String',
                value_default='',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='author_industry',
                key_description='Author Industry',
                value_hint_type='String',
                value_default='',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='author_keyword',
                key_description='Author Keyword',
                value_hint_type='String',
                value_default='',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='page',
                key_description='Page (Pagination)',
                value_hint_type='String',
                value_default='1',
                required=True
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Find Custom Headcount
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/find-custom-headcount') and
            i.nice_name == 'Find Custom Headcount')
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='linkedin_url',
                key_description='LinkedIn URL',
                value_hint_type='URL',
                value_default='https://www.linkedin.com/company/amazon',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='keywords',
                key_description='Keywords',
                value_hint_type='String',
                value_default='',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='where_they_live',
                key_description='Where they live',
                value_hint_type='Array',
                value_default='[103644278, 102713980]',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='where_they_studied',
                key_description='Where they studied',
                value_hint_type='Array',
                value_default='[2584, 3084]',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='what_they_do',
                key_description='What they do',
                value_hint_type='Array',
                value_default='[18, 8]',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='what_they_are_skilled_at',
                key_description='What they are skilled at',
                value_hint_type='Array',
                value_default='[1346, 147]',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='what_they_studied',
                key_description='What they studied',
                value_hint_type='Array',
                value_default='[100189]',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='include_subsidiaries',
                key_description='Include Subsidiaries',
                value_hint_type='Boolean',
                value_default='False',
                required=True
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Employees
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/search-employees') and
            i.nice_name == 'Search Employees')
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='geo_codes',
                key_description='Geolocation Codes '
                                '(i.e. [103644278, 102299470])',
                value_hint_type='Array',
                value_default='',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='geo_codes_exclude',
                key_description='Geolocation Codes (exclude)'
                                '(i.e. [105080838, 102257491])',
                value_hint_type='Array',
                value_default='',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='title_keywords',
                key_description='Title Keywords '
                                '(i.e. ["Director", "Operation"])',
                value_hint_type='Array',
                value_default='',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='title_keywords_exclude',
                key_description='Title Keywords (Exclude) '
                                '(i.e. ["Sales"])',
                value_hint_type='Array',
                value_default='',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='current_company_ids',
                key_description="Current Company ID's "
                                "(i.e. [162479])",
                value_hint_type='Array',
                value_default='',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='past_company_ids',
                key_description="Past Company ID's "
                                "(i.e. [1053])",
                value_hint_type='Array',
                value_default='',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='functions',
                key_description='Functions '
                                '(i.e. ["Accounting", "Administrative"])',
                value_hint_type='Array',
                value_default='',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='keywords',
                key_description="Keywords (i.e. system)",
                value_hint_type='String',
                value_default='Software Engineer',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='limit',
                key_description="Limit (i.e. 25)",
                value_hint_type='Number',
                value_default='25',
                required=True
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Employees by Sales Nav URL
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/search-employees-by-sales-nav-url') and
            i.nice_name == 'Search Employees by Sales Nav URL')
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='url',
                key_description='LinkedIn URL (with Filters)',
                value_hint_type='URL',
                value_default="""\
https://www.linkedin.com/sales/search/people?coach=false&query=(\
filters%3AList((type%3AREGION%2Cvalues%3AList((id%3A103644278%2CselectionType%3\
AINCLUDED)))%2C(type%3ACURRENT_COMPANY%2Cvalues%3AList((id%3A82274765%2Cselecti\
onType%3AINCLUDED)))))\
""",
                required=True,
                disabled=True,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='limit',
                key_description='Limit Employees per page',
                value_hint_type='Number',
                value_default='25',
                required=True,
                disabled=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Companies
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/search-companies') and
            i.nice_name == "Search Companies")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='company_headcounts',
                key_description='Company Headcount - (i.e. 1-10, '
                                '11-50, 51-200, 201-500, 501-1000, 1001-5000, '
                                '5001-10000, 10001+) '
                                '(e.g. ["1001-5000", "5001-10000"])',
                value_hint_type='Array',
                value_default='',
                required=True,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='company_headcount_growth',
                key_description='Company Headcount Growth (Example: {"min": '
                                '-10, "max": 10}) '
                                '(e.g. {"min": -10, "max": 10})',
                value_hint_type='Object',
                value_default='{"min": -10, "max": 10}',
                required=True,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='headquarters_location',
                key_description='Headquarter Location (Example: 103644278 ==> '
                                'United States. See how to find country_code '
                                'to get headquarters_location)'
                                'https://rapidapi.com/freshdata-freshdata-'
                                'default/api/fresh-linkedin-profile-data/'
                                'tutorials/how-to-find-a-geo_code-(geoid)-'
                                'on-linkedin%3F (e.g. [103644278])',
                value_hint_type='Array',
                value_default='',
                required=True,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='industry_codes',
                key_description='Industry Codes (Example: [4] ==> '
                                'Computer Soft'
                                'ware. You can find valid industry_codes '
                                'here) https://learn.microsoft.com/en-us/'
                                'linkedin/shared/references/reference-tables/'
                                'industry-codes-v2 (e.g. [3, 4])',
                value_hint_type='Array',
                value_default='[3, 4]',
                required=True,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='hiring_on_linkedin',
                key_description='Hiring on LinkedIn '
                                '(i.e. "false" '
                                'Possible values: "true", "false")',
                value_hint_type='Boolean',
                value_default='False',
                required=True,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='recent_activities',
                key_description='Recent Activities '
                                '(i.e. ["Senior leadership changes in last '
                                '3 months"]. i.e. Senior leadership changes '
                                'in last 3 months Funding events in past 12 '
                                'months")',
                value_hint_type='Boolean',
                value_default='False',
                required=True,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='keywords',
                key_description='Keywords (i.e. "Sales OR Engineer")',
                value_hint_type='String',
                value_default='False',
                required=True,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='limit',
                key_description='Limit (i.e. 1000) '
                                'Maximum: 1000. 1000 for default',
                value_hint_type='Number',
                value_default='1000',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Jobs
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/search-jobs') and
            i.nice_name == "Search Jobs")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='keywords',
                key_description='Keywords',
                value_hint_type='String',
                value_default='Software Engineer',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='geo_code',
                key_description="""Geolocation Code: Use this param to target \
jobs in specific region/country. To search worldwide, use 92000000. To find \
other geo codes, please follow this link\n\
https://rapidapi.com/freshdata-freshdata-default/api/fresh-linkedin-profile-dat\
a/tutorials/how-to-find-a-geo_code-(geoid)-on-linkedin%3F""",
                value_hint_type='Number',
                value_default='103644278',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='date_posted',
                key_description="""Date Posted: \
(i.e. \
Any time, \
Past month, \
Past week, \
Past 24 hours)""",
                value_hint_type='String',
                value_default='Any time',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='experience_levels',
                key_description="""\
Experience Level: \
(i.e. \
Internship, 
Entry level, 
Associate, \
Mid-Senior level, \
Director, \
Executive)""",
                value_hint_type='Array String',
                value_default='["Entry level"]',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='company_ids',
                key_description="""\
Company ID (Max 5 values) \
https://rapidapi.com/freshdata-freshdata-default/api/fresh-linkedin-profile-dat\
a/tutorials/how-to-find-a-company_id-on-linkedin%3F\
""",
                value_hint_type='Array Number',
                value_default='',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='title_ids',
                key_description="""\
Title ID: To find title_id by title, please follow this link \
https://rapidapi.com/freshdata-freshdata-default/api/fresh-linkedin-profile-dat\
a/tutorials/how-to-find-a-title_id-on-linkedin%3F \
(e.g. [448,179])""",
                value_hint_type='Array Number',
                value_default='',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='onsite_remotes',
                key_description="""\
On-site/Remote/Hybrid: (i.e. \
On-site, \
Remote, \
Hybrid) \
(e.g. ["Remote", "Hybrid"])""",
                value_hint_type='Array String',
                value_default='["Remote"]',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='functions',
                key_description="""\
Function ID: Please follow this instruction to get the function_id of your \
choice. \
https://rapidapi.com/freshdata-freshdata-default/api/fresh-linkedin-profile-da\
ta/tutorials/how-to-find-a-function_id-on-linkedin%3F \
(i.e. ["Sales", "Management"]) 
(Possible functions: Marketing,Sales,Business Development,Other,\
Strategy/Planning,Writing/Editing,Public Relations,Information Technology,\
Art/Creative,Administrative,Advertising)\
""",
                value_hint_type='Array String',
                value_default='',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='industries',
                key_description="""\
Industry Code: You can find all valid industry codes from this page. \
https://learn.microsoft.com/en-us/linkedin/shared/references/reference-tables/i\
ndustry-codes-v2 \
industry-codes \
(i.e. "Retail","Software Development")\
""",
                value_hint_type='Array String',
                value_default='',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='job_types',
                key_description="""\
Job Type: (i.e. \
Full-time, \
Part-time, \
Contract, \
Temporary, \
Internship, \
Other) \
(e.g. ["Internship", "Full-time", "Part-time"])""",
                value_hint_type='Array String',
                value_default='["Internship"]',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='sort_by',
                key_description="""\
Sort By: (i.e. \
Most relevant, \
Most recent)\
""",
                value_hint_type='String',
                value_default='Most recent',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='easy_apply',
                key_description='Easy Apply? (i.e. true or false)',
                value_hint_type='Boolean String',
                value_default='',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='under_10_applicants',
                key_description='Under 10 Applicants? (i.e. true or false)',
                value_hint_type='Boolean String',
                value_default='false',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='start',
                key_description="""\
Start: Should be one of: \
(i.e. 0, \
25, \
50, \
75, \
etc.)\
""",
                value_hint_type='Number',
                value_default='0',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Linkedin Profiles via Google /google-profiles
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/google-profiles') and
            i.nice_name == "Search Linkedin Profile via Google "
                           "/google-profiles")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='name',
                key_description='Full Name',
                value_hint_type='String',
                value_default='Anthony James',
                required=True,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='company',
                key_description='Company Name',
                value_hint_type='String',
                value_default='Trinity',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='job_title',
                key_description='Job Title',
                value_hint_type='String',
                value_default='CEO',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='location',
                key_description='Location',
                value_hint_type='String',
                value_default='United States',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='keyword',
                key_description='Keyword',
                value_hint_type='String',
                value_default='Software Engineer',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='page',
                key_description='Page Number',
                value_hint_type='Number',
                value_default='1',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search LinkedIn Company Pages via Google /google-companies
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/google-companies') and
            i.nice_name == "Search LinkedIn Company Pages via Google "
                           "/google-companies")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='company_name',
                key_description='Company Name',
                value_hint_type='String',
                value_default='Google',
                required=True,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='location',
                key_description='Location',
                value_hint_type='String',
                value_default='United States',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='keyword',
                key_description='Keyword',
                value_hint_type='String',
                value_default='Software Engineer',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='page',
                key_description='Page Number',
                value_hint_type='Number',
                value_default='1',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search LinkedIn School Pages via Google /google-schools
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/google-schools') and
            i.nice_name == "Search LinkedIn School Pages via Google "
                           "/google-schools")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='school_name',
                key_description='School Name',
                value_hint_type='String',
                value_default='Stanford',
                required=True,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='location',
                key_description='Location',
                value_hint_type='String',
                value_default='United States',
                required=True,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='keyword',
                key_description='Keyword',
                value_hint_type='String',
                value_default='',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='page',
                key_description='Page Number',
                value_hint_type='Number',
                value_default='1',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Decision Makers
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/search-decision-makers') and
            i.nice_name == "Search Decision Makers")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='company_ids',
                key_description='Company ID\'s (i.e. ["163640","19080118"])',
                value_hint_type='Array String',
                value_default='',
                required=True,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='title_keywords',
                key_description='Title Keywords ["CEO", "Founder", "Owner"]',
                value_hint_type='Array String',
                value_default='',
                required=True,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='geo_codes',
                key_description="Geographic Codes (i.e. "
                                "[103644278, 10229947])",
                value_hint_type='Array Number',
                value_default='[103644278]',
                required=True,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='limit',
                key_description="Limit",
                value_hint_type='String Number',
                value_default='25',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Jobs
        # Freshdata | Linkedin Jobs
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                    'https://linkedin-jobs4.p.rapidapi.com'
                    '/search-jobs') and
            i.nice_name == "Search Jobs")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='keywords',
                key_description='Keywords',
                value_hint_type='String',
                value_default='Software Engineer',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='geo_code',
                key_description="""Geolocation Code: Use this param to target \
jobs in specific region/country. To search worldwide, use 92000000. To find \
other geo codes, please follow this link\n\
https://rapidapi.com/freshdata-freshdata-default/api/fresh-linkedin-profile-
data/tutorials/how-to-find-a-geo_code-(geoid)-on-linkedin%3F""",
                value_hint_type='Number',
                value_default='103644278',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='date_posted',
                key_description="""Date Posted: \
(i.e. \
Any time, \
Past month, \
Past week, \
Past 24 hours)""",
                value_hint_type='String',
                value_default='Any time',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='experience_levels',
                key_description="""\
Experience Level: \
(i.e. \
Internship, 
Entry level, 
Associate, \
Mid-Senior level, \
Director, \
Executive)""",
                value_hint_type='Array String',
                value_default='["Entry level"]',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='company_ids',
                key_description="""\
Company ID (Max 5 values) \
https://rapidapi.com/freshdata-freshdata-default/api/fresh-linkedin-profile-dat\
a/tutorials/how-to-find-a-company_id-on-linkedin%3F\
""",
                value_hint_type='Array Number',
                value_default='',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='title_ids',
                key_description="""\
Title ID: To find title_id by title, please follow this link \
https://rapidapi.com/freshdata-freshdata-default/api/fresh-linkedin-profile-dat\
a/tutorials/how-to-find-a-title_id-on-linkedin%3F \
(e.g. [448,179])""",
                value_hint_type='Array Number',
                value_default='',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='onsite_remotes',
                key_description="""\
On-site/Remote/Hybrid: (i.e. \
On-site, 
Hybrid, \
Remote\
) \
(e.g. ["Remote", "Hybrid"])""",
                value_hint_type='Array String',
                value_default='["Remote"]',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='functions',
                key_description="""\
Function ID: Please follow this instruction to get the function_id of your \
choice. \
https://rapidapi.com/freshdata-freshdata-default/api/fresh-linkedin-profile-da\
ta/tutorials/how-to-find-a-function_id-on-linkedin%3F \
(i.e. ["Sales", "Management"]) 
(Possible functions: Marketing,Sales,Business Development,Other,\
Strategy/Planning,Writing/Editing,Public Relations,Information Technology,\
Art/Creative,Administrative,Advertising)\
""",
                value_hint_type='Array String',
                value_default='',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='industries',
                key_description="""\
Industry Code: You can find all valid industry codes from this page. \
https://learn.microsoft.com/en-us/linkedin/shared/references/reference-tables/i\
ndustry-codes-v2 \
industry-codes \
(i.e. "Retail","Software Development")\
""",
                value_hint_type='Array String',
                value_default='',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='job_types',
                key_description="""\
Job Type: (i.e. \
Full-time, \
Part-time, \
Contract, \
Temporary, \
Internship, \
Other) \
(e.g. ["Internship", "Full-time", "Part-time"])""",
                value_hint_type='Array String',
                value_default='["Internship"]',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='sort_by',
                key_description="""\
Sort By: (i.e. \
Most relevant, \
Most recent)\
""",
                value_hint_type='String',
                value_default='Most recent',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='easy_apply',
                key_description='Easy Apply? (i.e. true or false)',
                value_hint_type='Boolean String',
                value_default='',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='under_10_applicants',
                key_description='Under 10 Applicants? (i.e. true or false)',
                value_hint_type='Boolean String',
                value_default='false',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='start',
                key_description="""\
Start: Should be one of: \
(i.e. 0, \
25, \
50, \
75, \
etc.)\
""",
                value_hint_type='Number',
                value_default='0',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search
        # jaypat87 | Indeed
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://indeed11.p.rapidapi.com'
                '/') and
            i.nice_name == "Search")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='search_terms',
                key_description="Search Terms",
                value_hint_type='String',
                value_default='Software Engineer',
                required=True,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='location',
                key_description="Location",
                value_hint_type='String',
                value_default='United States',
                required=True,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='page',
                key_description="Page Number",
                value_hint_type='String Number',
                value_default='1',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Jobs Search
        # jaypat87 | Job Search
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://job-search15.p.rapidapi.com'
                '/') and
            i.nice_name == "Jobs Search")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='api_type',
                key_description="API Type",
                value_hint_type='String',
                value_default='fetch_jobs',
                required=True,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='search_terms',
                key_description="Search Terms",
                value_hint_type='String',
                value_default='Software Engineer',
                required=True,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='location',
                key_description="Location",
                value_hint_type='String',
                value_default='United States',
                required=True,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='page',
                key_description="Page Number",
                value_hint_type='String Number',
                value_default='1',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Job Description Full-Text
        # jaypat87 | Job Search
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://job-search15.p.rapidapi.com'
                '/') and
            i.nice_name == "Job Description Full-Text")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='api_type',
                key_description="API Type",
                value_hint_type='String',
                value_default='fetch_parsed_jd_by_url',
                required=True,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='job_url',
                key_description="Job URL",
                value_hint_type='URL',
                value_default='https://www.linkedin.com/jobs/view/regional'
                              '-marketing-manager-at-sweetgreen-3588494268',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Named Entity Extraction
        # jaypat87 | Job Search
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://job-search15.p.rapidapi.com'
                '/') and
            i.nice_name == "Named Entity Extraction")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='api_type',
                key_description="API Type",
                value_hint_type='String',
                value_default='named_entity_extraction',
                required=True,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='input_text',
                key_description="Input Text",
                value_hint_type='String',
                value_default="""\
Key Expectations:  To create a caring strategy to strengthen relationships with\
guests and our local community by investing in our unique assets; Food, People,\
Cows and Influence, by operating as the face of our brand both in the store and\
in the community. \\n \\n \\n  Community \\n  Oversee food donation program. \
\\n Oversee store events including Spirit Nights, Family Nights, Daddy/Daughter\
Nights, etc. \\n  Oversee and build strategic business partnerships with \
schools\
and businesses. \\n  Create processes that protect and build brand awareness,\
drive sales, and demonstrate the Winning Hearts Everyday strategy. \\n  Manage\
community request forms in store email. \\n  Lead with real food through\
sampling and encouraging team members to personalize the customer's experience.\
\\n \\n \\n \\n  Outside Sales \\n  Own the full-cycle of the catering process.\
\\n  Collaborate with the Back of House Director to ensure catering material\
inventory is managed. \\n  Oversee alongside Administrative Coordinator\
maintenance of catering vehicles (gas, oil change, cleanliness, etc.) \\n \
Oversee Additional Distribution Points (ADPs). \\n  Proactively seek new\
catering business to increase sales and awareness. \\n  Develop a catering \
sales\
database. \\n  Collaborate with General Managers to develop and maintain\
catering sales guidelines. \\n \\n \\n \\n  Marketing \\n  Oversee social media\
strategy: Facebook, Instagram, Spotlight, & CFA One App. \\n  Develop a\
quarterly marketing and community outreach calendar. \\n  Oversee Cow Program\
including identifying opportunities, collaborating with General Managers on\
scheduling Cow and Handler and maintaining clean uniforms. \\n  Collaborate \
with\
General Managers to schedule and execute a monthly Sampling Program. \\n  \
Manage\
Community Boards and holiday decor. \\n  Collaborate with the General Manager\
and Sr. Business Director on monthly budget and tracking. \\n  Identify paid \
and\
unpaid (trade or otherwise) advertising and marketing opportunities \
(Billboards,\
Sponsorships, Signage, Vehicle Wraps, Events, etc.) \\n  Oversee flower \
pickup\
and delivery from Wegmans every 3 weeks and setting up fresh flowers in the\
dining room \\n  Create a marketing plan and work with the General Manager to\
execute. \\n \\n \\n  Marketing Manager: (Subject to change) \\n \\n  Must be\
available and work up to 40 hours per week in the restaurant. \\n  Must be\
ServeSafe, Choke, and Allergen Certified. \\n  Execute the S.E.R.V.E. \
Leadership\
Model. \\n  Lead the team with enthusiasm and passion. \\n  10-12 Hours of \
admin\
per week (Subject to operational needs) \\n \\n \\n  REQUIREMENTS \\n \\n  Must\
be at least 18 years of age upon hire date \\n  Must be eligible to work in the\
United States \\n  Must have a source of reliable transportation \\n  Must have\
reliable transportation \\n  Works in fast paced environment \\n  Mobility\
required during shifts \\n  Must work well under pressure \\n \\n  In our\
kitchens, we focus on fresh and simple ingredients. And we always have. Since\
the beginning, we've served chicken that is whole breast meat, with no added\
fillers or hormones, and we bread it by hand in our restaurants. Produce is\
delivered fresh to our kitchens several times a week. Salads are chopped and\
prepared fresh throughout the day. Whole lemons are freshly squeezed in our\
restaurants and combined with pure cane sugar and water (yep, that\\u2019s all)\
to make Chick-fil-A Lemonade\\u00ae. It may not be the easy way, but it's the\
only way we know.\
""",
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Jobs Classifier
        # jaypat87 | Job Search
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://job-search15.p.rapidapi.com'
                '/') and
            i.nice_name == "Jobs Classifier")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='api_type',
                key_description="API Type",
                value_hint_type='String',
                value_default='jobs_classifier',
                required=True,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='input_text',
                key_description="Input Text",
                value_hint_type='String',
                value_default="""\
Key Expectations:  To create a caring strategy to strengthen relationships with\
guests and our local community by investing in our unique assets; Food, People,\
Cows and Influence, by operating as the face of our brand both in the store and\
in the community. \\n \\n \\n  Community \\n  Oversee food donation program. \
\\n Oversee store events including Spirit Nights, Family Nights, Daddy/Daughter\
Nights, etc. \\n  Oversee and build strategic business partnerships with \
schools\
and businesses. \\n  Create processes that protect and build brand awareness,\
drive sales, and demonstrate the Winning Hearts Everyday strategy. \\n  Manage\
community request forms in store email. \\n  Lead with real food through\
sampling and encouraging team members to personalize the customer's experience.\
\\n \\n \\n \\n  Outside Sales \\n  Own the full-cycle of the catering process.\
\\n  Collaborate with the Back of House Director to ensure catering material\
inventory is managed. \\n  Oversee alongside Administrative Coordinator\
maintenance of catering vehicles (gas, oil change, cleanliness, etc.) \\n \
Oversee Additional Distribution Points (ADPs). \\n  Proactively seek new\
catering business to increase sales and awareness. \\n  Develop a catering \
sales\
database. \\n  Collaborate with General Managers to develop and maintain\
catering sales guidelines. \\n \\n \\n \\n  Marketing \\n  Oversee social media\
strategy: Facebook, Instagram, Spotlight, & CFA One App. \\n  Develop a\
quarterly marketing and community outreach calendar. \\n  Oversee Cow Program\
including identifying opportunities, collaborating with General Managers on\
scheduling Cow and Handler and maintaining clean uniforms. \\n  Collaborate \
with\
General Managers to schedule and execute a monthly Sampling Program. \\n  \
Manage\
Community Boards and holiday decor. \\n  Collaborate with the General Manager\
and Sr. Business Director on monthly budget and tracking. \\n  Identify paid \
and\
unpaid (trade or otherwise) advertising and marketing opportunities \
(Billboards,\
Sponsorships, Signage, Vehicle Wraps, Events, etc.) \\n  Oversee flower \
pickup\
and delivery from Wegmans every 3 weeks and setting up fresh flowers in the\
dining room \\n  Create a marketing plan and work with the General Manager to\
execute. \\n \\n \\n  Marketing Manager: (Subject to change) \\n \\n  Must be\
available and work up to 40 hours per week in the restaurant. \\n  Must be\
ServeSafe, Choke, and Allergen Certified. \\n  Execute the S.E.R.V.E. \
Leadership\
Model. \\n  Lead the team with enthusiasm and passion. \\n  10-12 Hours of \
admin\
per week (Subject to operational needs) \\n \\n \\n  REQUIREMENTS \\n \\n  Must\
be at least 18 years of age upon hire date \\n  Must be eligible to work in the\
United States \\n  Must have a source of reliable transportation \\n  Must have\
reliable transportation \\n  Works in fast paced environment \\n  Mobility\
required during shifts \\n  Must work well under pressure \\n \\n  In our\
kitchens, we focus on fresh and simple ingredients. And we always have. Since\
the beginning, we've served chicken that is whole breast meat, with no added\
fillers or hormones, and we bread it by hand in our restaurants. Produce is\
delivered fresh to our kitchens several times a week. Salads are chopped and\
prepared fresh throughout the day. Whole lemons are freshly squeezed in our\
restaurants and combined with pure cane sugar and water (yep, that\\u2019s all)\
to make Chick-fil-A Lemonade\\u00ae. It may not be the easy way, but it's the\
only way we know.\
""",
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Summarize Job Descriptions
        # jaypat87 | Job Search
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://job-search15.p.rapidapi.com'
                '/') and
            i.nice_name == "Summarize Job Descriptions")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='api_type',
                key_description="API Type",
                value_hint_type='String',
                value_default='summarization',
                required=True,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='input_text',
                key_description="Input Text",
                value_hint_type='String',
                value_default="""\
Key Expectations:  To create a caring strategy to strengthen relationships with\
guests and our local community by investing in our unique assets; Food, People,\
Cows and Influence, by operating as the face of our brand both in the store and\
in the community. \\n \\n \\n  Community \\n  Oversee food donation program. \
\\n Oversee store events including Spirit Nights, Family Nights, Daddy/Daughter\
Nights, etc. \\n  Oversee and build strategic business partnerships with \
schools\
and businesses. \\n  Create processes that protect and build brand awareness,\
drive sales, and demonstrate the Winning Hearts Everyday strategy. \\n  Manage\
community request forms in store email. \\n  Lead with real food through\
sampling and encouraging team members to personalize the customer's experience.\
\\n \\n \\n \\n  Outside Sales \\n  Own the full-cycle of the catering process.\
\\n  Collaborate with the Back of House Director to ensure catering material\
inventory is managed. \\n  Oversee alongside Administrative Coordinator\
maintenance of catering vehicles (gas, oil change, cleanliness, etc.) \\n \
Oversee Additional Distribution Points (ADPs). \\n  Proactively seek new\
catering business to increase sales and awareness. \\n  Develop a catering \
sales\
database. \\n  Collaborate with General Managers to develop and maintain\
catering sales guidelines. \\n \\n \\n \\n  Marketing \\n  Oversee social media\
strategy: Facebook, Instagram, Spotlight, & CFA One App. \\n  Develop a\
quarterly marketing and community outreach calendar. \\n  Oversee Cow Program\
including identifying opportunities, collaborating with General Managers on\
scheduling Cow and Handler and maintaining clean uniforms. \\n  Collaborate \
with\
General Managers to schedule and execute a monthly Sampling Program. \\n  \
Manage\
Community Boards and holiday decor. \\n  Collaborate with the General Manager\
and Sr. Business Director on monthly budget and tracking. \\n  Identify paid \
and\
unpaid (trade or otherwise) advertising and marketing opportunities \
(Billboards,\
Sponsorships, Signage, Vehicle Wraps, Events, etc.) \\n  Oversee flower \
pickup\
and delivery from Wegmans every 3 weeks and setting up fresh flowers in the\
dining room \\n  Create a marketing plan and work with the General Manager to\
execute. \\n \\n \\n  Marketing Manager: (Subject to change) \\n \\n  Must be\
available and work up to 40 hours per week in the restaurant. \\n  Must be\
ServeSafe, Choke, and Allergen Certified. \\n  Execute the S.E.R.V.E. \
Leadership\
Model. \\n  Lead the team with enthusiasm and passion. \\n  10-12 Hours of \
admin\
per week (Subject to operational needs) \\n \\n \\n  REQUIREMENTS \\n \\n  Must\
be at least 18 years of age upon hire date \\n  Must be eligible to work in the\
United States \\n  Must have a source of reliable transportation \\n  Must have\
reliable transportation \\n  Works in fast paced environment \\n  Mobility\
required during shifts \\n  Must work well under pressure \\n \\n  In our\
kitchens, we focus on fresh and simple ingredients. And we always have. Since\
the beginning, we've served chicken that is whole breast meat, with no added\
fillers or hormones, and we bread it by hand in our restaurants. Produce is\
delivered fresh to our kitchens several times a week. Salads are chopped and\
prepared fresh throughout the day. Whole lemons are freshly squeezed in our\
restaurants and combined with pure cane sugar and water (yep, that\\u2019s all)\
to make Chick-fil-A Lemonade\\u00ae. It may not be the easy way, but it's the\
only way we know.\
""",
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search
        # jaypat87 | Linkedin Jobs Search
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-jobs-search.p.rapidapi.com'
                '/') and
            i.nice_name == "Search")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='search_terms',
                key_description="Search Terms",
                value_hint_type='String',
                value_default='Software Engineer',
                required=True,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='location',
                key_description="Location",
                value_hint_type='String',
                value_default='United States',
                required=True,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='page',
                key_description="Page Number",
                value_hint_type='String Number',
                value_default='1',
                required=True,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='fetch_full_text',
                key_description="Fetch Full Text",
                value_hint_type='Boolean String',
                value_default='False',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Jobs
        # jobisite | Job Search
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://job-search38.p.rapidapi.com'
                '/my/searchJobs') and
            i.nice_name == "Search Jobs")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='id',
                key_description="ID",
                value_hint_type='String',
                value_default='LKJLJ12JHV',
                required=True,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='key',
                key_description="Key",
                value_hint_type='String',
                value_default='6576CGF55C5X9CVX12X9CVX12POG9VG4LKL99JH',
                required=True,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='filter',
                key_description='Filters (Limit Required)',
                value_hint_type='Object',
                value_default="""\
"skill": "Software Engineer", "location": "New York", "limit": 10
""",
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # httpsJobapiCoUkGet
        # JobsAPI2020 | Zambian Jobs API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://zambian-jobs-api1.p.rapidapi.com'
                '/getdataNew.php') and
            i.nice_name == "httpsJobapiCoUkGet")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='page',
                key_description="Page Number",
                value_hint_type='Number',
                value_default='1',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='get_descr',
                key_description="Get Description",
                value_hint_type='String',
                value_default='get_descr',
                required=False,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='password',
                key_description="Password",
                value_hint_type='String',
                value_default='&AwmDxwwzG9Z&Ed6ygo0?%&@q',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # classifyJD
        # Jobwiz | Job Descriptions API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://job-descriptions-api.p.rapidapi.com'
                '/v1/job-description-classification-onet') and
            i.nice_name == "classifyJD")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='title',
                key_description="Title",
                value_hint_type='String',
                value_default='Software Engineer',
                required=True,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='job_description',
                key_description="Job Description",
                value_hint_type='String',
                value_default="""\
Job Summary:\n\nWe are looking for a skilled Front End Web Developer who will \
be\
responsible for developing and implementing the user interface of our websites.\
You will work closely with our web team to ensure that our sites are visually\
appealing and user-friendly. Your primary focus will be to improve the user\
experience by partnering with the web team to create responsive, intuitive, and\
engaging web pages.\n\nKey Responsibilities:\n• Be a core contributor to the\
front-end development, optimization, and infrastructure of business messaging\
marketing websites such as business.whatsapp.com\n• Develop and implement new\
features and functionality using front-end technologies such as HTML, CSS,\
JavaScript, and React.js\n• Write clean, efficient, and well-documented code\
that is compatible with all modern browsers and devices.\n• Help us build a\
best-in-class experience on our marketing website for both end-users and our\
internal team\n• Collaborate with design to create visually appealing and\
intuitive user interfaces for our websites\n• Create and optimize web pages for\
speed, performance, and accessibility best practices and techniques for \
creating\
web content that is inclusive and usable by all individuals.\n• Test and debug\
web pages across multiple browsers and devices to ensure cross-browser\
compatibility\n• Stay up-to-date with emerging trends and technologies in\
front-end development.\n• Proactive communication skills and the ability to\
communicate technical concepts to non-technical\
collaborators\n\nQualifications:\n• Bachelor's degree in Computer Science, Web\
Development, or related field.\n• 2-5 years of experience as a Front End Web\
Developer or similar role.\n• Strong proficiency in front-end technologies \
such\
as HTML, CSS, JavaScript, and React.js\n• Experience with responsive design and\
development.\n• Knowledge of cross-browser compatibility issues and ways to \
work\
around them.\n• Understanding of web development best practices, including\
optimization for speed and performance.\n• Familiarity with server-side CSS\
pre-processing platforms such as Sass or Less is a plus.\n• Ability to work\
independently and as part of a team in a fast-paced environment..\n• Strong\
communication skills and ability to collaborate with both technical and\
non-technical stakeholders\n\nIf you are passionate about web development and\
have a keen eye for design, we encourage you to apply for this exciting\
opportunity to work with our team.\n\nMUST HAVES:\n\n1. Develop and implement\
new features and functionality using front-end technologies such as HTML, CSS,\
JavaScript, and React.js\n\n2. Collaborate with design to create visually\
appealing and intuitive user interfaces for our websites\n\n3. Create and\
optimize web pages for speed, performance, and accessibility best practices and\
techniques for creating web content that is inclusive and usable by all\
individuals.\n\nQualifications\n\nReactJS, Javascript, HTML, CSS\n\nAdditional\
Information\n\nAll your information will be kept confidential according to EEO\
guidelines\
""",
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # batchClassifyJD
        # Jobwiz | Job Descriptions API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://job-descriptions-api.p.rapidapi.com'
                '/v1/job-description-classification-onet-batch') and
            i.nice_name == "batchClassifyJD")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='jobs',
                key_description="Jobs",
                value_hint_type='Array Object',
                value_default="""\
[
    {
    "title": "React.js developer",
    "job_description": "Job Summary:\n\nWe are looking for a skilled Front End\
Web Developer who will be responsible for developing and implementing the\
user interface of our websites. You will work closely with our web team to\
ensure that our sites are visually appealing and user-friendly. Your primary\
focus will be to improve the user experience by partnering with the web team\
to create responsive, intuitive, and engaging web pages.\n\nKey\
Responsibilities:\n• Be a core contributor to the front-end development,\
optimization, and infrastructure of business messaging marketing websites\
such as business.whatsapp.com\n• Develop and implement new features and\
functionality using front-end technologies such as HTML, CSS, JavaScript,\
and React.js\n• Write clean, efficient, and well-documented code that is\
compatible with all modern browsers and devices.\n• Help us build a\
best-in-class experience on our marketing website for both end-users and our\
internal team\n• Collaborate with design to create visually appealing and\
intuitive user interfaces for our websites\n• Create and optimize web pages\
for speed, performance, and accessibility best practices and techniques for\
creating web content that is inclusive and usable by all individuals.\n•\
Test and debug web pages across multiple browsers and devices to ensure\
cross-browser compatibility\n• Stay up-to-date with emerging trends and\
technologies in front-end development.\n• Proactive communication skills and\
the ability to communicate technical concepts to non-technical\
collaborators\n\nQualifications:\n• Bachelor's degree in Computer Science,\
Web Development, or related field.\n• 2-5 years of experience as a Front End\
Web Developer or similar role.\n• Strong proficiency in front-end\
technologies such as HTML, CSS, JavaScript, and React.js\n• Experience with\
responsive design and development.\n• Knowledge of cross-browser\
compatibility issues and ways to work around them.\n• Understanding of web\
development best practices, including optimization for speed and\
performance.\n• Familiarity with server-side CSS pre-processing platforms\
such as Sass or Less is a plus.\n• Ability to work independently and as part\
of a team in a fast-paced environment..\n• Strong communication skills and\
ability to collaborate with both technical and non-technical\
stakeholders\n\nIf you are passionate about web development and have a keen\
eye for design, we encourage you to apply for this exciting opportunity to\
work with our team.\n\nMUST HAVES:\n\n1. Develop and implement new features\
and functionality using front-end technologies such as HTML, CSS,\
JavaScript, and React.js\n\n2. Collaborate with design to create visually\
appealing and intuitive user interfaces for our websites\n\n3. Create and\
optimize web pages for speed, performance, and accessibility best practices\
and techniques for creating web content that is inclusive and usable by all\
individuals.\n\nQualifications\n\nReactJS, Javascript, HTML,\
CSS\n\nAdditional Information\n\nAll your information will be kept\
confidential according to EEO guidelines"\
    }
]\
""",
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # batchExtractSalaryRange
        # Jobwiz | Job Descriptions API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://job-descriptions-api.p.rapidapi.com'
                '/v1/job-description-salary-range-batch') and
            i.nice_name == "batchExtractSalaryRange")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='jobs',
                key_description="Jobs",
                value_hint_type='Array Object',
                value_default="""\
[
    {
      "job_description": "DESCRIPTION:\n\nDuties: Serve as technical project\
lead for a geographically diverse engineering team across global time\
zones. Design and develop data models and build complex stored procedures\
and SQL queries and reports. Perform database troubleshooting and\
performance tuning. Serve as Scrum Lead for Agile Scrum development\
framework. Utilize strong knowledge of Fixed Income Products specifically\
Securitized Products, to engage with stakeholders and clients to\
understand and meet needs through design and solutions. Translate\
requirements into technical specifications and lead development projects\
to satisfy requirements. Provide hands-on support to product users.\
Develop and leverage experience with internal Market Risk infrastructure\
and systems to coordinate with other applications to deliver complete\
product solutions for users. Deliver trainings on all application\
technical components, as well as business purpose and functionality.\
Telecommuting permitted up to 40% of the\
week.\n\nQUALIFICATIONS:\n\nMinimum education and experience required:\
Bachelor's Degree in Computer Engineering, Computer Science, Information\
Technology, or related field of study plus 7 years of experience in the\
job offered or as Software Engineer, Software Developer, Database Analyst,\
Application Developer, IT Consultant or related occupation.\n\nSkills\
Required: Requires experience in the following: leading technical\
projects; designing and developing SQL Server databases, using SSIS ETL\
tool; database performance and tuning; Microsoft C# .Net Core; Microsoft\
Visual Studio; UI skills with JavaScript and React.js; system design and\
implementation on Cloud platform; Agile Scrum development framework; code\
and release management and deployment tools; Bitbucket; Jules; Fixed\
Income products, including Securitized Products; implementing unit test\
coverage; and secure authentication and authorization patterns.\n\nJob\
Location: 383 Madison Avenue, New York, NY 10179. Telecommuting permitted\
up to 40% of the week.\n\nFull-Time. Salary: $180,000 - $260,000 per\
year.\nThe Corporate & Investment Bank is a global leader across\
investment banking, wholesale payments, markets and securities services.\
The world's most important corporations, governments and institutions\
entrust us with their business in more than 100 countries. We provide\
strategic advice, raise capital, manage risk and extend liquidity in\
markets around the world. JPMorgan Chase & Co., one of the oldest\
financial institutions, offers innovative financial solutions to millions\
of consumers, small businesses and many of the world's most prominent\
corporate, institutional and government clients under the J.P. Morgan and\
Chase brands. Our history spans over 200 years and today we are a leader\
in investment banking, consumer and small business banking, commercial\
banking, financial transaction processing and asset management.\n\nWe\
recognize that our people are our strength and the diverse talents and\
perspectives that they bring to our global workforce are directly linked\
to our success. We are an equal opportunity employer and place a high\
value on diversity and inclusion at our company. We do not discriminate on\
the basis of any protected attribute, including race, religion, color,\
national origin, gender, sexual orientation, gender identity, gender\
expression, age, marital or veteran status, pregnancy or disability, or\
any other basis protected under applicable law. In accordance with\
applicable law, we make reasonable accommodations for applicants' and\
employees' religious practices and beliefs, as well as any mental health\
or physical disability needs. (If you are a US or Canadian applicant with\
a disability and wish to request an accommodation to complete the\
application process, please contact us by calling the Accessibility Line\
(US and Canada Only) 1-866-777-4690 and indicate the specifics of the\
assistance needed.)\n\nWe offer a competitive total rewards package\
including base salary determined based on the role, experience, skill set,\
and location. For those in eligible roles, we offer discretionary\
incentive compensation which may be awarded in recognition of firm\
performance and individual achievements and contributions. We also offer a\
range of benefits and programs to meet employee needs, based on\
eligibility. These benefits include comprehensive health care coverage,\
on-site health and wellness centers, a retirement savings plan, backup\
childcare, tuition reimbursement, mental health support, financial\
coaching and more. Additional details about total compensation and\
benefits will be provided during the hiring process.\n\nJPMorgan Chase is\
an Equal Opportunity Employer, including Disability/Veterans"\
    }
  ]
""",
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # batchExtractYearsExperience
        # Jobwiz | Job Descriptions API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://job-descriptions-api.p.rapidapi.com'
                '/v1/job-description-years-experience-batch') and
            i.nice_name == "batchExtractYearsExperience")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='language',
                key_description="Language",
                value_hint_type='String',
                value_default='en',
                required=True,
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='jobs',
                key_description="Jobs",
                value_hint_type='Array Object',
                value_default="""\
[
    {
      "job_description": "DESCRIPTION:\n\nDuties: Serve as technical project\
lead for a geographically diverse engineering team across global time\
zones. Design and develop data models and build complex stored procedures\
and SQL queries and reports. Perform database troubleshooting and\
performance tuning. Serve as Scrum Lead for Agile Scrum development\
framework. Utilize strong knowledge of Fixed Income Products specifically\
Securitized Products, to engage with stakeholders and clients to\
understand and meet needs through design and solutions. Translate\
requirements into technical specifications and lead development projects\
to satisfy requirements. Provide hands-on support to product users.\
Develop and leverage experience with internal Market Risk infrastructure\
and systems to coordinate with other applications to deliver complete\
product solutions for users. Deliver trainings on all application\
technical components, as well as business purpose and functionality.\
Telecommuting permitted up to 40% of the\
week.\n\nQUALIFICATIONS:\n\nMinimum education and experience required:\
Bachelor's Degree in Computer Engineering, Computer Science, Information\
Technology, or related field of study plus 7 years of experience in the\
job offered or as Software Engineer, Software Developer, Database Analyst,\
Application Developer, IT Consultant or related occupation.\n\nSkills\
Required: Requires experience in the following: leading technical\
projects; designing and developing SQL Server databases, using SSIS ETL\
tool; database performance and tuning; Microsoft C# .Net Core; Microsoft\
Visual Studio; UI skills with JavaScript and React.js; system design and\
implementation on Cloud platform; Agile Scrum development framework; code\
and release management and deployment tools; Bitbucket; Jules; Fixed\
Income products, including Securitized Products; implementing unit test\
coverage; and secure authentication and authorization patterns.\n\nJob\
Location: 383 Madison Avenue, New York, NY 10179. Telecommuting permitted\
up to 40% of the week.\n\nFull-Time. Salary: $180,000 - $260,000 per\
year.\nThe Corporate & Investment Bank is a global leader across\
investment banking, wholesale payments, markets and securities services.\
The world's most important corporations, governments and institutions\
entrust us with their business in more than 100 countries. We provide\
strategic advice, raise capital, manage risk and extend liquidity in\
markets around the world. JPMorgan Chase & Co., one of the oldest\
financial institutions, offers innovative financial solutions to millions\
of consumers, small businesses and many of the world's most prominent\
corporate, institutional and government clients under the J.P. Morgan and\
Chase brands. Our history spans over 200 years and today we are a leader\
in investment banking, consumer and small business banking, commercial\
banking, financial transaction processing and asset management.\n\nWe\
recognize that our people are our strength and the diverse talents and\
perspectives that they bring to our global workforce are directly linked\
to our success. We are an equal opportunity employer and place a high\
value on diversity and inclusion at our company. We do not discriminate on\
the basis of any protected attribute, including race, religion, color,\
national origin, gender, sexual orientation, gender identity, gender\
expression, age, marital or veteran status, pregnancy or disability, or\
any other basis protected under applicable law. In accordance with\
applicable law, we make reasonable accommodations for applicants' and\
employees' religious practices and beliefs, as well as any mental health\
or physical disability needs. (If you are a US or Canadian applicant with\
a disability and wish to request an accommodation to complete the\
application process, please contact us by calling the Accessibility Line\
(US and Canada Only) 1-866-777-4690 and indicate the specifics of the\
assistance needed.)\n\nWe offer a competitive total rewards package\
including base salary determined based on the role, experience, skill set,\
and location. For those in eligible roles, we offer discretionary\
incentive compensation which may be awarded in recognition of firm\
performance and individual achievements and contributions. We also offer a\
range of benefits and programs to meet employee needs, based on\
eligibility. These benefits include comprehensive health care coverage,\
on-site health and wellness centers, a retirement savings plan, backup\
childcare, tuition reimbursement, mental health support, financial\
coaching and more. Additional details about total compensation and\
benefits will be provided during the hiring process.\n\nJPMorgan Chase is\
an Equal Opportunity Employer, including Disability/Veterans"\
    }
  ]
""",
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # extractYearsExperience
        # Jobwiz | Job Descriptions API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://job-descriptions-api.p.rapidapi.com'
                '/v1/job-description-years-experience') and
            i.nice_name == "extractYearsExperience")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='job_description',
                key_description="Job Description",
                value_hint_type='String',
                value_default="""\
"DESCRIPTION:\n\nDuties: Serve as technical project lead for a geographically\
diverse engineering team across global time zones. Design and develop data\
models and build complex stored procedures and SQL queries and reports. Perform\
database troubleshooting and performance tuning. Serve as Scrum Lead for Agile\
Scrum development framework. Utilize strong knowledge of Fixed Income Products\
specifically Securitized Products, to engage with stakeholders and clients to\
understand and meet needs through design and solutions. Translate requirements\
into technical specifications and lead development projects to satisfy\
requirements. Provide hands-on support to product users. Develop and leverage\
experience with internal Market Risk infrastructure and systems to coordinate\
with other applications to deliver complete product solutions for users. \
Deliver\
trainings on all application technical components, as well as business purpose\
and functionality. Telecommuting permitted up to 40% of the\
week.\n\nQUALIFICATIONS:\n\nMinimum education and experience required:\
Bachelor's Degree in Computer Engineering, Computer Science, Information\
Technology, or related field of study plus 7 years of experience in the job\
offered or as Software Engineer, Software Developer, Database Analyst,\
Application Developer, IT Consultant or related occupation.\n\nSkills Required:\
Requires experience in the following: leading technical projects; designing and\
developing SQL Server databases, using SSIS ETL tool; database performance and\
tuning; Microsoft C# .Net Core; Microsoft Visual Studio; UI skills with\
JavaScript and React.js; system design and implementation on Cloud platform;\
Agile Scrum development framework; code and release management and deployment\
tools; Bitbucket; Jules; Fixed Income products, including Securitized Products;\
implementing unit test coverage; and secure authentication and authorization\
patterns.\n\nJob Location: 383 Madison Avenue, New York, NY 10179. \
Telecommuting\
permitted up to 40% of the week.\n\nFull-Time. Salary: $180,000 - $260,000 per\
year."\
""",
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # extractSalaryRange
        # Jobwiz | Job Descriptions API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://job-descriptions-api.p.rapidapi.com'
                '/v1/job-description-salary-range') and
            i.nice_name == "extractSalaryRange")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='job_description',
                key_description="Job Description",
                value_hint_type='String',
                value_default="""\
"DESCRIPTION:\n\nDuties: Serve as technical project lead for a geographically\
diverse engineering team across global time zones. Design and develop data\
models and build complex stored procedures and SQL queries and reports. Perform\
database troubleshooting and performance tuning. Serve as Scrum Lead for Agile\
Scrum development framework. Utilize strong knowledge of Fixed Income Products\
specifically Securitized Products, to engage with stakeholders and clients to\
understand and meet needs through design and solutions. Translate requirements\
into technical specifications and lead development projects to satisfy\
requirements. Provide hands-on support to product users. Develop and leverage\
experience with internal Market Risk infrastructure and systems to coordinate\
with other applications to deliver complete product solutions for users. \
Deliver\
trainings on all application technical components, as well as business purpose\
and functionality. Telecommuting permitted up to 40% of the\
week.\n\nQUALIFICATIONS:\n\nMinimum education and experience required:\
Bachelor's Degree in Computer Engineering, Computer Science, Information\
Technology, or related field of study plus 7 years of experience in the job\
offered or as Software Engineer, Software Developer, Database Analyst,\
Application Developer, IT Consultant or related occupation.\n\nSkills Required:\
Requires experience in the following: leading technical projects; designing and\
developing SQL Server databases, using SSIS ETL tool; database performance and\
tuning; Microsoft C# .Net Core; Microsoft Visual Studio; UI skills with\
JavaScript and React.js; system design and implementation on Cloud platform;\
Agile Scrum development framework; code and release management and deployment\
tools; Bitbucket; Jules; Fixed Income products, including Securitized Products;\
implementing unit test coverage; and secure authentication and authorization\
patterns.\n\nJob Location: 383 Madison Avenue, New York, NY 10179. \
Telecommuting\
permitted up to 40% of the week.\n\nFull-Time. Salary: $180,000 - $260,000 per\
year."\
""",
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Person Data
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/person') and
            i.nice_name == "Person Data")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='link',
                key_description='LinkedIn URL Profile',
                value_hint_type='URL',
                value_default='http://www.linkedin.com/in/ingmar-klein/',
                required=True
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Person Data (Using Urn)
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/person_urn') and
            i.nice_name == "Person Data ( Using Urn )")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='link',
                key_description='LinkedIn URL Profile',
                value_hint_type='URL',
                value_default='http://www.linkedin.com/in/ingmar-klein/',
                required=True
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Person Posts ( BETA )
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/profile_updates') and
            i.nice_name == "Person Posts ( BETA )")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='profile_url',
                key_description='LinkedIn URL Profile',
                value_hint_type='URL',
                value_default='http://www.linkedin.com/in/ingmar-klein/',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='posts',
                key_description='Posts',
                value_hint_type='Number',
                value_default='1',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='comments',
                key_description='Comments',
                value_hint_type='Number',
                value_default='1',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='reposts',
                key_description='Reposts',
                value_hint_type='Number',
                value_default='1',
                required=True
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Person Recent Activity (Comments on Posts) /profile_recent_comments
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/profile_recent_comments') and
            i.nice_name == "Person Recent Activity ( Comments on Posts ) "
                           "/profile_recent_comments")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='profile_url',
                key_description='LinkedIn URL Profile',
                value_hint_type='URL',
                value_default='https://www.linkedin.com/in/williamhgates/',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='page',
                key_description='Page Number',
                value_hint_type='Number',
                value_default='1',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='paginationToken',
                key_description='Pagination Token',
                value_hint_type='String',
                value_default='dXJuOmxpOmFjdGl2aXR5OjY4NTgwNTk2MjQ1NDU4NDkzNDQt'
                              'MTYzNTA4ODgxMjUwNA==',
                required=False
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Email to Linkedin Profile (BETA) /email_to_linkedin_profile
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/email_to_linkedin_profile') and
            i.nice_name == "Email to Linkedin Profile ( BETA ) "
                           "/email_to_linkedin_profile")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='email',
                key_description='Email of LinkedIn User',
                value_hint_type='String Email',
                value_default='mgujjargamingm@gmail.com',
                required=True
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Check on Person Job Changed Status /person_job_change_status
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/person_job_change_status') and
            i.nice_name == "Check on Person Job Changed Status "
                           "/person_job_change_status")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='link',
                key_description='LinkedIn URL Profile',
                value_hint_type='URL',
                value_default='https://www.linkedin.com/in/ingmar-klein',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='currentCompanyId',
                key_description='Current Company ID',
                value_hint_type='String',
                value_default='69513203',
                required=True
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Similar Profiles
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/similar_profiles') and
            i.nice_name == "Similar Profiles")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='profileUrl',
                key_description='LinkedIn URL Profile',
                value_hint_type='URL',
                value_default='https://www.linkedin.com/in/ingmar-klein',
                required=True
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Company Data
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/company') and
            i.nice_name == "Company Data")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='link',
                key_description='LinkedIn Company URL Profile',
                value_hint_type='URL',
                value_default='http://www.linkedin.com/company/google',
                required=True
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Company Data (Premium)
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/company_pro') and
            i.nice_name == "Company Data (Premium)")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='link',
                key_description='LinkedIn Company URL Profile',
                value_hint_type='URL',
                value_default='http://www.linkedin.com/company/google',
                required=True
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Company data from web-domain /web-domain
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/web-domain') and
            i.nice_name == "Company data from web-domain /web-domain")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='link',
                key_description='Company URL Profile',
                value_hint_type='URL',
                value_default='huzzle.app',
                required=True
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Company Jobs
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/company_jobs') and
            i.nice_name == "Company Jobs")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='company_url',
                key_description='LinkedIn Company URL Profile',
                value_hint_type='URL',
                value_default='http://www.linkedin.com/company/google',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='count',
                key_description='Number of Jobs',
                value_hint_type='Number',
                value_default='10',
                required=True
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Company Employee count per skill /company_employee_count_per_skill
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/company_employee_count_per_skill') and
            i.nice_name == "Company Employee count per skill "
                           "/company_employee_count_per_skill")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='company_url',
                key_description='LinkedIn Company URL Profile',
                value_hint_type='URL',
                value_default='https://www.linkedin.com/company/flying-bark'
                              '-productions',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='skillExplicits',
                key_description='Explicit Skills (i.e. 1840,1455)',
                value_hint_type='String',
                value_default='',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='keyword',
                key_description='Keyword',
                value_hint_type='String',
                value_default='Software Engineer',
                required=True
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Company Posts ( BETA )
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/company_updates') and
            i.nice_name == "Company Posts ( BETA )")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='company_url',
                key_description='LinkedIn Company URL Profile',
                value_hint_type='URL',
                value_default='http://www.linkedin.com/company/google',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='posts',
                key_description='Posts',
                value_hint_type='Number',
                value_default='10',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='comments',
                key_description='Comments',
                value_hint_type='Number',
                value_default='10',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='reposts',
                key_description='Reposts',
                value_hint_type='Number',
                value_default='10',
                required=False
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Leads
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/premium_search_person') and
            i.nice_name == "Search Leads")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='page',
                key_description='Page Number',
                value_hint_type='Number',
                value_default='1',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='keywords',
                key_description='Keywords',
                value_hint_type='String',
                value_default='paul',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='filters',
                key_description='Filters',
                value_hint_type='Array Object',
                value_default='''\
[
  {
    "type": "CURRENT_COMPANY",
    "values": [
      {
        "id": "urn:li:organization:1586",
        "text": "Amazon",
        "selectionType": "INCLUDED"
      },
      {
        "id": "urn:li:organization:1441",
        "text": "Google",
        "selectionType": "INCLUDED"
      }
    ]
  },
  {
    "type": "COMPANY_HEADCOUNT",
    "values": [
      {
        "id": "A",
        "text": "Self-employed",
        "selectionType": "INCLUDED"
      }
    ]
  }
]
''',
                required=False
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Leads (Using URL)
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/premium_search_person_via_url') and
            i.nice_name == "Search Leads ( Using URL )")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='company_url',
                key_description='LinkedIn Sales Search URL',
                value_hint_type='URL',
                value_default='''\
https://www.linkedin.com/sales/search/people?query=(spellCorrectionEnabled%3At\
rue%2CrecentSearchParam%3A(id%3A3268364538%2CdoLogHistory%3Atrue)%2Cfilters%3A\
List((type%3ACURRENT_COMPANY%2Cvalues%3AList((id%3Aurn%253Ali%253Aorganization\
%253A1586%2Ctext%3AAmazon%2CselectionType%3AINCLUDED%2Cparent%3A(id%3A0)))))%2\
Ckeywords%3AAlex)&sessionId=aPfz97yIToabLyLdYnUQQg%3D%3D&viewAllFilters=true\
''',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='page',
                key_description='Page Number',
                value_hint_type='Number',
                value_default='1',
                required=True
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Companies ( Using URL )
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/premium_search_company_via_url') and
            i.nice_name == "Search Companies ( Using URL )")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='page',
                key_description='Page Number',
                value_hint_type='Number',
                value_default='1',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='company_url',
                key_description='LinkedIn Sales Search URL',
                value_hint_type='URL',
                value_default='''\
https://www.linkedin.com/sales/search/company?query=(filters%3AList((type%3AIND\
USTRY%2Cvalues%3AList((id%3A43%2Ctext%3AFinanci%25C3%25ABle%2520diensten%2Csele\
ctionType%3AINCLUDED)))%2C(type%3AREGION%2Cvalues%3AList((id%3A101461601%2Ctext\
%3ADen%2520Haag%252C%2520Zuid-Holland%252C%2520Nederland%2CselectionType%3AINCL\
UDED)%2C(id%3A100467493%2Ctext%3ARotterdam%252C%2520Zuid-Holland%252C%2520Neder\
land%2CselectionType%3AINCLUDED)))%2C(type%3ACOMPANY_HEADCOUNT%2Cvalues%3AList(\
(id%3AC%2Ctext%3A11-50%2CselectionType%3AINCLUDED)))))&sessionId=%2FGJNM6q2S6aA\
qffsV1Cqxg%3D%3D\
''',
                required=True
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search People
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/search_person') and
            i.nice_name == "Search People")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='keywords',
                key_description='Keywords',
                value_hint_type='String',
                value_default='Andrew',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='geoUrns',
                key_description='Geo Urns (i.e. 103644278,101728296)',
                value_hint_type='String',
                value_default='103644278',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='count',
                key_description='Count',
                value_hint_type='Number',
                value_default='10',
                required=False
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Company
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/search_company') and
            i.nice_name == "Search Company")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='keywords',
                key_description='Keywords',
                value_hint_type='String',
                value_default='Technology',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='geoUrns',
                key_description='Geo Urns (i.e. 100506914)',
                value_hint_type='String',
                value_default='103644278',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='count',
                key_description='Count',
                value_hint_type='Number',
                value_default='10',
                required=False
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Jobs
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/search_jobs') and
            i.nice_name == "Search Jobs" and
            i.http_method == "POST")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='keywords',
                key_description='Keywords',
                value_hint_type='String',
                value_default='Software Engineer',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='location',
                key_description='Location',
                value_hint_type='String',
                value_default='United States',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='count',
                key_description='Count',
                value_hint_type='Number',
                value_default='10',
                required=False
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search GeoUrns
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/search_geourns') and
            i.nice_name == "Search GeoUrns")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='keyword',
                key_description='Keyword',
                value_hint_type='String',
                value_default='United States',
                required=True
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Companies With Filters
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/search_company_with_filters') and
            i.nice_name == "Search Companies With Filters")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='keyword',
                key_description='Keyword',
                value_hint_type='String',
                value_default='Google',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='page',
                key_description='Page Number',
                value_hint_type='Number',
                value_default='1',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='company_size_list',
                key_description='Company Size List (i.e. A,D)',
                value_hint_type='String CSV',
                value_default='A,D',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='hasJobs',
                key_description='Has Jobs (i.e. True or False)',
                value_hint_type='Boolean',
                value_default='False',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='location_list',
                key_description='Location List (i.e. 91000002)',
                value_hint_type='String CSV',
                value_default='103644278',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='industry_list',
                key_description='Industry List (i.e. 1810)',
                value_hint_type='String CSV',
                value_default='',
                required=True
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search People With Filters
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/search_people_with_filters') and
            i.nice_name == "Search People With Filters")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='keyword',
                key_description='Keyword',
                value_hint_type='String',
                value_default='G',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='page',
                key_description='Page Number',
                value_hint_type='Number',
                value_default='1',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='title_free_text',
                key_description='Title Free Text',
                value_hint_type='String',
                value_default='CEO',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='company_free_text',
                key_description='Company Free Text',
                value_hint_type='String',
                value_default='Huzzle',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='first_name',
                key_description='First Name',
                value_hint_type='String',
                value_default='Ingmar',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='last_name',
                key_description='Last Name',
                value_hint_type='String',
                value_default='Klein',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='current_company_list',
                key_description='Current Company List',
                value_hint_type='String CSV',
                value_default='',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='past_company_list',
                key_description='Past Company List',
                value_hint_type='String CSV',
                value_default='',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='location_list',
                key_description='Location List',
                value_hint_type='String CSV',
                value_default='',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='language_list',
                key_description='Language List',
                value_hint_type='String CSV',
                value_default='',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='service_catagory_list',
                key_description='Service Category List',
                value_hint_type='String CSV',
                value_default='',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='school_free_text',
                key_description='School Free Text',
                value_hint_type='String',
                value_default='',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='industry_list',
                key_description='Industry List',
                value_hint_type='String CSV',
                value_default='',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='school_list',
                key_description='School List',
                value_hint_type='String CSV',
                value_default='',
                required=False
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Companies
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/bulk_companies') and
            i.nice_name == "Companies")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='links',
                key_description='Links to LinkedIn Companies',
                value_hint_type='Array',
                value_default="""\
[
  "http://www.linkedin.com/company/aep-energy",
  "http://www.linkedin.com/company/johnson-&-johnson",
  "http://www.linkedin.com/company/ametek",
  "http://www.linkedin.com/company/insurance-commission-of-the-bahamas",
  "http://www.linkedin.com/company/chs",
  "http://www.linkedin.com/company/vitas-healthcare",
  "http://www.linkedin.com/company/citgo",
  "http://www.linkedin.com/company/mars",
  "http://www.linkedin.com/company/suffolk-construction",
  "http://www.linkedin.com/company/sumitomo-mitsui-banking-corporation",
  "http://www.linkedin.com/company/nemours",
  "http://www.linkedin.com/company/tvars",
  "http://www.linkedin.com/company/farmers-new-world-life",
  "http://www.linkedin.com/company/cincinnatichildrens",
  "http://www.linkedin.com/company/thecpso",
  "http://www.linkedin.com/company/jefferson-county-public-schools",
  "http://www.linkedin.com/company/university-of-illinois-at-urbana-champaign",
  "http://www.linkedin.com/company/s&c-electric-company",
  "http://www.linkedin.com/company/fayette-county-public-schools-ky",
  "http://www.linkedin.com/company/booz-allen-hamilton",
  "http://www.linkedin.com/company/elon-university",
  "http://www.linkedin.com/company/the-walt-disney-company",
  "http://www.linkedin.com/company/texas-tech-university",
  "http://www.linkedin.com/company/merck",
  "http://www.linkedin.com/company/everwise-cu",
  "http://www.linkedin.com/company/peabody-trust",
  "http://www.linkedin.com/company/wsfs-bank",
  "http://www.linkedin.com/company/saia-inc",
  "http://www.linkedin.com/company/the-coca-cola-company",
  "http://www.linkedin.com/company/tcenergy",
  "http://www.linkedin.com/company/the-trust-company-of-tennessee",
  "http://www.linkedin.com/company/stowers-institute-for-medical-research",
  "http://www.linkedin.com/company/dick's-sporting-goods",
  "http://www.linkedin.com/company/southwest-airlines",
  "http://www.linkedin.com/company/neighborsfcu",
  "http://www.linkedin.com/company/arevon",
  "http://www.linkedin.com/company/r-d-offutt-company",
  "http://www.linkedin.com/company/camden-property-trust",
  "http://www.linkedin.com/company/autozone",
  "http://www.linkedin.com/company/fraser-health-authority",
  "http://www.linkedin.com/company/ga-asi",
  "http://www.linkedin.com/company/the-walt-disney-company",
  "http://www.linkedin.com/company/miter-brands",
  "http://www.linkedin.com/company/bartonmalow",
  "http://www.linkedin.com/company/msa-the-safety-company",
  "http://www.linkedin.com/company/oklahoma-state-school-boards-association",
  "http://www.linkedin.com/company/fayette-county-public-schools-ky",
  "http://www.linkedin.com/company/bankers-financial-corporation",
  "http://www.linkedin.com/company/mobile-county-public-school-system",
  "http://www.linkedin.com/company/multi-health-systems-inc--mhs",
  "http://www.linkedin.com/company/turning-point-of-central-california-inc.",
  "http://www.linkedin.com/company/american-residential-services",
  "http://www.linkedin.com/company/nationwide",
  "http://www.linkedin.com/company/genmab",
  "http://www.linkedin.com/company/crayon-group",
  "http://www.linkedin.com/company/crowe",
  "http://www.linkedin.com/company/chevron",
  "http://www.linkedin.com/company/jefferson-county-public-schools",
  "http://www.linkedin.com/company/nationwide",
  "http://www.linkedin.com/company/1915south-ashley-south-east",
  "http://www.linkedin.com/company/newyorklife",
  "http://www.linkedin.com/company/dream-motor-group",
  "http://www.linkedin.com/company/honda",
  "http://www.linkedin.com/company/jd-irving",
  "http://www.linkedin.com/company/harvard-university",
  "http://www.linkedin.com/company/shockwave-medical",
  "http://www.linkedin.com/company/alabama-department-of-transportation",
  "http://www.linkedin.com/company/goodwill-keystone-area",
  "http://www.linkedin.com/company/national-basketball-association",
  "http://www.linkedin.com/company/lodiusd",
  "http://www.linkedin.com/company/nymta",
  "http://www.linkedin.com/company/national-association-of-chain-drug-stores\
-nacds-",
  "http://www.linkedin.com/company/ford-motor-company",
  "http://www.linkedin.com/company/clark-county-credit-union",
  "http://www.linkedin.com/company/caterpillar-inc",
  "http://www.linkedin.com/company/kennedyjenks-consultants",
  "http://www.linkedin.com/company/chadwellsupply",
  "http://www.linkedin.com/company/agtexas-farm-credit",
  "http://www.linkedin.com/company/fidelity-investments",
  "http://www.linkedin.com/company/scotiabank",
  "http://www.linkedin.com/company/georgia-system-operations-corporation",
  "http://www.linkedin.com/company/aaa-life-insurance-company",
  "http://www.linkedin.com/company/missouri-employers-mutual",
  "http://www.linkedin.com/company/kennesaw-state-university",
  "http://www.linkedin.com/company/fayette-county-public-schools-ky",
  "http://www.linkedin.com/company/lockheed-martin",
  "http://www.linkedin.com/company/redwood-living",
  "http://www.linkedin.com/company/playhousesquare",
  "http://www.linkedin.com/company/french-brothers-homes",
  "http://www.linkedin.com/company/big-bear-vacations-cabins",
  "http://www.linkedin.com/company/georgia-system-operations-corporation",
  "http://www.linkedin.com/company/aaa-life-insurance-company",
  "http://www.linkedin.com/company/missouri-employers-mutual",
  "http://www.linkedin.com/company/kennesaw-state-university",
  "http://www.linkedin.com/company/fayette-county-public-schools-ky",
  "http://www.linkedin.com/company/lockheed-martin",
  "http://www.linkedin.com/company/redwood-living",
  "http://www.linkedin.com/company/playhousesquare",
  "http://www.linkedin.com/company/french-brothers-homes",
  "http://www.linkedin.com/company/big-bear-vacations-cabins"
]\
""",
                required=True
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Profiles
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/bulk_profiles') and
            i.nice_name == "Profiles")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='links',
                key_description='Links to LinkedIn Companies',
                value_hint_type='Array',
                value_default="""\
[
  "http://www.linkedin.com/in/luke-sharp-b3838719a",
  "http://www.linkedin.com/in/hollie-smith-96ab44b5",
  "http://www.linkedin.com/in/jeannie-wyrick-b4760710a",
  "http://www.linkedin.com/in/rodneydbainjr",
  "http://www.linkedin.com/in/arielschmid",
  "http://www.linkedin.com/in/christopher-ambrose-3248a540",
  "http://www.linkedin.com/in/daniel-schmidt-611b15149",
  "http://www.linkedin.com/in/alexandra-birurakis-326ba692",
  "http://www.linkedin.com/in/paul-tomco-4b9709117",
  "http://www.linkedin.com/in/lindseystevenss",
  "http://www.linkedin.com/in/christophermichaelsmith",
  "http://www.linkedin.com/in/shane-smith-4baa69126",
  "http://www.linkedin.com/in/benbarnard",
  "http://www.linkedin.com/in/gemayelabdullah",
  "http://www.linkedin.com/in/jill-tuttle-a2704087",
  "http://www.linkedin.com/in/daniel-yoo-123a4038",
  "http://www.linkedin.com/in/claudia-sparks-7799546",
  "http://www.linkedin.com/in/francesca-schena-710129195",
  "http://www.linkedin.com/in/joseph-bonk-709969156",
  "http://www.linkedin.com/in/ryan-hanson-8348b71a4",
  "http://www.linkedin.com/in/mounika-banda-45a59b110",
  "http://www.linkedin.com/in/dan-sigmans-4a7a3252",
  "http://www.linkedin.com/in/alexanderharmon256",
  "http://www.linkedin.com/in/sanj-appakonam-96680790",
  "http://www.linkedin.com/in/bryson-bosson-0b68b915",
  "http://www.linkedin.com/in/ian-healey-4b8649101",
  "http://www.linkedin.com/in/dan-beauchamp-b200128",
  "http://www.linkedin.com/in/bradley-hebert-78659b1a0",
  "http://www.linkedin.com/in/keerthanasureshanand",
  "http://www.linkedin.com/in/jdyork",
  "http://www.linkedin.com/in/jessica-mintz-178b0a94",
  "http://www.linkedin.com/in/mayela-bautista-07680042",
  "http://www.linkedin.com/in/amritpal-singh-9a7bb1194",
  "http://www.linkedin.com/in/thiago-alvares-9b485140",
  "http://www.linkedin.com/in/adam-blossey-8b080538",
  "http://www.linkedin.com/in/nathan-williard-328163a7",
  "http://www.linkedin.com/in/steffanie-schrader",
  "http://www.linkedin.com/in/carl-hayden-75044850",
  "http://www.linkedin.com/in/nathan-schroeder-535646105",
  "http://www.linkedin.com/in/david-akridge-5404a848",
  "http://www.linkedin.com/in/mikesparling",
  "http://www.linkedin.com/in/kevinworleyit",
  "http://www.linkedin.com/in/maria-williams-48031823b",
  "http://www.linkedin.com/in/joshua-bachleda-3075789a",
  "http://www.linkedin.com/in/lisa-song-17989a2a",
  "http://www.linkedin.com/in/james-tuttle-868b8194",
  "http://www.linkedin.com/in/kate-boes-833962106",
  "http://www.linkedin.com/in/melanie-stephens-2771b5141",
  "http://www.linkedin.com/in/ingmar-klein",
  "http://www.linkedin.com/in/tom-agresti-245b56233",
  "http://www.linkedin.com/in/luke-sharp-b3838719a",
  "http://www.linkedin.com/in/hollie-smith-96ab44b5",
  "http://www.linkedin.com/in/jeannie-wyrick-b4760710a",
  "http://www.linkedin.com/in/rodneydbainjr",
  "http://www.linkedin.com/in/arielschmid",
  "http://www.linkedin.com/in/christopher-ambrose-3248a540",
  "http://www.linkedin.com/in/daniel-schmidt-611b15149",
  "http://www.linkedin.com/in/alexandra-birurakis-326ba692",
  "http://www.linkedin.com/in/paul-tomco-4b9709117",
  "http://www.linkedin.com/in/lindseystevenss",
  "http://www.linkedin.com/in/christophermichaelsmith",
  "http://www.linkedin.com/in/shane-smith-4baa69126",
  "http://www.linkedin.com/in/benbarnard",
  "http://www.linkedin.com/in/gemayelabdullah",
  "http://www.linkedin.com/in/jill-tuttle-a2704087",
  "http://www.linkedin.com/in/daniel-yoo-123a4038",
  "http://www.linkedin.com/in/claudia-sparks-7799546",
  "http://www.linkedin.com/in/francesca-schena-710129195",
  "http://www.linkedin.com/in/joseph-bonk-709969156",
  "http://www.linkedin.com/in/ryan-hanson-8348b71a4",
  "http://www.linkedin.com/in/mounika-banda-45a59b110",
  "http://www.linkedin.com/in/dan-sigmans-4a7a3252",
  "http://www.linkedin.com/in/alexanderharmon256",
  "http://www.linkedin.com/in/sanj-appakonam-96680790",
  "http://www.linkedin.com/in/bryson-bosson-0b68b915",
  "http://www.linkedin.com/in/ian-healey-4b8649101",
  "http://www.linkedin.com/in/dan-beauchamp-b200128",
  "http://www.linkedin.com/in/bradley-hebert-78659b1a0",
  "http://www.linkedin.com/in/keerthanasureshanand",
  "http://www.linkedin.com/in/jdyork",
  "http://www.linkedin.com/in/jessica-mintz-178b0a94",
  "http://www.linkedin.com/in/mayela-bautista-07680042",
  "http://www.linkedin.com/in/amritpal-singh-9a7bb1194",
  "http://www.linkedin.com/in/thiago-alvares-9b485140",
  "http://www.linkedin.com/in/adam-blossey-8b080538",
  "http://www.linkedin.com/in/nathan-williard-328163a7",
  "http://www.linkedin.com/in/steffanie-schrader",
  "http://www.linkedin.com/in/carl-hayden-75044850",
  "http://www.linkedin.com/in/nathan-schroeder-535646105",
  "http://www.linkedin.com/in/david-akridge-5404a848",
  "http://www.linkedin.com/in/mikesparling",
  "http://www.linkedin.com/in/kevinworleyit",
  "http://www.linkedin.com/in/maria-williams-48031823b",
  "http://www.linkedin.com/in/joshua-bachleda-3075789a",
  "http://www.linkedin.com/in/lisa-song-17989a2a",
  "http://www.linkedin.com/in/james-tuttle-868b8194",
  "http://www.linkedin.com/in/kate-boes-833962106",
  "http://www.linkedin.com/in/melanie-stephens-2771b5141",
  "http://www.linkedin.com/in/ingmar-klein",
  "http://www.linkedin.com/in/tom-agresti-245b56233"
]\
""",
                required=True
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Profiles
        # mgujjargamingm | Linkedin BULK data scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-bulk-data-scraper.p.rapidapi.com'
                '/profiles') and
            i.nice_name == "Profiles")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='links',
                key_description='Links to LinkedIn Profiles',
                value_hint_type='Array',
                value_default="""\
[\
"http://www.linkedin.com/in/luke-sharp-b3838719a", \
"http://www.linkedin.com/in/hollie-smith-96ab44b5", \
"http://www.linkedin.com/in/jeannie-wyrick-b4760710a", \
"http://www.linkedin.com/in/rodneydbainjr", \
"http://www.linkedin.com/in/arielschmid", \
"http://www.linkedin.com/in/christopher-ambrose-3248a540", \
"http://www.linkedin.com/in/daniel-schmidt-611b15149", \
"http://www.linkedin.com/in/alexandra-birurakis-326ba692", \
"http://www.linkedin.com/in/paul-tomco-4b9709117", \
"http://www.linkedin.com/in/lindseystevenss", \
"http://www.linkedin.com/in/christophermichaelsmith", \
"http://www.linkedin.com/in/shane-smith-4baa69126", \
"http://www.linkedin.com/in/benbarnard", \
"http://www.linkedin.com/in/gemayelabdullah", \
"http://www.linkedin.com/in/jill-tuttle-a2704087", \
"http://www.linkedin.com/in/daniel-yoo-123a4038", \
"http://www.linkedin.com/in/claudia-sparks-7799546", \
"http://www.linkedin.com/in/francesca-schena-710129195", \
"http://www.linkedin.com/in/joseph-bonk-709969156", \
"http://www.linkedin.com/in/ryan-hanson-8348b71a4", \
"http://www.linkedin.com/in/mounika-banda-45a59b110", \
"http://www.linkedin.com/in/dan-sigmans-4a7a3252", \
"http://www.linkedin.com/in/alexanderharmon256", \
"http://www.linkedin.com/in/sanj-appakonam-96680790", \
"http://www.linkedin.com/in/bryson-bosson-0b68b915", \
"http://www.linkedin.com/in/ian-healey-4b8649101", \
"http://www.linkedin.com/in/dan-beauchamp-b200128", \
"http://www.linkedin.com/in/bradley-hebert-78659b1a0", \
"http://www.linkedin.com/in/keerthanasureshanand", \
"http://www.linkedin.com/in/jdyork", \
"http://www.linkedin.com/in/jessica-mintz-178b0a94", \
"http://www.linkedin.com/in/mayela-bautista-07680042", \
"http://www.linkedin.com/in/amritpal-singh-9a7bb1194", \
"http://www.linkedin.com/in/thiago-alvares-9b485140", \
"http://www.linkedin.com/in/adam-blossey-8b080538", \
"http://www.linkedin.com/in/nathan-williard-328163a7", \
"http://www.linkedin.com/in/steffanie-schrader", \
"http://www.linkedin.com/in/carl-hayden-75044850", \
"http://www.linkedin.com/in/nathan-schroeder-535646105", \
"http://www.linkedin.com/in/david-akridge-5404a848", \
"http://www.linkedin.com/in/mikesparling", \
"http://www.linkedin.com/in/kevinworleyit", \
"http://www.linkedin.com/in/maria-williams-48031823b", \
"http://www.linkedin.com/in/joshua-bachleda-3075789a", \
"http://www.linkedin.com/in/lisa-song-17989a2a", \
"http://www.linkedin.com/in/james-tuttle-868b8194", \
"http://www.linkedin.com/in/kate-boes-833962106", \
"http://www.linkedin.com/in/melanie-stephens-2771b5141", \
"http://www.linkedin.com/in/ingmar-klein", \
"http://www.linkedin.com/in/tom-agresti-245b56233"
]\
""",
                required=True
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Companies
        # mgujjargamingm | Linkedin BULK data scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-bulk-data-scraper.p.rapidapi.com'
                '/companies') and
            i.nice_name == "Companies")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='links',
                key_description='Links to LinkedIn Companies',
                value_hint_type='Array',
                value_default="""\
[\
"http://www.linkedin.com/company/aep-energy", \
"http://www.linkedin.com/company/johnson-&-johnson", \
"http://www.linkedin.com/company/ametek", \
"http://www.linkedin.com/company/insurance-commission-of-the-bahamas", \
"http://www.linkedin.com/company/chs", \
"http://www.linkedin.com/company/vitas-healthcare", \
"http://www.linkedin.com/company/citgo", \
"http://www.linkedin.com/company/mars", \
"http://www.linkedin.com/company/suffolk-construction", \
"http://www.linkedin.com/company/sumitomo-mitsui-banking-corporation", \
"http://www.linkedin.com/company/nemours", \
"http://www.linkedin.com/company/tvars", \
"http://www.linkedin.com/company/farmers-new-world-life", \
"http://www.linkedin.com/company/cincinnatichildrens", \
"http://www.linkedin.com/company/thecpso", \
"http://www.linkedin.com/company/jefferson-county-public-schools", \
"http://www.linkedin.com/company/university-of-illinois-at-urbana-champaign", \
"http://www.linkedin.com/company/s&c-electric-company", \
"http://www.linkedin.com/company/fayette-county-public-schools-ky", \
"http://www.linkedin.com/company/booz-allen-hamilton", \
"http://www.linkedin.com/company/elon-university", \
"http://www.linkedin.com/company/the-walt-disney-company", \
"http://www.linkedin.com/company/texas-tech-university", \
"http://www.linkedin.com/company/merck", \
"http://www.linkedin.com/company/everwise-cu", \
"http://www.linkedin.com/company/peabody-trust", \
"http://www.linkedin.com/company/wsfs-bank", \
"http://www.linkedin.com/company/saia-inc", \
"http://www.linkedin.com/company/the-coca-cola-company", \
"http://www.linkedin.com/company/tcenergy", \
"http://www.linkedin.com/company/the-trust-company-of-tennessee", \
"http://www.linkedin.com/company/stowers-institute-for-medical-research", \
"http://www.linkedin.com/company/dick's-sporting-goods", \
"http://www.linkedin.com/company/southwest-airlines", \
"http://www.linkedin.com/company/neighborsfcu", \
"http://www.linkedin.com/company/arevon", \
"http://www.linkedin.com/company/r-d-offutt-company", \
"http://www.linkedin.com/company/camden-property-trust", \
"http://www.linkedin.com/company/autozone", \
"http://www.linkedin.com/company/fraser-health-authority", \
"http://www.linkedin.com/company/ga-asi", \
"http://www.linkedin.com/company/the-walt-disney-company", \
"http://www.linkedin.com/company/miter-brands", \
"http://www.linkedin.com/company/bartonmalow", \
"http://www.linkedin.com/company/msa-the-safety-company", \
"http://www.linkedin.com/company/oklahoma-state-school-boards-association", \
"http://www.linkedin.com/company/fayette-county-public-schools-ky", \
"http://www.linkedin.com/company/bankers-financial-corporation", \
"http://www.linkedin.com/company/mobile-county-public-school-system", \
"http://www.linkedin.com/company/multi-health-systems-inc--mhs", \
"http://www.linkedin.com/company/turning-point-of-central-california-inc.", \
"http://www.linkedin.com/company/american-residential-services", \
"http://www.linkedin.com/company/nationwide", \
"http://www.linkedin.com/company/genmab", \
"http://www.linkedin.com/company/crayon-group", \
"http://www.linkedin.com/company/crowe", \
"http://www.linkedin.com/company/chevron", \
"http://www.linkedin.com/company/jefferson-county-public-schools", \
"http://www.linkedin.com/company/nationwide", \
"http://www.linkedin.com/company/1915south-ashley-south-east", \
"http://www.linkedin.com/company/newyorklife", \
"http://www.linkedin.com/company/dream-motor-group", \
"http://www.linkedin.com/company/honda", \
"http://www.linkedin.com/company/jd-irving", \
"http://www.linkedin.com/company/harvard-university", \
"http://www.linkedin.com/company/shockwave-medical", \
"http://www.linkedin.com/company/alabama-department-of-transportation", \
"http://www.linkedin.com/company/goodwill-keystone-area", \
"http://www.linkedin.com/company/national-basketball-association", \
"http://www.linkedin.com/company/lodiusd", \
"http://www.linkedin.com/company/nymta", \
"http://www.linkedin.com/company/national-association-of-chain-drug\
-stores-nacds-", \
"http://www.linkedin.com/company/ford-motor-company", \
"http://www.linkedin.com/company/clark-county-credit-union", \
"http://www.linkedin.com/company/caterpillar-inc", \
"http://www.linkedin.com/company/kennedyjenks-consultants", \
"http://www.linkedin.com/company/chadwellsupply", \
"http://www.linkedin.com/company/agtexas-farm-credit", \
"http://www.linkedin.com/company/fidelity-investments", \
"http://www.linkedin.com/company/scotiabank", \
"http://www.linkedin.com/company/georgia-system-operations-corporation", \
"http://www.linkedin.com/company/aaa-life-insurance-company", \
"http://www.linkedin.com/company/missouri-employers-mutual", \
"http://www.linkedin.com/company/kennesaw-state-university", \
"http://www.linkedin.com/company/fayette-county-public-schools-ky", \
"http://www.linkedin.com/company/lockheed-martin", \
"http://www.linkedin.com/company/redwood-living", \
"http://www.linkedin.com/company/playhousesquare", \
"http://www.linkedin.com/company/french-brothers-homes", \
"http://www.linkedin.com/company/big-bear-vacations-cabins", \
"http://www.linkedin.com/company/georgia-system-operations-corporation", \
"http://www.linkedin.com/company/aaa-life-insurance-company", \
"http://www.linkedin.com/company/missouri-employers-mutual", \
"http://www.linkedin.com/company/kennesaw-state-university", \
"http://www.linkedin.com/company/fayette-county-public-schools-ky", \
"http://www.linkedin.com/company/lockheed-martin", \
"http://www.linkedin.com/company/redwood-living", \
"http://www.linkedin.com/company/playhousesquare", \
"http://www.linkedin.com/company/french-brothers-homes", \
"http://www.linkedin.com/company/big-bear-vacations-cabins"\
]\
""",
                required=True
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Company Posts ( BETA )
        # mgujjargamingm | Linkedin BULK data scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-bulk-data-scraper.p.rapidapi.com'
                '/company_posts') and
            i.nice_name == "Company Posts ( BETA )")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='links',
                key_description='Links to LinkedIn Companies',
                value_hint_type='Array',
                value_default="""\
[\
"https://www.linkedin.com/company/huzzle-app/", \
"http://www.linkedin.com/company/aep-energy", \
"http://www.linkedin.com/company/johnson-&-johnson", \
"http://www.linkedin.com/company/ametek", \
"http://www.linkedin.com/company/insurance-commission-of-the-bahamas", \
"http://www.linkedin.com/company/chs", \
"http://www.linkedin.com/company/vitas-healthcare", \
"http://www.linkedin.com/company/citgo", \
"http://www.linkedin.com/company/mars", \
"http://www.linkedin.com/company/suffolk-construction", \
"http://www.linkedin.com/company/sumitomo-mitsui-banking-corporation", \
"http://www.linkedin.com/company/nemours", \
"http://www.linkedin.com/company/huzzle-app", \
"http://www.linkedin.com/company/huzzle-app", \
"http://www.linkedin.com/company/cincinnatichildrens", \
"http://www.linkedin.com/company/thecpso", \
"http://www.linkedin.com/company/jefferson-county-public-schools", \
"http://www.linkedin.com/company/university-of-illinois-at-urbana-champaign", \
"http://www.linkedin.com/company/s&c-electric-company", \
"http://www.linkedin.com/company/fayette-county-public-schools-ky", \
"http://www.linkedin.com/company/booz-allen-hamilton", \
"http://www.linkedin.com/company/elon-university", \
"http://www.linkedin.com/company/the-walt-disney-company", \
"http://www.linkedin.com/company/texas-tech-university", \
"http://www.linkedin.com/company/merck", \
"http://www.linkedin.com/company/everwise-cu", \
"http://www.linkedin.com/company/peabody-trust", \
"http://www.linkedin.com/company/wsfs-bank", \
"http://www.linkedin.com/company/saia-inc", \
"http://www.linkedin.com/company/the-coca-cola-company", \
"http://www.linkedin.com/company/tcenergy", \
"http://www.linkedin.com/company/the-trust-company-of-tennessee", \
"http://www.linkedin.com/company/stowers-institute-for-medical-research", \
"http://www.linkedin.com/company/dick's-sporting-goods", \
"http://www.linkedin.com/company/southwest-airlines", \
"http://www.linkedin.com/company/neighborsfcu", \
"http://www.linkedin.com/company/arevon", \
"http://www.linkedin.com/company/huzzle-app", \
"http://www.linkedin.com/company/camden-property-trust", \
"http://www.linkedin.com/company/autozone", \
"http://www.linkedin.com/company/fraser-health-authority", \
"http://www.linkedin.com/company/ga-asi", \
"http://www.linkedin.com/company/the-walt-disney-company", \
"http://www.linkedin.com/company/miter-brands", \
"http://www.linkedin.com/company/bartonmalow", \
"http://www.linkedin.com/company/msa-the-safety-company", \
"http://www.linkedin.com/company/oklahoma-state-school-boards-association", \
"http://www.linkedin.com/company/fayette-county-public-schools-ky", \
"http://www.linkedin.com/company/bankers-financial-corporation", \
"http://www.linkedin.com/company/google"\
]\
""",
                required=True
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Company Data
        # mgujjargamingm | Linkedin BULK data scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-bulk-data-scraper.p.rapidapi.com'
                '/company') and
            i.nice_name == "Company Data")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='links',
                key_description='Link to LinkedIn Company',
                value_hint_type='String',
                value_default="""\
"https://www.linkedin.com/company/huzzle-app/"
""",
                required=True
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Company With Filters
        # mgujjargamingm | Linkedin BULK data scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-bulk-data-scraper.p.rapidapi.com'
                '/search_company_with_filters') and
            i.nice_name == "Search Company With Filters")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='keyword',
                key_description='Keyword',
                value_hint_type='String',
                value_default='Google',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='page',
                key_description='Page Number',
                value_hint_type='Number',
                value_default='1',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='hasJobs',
                key_description='Has Jobs (i.e. True or False)',
                value_hint_type='Boolean',
                value_default='False',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='company_size_list',
                key_description='Company Size List (i.e. A,D)',
                value_hint_type='String CSV',
                value_default='A,D',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='location_list',
                key_description='Location List (i.e. 91000002)',
                value_hint_type='String CSV',
                value_default='103644278',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='industry_list',
                key_description='Industry List (i.e. 1810)',
                value_hint_type='String CSV',
                value_default='',
                required=True
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # get_related_jobs_jobs__int_id___related_post
        # qurazor1 | Remoote Job Search
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://remoote-job-search1.p.rapidapi.com'
                '/remoote/jobs/') and
            i.nice_name == "get_related_jobs_jobs__int_id___related_post")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='exclude_ids',
                key_description="Exclude ID's",
                value_hint_type='Array Number',
                value_default="""\
[]\
""",
                required=True
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Company Employees Count
        # RockAPIs | Linkedin API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-api8.p.rapidapi.com/'
                'get-company-employees-count') and
            i.nice_name == "Get Company Employees Count")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='companyId',
                key_description='Company ID',
                value_hint_type='String',
                value_default="1441",
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='locations',
                key_description='Locations (i.e. ["90009496"])',
                value_hint_type='Array String',
                value_default='',
                required=True
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Company Employees Count
        # RockAPIs | Rapid LinkedIn Data API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-api.p.rapidapi.com'
                '/get-company-employees-count') and
            i.nice_name == "Get Company Employees Count")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='companyId',
                key_description='Company ID (i.e. 1441)',
                value_hint_type='String',
                value_default="",
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='locations',
                key_description='Locations (i.e. ["90009496"])',
                value_hint_type='Array String',
                value_default='',
                required=True
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Company Search
        # sohailglt | Linkedin Live Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-live-data.p.rapidapi.com'
                '/company-search') and
            i.nice_name == "Company Search")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='per_page',
                key_description='Result per Page',
                value_hint_type='Number',
                value_default="10",
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='offset',
                key_description='Offset',
                value_hint_type='Number',
                value_default="0",
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='keyword',
                key_description='Keyword',
                value_hint_type='String',
                value_default="",
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='followers',
                key_description='Followers Count',
                value_hint_type='String',
                value_default="gt:100",
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='industries',
                key_description='Industries '
                                '(i.e. ["Computer Software", "Accounting"])',
                value_hint_type='Array String',
                value_default='',
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='country_codes',
                key_description='Country Codes (i.e. ["us", "ca", "in"])',
                value_hint_type='Array String',
                value_default='["us"]',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='company_size',
                key_description='Company Size (i.e. 1-100)',
                value_hint_type='String',
                value_default="1-100",
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='year_founded',
                key_description='Year Founded (i.e. gt:1999)',
                value_hint_type='String',
                value_default="gt:1999",
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='company_type',
                key_description='Company Type (i.e. Privately Held)',
                value_hint_type='String',
                value_default="Privately Held",
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='website',
                key_description='Website',
                value_hint_type='String',
                value_default="google.com",
                required=False
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # People Search
        # sohailglt | Linkedin Live Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-live-data.p.rapidapi.com'
                '/people-search') and
            i.nice_name == "People Search")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='per_page',
                key_description='Result per Page',
                value_hint_type='Number',
                value_default="10",
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='offset',
                key_description='Offset',
                value_hint_type='Number',
                value_default="0",
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='keyword',
                key_description='Keyword',
                value_hint_type='String',
                value_default="",
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='countries',
                key_description='Countries '
                                '(i.e. ["United States", "Canada", "Israel"])',
                value_hint_type='Array String',
                value_default='["United States"]',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='current_companies',
                key_description='Current Companies (i.e. ["1035", "1441"])',
                value_hint_type='Array String',
                value_default='',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='past_companies',
                key_description='Past Companies (i.e. ["1035", "1441"])',
                value_hint_type='Array String',
                value_default='',
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='current_job_title',
                key_description='Current Job Title (i.e. Data Scientist)',
                value_hint_type='String',
                value_default="Software Engineer",
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='past_job_title',
                key_description='Past Job Title (i.e. Data Scientist)',
                value_hint_type='String',
                value_default="Software Engineer",
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='industry',
                key_description='Industry',
                value_hint_type='String',
                value_default="",
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='certification',
                key_description='Certification',
                value_hint_type='String',
                value_default="",
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='edu_degree',
                key_description='Education Degree',
                value_hint_type='String',
                value_default="",
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='study_field',
                key_description='Study Field',
                value_hint_type='String',
                value_default="",
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='school_name',
                key_description='School Name',
                value_hint_type='String',
                value_default="",
                required=False
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Profile Details
        # sohailglt | Linkedin Live Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-live-data.p.rapidapi.com'
                '/profile-details') and
            i.nice_name == "Get Profile Details")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='profile_id',
                key_description='Profile ID',
                value_hint_type='String',
                value_default="williamhgates",
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='profile_type',
                key_description='Profile Type',
                value_hint_type='String',
                value_default="personal",
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='contact_info',
                key_description='Include Contact Info',
                value_hint_type='Boolean',
                value_default="False",
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='recommendations',
                key_description='Include Recommendations',
                value_hint_type='Boolean',
                value_default="False",
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='related_profiles',
                key_description='Include Related Profiles',
                value_hint_type='Boolean',
                value_default="False",
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='network_info',
                key_description='Include Network Information',
                value_hint_type='Boolean',
                value_default="False",
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='bypass_cache',
                key_description='Bypass Cache',
                value_hint_type='Boolean',
                value_default="True",
                required=True
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Company Details
        # sohailglt | Linkedin Live Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-live-data.p.rapidapi.com'
                '/profile-details') and
            i.nice_name == "Get Company Details")
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='profile_id',
                key_description='Profile ID',
                value_hint_type='String',
                value_default="google",
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='profile_type',
                key_description='Profile Type',
                value_hint_type='String',
                value_default="company",
                required=True
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='contact_info',
                key_description='Include Contact Info',
                value_hint_type='Boolean',
                value_default="True",
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='recommendations',
                key_description='Include Recommendations',
                value_hint_type='Boolean',
                value_default="True",
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='related_profiles',
                key_description='Include Related Profiles',
                value_hint_type='Boolean',
                value_default="True",
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='network_info',
                key_description='Include Network Information',
                value_hint_type='Boolean',
                value_default="True",
                required=False
            ),
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='bypass_cache',
                key_description='Bypass Cache',
                value_hint_type='Boolean',
                value_default="True",
                required=True
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Jobs
        # APIJobs | Job Searching API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://api.apijobs.dev'
                '/v1/job/') and
            i.nice_name == 'Search Jobs')
        db.session.add_all([

            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='q',
                key_description='Search Keyword',
                value_hint_type='String',
                value_default='Full Stack Engineer',
                required=True
            ),

            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='published_since',
                key_description='Published since a specific date',
                value_hint_type='String',
                value_default='',
                required=False,
            ),

            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='published_until',
                key_description='Published until a specific date',
                value_hint_type='String',
                value_default='',
                required=False,
            ),

            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='country',
                key_description='''\
The country filter can be used in the POST /job/search endpoint to narrow down \
job listings to specific countries. Use the country codes from the /countries \
endpoint to specify which countries you want to include in your job search \
query. This allows for more targeted job searches based on the location of \
the job listings.''',
                value_hint_type='String',
                value_default='United States',
                required=False,
            ),

            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='employment_type',
                key_description='''\
Employment Type - The employment_types filter can be used in the  \
POST /job/search endpoint to narrow down job listings to specific \
types of employment. Use the employment type codes from the /employment_types\
 endpoint to specify which types of employment you want to include in your job\
 search query. This allows for more targeted job searches based on the nature\
 of employment, such as full-time, part-time, contract, etc. ("Contract", \
"Freelance", "Internship", "Temporary", "Part Time", "Full Time", "Other")\
''',
                value_hint_type='String',
                value_default='Full Time',
                required=False,
            ),

            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='language',
                key_description='''\
The languages filter can be used in the  POST job/search endpoint to narrow \
down job listings to specific languages. Use the language codes from the \
/languages endpoint to specify which languages you want to include in your \
job search query. This allows for more targeted job searches based on the \
preferred language of the job listings.''',
                value_hint_type='String',
                value_default='English',
                required=False,
            ),

            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='domains',
                key_description='''Domains where the job is present. Example : \
["boards.eu.greenhouse.io", "boards.greenhouse.io"]''',
                value_hint_type='Array String',
                value_default='',
                required=False,
            ),

            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='hiringOrganizationName',
                key_description='''\
filter by the organization Name. Organizations can be fetch using the \
organization route ''',
                value_hint_type='String',
                value_default='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        db.session.close()
        print(APIEndpointBody.__tablename__ + " seeded successfully!")

    except Exception as e:
        print(f"Error committing data: {e}")

# Example Seed Format
# nice_description can have """ and stores TEXT in the column.
"""

        # HTTP_Path and Endpoint Nice_Name
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                '___'
                '___') and
            i.nice_name == '___')
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='___',
                key_description='___',
                value_hint_type='___',
                value_default='___',
                required=True
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " + 
              str(new_api_endpoint_nice_name))
"""
