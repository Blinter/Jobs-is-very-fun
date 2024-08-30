"""
API Endpoints

Seed file can be run
cd <base_dir>
PYTHONPATH=<base_dir> python3 <base_dir>/<file_name>.py

Table drop and creation must also drop:
    APIEndpointParams, APIEndpointHeaders, APIEndpointBodies due to FK
    restraints

APIHeader needs to be imported due to APIListURL relationship.
"""
from sqlalchemy import inspect, text, MetaData
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy_utils import database_exists, create_database

from enums.api_endpoint_types import APIEndpointTypes
from secrets_jobs.credentials import (
    maria_information_login_details,
    mariadb_database_name
)
from models.mariadb.api_list_url import APIListURL
from models.mariadb.api_endpoints import APIEndpoint
from models.mariadb.api_endpoint_headers import APIEndpointHeader
from models.mariadb.api_endpoint_params import APIEndpointParam
from models.mariadb.api_endpoint_bodies import APIEndpointBody
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
    SELECT COUNT(*)
    FROM information_schema.TABLES
    WHERE TABLE_SCHEMA = '{schema}' AND TABLE_NAME = '{table_name}'\
    """)
    result = temp_db.session.execute(query)
    return result.scalar() > 0


with app.app_context():
    try:
        metadata = MetaData()

        # APIEndpoint
        table = db.Table(
            APIEndpoint.__tablename__,
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

        # APIEndpointParam
        table2 = db.Table(
            APIEndpointParam.__tablename__,
            metadata=metadata,
            bind_key="mariadb",
            autoload_with=engine)
        if table_exists(db, table2.name):
            fk_names = get_foreign_key_constraint_names(table2, engine)
            for fk_name in fk_names:
                if fk_name:
                    sql_text = (f'ALTER TABLE {table2.name} DROP FOREIGN KEY '
                                f'{fk_name}')
                    db.session.execute(text(sql_text))

        # APIEndpointHeader
        table3 = db.Table(
            APIEndpointHeader.__tablename__,
            metadata=metadata,
            bind_key="mariadb",
            autoload_with=engine)
        if table_exists(db, table3.name):
            fk_names = get_foreign_key_constraint_names(table3, engine)
            for fk_name in fk_names:
                if fk_name:
                    sql_text = (f'ALTER TABLE {table3.name} DROP FOREIGN KEY '
                                f'{fk_name}')
                    db.session.execute(text(sql_text))

        # APIEndpointBody
        table4 = db.Table(
            APIEndpointBody.__tablename__,
            metadata=metadata,
            bind_key="mariadb",
            autoload_with=engine)
        if table_exists(db, table4.name):
            fk_names = get_foreign_key_constraint_names(table4, engine)
            for fk_name in fk_names:
                if fk_name:
                    sql_text = (f'ALTER TABLE {table4.name} DROP FOREIGN KEY '
                                f'{fk_name}')
                    db.session.execute(text(sql_text))

        # APIEndpointExtra
        table5 = db.Table(
            APIEndpointExtra.__tablename__,
            metadata=metadata,
            bind_key="mariadb",
            autoload_with=engine)
        if table_exists(db, table5.name):
            fk_names = get_foreign_key_constraint_names(table5, engine)
            for fk_name in fk_names:
                if fk_name:
                    sql_text = (f'ALTER TABLE {table5.name} DROP FOREIGN KEY '
                                f'{fk_name}')
                    db.session.execute(text(sql_text))

        table5.drop(engine, checkfirst=True)
        table4.drop(engine, checkfirst=True)
        table3.drop(engine, checkfirst=True)
        table2.drop(engine, checkfirst=True)
        table.drop(engine, checkfirst=True)

        table.create(engine, checkfirst=True)
        table2.create(engine, checkfirst=True)
        table3.create(engine, checkfirst=True)
        table4.create(engine, checkfirst=True)
        table5.create(engine, checkfirst=True)

        # retrieve API List URL's in order to reference foreign keys.
        API_list = db.session.query(APIListURL).all()

        # APIJobs | Job Searching API
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in
            API_list if i.url == (
                'https://rapidapi.com'
                '/apijobs-apijobs-default/api/apijob-job-searching-api/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search jobs",
                nice_description="\
This route, searchJobs, is designed to fetch the latest job li"
                "stings from the database. When a POST request is sent to /sear"
                "ch, the server executes a search operation without specific qu"
                "ery parameters, thus retrieving the most recent 100 job listin"
                "gs based on their creation date. It also calculates the total "
                "number of job listings available. The route responds with a JS"
                "ON object containing a success status, the list of job data, a"
                "nd the total job count. In case of an error, it logs the error"
                " and returns a server error response.",
                http_method="POST",
                http_path='https://apijob-job-searching-api.p.rapidapi.com'
                          '/v1/job/search',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search organization",
                nice_description='Search inside organization that are currently'
                                 ' hiring',
                http_method="POST",
                http_path='https://apijob-job-searching-api.p.rapidapi.com'
                          '/v1/organization/search',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get job by id",
                nice_description="\
This route retrieves detailed information about a specific job"
                " using its unique ID. When you send a GET request with a job I"
                "D, the route provides you with all the relevant job details in"
                " response. If there's an issue with your request, you'll recei"
                "ve an error message.",
                http_method="GET",
                http_path='https://apijob-job-searching-api.p.rapidapi.com'
                          '/v1/job/',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOB_DETAILS, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # avadataservices | Job Postings
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/avadataservices-avadataservices-default/api/job-postings1/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="/api/v2/Jobs/Latest",
                nice_description="Latest Jobs",
                http_method="GET",
                http_path='https://job-postings1.p.rapidapi.com'
                          '/',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_FEED, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="/api/v2/Jobs/{slug}",
                nice_description="\
Once you have found your job from the search end point, you ca"
                "n use this endpoint to get more information about it.",
                http_method="GET",
                http_path='https://job-postings1.p.rapidapi.com'
                          '/api/v2/Jobs/',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOB_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="/api/v2/Jobs/Search",
                nice_description="\
Provides the ability to do a full text search on all our jobs."
                " All returned jobs are ordered from newest to oldest.",
                http_method="GET",
                http_path='https://job-postings1.p.rapidapi.com'
                          '/api/v2/Jobs/Search',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # bareq | Remote Jobs API
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/bareq/api/remote-jobs-api1/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search jobs",
                nice_description="\
Use a keyword to search from the available jobs.\nYou can also specify a "
                                 "country or a region.",
                http_method="POST",
                http_path='https://remote-jobs-api1.p.rapidapi.com'
                          '/jobs/search',
                # Endpoint is disabled on free
                disabled=True,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="List jobs",
                nice_description="\
Returns a list of the most recent jobs sorted by publishing date.",
                http_method="GET",
                http_path='https://remote-jobs-api1.p.rapidapi.com'
                          '/jobs/all',
                # Endpoint is disabled on free
                disabled=True,
                type__=db.cast(APIEndpointTypes.JOBS_FEED, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="List jobs free",
                nice_description="\
A free endpoint that can be used without a paid subscription."
                "\nReturns a list of the 10 most recent jobs sorted by publishi"
                "ng date.",
                http_method="GET",
                http_path='https://remote-jobs-api1.p.rapidapi.com'
                          '/jobs/free',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_FEED, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # Bebity | Linkedin Jobs Scraper API
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/bebity-bebity-default/api/linkedin-jobs-scraper-api/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get jobs (JSON)",
                nice_description="Get LinkedIn jobs in json",
                http_method="POST",
                http_path='https://linkedin-jobs-scraper-api.p.rapidapi.com'
                          '/jobs',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get jobs trial (JSON)",
                nice_description="Same as get jobs JSON, but limited to 25 jobs"
                                 " max",
                http_method="POST",
                http_path='https://linkedin-jobs-scraper-api.p.rapidapi.com'
                          '/jobs/trial',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get jobs (CSV)",
                nice_description="Get LinkedIn jobs in CSV format",
                http_method="POST",
                http_path='https://linkedin-jobs-scraper-api.p.rapidapi.com'
                          '/jobs/csv',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get jobs (CSV File)",
                nice_description="Get LinkedIn jobs directly in CSV file",
                http_method="POST",
                http_path='https://linkedin-jobs-scraper-api.p.rapidapi.com'
                          '/jobs/csv/file',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # Betoalien | USA Jobs for IT
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/betoalien/api/usa-jobs-for-it/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Full Stack Jobs",
                nice_description="Full Stack Jobs Api",
                http_method="GET",
                http_path='https://usa-jobs-for-it.p.rapidapi.com'
                          '/FullStack',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_FEED, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Data Engineer Jobs",
                nice_description="Data Engineer Jobs Api",
                http_method="GET",
                http_path='https://usa-jobs-for-it.p.rapidapi.com'
                          '/DataEngineer',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_FEED, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Business Intelligence Jobs",
                nice_description="Business Intelligence Jobs Api",
                http_method="GET",
                http_path='https://usa-jobs-for-it.p.rapidapi.com'
                          '/BusinessIntelligence',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_FEED, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Laravel Jobs",
                nice_description="Laravel Jobs Api",
                http_method="GET",
                http_path='https://usa-jobs-for-it.p.rapidapi.com'
                          '/Laravel',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_FEED, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="JavaScript Jobs",
                nice_description="JavaScript Jobs Api",
                http_method="GET",
                http_path='https://usa-jobs-for-it.p.rapidapi.com'
                          '/JavaScript',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_FEED, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Java Jobs",
                nice_description="Java Jobs Api",
                http_method="GET",
                http_path='https://usa-jobs-for-it.p.rapidapi.com'
                          '/Java',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_FEED, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="NodeJS Jobs",
                nice_description="NodeJS Jobs Api",
                http_method="GET",
                http_path='https://usa-jobs-for-it.p.rapidapi.com'
                          '/NodeJs',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_FEED, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Data Analyst Jobs",
                nice_description="Data Analyst Jobs Api",
                http_method="GET",
                http_path='https://usa-jobs-for-it.p.rapidapi.com'
                          '/DataAnalyst',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_FEED, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="React Jobs",
                nice_description="React Jobs Api",
                http_method="GET",
                http_path='https://usa-jobs-for-it.p.rapidapi.com'
                          '/React',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_FEED, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Angular Jobs",
                nice_description="Angular Jobs Api",
                http_method="GET",
                http_path='https://usa-jobs-for-it.p.rapidapi.com'
                          '/Angular',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_FEED, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Python Jobs",
                nice_description="API for Python Jobs",
                http_method="GET",
                http_path='https://usa-jobs-for-it.p.rapidapi.com'
                          '/Python',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_FEED, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # Dodocr7 | Google Jobs
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/dodocr7/api/google-jobs/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="SearchOffers",
                nice_description="Get All Offers URL",
                http_method="GET",
                http_path='https://google-jobs.p.rapidapi.com'
                          '/',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOB_MISC, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="OfferInfo",
                nice_description="Get Offer Data",
                http_method="GET",
                http_path='https://google-jobs.p.rapidapi.com'
                          '/',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOB_DETAILS, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # Fantastic Jobs | Active Jobs DB
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/fantastic-jobs-fantastic-jobs-default/api/active-jobs-db/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Jobs",
                nice_description="\
Search and retrieve jobs on title, location, and organization. Optionally add \
a text or html description",
                http_method="GET",
                http_path='https://active-jobs-db.p.rapidapi.com'
                          '/active-ats',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # fernandelcapo | pizzaallapala | TEST
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/fernandelcapo/api/pizzaallapala'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Producto Promo",
                http_method="GET",
                http_path='https://pizzaallapala.p.rapidapi.com'
                          '/productos-promo',
                disabled=False,
                type__=db.cast(APIEndpointTypes.NONE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Productos",
                http_method="GET",
                http_path='https://pizzaallapala.p.rapidapi.com'
                          '/productos',
                disabled=False,
                type__=db.cast(APIEndpointTypes.NONE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Tags",
                http_method="GET",
                http_path='https://pizzaallapala.p.rapidapi.com'
                          '/tags',
                disabled=False,
                type__=db.cast(APIEndpointTypes.NONE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Usuarios",
                http_method="GET",
                http_path='https://pizzaallapala.p.rapidapi.com'
                          '/usuarios/',
                disabled=False,
                type__=db.cast(APIEndpointTypes.NONE, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # Flatroy | Jobs from Remoteok
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/Flatroy/api/jobs-from-remoteok/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get list",
                nice_description="\
Will show you all job posts. Also you can filter it by adding "
                "in the end of endpoint ?tags=digital+nomad",
                http_method="GET",
                http_path='https://jobs-from-remoteok.p.rapidapi.com'
                          '/',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_FEED, TINYINT()),
            )
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # Freshdata | Fresh Linkedin Profile Data
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/freshdata-freshdata-default/api/fresh-linkedin-profile-data/')
        )
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Personal Profile",
                nice_category="Personal Data",
                nice_description="\
Get full profile data, including experience, education "
                "history, skill-set and company related details. Accept all "
                "type of profile urls. **1 credit per call.**",
                http_method="GET",
                http_path='https://fresh-linkedin-profile-data.p.rapidapi.com'
                          '/get-linkedin-profile',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Profile's Posts",
                nice_category="Personal Data",
                nice_description="\
Get posts of a person based on profile url. Pagination is "
                "supported to get all posts. **2 credits per call.**",
                http_method="GET",
                http_path='https://fresh-linkedin-profile-data.p.rapidapi.com'
                          '/get-profile-posts',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_POSTS_SEARCH, TINYINT()
                               ),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Posts",
                nice_category="Personal Data",
                nice_description="\
Simulates LinkedIn's Post Search Function with most "
                "important filters.  **2 credits per call**",
                http_method="POST",
                http_path='https://fresh-linkedin-profile-data.p.rapidapi.com'
                          '/search-posts',
                disabled=True,
                type__=db.cast(APIEndpointTypes.POSTS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Detect Activity Time",
                nice_category="Personal Data",
                nice_description="\
Get the time of the latest activity. **2 credits per call.**",
                http_method="GET",
                http_path='https://fresh-linkedin-profile-data.p.rapidapi.com'
                          '/get-profile-recent-activity-time',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_MISC, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Profile by Sales Nav URL",
                nice_category="Personal Data",
                nice_description="\
Get full profile data, including experience, education "
                "history, skill-set and company related details. **1 credit "
                "per call.**",
                http_method="GET",
                http_path='https://fresh-linkedin-profile-data.p.rapidapi.com'
                          '/get-linkedin-profile-by-salesnavurl',
                disabled=False,
                type__=db.cast(APIEndpointTypes.PROFILE_MISC, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Company by URL",
                nice_category="Company Data",
                nice_description="\
Given a company’s LinkedIn URL, the API will return "
                "valuable data points in JSON format. **1 credit per call.**",
                http_method="GET",
                http_path='https://fresh-linkedin-profile-data.p.rapidapi.com'
                          '/get-company-by-linkedinurl',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Company's Posts",
                nice_category="Company Data",
                nice_description="\
Get posts from a LinkedIn company page. Pagination is support"
                "ed to fetch all posts. **2 credits per call.*",
                http_method="GET",
                http_path='https://fresh-linkedin-profile-data.p.rapidapi.com'
                          '/get-company-posts',
                disabled=True,
                type__=db.cast(APIEndpointTypes.COMPANY_POSTS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Company by Domain",
                nice_category="Company Data",
                nice_description="\
Find a company on LinkedIn using its web domain. **1 credit pe"
                "r call.**",
                http_method="GET",
                http_path='https://fresh-linkedin-profile-data.p.rapidapi.com'
                          '/get-company-by-domain',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Company by ID",
                nice_category="Company Data",
                nice_description="\
Given a company’s LinkedIn internal ID, the API will return va"
                "luable data points in JSON format. **1 credit per call.**",
                http_method="GET",
                http_path='https://fresh-linkedin-profile-data.p.rapidapi.com'
                          '/get-company-by-id',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Find Custom Headcount",
                nice_category="Company Data",
                nice_description="\
Discover the count of employees within a specific company who "
                "meet designated criteria. **1 credits per call.**",
                http_method="POST",
                http_path='https://fresh-linkedin-profile-data.p.rapidapi.com'
                          '/find-custom-headcount',
                disabled=True,
                type__=db.cast(APIEndpointTypes.COMPANY_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Company Jobs Count",
                nice_category="Company Data",
                nice_description="\
Get number of opening jobs the company posted on LinkedIn. **1"
                " credit per call.**",
                http_method="GET",
                http_path='https://fresh-linkedin-profile-data.p.rapidapi.com'
                          '/get-company-jobs-count',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Crunchbase Details",
                nice_category="Company Data",
                nice_description="\
Get all public details of a company on Crunchbase - including"
                " funding rounds. **2 credits per call.**",
                http_method="GET",
                http_path='https://fresh-linkedin-profile-data.p.rapidapi.com'
                          '/get-company-details-from-crunchbase',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Employees",
                nice_category="Employee Search (Sales Nav)",
                nice_description="""\
Streamline your  Sales Navigator lead searches effortlessly \
without connecting your own account. \n**[See demo script.]\
(http://bit.ly/3UyCGum)**\n\n**How the Process Works:**\n\n- \
**Step 1: Initiate Search**\nLaunch your search with specific \
criteria via a dedicated endpoint. Upon request, you'll receive\
a unique \"request_id\" enabling continuous status checks in \
Step 2. Each search request deducts 50 credits from your \
account.\n\n- **Step 2: Monitor Search Progress**\nUtilize \
the **Check Search Status** endpoint to keep tabs on your \
search's progress. This action is entirely complimentary.\n\n-\
**Step 3: Retrieve Results**\nWith your search complete, \
access the results through the **Get Search Result** \
endpoint. Retrieving each profile incurs a nominal fee of \
0.5 credits. For instance, accessing 100 results consumes 50\
credits.\n\n**Additional Information:**\n- **Timing:** \
Searches are generally concluded within a few minutes, \
although some may extend up to 1 hours. For optimal \
efficiency, submit all your searches concurrently, allowing\
the API to process them within a 1 -hour window.\n\n- \
**Data Retention:** Your search data remains accessible \
for 15 days, ensuring ample time for review and \
utilization.\n\nThis streamlined approach guarantees a \
hassle-free experience, providing precise, targeted results\
while conserving both time and resources.\
""",
                http_method="POST",
                http_path='https://fresh-linkedin-profile-data.p.rapidapi.com'
                          '/search-employees',
                disabled=True,
                type__=db.cast(APIEndpointTypes.WORKERS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Employees by Sales Nav URL",
                nice_category="Employee Search (Sales Nav)",
                nice_description="""\
Works exactly the same endpoint "Search Employees" except that 
it takes a search url as the input. It's helpful when you 
already have sales navigator search url(s).
""",
                http_method="POST",
                http_path='https://fresh-linkedin-profile-data.p.rapidapi.com'
                          '/search-employees-by-sales-nav-url',
                disabled=True,
                type__=db.cast(APIEndpointTypes.WORKERS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Check Search Status",
                nice_category="Employee Search (Sales Nav)",
                nice_description="\
Get the status of your search using the request_id given in "
                "step 1.",
                http_method="GET",
                http_path='https://fresh-linkedin-profile-data.p.rapidapi.com'
                          '/check-search-status',
                disabled=True,
                type__=db.cast(APIEndpointTypes.WORKERS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Search Results",
                nice_category="Employee Search (Sales Nav)",
                nice_description="""\
Get search results. Please make sure the search is "done" \
before calling this endpoint.\
""",
                http_method="GET",
                http_path='https://fresh-linkedin-profile-data.p.rapidapi.com'
                          '/get-search-results',
                disabled=True,
                type__=db.cast(APIEndpointTypes.WORKERS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Companies",
                nice_category="Company Search (Sales Nav)",
                nice_description="""\
Automate LinkedIn Sales Navigator account searches without\
connecting your own account.\n\nHow it works:\n\n**Step 1**:\
Use this endpoint to make a search using your criteria. This\
endpoint will return a "request_id" so that you can check\
for the search status anytime in step 2. This endpoint will cost\
you 25 credits per request.\n\n**Step 2**: Check the search\
status using the endpoint **Check Company Search Status**\
(free).\n\n**Step 3**: Once the search is done, you can start\
collecting the results by using the endpoint **Get Companies**.\
This endpoint will cost you **0.3 credit per one company**. For\
example, if your search returns 100 results, it'll cost 30\
credits.\n\nPlease note: \n- It normally takes a few minutes\
to complete such a search - but sometimes it may need 24 hours.\
We recommend you put in all your searches and let this api\
process them all within 24 hours.\n- We will save your data for\
15 days.\
""",
                http_method="POST",
                http_path='https://fresh-linkedin-profile-data.p.rapidapi.com'
                          '/search-companies',
                disabled=True,
                type__=db.cast(APIEndpointTypes.COMPANY_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Check Company Search Status",
                nice_category="Company Search (Sales Nav)",
                nice_description="""\
Get the status of your search using the request_id given in \
step 1.\
""",
                http_method="GET",
                http_path='https://fresh-linkedin-profile-data.p.rapidapi.com'
                          '/check-search-companies-status',
                disabled=True,
                type__=db.cast(APIEndpointTypes.COMPANY_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Companies",
                nice_category="Company Search (Sales Nav)",
                nice_description="""\
Get search results. Please make sure the search is "done" \
before calling this endpoint.\
""",
                http_method="GET",
                http_path='https://fresh-linkedin-profile-data.p.rapidapi.com'
                          '/get-search-companies-results',
                disabled=True,
                type__=db.cast(APIEndpointTypes.COMPANY_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Jobs",
                nice_category="Job Search",
                nice_description="""\
Search jobs posted on LinkedIn. This endpoint is useful for\
scraping job openings of a specific company on LinkedIn.\
\n\nTo scrape all results from each search, change the param\
*start* from 0 to 25, 50, ... until you see less than 25 results\
returned.\n\n**2 credits per call.**\
""",
                http_method="POST",
                http_path='https://fresh-linkedin-profile-data.p.rapidapi.com'
                          '/search-jobs',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Job Details",
                nice_category="Job Search",
                nice_description="\
Scrape the full job details, including the company basic "
                "information. **1 credit per call.**",
                http_method="GET",
                http_path='https://fresh-linkedin-profile-data.p.rapidapi.com'
                          '/get-job-details',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOB_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Linkedin Profile via Google /google-profiles",
                nice_category="Other Endpoints",
                nice_description="""\
Search LinkedIn profiles via Google by specifying keywords,\
names, locations, job titles, and companies. This API will\
retrieve the most relevant profiles from the top 100 Google\
search results. **2** credits per call.\
""",
                http_method="POST",
                http_path='https://fresh-linkedin-profile-data.p.rapidapi.com'
                          '/google-profiles',
                disabled=False,
                type__=db.cast(APIEndpointTypes.PROFILE_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Recommendation Given",
                nice_category="Other Endpoints",
                nice_description="""\
Get profile’s recommendations (given). **1 credit per call**.\
""",
                http_method="GET",
                http_path='https://fresh-linkedin-profile-data.p.rapidapi.com'
                          '/get-recommendations-given',
                disabled=False,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Recommendation Received",
                nice_category="Other Endpoints",
                nice_description="""\
Get profile’s recommendations (received). **1 credit per call**.\
""",
                http_method="GET",
                http_path='https://fresh-linkedin-profile-data.p.rapidapi.com'
                          '/get-recommendations-received',
                disabled=False,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Years of Experience",
                nice_category="Other Endpoints",
                nice_description="""\
Get the total number of years of experience of a profile.\
""",
                http_method="GET",
                http_path='https://fresh-linkedin-profile-data.p.rapidapi.com'
                          '/get-year-of-experiences',
                disabled=False,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Open to Work Status",
                nice_category="Other Endpoints",
                nice_description="""\
Given a LinkedIn profile URL, the API will let you know if that\
profile is “open to work” or not. **1 credit per call.**\
""",
                http_method="GET",
                http_path='https://fresh-linkedin-profile-data.p.rapidapi.com'
                          '/get-opentowork-status',
                disabled=False,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Open Profile Status",
                nice_category="Other Endpoints",
                nice_description="""\
Given a LinkedIn profile URL, the API will let you know if that\
profile is “open profile” or not. **1 credit per call.**\
""",
                http_method="GET",
                http_path='https://fresh-linkedin-profile-data.p.rapidapi.com'
                          '/get-open-profile-status',
                disabled=False,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Profile PDF CSV",
                nice_category="Other Endpoints",
                nice_description="""\
Get the CV of a LinkedIn profile in PDF format. **1 credit per call.**\
""",
                http_method="GET",
                http_path='https://fresh-linkedin-profile-data.p.rapidapi.com'
                          '/get-profile-pdf-cv',
                disabled=False,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Extra Profile Data",
                nice_category="Other Endpoints",
                nice_description="""\
Get more profile’s data fields like languages, top skills,\
certifications, publications, patents, awards\
""",
                http_method="GET",
                http_path='https://fresh-linkedin-profile-data.p.rapidapi.com'
                          '/get-extra-profile-data',
                disabled=False,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search LinkedIn Company Pages via Google "
                          "/google-companies",
                nice_category="Other Endpoints",
                nice_description="""\
Find up to 100 companies that match your criteria via Google.\
**2** credits per call.\
""",
                http_method="POST",
                http_path='https://fresh-linkedin-profile-data.p.rapidapi.com'
                          '/google-companies',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Company Ads Count",
                nice_category="Other Endpoints",
                nice_description="""\
Get number of ads the company posted on LinkedIn. **1 credit per\
call.**\
""",
                http_method="GET",
                http_path='https://fresh-linkedin-profile-data.p.rapidapi.com'
                          '/get-company-ads-count',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_MISC, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search LinkedIn School Pages via Google "
                          "/google-schools",
                nice_category="Other Endpoints",
                nice_description="""\
Find up to 100 schools that match your criteria via Google.\
**2** credits per call.\
""",
                http_method="POST",
                http_path='https://fresh-linkedin-profile-data.p.rapidapi.com'
                          '/google-schools',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Decision Makers",
                nice_category="Other Endpoints",
                nice_description="""\
Search for decision makers of any company on LinkedIn. This\
endpoint will remove any unmatched profiles that returned by\
LinkedIn. It does much more than a simple search on LinkedIn\
sales navigator.\n\n**It takes 50 credits to initiate a search\
and then takes 0.5 credit per profile returned.**\n\nHow it\
works:\n\nStep 1: Use this endpoint to make a search using your\
criteria. This endpoint will return a "request_id" so that you\
can check for the search status anytime in step 2. This endpoint\
will cost you 50 credit per request.\n\nStep 2: Check the search\
status using the endpoint "/check-search-status". Calling to\
this endpoint is FREE.\n\nStep 3: Once the search is done, you\
can start collecting the results by using the endpoint\
"/get-search-results". This endpoint will cost you 0.5 credit\
per one profile. For example, if your search returns 100\
results, it'll cost 50 credits.\n\n**Please note**:  it normally\
takes a few minutes to complete such a search - but sometimes it\
may need 24 hours. We recommend you put in all your searches \
and let this api process them all within 24 hours.\
""",
                http_method="POST",
                http_path='https://fresh-linkedin-profile-data.p.rapidapi.com'
                          '/search-decision-makers',
                disabled=False,
                type__=db.cast(APIEndpointTypes.WORKERS_SEARCH, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # Freshdata | Linkedin Jobs
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/freshdata-freshdata-default/api/linkedin-jobs4/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Jobs",
                nice_description="""\
Search jobs posted on LinkedIn. This endpoint is useful for scraping job\
openings of a specific company on LinkedIn. \n\nTo scrape all results from\
each search, change the param *start* from 0 to 25, 50, ... until you see less\
than 25 results returned.\n\n**2 credits per call.**\
""",
                http_method="POST",
                http_path='https://linkedin-jobs4.p.rapidapi.com'
                          '/search-jobs',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Job Details",
                nice_description="""\
Scrape the full job details, including the company basic information. **1 \
credit per call.**\
""",
                http_method="GET",
                http_path='https://linkedin-jobs4.p.rapidapi.com'
                          '/get-job-details',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOB_DETAILS, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # jaypat87 | Indeed
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/jaypat87/api/indeed11/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search",
                nice_description="\
Search job postings on Indeed by specifying page, location and"
                " search **query.**",
                http_method="POST",
                http_path='https://indeed11.p.rapidapi.com'
                          '/',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            )
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # jaypat87 | Job Search
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/jaypat87/api/job-search15'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Jobs Search",
                nice_description='\
Search for jobs by specifying zipcode location, or city, '
                'state or just mention "United States" if you want all jobs '
                'matching a keyword.',
                http_method="POST",
                http_path='https://job-search15.p.rapidapi.com'
                          '/',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Job Description Full-Text",
                nice_description="\
Get the full text of the job description.",
                http_method="POST",
                http_path='https://job-search15.p.rapidapi.com'
                          '/',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOB_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Named Entity Extraction",
                nice_category="Text Analytics",
                nice_description="\
Use a named entity Extraction model on Job description.",
                http_method="POST",
                http_path='https://job-search15.p.rapidapi.com'
                          '/',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOB_MISC, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Jobs Classifier",
                nice_category="Text Analytics",
                nice_description="\
Classify jobs based on education level, job function, "
                "seniority level using our state of the art AI model.",
                http_method="POST",
                http_path='https://job-search15.p.rapidapi.com'
                          '/',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOB_MISC, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Summarize Job Descriptions",
                nice_category="Text Analytics",
                nice_description="\
Summarize Job descriptions using our state of the art NLP "
                "based generative model.",
                http_method="POST",
                http_path='https://job-search15.p.rapidapi.com'
                          '/',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOB_MISC, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # jaypat87 | Linkedin Jobs Search
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/jaypat87/api/linkedin-jobs-search/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search",
                nice_description='\
Search for jobs on Linkedin by specifying zipcode location, '
                'or city, state or just mention "United States" if you want '
                'all jobs matching a keyword.',
                http_method="POST",
                http_path='https://linkedin-jobs-search.p.rapidapi.com'
                          '/',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            )
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # jobicy | Remote Jobs API
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/jobicy-jobicy-default/api/jobicy/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Remote Jobs API",
                nice_description="""\
This [API](https://jobicy.com/jobs-rss-feed) provides access to the latest 50\
remote job listings from a diverse range of industries and companies.\
""",
                http_method="GET",
                http_path='https://jobicy.p.rapidapi.com'
                          '/api/v2/remote-jobs',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_FEED, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # jobisite | Job Search
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/jobisite/api/job-search38/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Post Jobs",
                nice_description="\
Post Jobs on Jobisite",
                http_method="POST",
                http_path='https://job-search38.p.rapidapi.com'
                          '/my/add',
                # Disable posting to their job board.
                disabled=True,
                type__=db.cast(APIEndpointTypes.NONE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Jobs",
                nice_description="searchJobs",
                http_method="POST",
                http_path='https://job-search38.p.rapidapi.com'
                          '/my/searchJobs',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # JobsAPI2020 | Zambian Jobs API
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/JobsAPI2020/api/zambian-jobs-api1/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="httpsJobapiCoUkGet",
                nice_description="Body Params Required",
                http_method="POST",
                http_path='https://zambian-jobs-api1.p.rapidapi.com'
                          '/getdataNew.php',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_FEED, TINYINT()),
            )
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # Jobwiz | Job Descriptions API
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/jobwiz-jobwiz-default/api/job-descriptions-api/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="estimateSalaryRange",
                nice_description="""\
Estimates a salary range.\nIt returns a 404 if it cannot estimate the salary\
range.\nThe salary_type value can be "yearly", "monthly",\
"weekly", "daily" or "hourly".\
""",
                nice_category='Salary',
                http_method="GET",
                http_path='https://job-descriptions-api.p.rapidapi.com'
                          '/v1/salary-range-estimate',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOB_SALARY_MISC, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="classifyJD",
                nice_description="""\
Classifies the job function and seniority of a job description.\nThe job\
function uses the 1016 occupations from the 2019 version of O*NET SOC codes:\
https://www.onetcenter.org/taxonomy/2019/list.html\nThe job title is required\
and the job description is optional. The job description can be in HTML or in\
plain text.\nWe currently support Dutch, English, French, German, Italian,\
Polish, Portuguese, Spanish and Turkish for the extraction of the number of\
years of experience.\n\nThe list of seniority values is:\n\n- junior\n-\
mid\n- senior\n- staff\n- principal\n- lead\n- manager\n- director\n-\
vice-president\n- c-suite\
""",
                nice_category='JD classification',
                http_method="POST",
                http_path='https://job-descriptions-api.p.rapidapi.com'
                          '/v1/job-description-classification-onet',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOB_MISC, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="batchClassifyJD",
                nice_description="""\
The batch API endpoint can accept up to 100 job listings.\nWe currently support\
Dutch, English, French, German, Italian, Polish, Portuguese, Spanish and \
Turkish for the extraction of the number of years of experience.\nThe \
possible error codes are:\n\n- MissingJobTitle when the job title is missing \
in the request\n- NoClassification when no occupation matches with the \
content - \nInternalServerError when something went wrong. Please retry when \
you get an InternalServerError.\
""",
                nice_category='JD classification',
                http_method="POST",
                http_path='https://job-descriptions-api.p.rapidapi.com'
                          '/v1/job-description-classification-onet-batch',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOB_MISC, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="batchExtractSalaryRange",
                nice_description="""\
The job description can be sent in HTML or in plain text.\nThe Salary Range API\
endpoint returns the minimum and the maximum values of the salary range, the\
currency and the salary type (e.g. hourly, yearly).\nThe batch API endpoints \
can accept up to 100 job listings.\nThe possible error codes are:\n\n-\
MissingJobDescription when the job description is missing in the request\n-\
InternalServerError when something went wrong. Please retry when you get an\
InternalServerError.\
""",
                nice_category='JD info extraction',
                http_method="POST",
                http_path='https://job-descriptions-api.p.rapidapi.com'
                          '/v1/job-description-salary-range-batch',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOB_SALARY_MISC, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="batchExtractYearsExperience",
                nice_description="""\
The job description can be sent in HTML or in plain text.\nThe Years of\
Experience API endpoint returns the minimum and the maximum required numbers of\
years of experience.\nThe API endpoint returns -1 for both the minimum and\
maximum if there are no required numbers of years of experience.\nIt returns -1\
for the maximum if there is only a minimum number of years of experience.\nWe\
currently support Dutch, English, French, German, Italian, Polish, Portuguese,\
Spanish and Turkish.\nThe batch API endpoints can accept up to 100 job\
listings.\nThe possible error codes are:\n\n- MissingJobDescription when the \
job description is missing in the request\n- InternalServerError when \
something went wrong. Please retry when you get an InternalServerError.\
""",
                nice_category='JD info extraction',
                http_method="POST",
                http_path='https://job-descriptions-api.p.rapidapi.com'
                          '/v1/job-description-years-experience-batch',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOB_YEARS_EXP_MISC, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="extractYearsExperience",
                nice_description="""\
Extract the numbers of years of experience. The job description can be in HTML\
or in plain text. It returns -1 for both the minimum and maximum if there are\
no required numbers of years of experience. It returns -1 for both the maximum\
if there is only a minimum number of years of experience.\
""",
                nice_category='JD info extraction',
                http_method="POST",
                http_path='https://job-descriptions-api.p.rapidapi.com'
                          '/v1/job-description-years-experience',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOB_YEARS_EXP_MISC, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="extractSalaryRange",
                nice_description="""\
Extracts a salary range from a job description. The job description can be in\
HTML or plain text.\
""",
                nice_category='JD info extraction',
                http_method="POST",
                http_path='https://job-descriptions-api.p.rapidapi.com'
                          '/v1/job-description-salary-range',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOB_SALARY_MISC, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # Jobwiz | Job Search API
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/jobwiz-jobwiz-default/api/job-search-api1/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="searchJob",
                nice_description="""\
Searches job with a search query.\nThe search query is mandatory.\nWhen there\
are no results, a 200 status code with an empty jobs array will be\
returned.\nThe salary range is provided when it's available.\nThe salary_type\
has 5 possible values: "yearly", "monthly", "weekly", "daily" and "hourly".\
""",
                http_method="GET",
                http_path='https://job-search-api1.p.rapidapi.com'
                          '/v1/job-description-search',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            )
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # letscrape | Job Salary Data
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/letscrape-6bRBa3QguO5/api/job-salary-data/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Job Salary",
                nice_description="\
Get estimated job salaries/pay by job title and location.",
                http_method="GET",
                http_path='https://job-salary-data.p.rapidapi.com'
                          '/job-salary',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOB_SALARY_MISC, TINYINT()),
            )
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # letscrape | JSearch
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/letscrape-6bRBa3QguO5/api/jsearch/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search",
                nice_description="""\
Search for jobs posted on any public job site across the web on the largest job\
aggregate in the world (Google for Jobs). Extensive filtering support and most\
options available on Google for Jobs.\
""",
                http_method="GET",
                http_path='https://jsearch.p.rapidapi.com'
                          '/search',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Filters",
                nice_description="""\
Accepts all **Search** endpoint parameters (except for `page` and `num_pages`)\
and returns the relevant filters and their estimated result counts for later \
use in search or for analytics.\
""",
                http_method="GET",
                http_path='https://jsearch.p.rapidapi.com'
                          '/search-filters',
                disabled=False,
                type__=db.cast(APIEndpointTypes.MISC_GENERAL, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Job Details",
                nice_description="""\
Get all job details, including additional information such as: application\
options / links, employer reviews and estimated salaries for similar jobs.\
""",
                http_method="GET",
                http_path='https://jsearch.p.rapidapi.com'
                          '/job-details',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOB_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Estimated Salary",
                nice_description="""\
Get estimated salaries / pay for a jobs around a location by job title and\
location. The salary estimations are returned for several periods, depending on\
data availability / relevance, and includes: hourly, daily, weekly, monthly, or\
yearly.\
""",
                http_method="GET",
                http_path='https://jsearch.p.rapidapi.com'
                          '/estimated-salary',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOB_SALARY_MISC, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # letscrape | Real-Time Glassdoor Data
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/letscrape-6bRBa3QguO5/api/real-time-glassdoor-data/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Company Search",
                nice_description="""\
Search for companies (employers) on Glassdoor.\
""",
                http_method="GET",
                http_path='https://real-time-glassdoor-data.p.rapidapi.com'
                          '/company-search',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Company Reviews",
                nice_description="""\
Get company (employer) reviews from Glassdoor, with filters, sort option, and\
pagination support.
""",
                http_method="GET",
                http_path='https://real-time-glassdoor-data.p.rapidapi.com'
                          '/company-reviews',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_REVIEWS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Company Overview",
                nice_description="""\
Get company (employer) overview/details from Glassdoor (e.g.\
https://www.glassdoor.com/Overview/Working-at-Apple-EI_IE1138.11,16.htm).\
""",
                http_method="GET",
                http_path='https://real-time-glassdoor-data.p.rapidapi.com'
                          '/company-overview',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_DETAILS, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # Lundehund | Twitter X Job API
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/Lundehund/api/twitter-x-api'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get User Detail",
                nice_category="User",
                http_method="GET",
                http_path='https://twitter-x-api.p.rapidapi.com'
                          '/api/user/detail',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get User Followers",
                nice_category="User",
                http_method="GET",
                http_path='https://twitter-x-api.p.rapidapi.com'
                          '/api/user/followers',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get User Verified Followers",
                nice_category="User",
                http_method="GET",
                http_path='https://twitter-x-api.p.rapidapi.com'
                          '/api/user/followers/blue-verified',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get User Following",
                nice_category="User",
                http_method="GET",
                http_path='https://twitter-x-api.p.rapidapi.com'
                          '/api/user/following',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get User Subscriptions",
                nice_category="User",
                http_method="GET",
                http_path='https://twitter-x-api.p.rapidapi.com'
                          '/api/user/subscriptions',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get User Tweets",
                nice_category="User",
                http_method="GET",
                http_path='https://twitter-x-api.p.rapidapi.com'
                          '/api/user/tweets',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get User Replies",
                nice_category="User",
                http_method="GET",
                http_path='https://twitter-x-api.p.rapidapi.com'
                          '/api/user/replies',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get User Medias",
                nice_category="User",
                http_method="GET",
                http_path='https://twitter-x-api.p.rapidapi.com'
                          '/api/user/medias',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get User Likes",
                nice_category="User",
                http_method="GET",
                http_path='https://twitter-x-api.p.rapidapi.com'
                          '/api/user/likes',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get User Highlights",
                nice_category="User",
                http_method="GET",
                http_path='https://twitter-x-api.p.rapidapi.com'
                          '/api/user/highlights',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Tweet Detail",
                nice_category="Tweet",
                http_method="GET",
                http_path='https://twitter-x-api.p.rapidapi.com'
                          '/api/tweet/detail',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Tweet Retweeters",
                nice_category="Tweet",
                http_method="GET",
                http_path='https://twitter-x-api.p.rapidapi.com'
                          '/api/tweet/retweeters',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Tweet Retweets",
                nice_category="Tweet",
                http_method="GET",
                http_path='https://twitter-x-api.p.rapidapi.com'
                          '/api/tweet/quotes',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Tweet Likes",
                nice_category="Tweet",
                http_method="GET",
                http_path='https://twitter-x-api.p.rapidapi.com'
                          '/api/tweet/likes',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Tweet Hidden Replies",
                nice_category="Tweet",
                http_method="GET",
                http_path='https://twitter-x-api.p.rapidapi.com'
                          '/api/tweet/hidden-replies',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Top",
                nice_category="Search",
                http_method="GET",
                http_path='https://twitter-x-api.p.rapidapi.com'
                          '/api/search/top',
                disabled=True,
                type__=db.cast(APIEndpointTypes.POSTS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Latest",
                nice_category="Search",
                http_method="GET",
                http_path='https://twitter-x-api.p.rapidapi.com'
                          '/api/search/latest',
                disabled=True,
                type__=db.cast(APIEndpointTypes.POSTS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search People",
                nice_category="Search",
                http_method="GET",
                http_path='https://twitter-x-api.p.rapidapi.com'
                          '/api/search/people',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Media",
                nice_category="Search",
                http_method="GET",
                http_path='https://twitter-x-api.p.rapidapi.com'
                          '/api/search/media',
                disabled=True,
                type__=db.cast(APIEndpointTypes.POSTS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Lists",
                nice_category="Search",
                http_method="GET",
                http_path='https://twitter-x-api.p.rapidapi.com'
                          '/api/search/lists',
                disabled=True,
                type__=db.cast(APIEndpointTypes.POSTS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get List Tweets",
                nice_category="List",
                http_method="GET",
                http_path='https://twitter-x-api.p.rapidapi.com'
                          '/api/list/tweets',
                disabled=True,
                type__=db.cast(APIEndpointTypes.POSTS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get List Followers",
                nice_category="List",
                http_method="GET",
                http_path='https://twitter-x-api.p.rapidapi.com'
                          '/api/list/followers',
                disabled=True,
                type__=db.cast(APIEndpointTypes.POSTS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get List Member",
                nice_category="List",
                http_method="GET",
                http_path='https://twitter-x-api.p.rapidapi.com'
                          '/api/list/member',
                disabled=True,
                type__=db.cast(APIEndpointTypes.POSTS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Job Detail",
                nice_category="Job",
                http_method="GET",
                http_path='https://twitter-x-api.p.rapidapi.com'
                          '/api/job/detail',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOB_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Job",
                nice_category="Job",
                http_method="GET",
                http_path='https://twitter-x-api.p.rapidapi.com'
                          '/api/job/search',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Location",
                nice_category="Job",
                http_method="GET",
                http_path='https://twitter-x-api.p.rapidapi.com'
                          '/api/job/search/location',
                disabled=False,
                type__=db.cast(APIEndpointTypes.LOCATIONS_SEARCH, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # mantiks | Glassdoor
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/mantiks-mantiks-default/api/glassdoor/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Company Details",
                nice_category="Companies",
                nice_description="\
Crawl information for Glassdoor's Companies",
                http_method="GET",
                http_path='https://glassdoor.p.rapidapi.com'
                          '/company/',
                # 403 errors when querying based on ID.
                disabled=True,
                type__=db.cast(APIEndpointTypes.COMPANY_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Companies Search",
                nice_category="Companies",
                nice_description="Search companies by name.",
                http_method="GET",
                http_path='https://glassdoor.p.rapidapi.com'
                          '/companies/search',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Job details",
                nice_category="Jobs",
                nice_description="Crawl information for Glassdoor's Job",
                http_method="GET",
                http_path='https://glassdoor.p.rapidapi.com'
                          '/job/',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOB_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Jobs Search",
                nice_category="Jobs",
                nice_description="Search jobs with by keyword and location.",
                http_method="GET",
                http_path='https://glassdoor.p.rapidapi.com'
                          '/jobs/search',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Locations Search",
                nice_category="Locations",
                nice_description="""\
Search a city / country / state to retrieve location_id / location_type. \
Useful for jobs search\
""",
                http_method="GET",
                http_path='https://glassdoor.p.rapidapi.com'
                          '/locations/search',
                disabled=False,
                type__=db.cast(APIEndpointTypes.LOCATIONS_SEARCH, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # mantiks | Indeed
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/mantiks-mantiks-default/api/indeed12/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Job details",
                nice_category="Jobs",
                nice_description="Crawl information for Indeed's Job.",
                http_method="GET",
                http_path='https://indeed12.p.rapidapi.com'
                          '/job/',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOB_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Jobs Search",
                nice_category="Jobs",
                nice_description="Search jobs with by query and location.",
                http_method="GET",
                http_path='https://indeed12.p.rapidapi.com'
                          '/jobs/search',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Company details",
                nice_category="Companies",
                nice_description="Crawl information for Indeed's companies.",
                http_method="GET",
                http_path='https://indeed12.p.rapidapi.com'
                          '/company/',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Company Search",
                nice_category="Companies",
                nice_description="Search companies by name.",
                http_method="GET",
                http_path='https://indeed12.p.rapidapi.com'
                          '/companies/search',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Company jobs",
                nice_category="Companies",
                nice_description="Search jobs by company.",
                http_method="GET",
                http_path='https://indeed12.p.rapidapi.com'
                          '/company/',
                http_path_suffix='/jobs',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # mgujjargamingm | LinkedIn Data Scraper
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/mgujjargamingm/api/linkedin-data-scraper/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Person Data",
                nice_category="Person",
                nice_description="\
Scrapes any Linkedin profiles data including skills, "
                "certificates, experiences, qualifications and much more.",
                http_method="POST",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/person',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Person Data ( Using Urn )",
                nice_category="Person",
                nice_description="\
It takes profile urn instead of profile public identifier in input",
                http_method="POST",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/person_urn',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Person Data ( Deep )",
                nice_category="Person",
                nice_description="\
Scrapes All experiences, educations, skills, languages, publications... related\
 to a profile.",
                http_method="POST",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/person_deep',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Person Posts ( WITH PAGINATION )",
                nice_category="Person",
                nice_description="\
Scrapes posts of a linkedin profile along with reaction, comments, postLink and\
 reposts data.",
                http_method="GET",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/profile_updates',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_POSTS_SEARCH, TINYINT()
                               ),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Person Posts ( BETA )",
                nice_category="Person",
                nice_description="\
Scrapes posts on a linkedin profile along with reactions, "
                "comments, reposts data.",
                http_method="POST",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/profile_updates',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_POSTS_SEARCH, TINYINT()
                               ),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Person Recent Activity ( Comments on Posts ) "
                          "/profile_recent_comments",
                nice_category="Person",
                nice_description="\
Scrapes 20 most recent comments posted by a linkedin user ("
                "per page)",
                http_method="POST",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/profile_recent_comments',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_POSTS_SEARCH, TINYINT()
                               ),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Email to Linkedin Profile ( BETA ) "
                          "/email_to_linkedin_profile",
                nice_category="Person",
                nice_description="\
Takes email and returns linkedin profile registered against "
                "that mail",
                http_method="POST",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/email_to_linkedin_profile',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Check on Person Job Changed Status "
                          "/person_job_change_status",
                nice_category="Person",
                nice_description="\
Takes a linkedin user's profile and his current companyID "
                "in input and returns job_changed flag reflecting job change "
                "status",
                http_method="POST",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/person_job_change_status',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Similar Profiles",
                nice_category="Person",
                nice_description="\
Returns similar profiles to a profile linkedin profile link",
                http_method="GET",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/similar_profiles',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_MISC, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Company Data",
                nice_category="Company",
                nice_description="\
Scrapes any LinkedIn company data including investors info, "
                "recent updates, top employees and much more.",
                http_method="POST",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/company',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Company Data (Premium)",
                nice_category="Company",
                nice_description="\
Deep scrapes company data",
                http_method="POST",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/company_pro',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Company data from web-domain /web-domain",
                nice_category="Company",
                nice_description="\
First searches for LinkedIn company URL from website, "
                "then scrapes data against that URL from /company endpoint.",
                http_method="POST",
                http_path='https://linkedin-data-scraper.p.rapidapi.com/'
                          'web-domain',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Company Jobs",
                nice_category="Company",
                nice_description="\
Scrapes any LinkedIn company jobs in recent order, including "
                "job apply URL, Number of applications, Job location, and much "
                "more.",
                http_method="POST",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/company_jobs',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Company Posts ( WITH PAGINATION ) /company_updates",
                nice_category="Company",
                nice_description="\
Scrapes LinkedIn company posts along with reactions, "
                "comments, and reposts data.",
                http_method="GET",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/company_updates',
                disabled=True,
                type__=db.cast(APIEndpointTypes.COMPANY_POSTS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Company Employee count per skill "
                          "/company_employee_count_per_skill",
                nice_category="Company",
                nice_description="""\
This endpoint returns number of employees in a company as per "people" tab.""",
                http_method="POST",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/company_employee_count_per_skill',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_MISC, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Company Employee",
                nice_category="Company",
                nice_description="""\
As per "People" tab in a company page, this endpoint scrapes 12 people data \
per API call.""",
                http_method="GET",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/company_employee',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Company Posts ( BETA )",
                nice_category="Company",
                nice_description="\
Scrapes LinkedIn company posts along with reactions, comments, and reposts "
                "data.",
                http_method="POST",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/company_updates',
                disabled=True,
                type__=db.cast(APIEndpointTypes.COMPANY_POSTS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Leads",
                nice_category="Sales Navigator",
                nice_description="\
LinkedIn sales navigator search leads page with filters",
                http_method="POST",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/premium_search_person',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Leads ( Using URL )",
                nice_category="Sales Navigator",
                nice_description="\
Apply all filters at sales navigator, copy the URL and use it here.",
                http_method="POST",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/premium_search_person_via_url',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Companies ( Using URL )",
                nice_category="Sales Navigator",
                nice_description="\
Apply all filters at sales navigator, copy the URL and use it here.",
                http_method="POST",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/premium_search_company_via_url',
                disabled=True,
                type__=db.cast(APIEndpointTypes.COMPANY_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Filter Company Headcount",
                nice_category="Sales Navigator",
                nice_description="\
When you select Company Headcount in LinkedIn Sales "
                "Navigator Filters, a list of suggested employee range "
                "appears in a dropdown. This endpoint returns those "
                "suggestions.",
                http_method="GET",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/filter_company_headcount',
                disabled=True,
                type__=db.cast(APIEndpointTypes.COMPANY_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Filter Function Suggestions",
                nice_category="Sales Navigator",
                nice_description="\
When you type something in search bar of LinkedIn sales "
                "navigator filter Functions, a list of suggested Job "
                "functions appears in a dropdown. This endpoint returns those "
                "suggestions.",
                http_method="GET",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/filter_function_suggestions',
                disabled=True,
                type__=db.cast(APIEndpointTypes.JOB_MISC, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Filter Job Title Suggestions",
                nice_category="Sales Navigator",
                nice_description="\
When you type something in search bar LinkedIn Sales "
                "navigator filter Job Title, a list of suggested Job Titles "
                "appear in a dropdown. This endpoint returns those "
                "suggestions.",
                http_method="GET",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/filter_job_title_suggestions',
                disabled=True,
                type__=db.cast(APIEndpointTypes.JOB_MISC, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Filter Company Type",
                nice_category="Sales Navigator",
                nice_description="\
When you selected Company Type in LinkedIn Sales Navigator "
                "Filters, a list of suggested Company types appear in a "
                "dropdown. This endpoint returns those suggestions.",
                http_method="GET",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/filter_company_type',
                disabled=True,
                type__=db.cast(APIEndpointTypes.COMPANY_MISC, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Filter Company Suggestions",
                nice_category="Sales Navigator",
                nice_description="\
When you type something in search bar of LinkedIn Sales "
                "Navigator filter Past Company or Current Company, a list if "
                "suggested companies appears in a dropdown. This endpoint "
                "returns those suggestions.",
                http_method="GET",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/filter_company_suggestions',
                disabled=True,
                type__=db.cast(APIEndpointTypes.COMPANY_MISC, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Filter Search Suggestions",
                nice_category="Sales Navigator",
                nice_description="\
When you type something in search bar of LinkedIn Sales "
                "Navigator, a list of suggested people appears in a dropdown. "
                "This endpoint returns those suggestions.",
                http_method="GET",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/filter_search_suggestions',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Filter Seniority Level",
                nice_category="Sales Navigator",
                nice_description="\
When you selected Seniority level in LinkedIn Sales "
                "Navigator Filters, a list of suggested Seniority levels "
                "appear in a dropdown. This endpoint returns those "
                "suggestions.",
                http_method="GET",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/filter_seniority_level',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_MISC, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Filter Years In",
                nice_category="Sales Navigator",
                nice_description="\
When you select Years in LinkedIn Sales Navigator Filters, "
                "a list of suggested years appear in a dropdown. This "
                "endpoint returns those suggestions.",
                http_method="GET",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/filter_years_in',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_MISC, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Filter Geography Location Suggestions",
                nice_category="Sales Navigator",
                nice_description="\
When you type something in search bar of LinkedIn Sales "
                "Navigator Filter Geography, a list of suggested Geography "
                "Locations appears in a dropdown. This endpoint returns those "
                "suggestions. ( Zipcode filter not included )",
                http_method="GET",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/filter_geography_location_suggestions',
                disabled=True,
                type__=db.cast(APIEndpointTypes.LOCATIONS_QUERY, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Filter Industry Suggestions",
                nice_category="Sales Navigator",
                nice_description="\
When you type something in the search bar of LinkedIn Sales "
                "navigator filter Industry, a list of suggested industries "
                "appear in a dropdown. This endpoint returns those "
                "suggestions.",
                http_method="GET",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/filter_industry_suggestions',
                disabled=True,
                type__=db.cast(APIEndpointTypes.INDUSTRY_QUERY, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Filter Languages",
                nice_category="Sales Navigator",
                nice_description="\
When you select Languages in LinkedIn Sales Navigator "
                "Filters, a list of suggested languages appear in a dropdown. "
                "This endpoint returns those suggestions.",
                http_method="GET",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/filter_languages',
                disabled=True,
                type__=db.cast(APIEndpointTypes.MISC_GENERAL, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Filter School Suggestions",
                nice_category="Sales Navigator",
                nice_description="\
When you type something in the search bar of LinkedIn Sales "
                "Navigator filter School, a list of suggested schools appear "
                "in a dropdown. This endpoint returns those suggestions.",
                http_method="GET",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/filter_school_suggestions',
                disabled=True,
                type__=db.cast(APIEndpointTypes.MISC_GENERAL, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search People",
                nice_category="Search",
                nice_description="\
Grabs top matching results of LinkedIn Profiles against a keyword",
                http_method="POST",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/search_person',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Company",
                nice_category="Search",
                nice_description="\
(*geoUrns is optional) Search for companies against a "
                "keyword. Can provide as much results as from LinkedIn.",
                http_method="POST",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/search_company',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Jobs",
                nice_category="Search",
                nice_description='''\
Search for jobs on LinkedIn with specific  keywords and location. Scrapes all \
data posted at LinkedIn site.''',
                http_method="POST",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/search_jobs',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Jobs ( with filters )",
                nice_category="Search",
                nice_description="\
You can search for jobs using LinkedIn built-in filters.",
                http_method="GET",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/search_jobs',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search GeoUrns",
                nice_category="Search",
                nice_description="\
You can search geourn ids with location name. This endpoint "
                "is like an autocomplete. It will give you a list of 10 "
                "locations (name and geourn).",
                http_method="POST",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/search_geourns',
                disabled=False,
                type__=db.cast(APIEndpointTypes.LOCATIONS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Suggestion Language",
                nice_category="Search",
                nice_description="\
List of languages to be passed to language_list filter in "
                "search_people_with_filters endpoint",
                http_method="GET",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/suggestion_language',
                disabled=True,
                type__=db.cast(APIEndpointTypes.MISC_GENERAL, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Suggestion Service Category",
                nice_category="Search",
                nice_description="\
Suggestions for Service Category per query.",
                http_method="GET",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/suggestion_service_catagory',
                disabled=True,
                type__=db.cast(APIEndpointTypes.MISC_GENERAL, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Suggestion School",
                nice_category="Search",
                nice_description="School suggestion per query",
                http_method="GET",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/suggestion_school',
                disabled=True,
                type__=db.cast(APIEndpointTypes.MISC_GENERAL, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Suggestion Company",
                nice_category="Search",
                nice_description="Company suggestions per query",
                http_method="GET",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/suggestion_company',
                disabled=True,
                type__=db.cast(APIEndpointTypes.COMPANY_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Suggestion Industry",
                nice_category="Search",
                nice_description="Suggestions for industry per query",
                http_method="GET",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/suggestion_industry',
                disabled=True,
                type__=db.cast(APIEndpointTypes.INDUSTRY_QUERY, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Suggestion Location",
                nice_category="Search",
                nice_description="Location suggestions per query",
                http_method="GET",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/suggestion_location',
                disabled=True,
                type__=db.cast(APIEndpointTypes.LOCATIONS_QUERY, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Suggestion Company Size",
                nice_category="Search",
                nice_description="\
Company Size suggestions for search company with filters endpoint",
                http_method="GET",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/suggestion_company_size',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Companies With Filters",
                nice_category="Search",
                nice_description="Search Companies with Filters",
                http_method="POST",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/search_company_with_filters',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search People With Filters",
                nice_category="Search",
                nice_description="Search People with Filters",
                http_method="POST",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/search_people_with_filters',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SEARCH, TINYINT()),
            ),
            # API Provider moved Bulk scraping to
            # https://rapidapi.com/mgujjargamingm/api/linkedin-bulk-data-scraper
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Companies",
                nice_category="Mass OR Bulk",
                nice_description="Scrapes 100 companies in one go",
                http_method="POST",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/bulk_companies',
                disabled=True,
                type__=db.cast(APIEndpointTypes.COMPANY_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Profiles",
                nice_category="Mass OR Bulk",
                nice_description="Mass scrapes 50 profiles in one go",
                http_method="POST",
                http_path='https://linkedin-data-scraper.p.rapidapi.com'
                          '/bulk_profiles',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # mgujjargamingm | Linkedin BULK data scraper
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/mgujjargamingm/api/linkedin-bulk-data-scraper'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Profiles",
                nice_category="1 Request/Sec Endpoints",
                nice_description="Scrapes 100 profiles",
                http_method="POST",
                http_path='https://linkedin-bulk-data-scraper.p.rapidapi.com'
                          '/profiles',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Companies",
                nice_category="1 Request/Sec Endpoints",
                nice_description="Scrapes 100 companies",
                http_method="POST",
                http_path='https://linkedin-bulk-data-scraper.p.rapidapi.com'
                          '/companies',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Company Posts ( BETA )",
                nice_category="1 Request/Sec Endpoints",
                nice_description="Scrapes 100 posts of 50 companies",
                http_method="POST",
                http_path='https://linkedin-bulk-data-scraper.p.rapidapi.com'
                          '/company_posts',
                disabled=True,
                type__=db.cast(APIEndpointTypes.COMPANY_POSTS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Posts",
                nice_category="25 Request/Sec Endpoints",
                nice_description="Search posts as per LinkedIn.com Search "
                                 "Engine (with Filters)",
                http_method="POST",
                http_path='https://linkedin-bulk-data-scraper.p.rapidapi.com'
                          '/search_posts',
                disabled=True,
                type__=db.cast(APIEndpointTypes.POSTS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Person Data",
                nice_category="25 Request/Sec Endpoints",
                nice_description="Scrapes all data of a person from LinkedIn.",
                http_method="POST",
                http_path='https://linkedin-bulk-data-scraper.p.rapidapi.com'
                          '/person',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Person Data ( Using URN )",
                nice_category="25 Request/Sec Endpoints",
                nice_description="Scrapes all data from a person' page using "
                                 "his/her profile URN.",
                http_method="POST",
                http_path='https://linkedin-bulk-data-scraper.p.rapidapi.com'
                          '/person_urn',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Person Skills",
                nice_category="25 Request/Sec Endpoints",
                nice_description="Scrapes all skills of a LinkedIn User.",
                http_method="POST",
                http_path='https://linkedin-bulk-data-scraper.p.rapidapi.com'
                          '/person_skills',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Company Data",
                nice_category="25 Request/Sec Endpoints",
                nice_description="Scrapes all data from provided company URL",
                http_method="POST",
                http_path='https://linkedin-bulk-data-scraper.p.rapidapi.com'
                          '/company',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search People With Filters",
                nice_category="25 Request/Sec Endpoints",
                nice_description="Search for people from LinkedIn using all "
                                 "filters as per LinkedIn.",
                http_method="POST",
                http_path='https://linkedin-bulk-data-scraper.p.rapidapi.com'
                          '/search_people_with_filters',
                disabled=True,
                type__=db.cast(APIEndpointTypes.PROFILE_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Company With Filters",
                nice_category="25 Request/Sec Endpoints",
                nice_description="Search for companies as per LinkedIn Search "
                                 "Engine",
                http_method="POST",
                http_path='https://linkedin-bulk-data-scraper.p.rapidapi.com'
                          '/search_company_with_filters',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Profile Updates",
                nice_category="25 Request/Sec Endpoints",
                nice_description="Scrapes updates posted by a LinkedIn User. "
                                 "Scrapes 20 updates per page. Must pass "
                                 "paginationToken from page 1 to page 2, from "
                                 "page 2 to page 3, from page 3 to page 4 and "
                                 "so on to get accurate results.",
                http_method="GET",
                http_path='https://linkedin-bulk-data-scraper.p.rapidapi.com'
                          '/profile_updates',
                disabled=False,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Company Updates",
                nice_category="25 Request/Sec Endpoints",
                nice_description="Scrapes updates of a given company",
                http_method="GET",
                http_path='https://linkedin-bulk-data-scraper.p.rapidapi.com'
                          '/company_updates',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_MISC, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Jobs",
                nice_category="25 Request/Sec Endpoints",
                nice_description="Search for jobs with filters as per LinkedIn."
                                 " It returns basic details of each job."
                                 " To get full data use Job Details Endpoint.",
                http_method="GET",
                http_path='https://linkedin-bulk-data-scraper.p.rapidapi.com'
                          '/search_jobs',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Job Details",
                nice_category="25 Request/Sec Endpoints",
                nice_description="Returns all data of a job posted at LinkedIn "
                                 "using jobPostingUrn (Obtained using Search "
                                 "Jobs Endpoint.)",
                http_method="GET",
                http_path='https://linkedin-bulk-data-scraper.p.rapidapi.com'
                          '/job_details',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOB_DETAILS, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # omarmohamed0 | Jobs API
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/omarmohamed0/api/freelancer-api/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get all freelancers in specific page",
                nice_description="\
Fetch all of the freelancers per specific page and the "
                "default number of freelancers search results is 10 (values "
                "may change).",
                http_method="GET",
                http_path='https://freelancer-api.p.rapidapi.com'
                          '/find-freelancers/',
                # 404 error
                disabled=True,
                type__=db.cast(APIEndpointTypes.WORKERS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get all freelancers",
                nice_description="\
Getting all of the freelancers and some details (title, "
                "rating, total earnings, reviews, description, hourly rate) "
                "and the default number of freelancers per request is 10 ("
                "values may change).",
                http_method="GET",
                http_path='https://freelancer-api.p.rapidapi.com'
                          '/api/find-freelancers',
                disabled=False,
                type__=db.cast(APIEndpointTypes.WORKERS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get all jobs in specific page",
                nice_description="\
This endpoint gets all of the jobs in specific page "
                "(default is the first page) till 100 pages.",
                http_method="GET",
                http_path='https://freelancer-api.p.rapidapi.com'
                          '/api/find-job/',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get All Jobs",
                nice_description="\
This endpoint gets all of the listed jobs for different "
                "skills and prices and bids number.",
                http_method="GET",
                http_path='https://freelancer-api.p.rapidapi.com'
                          '/api/find-job',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_FEED, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # Pat92 | Jobs API
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/Pat92/api/jobs-api14/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="List Jobs",
                nice_category="Job Search",
                nice_description="""\
The API simplifies the job search process by offering an array of filter \
criteria in the URL parameters, to receive relevant results.\n\n**Filters \
(URL-Parameters):**\n**- query:** Keywords, Company names, job titles, etc. \
*Required*\n**- location:** Country, city or general location. *Required*\n**-\
 remoteOnly:** Only return remote jobs (true/false). *Optional (default value =\
false)* \n**- employmentTypes:** Filter by fulltime, parttime, contractor, \
intern. Multiple values can be added semcolon separated. *Optional (default \
value = '': all results are returned)*\n**- datePosted:** Filter by creation \
date of th job posting; month, week, 3days, today. *Optional (default value =\
'': all results are returned)*\n**- distance:** Filter jobs based on \
proximity to a specified location in kilometers. *Optional (default value = \
-1.0: all results are returned)*\n**- language:** This is not the language \
of the jobs, but of specific fields. *Optional (default value = \
'en_GB':english is used)*\n**- index:** Normally you will receive 10 \
results for each request, to get more you can increase the index by one. \
*Optional (default value = 1)*\n\n**Returned Fields:**\n**- jobs:** A list \
of returned jobs.\n   - id: Base64 ID of the job-listing\n   - title: Job \
title\n   - company: Company name\n   - description: Job description\n   - \
image: Image of the company\n   - location: Location of the job\n   - \
employmentType: Types of employment for the job listing.\n   - datePosted: \
Date when the job-listing was posted\n   - salaryRange: Salary range for the\
job posting\n   - jobProviders: Array of jobboards, including their name \
and the url\n\n**- index:** Current search-index.\n**- jobCount:** Amount\
of jobs returned, maxiumum of jobs per request is 10.\n**- hasError:** \
Bolean to check for errors.\n**- errors:** Array of error messages.\
""",
                http_method="GET",
                http_path='https://jobs-api14.p.rapidapi.com'
                          '/list',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get salary range",
                nice_category="Salary range",
                nice_description="""\
Get salary ranges for specific job titles per 
country.\n**URL-Parameters:**\n**- jobTitle:** The job title you want the\
salary range from. use **Get job titles** for valid titles. *Required*\n**-\
countryCode:** The country you want the salary range from.  (for example: DE,\
US, CH) *Required*\
""",
                http_method="GET",
                http_path='https://jobs-api14.p.rapidapi.com'
                          '/salary/getSalaryRange',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOB_SALARY_MISC, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get job titles",
                nice_category="Salary range",
                nice_description="""\
Get job titles, for usage in the **Get salary range**\
endpoint.\n**URL-Parameters:**\n**- query:** Find job titles from your query.\
*Required*\n**- countryCode:** Find job titles for the country.  (for example:\
DE, US, CH)*Required*\
""",
                http_method="GET",
                http_path='https://jobs-api14.p.rapidapi.com'
                          '/salary/getJobTitles',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOB_TITLE_SEARCH, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # qurazor1 | Remoote Job Search
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/qurazor1/api/remoote-job-search1/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="list_skills_skills_get",
                nice_category="Jobs",
                http_method="GET",
                http_path='https://remoote-job-search1.p.rapidapi.com'
                          '/remoote/skills',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOB_SKILLS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="list_jobs_jobs_get",
                nice_category="Jobs",
                http_method="GET",
                http_path='https://remoote-job-search1.p.rapidapi.com'
                          '/remoote/jobs',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="get_related_jobs_jobs__int_id___related_post",
                nice_category="Jobs",
                http_method="POST",
                http_path='https://remoote-job-search1.p.rapidapi.com'
                          '/remoote/jobs/',
                http_path_suffix='/related',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="list_countries_countries_get",
                nice_category="Jobs",
                http_method="GET",
                http_path='https://remoote-job-search1.p.rapidapi.com'
                          '/remoote/countries',
                disabled=False,
                type__=db.cast(APIEndpointTypes.LOCATIONS_QUERY, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="list_titles_titles_get",
                nice_category="Jobs",
                http_method="GET",
                http_path='https://remoote-job-search1.p.rapidapi.com'
                          '/remoote/titles',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOB_TITLE_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="get_authenticated_user_users_me_get",
                nice_category="Jobs",
                http_method="GET",
                http_path='https://remoote-job-search1.p.rapidapi.com'
                          '/remoote/users/me',
                disabled=True,
                type__=db.cast(APIEndpointTypes.MISC_GENERAL, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="get_job_jobs__int_id__get",
                nice_category="Jobs",
                http_method="GET",
                http_path='https://remoote-job-search1.p.rapidapi.com'
                          '/remoote/jobs/',
                disabled=True,
                type__=db.cast(APIEndpointTypes.JOB_DETAILS, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # Relu Consultancy | Arbeitsagentur
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/relu-consultancy-relu-consultancy-default/api'
                '/arbeitsagentur-employement-agency/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Token",
                nice_description="Get Token",
                http_method="GET",
                http_path='\
https://arbeitsagentur-employement-agency.p.rapidapi.com'
                          '/get-token',
                disabled=False,
                type__=db.cast(APIEndpointTypes.MISC_CREATE_TOKEN, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Jobs",
                nice_description="\
Search jobs with input parameters keyword, location and radius",
                http_method="GET",
                http_path='\
https://arbeitsagentur-employement-agency.p.rapidapi.com'
                          '/search',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # Relu Consultancy | Indeed Scraper API - Germany
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/relu-consultancy-relu-consultancy-default/api'
                '/indeed-scraper-api-germany/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Token",
                nice_description="Generate Token",
                http_method="GET",
                http_path='https://indeed-scraper-api-germany.p.rapidapi.com'
                          '/get-token',
                disabled=False,
                type__=db.cast(APIEndpointTypes.MISC_CREATE_TOKEN, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Jobs",
                nice_description="""\
Search the jobs from Indeed Germany based on provided parameters for "keyword" 
and "location". """,
                http_method="GET",
                http_path='https://indeed-scraper-api-germany.p.rapidapi.com'
                          '/search',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Job View",
                nice_description="""\
Takes "jobkey" as a parameter and returns the details of job as output.""",
                http_method="GET",
                http_path='https://indeed-scraper-api-germany.p.rapidapi.com'
                          '/jobview',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOB_DETAILS, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # RockAPIs | Linkedin API
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/rockapis-rockapis-default/api/linkedin-api8/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Employees",
                nice_category="Employee Search",
                nice_description="Get employees of company. 50 result per "
                                 "page **20 credits per call**",
                http_method="GET",
                http_path='https://linkedin-api8.p.rapidapi.com'
                          '/search-employees',
                disabled=False,
                type__=db.cast(APIEndpointTypes.PROFILE_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Company Details",
                nice_category="Company",
                nice_description="The endpoint returns full details of the "
                                 "LinkedIn company details + Crunchbase URL "
                                 "in JSON format",
                http_method="GET",
                http_path='https://linkedin-api8.p.rapidapi.com'
                          '/get-company-details',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Company By Domain (BETA)",
                nice_category="Company",
                nice_description="Get Company Insight Details & Company "
                                 "Details in  single request **5 credits per "
                                 "call** If the request fails. You don't pay. "
                                 "Automate LinkedIn Sales Navigator. This "
                                 "endpoint is beta. If you are faced with an "
                                 "issue, please contact us.",
                http_method="GET",
                http_path='https://linkedin-api8.p.rapidapi.com'
                          '/get-company-by-domain',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Company Insights [PREMIUM] (Beta)",
                nice_category="Company",
                nice_description="Get Company Insight Details & Company "
                                 "Details in a single request. **5 Credits "
                                 "per call.** If the request fails, you don't "
                                 "pay. Automate LinkedIn Sales Navigator. This "
                                 "endpoint is beta. IF you are faced with an "
                                 "issue, please contact us.",
                http_method="GET",
                http_path='https://linkedin-api8.p.rapidapi.com'
                          '/get-company-insights',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Company Employees Count",
                nice_category="Company",
                nice_description="Get company employees count (location "
                                 "filter possible)",
                http_method="POST",
                http_path='https://linkedin-api8.p.rapidapi.com'
                          '/get-company-employees-count',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Company Jobs Count",
                nice_category="Company",
                nice_description="Get total number of opening jobs in the "
                                 "company.",
                http_method="GET",
                http_path='https://linkedin-api8.p.rapidapi.com'
                          '/get-company-jobs-count',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Company Pages People Also Viewed",
                nice_category="Company",
                nice_description="Get Company Pages People also viewed.",
                http_method="GET",
                http_path='https://linkedin-api8.p.rapidapi.com'
                          '/get-company-pages-people-also-viewed',
                disabled=True,
                type__=db.cast(APIEndpointTypes.COMPANY_MISC, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Company's Post",
                nice_category="Company",
                nice_description="Get last 50 posts of a company. **1 credit "
                                 "per call.**",
                http_method="GET",
                http_path='https://linkedin-api8.p.rapidapi.com'
                          '/get-company-posts',
                disabled=True,
                type__=db.cast(APIEndpointTypes.COMPANY_POSTS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Company Post Comments",
                nice_category="Company",
                nice_description="Get comments of a company post.",
                http_method="GET",
                http_path='https://linkedin-api8.p.rapidapi.com'
                          '/get-company-post-comments',
                disabled=True,
                type__=db.cast(APIEndpointTypes.COMPANY_POSTS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Job Details",
                nice_category="Job APIs",
                nice_description="Get the full job details, including the job "
                                 "skills and the company information.",
                http_method="GET",
                http_path='https://linkedin-api8.p.rapidapi.com'
                          '/get-job-details',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOB_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Jobs",
                nice_category="Job APIs",
                nice_description="Search Jobs",
                http_method="GET",
                http_path='https://linkedin-api8.p.rapidapi.com'
                          '/search-jobs',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Jobs V2",
                nice_category="Job APIs",
                nice_description="Search Jobs",
                http_method="GET",
                http_path='https://linkedin-api8.p.rapidapi.com'
                          '/search-jobs-v2',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Hiring Team",
                nice_category="Job APIs",
                nice_description="Get hiring team/job poster profile details. "
                                 "You can use either a Job ID or a Job URL. "
                                 "One of these is required.",
                http_method="GET",
                http_path='https://linkedin-api8.p.rapidapi.com'
                          '/get-hiring-team',
                disabled=False,
                type__=db.cast(APIEndpointTypes.PROFILE_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Locations",
                nice_category="Location",
                nice_description="Search locations by keyword.",
                http_method="GET",
                http_path='https://linkedin-api8.p.rapidapi.com'
                          '/search-locations',
                disabled=False,
                type__=db.cast(APIEndpointTypes.LOCATIONS_QUERY, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # RockAPIs | Rapid LinkedIn Data API
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/rockapis-rockapis-default/api/linkedin-data-api/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Employees",
                nice_category="Employee Search",
                nice_description="Get employees of company. 50 result per "
                                 "page **10 credits per call**",
                http_method="GET",
                http_path='https://linkedin-data-api.p.rapidapi.com'
                          '/search-employees',
                disabled=False,
                type__=db.cast(APIEndpointTypes.PROFILE_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Company Details",
                nice_category="Company",
                nice_description="The endpoint returns full details of the "
                                 "LinkedIn company details + Crunchbase URL "
                                 "in JSON format",
                http_method="GET",
                http_path='https://linkedin-data-api.p.rapidapi.com'
                          '/get-company-details',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Company By Domain (BETA)",
                nice_category="Company",
                nice_description="Get a company's LinkedIn data by domain. "
                                 "**1 credit per successful request.**",
                http_method="GET",
                http_path='https://linkedin-data-api.p.rapidapi.com'
                          '/get-company-by-domain',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Company Insights [PREMIUM] (Beta)",
                nice_category="Company",
                nice_description="Get Company Insight Details & Company "
                                 "Details in a single request. **5 Credits "
                                 "per call.** If the request fails, you don't "
                                 "pay. Automate LinkedIn Sales Navigator. This "
                                 "endpoint is beta.",
                http_method="GET",
                http_path='https://linkedin-data-api.p.rapidapi.com'
                          '/get-company-insights',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Company Employees Count",
                nice_category="Company",
                nice_description="Get company employees count (location "
                                 "filter possible)",
                http_method="POST",
                http_path='https://linkedin-data-api.p.rapidapi.com'
                          '/get-company-employees-count',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Company Jobs Count",
                nice_category="Company",
                nice_description="Get total number of opening jobs in the "
                                 "company.",
                http_method="GET",
                http_path='https://linkedin-data-api.p.rapidapi.com'
                          '/get-company-jobs-count',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_MISC, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Company Pages People Also Viewed",
                nice_category="Company",
                nice_description="Get Company Pages People also viewed.",
                http_method="GET",
                http_path='https://linkedin-data-api.p.rapidapi.com'
                          '/get-company-pages-people-also-viewed',
                disabled=True,
                type__=db.cast(APIEndpointTypes.COMPANY_MISC, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Company's Post",
                nice_category="Company",
                nice_description="Get last 50 posts of a company. 1 credit "
                                 "per call.",
                http_method="GET",
                http_path='https://linkedin-data-api.p.rapidapi.com'
                          '/get-company-posts',
                disabled=True,
                type__=db.cast(APIEndpointTypes.COMPANY_POSTS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Company Post Comments",
                nice_category="Company",
                nice_description="Get comments of a company post.",
                http_method="GET",
                http_path='https://linkedin-data-api.p.rapidapi.com'
                          '/get-company-post-comments',
                disabled=True,
                type__=db.cast(APIEndpointTypes.COMPANY_POSTS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Jobs",
                nice_category="Job APIs",
                nice_description="Search Jobs",
                http_method="GET",
                http_path='https://linkedin-data-api.p.rapidapi.com'
                          '/search-jobs',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Job Details",
                nice_category="Job APIs",
                nice_description="Get the full job details, including the job "
                                 "skills and the company information.",
                http_method="GET",
                http_path='https://linkedin-data-api.p.rapidapi.com'
                          '/get-job-details',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOB_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Jobs V2",
                nice_category="Job APIs",
                nice_description="Search Jobs",
                http_method="GET",
                http_path='https://linkedin-data-api.p.rapidapi.com'
                          '/search-jobs-v2',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Hiring Team",
                nice_category="Job APIs",
                nice_description="Get hiring team/job poster profile details. "
                                 "You can use either a Job ID or a Job URL. "
                                 "One of these is required.",
                http_method="GET",
                http_path='https://linkedin-data-api.p.rapidapi.com'
                          '/get-hiring-team',
                disabled=False,
                type__=db.cast(APIEndpointTypes.PROFILE_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Locations",
                nice_category="Location",
                nice_description="Search locations by keyword.",
                http_method="GET",
                http_path='https://linkedin-data-api.p.rapidapi.com'
                          '/search-locations',
                disabled=False,
                type__=db.cast(APIEndpointTypes.LOCATIONS_SEARCH, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # RockAPIs | Rapid Linkedin Jobs API
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/rockapis-rockapis-default/api/rapid-linkedin-jobs-api/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Jobs",
                nice_description="Search LinkedIn jobs with keywords, "
                                 "company, location, on-site/remote, "
                                 "date posted, title, function, industry, "
                                 "salary, experience level, and job type "
                                 "filters.",
                http_method="GET",
                http_path='https://rapid-linkedin-jobs-api.p.rapidapi.com'
                          '/search-jobs',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Job Details",
                nice_description="The endpoint returns all detail of the job "
                                 "and company.",
                http_method="GET",
                http_path='https://rapid-linkedin-jobs-api.p.rapidapi.com'
                          '/get-job-details',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOB_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Jobs V2",
                nice_description="Search LinkedIn jobs with keywords, "
                                 "company, location, on-site/remote, "
                                 "date posted, title, function, industry, "
                                 "salary, experience level, and job type "
                                 "filters.",
                http_method="GET",
                http_path='https://rapid-linkedin-jobs-api.p.rapidapi.com'
                          '/search-jobs-v2',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Hiring Team",
                nice_description="Get hiring team/job poster profile details. "
                                 "You can use either a job ID or a Job URL. "
                                 "One of these is required.",
                http_method="GET",
                http_path='https://rapid-linkedin-jobs-api.p.rapidapi.com'
                          '/get-hiring-team',
                disabled=False,
                type__=db.cast(APIEndpointTypes.PROFILE_MISC, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # sohailglt | Linkedin Live Data
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/sohailglt/api/linkedin-live-data/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Company Search",
                nice_description="This endpoint facilitates targeted search "
                                 "for up-to-date company profiles.",
                http_method="POST",
                http_path='https://linkedin-live-data.p.rapidapi.com'
                          '/company-search',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="People Search",
                nice_description="This endpoint facilitates targeted search "
                                 "for up-to-date people profiles.",
                http_method="POST",
                http_path='https://linkedin-live-data.p.rapidapi.com'
                          '/people-search',
                disabled=False,
                type__=db.cast(APIEndpointTypes.PROFILE_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Profile Details",
                nice_description="You can use this endpoint to get details "
                                 "for personal LinkedIn Profiles.",
                http_method="POST",
                http_path='https://linkedin-live-data.p.rapidapi.com'
                          '/profile-details',
                disabled=False,
                type__=db.cast(APIEndpointTypes.PROFILE_SCRAPE, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Company Details",
                nice_description="You can use this endpoint to get details "
                                 "for company's LinkedIn Profiles.",
                http_method="POST",
                http_path='https://linkedin-live-data.p.rapidapi.com'
                          '/profile-details',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_DETAILS, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Industries List",
                nice_description="Retrieve the list of industries applicable "
                                 "for utilization on the search endpoint.",
                http_method="GET",
                http_path='https://linkedin-live-data.p.rapidapi.com'
                          '/company-industries',
                disabled=False,
                type__=db.cast(APIEndpointTypes.INDUSTRY_QUERY, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Company Types",
                nice_description="Get the list of company types to use in "
                                 "company_type search filter.",
                http_method="GET",
                http_path='https://linkedin-live-data.p.rapidapi.com'
                          '/company-types',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_MISC, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # vuesdata | Indeed Jobs - Sweden
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/vuesdata/api/indeed-jobs-api-sweden/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="SearchJobs",
                nice_description="""\
offset = 0 (starting of the page, it must be increased by 10 to achieve \
pagination)\nkeyword = python (it can be any search keyword for ex: job title \
or skill title)\nlocation = Stockholm (For now this API gets data for Sweden \
Indeed. You can enter a specific city or state.)\nThis will provide you with \
a list of 15 jobs in the page, by default a single page can have a max of 15 \
jobs posting only. In order to get all the data using pagination you need to \
keep increasing the count of offset by 10.\n\nYou will get the following \
fields using this API.\n\n'position'\n'company_name'\n'job_title'\n\
'job_location'\n'salary'\n'date'\n'job_url'\n'urgently_hiring'\n'multiple_\
hiring'\n'company_rating'\n'company_reviews'\n'company_review_link'\n\
'company_logo_url'\n'page_number'\
""",
                http_method="GET",
                http_path='https://indeed-jobs-api-sweden.p.rapidapi.com'
                          '/indeed-se/',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # vuesdata | Indeed Jobs API
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/vuesdata/api/indeed-jobs-api/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="SearchJobs",
                nice_description="""\
offset = 0 (starting of the page, it must be increased by 10 to achieve \
pagination)\nkeyword = python (it can be any search keyword for ex: job title \
or skill title)\nlocation = Stockholm (For now this API gets data for Sweden \
Indeed. You can enter a specific city or state.)\nThis will provide you with \
a list of 15 jobs in the page, by default a single page can have a max of 15 \
jobs posting only. In order to get all the data using pagination you need to \
keep increasing the count of offset by 10.\n\nYou will get the following \
fields using this API.\n\n'position'\n'company_name'\n'job_title'\n\
'job_location'\n'salary'\n'date'\n'job_url'\n'urgently_hiring'\n'multiple_\
hiring'\n'company_rating'\n'company_reviews'\n'company_review_link'\n\
'company_logo_url'\n'page_number'\
""",
                http_method="GET",
                http_path='https://indeed-jobs-api.p.rapidapi.com'
                          '/indeed-us/',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # vuesdata | Indeed Jobs API - Denmark
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/vuesdata/api/indeed-jobs-api-denmark/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="SearchJobs",
                nice_description="""\
offset = 0 (starting of the page, it must be increased by 10 to achieve \
pagination)\nkeyword = python (it can be any search keyword for ex: job title \
or skill title)\nlocation = Stockholm (For now this API gets data for Sweden \
Indeed. You can enter a specific city or state.)\nThis will provide you with \
a list of 15 jobs in the page, by default a single page can have a max of 15 \
jobs posting only. In order to get all the data using pagination you need to \
keep increasing the count of offset by 10.\n\nYou will get the following \
fields using this API.\n\n'position'\n'company_name'\n'job_title'\n\
'job_location'\n'salary'\n'date'\n'job_url'\n'urgently_hiring'\n'multiple_\
hiring'\n'company_rating'\n'company_reviews'\n'company_review_link'\n\
'company_logo_url'\n'page_number'\
""",
                http_method="GET",
                http_path='https://indeed-jobs-api-denmark.p.rapidapi.com'
                          '/indeed-dk/',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # vuesdata | Indeed Jobs API - Finland
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/vuesdata/api/indeed-jobs-api-finland/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="SearchJobs",
                nice_description="""\
offset = 0 (starting of the page, it must be increased by 10 to achieve \
pagination)\nkeyword = python (it can be any search keyword for ex: job title \
or skill title)\nlocation = Stockholm (For now this API gets data for Sweden \
Indeed. You can enter a specific city or state.)\nThis will provide you with \
a list of 15 jobs in the page, by default a single page can have a max of 15 \
jobs posting only. In order to get all the data using pagination you need to \
keep increasing the count of offset by 10.\n\nYou will get the following \
fields using this API.\n\n'position'\n'company_name'\n'job_title'\n\
'job_location'\n'salary'\n'date'\n'job_url'\n'urgently_hiring'\n'multiple_\
hiring'\n'company_rating'\n'company_reviews'\n'company_review_link'\n\
'company_logo_url'\n'page_number'\
""",
                http_method="GET",
                http_path='https://indeed-jobs-api-finland.p.rapidapi.com'
                          '/indeed-fi/',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        # apijobs | apijobs
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
             'https://app.apijobs.dev/'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Jobs",
                nice_description='''\
This route, searchJobs, is designed to fetch the latest job listings from the \
database. When a POST request is sent to /search, the server executes a search \
operation without specific query parameters, thus retrieving the most recent \
100 job listings based on their creation date. It also calculates the total \
number of job listings available. The route responds with a JSON object \
containing a success status, the list of job data, and the total job count. In \
case of an error, it logs the error and returns a server error response.''',
                http_method="POST",
                http_path='https://api.apijobs.dev'
                          '/v1/job/search',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOBS_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Search Organization",
                nice_description='Search inside organization that are currently'
                                 ' hiring',
                http_method="POST",
                http_path='https://api.apijobs.dev'
                          '/v1/organization/search',
                disabled=False,
                type__=db.cast(APIEndpointTypes.COMPANY_SEARCH, TINYINT()),
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Job by ID",
                nice_description='''\
This route retrieves detailed information about a specific job using its unique\
 ID. When you send a GET request with a job ID, the route provides you with all\
  the relevant job details in response. If there's an issue with your request, \
  you'll receive an error message.\
''',
                http_method="GET",
                http_path='https://api.apijobs.dev'
                          '/job/',
                disabled=False,
                type__=db.cast(APIEndpointTypes.JOB_DETAILS, TINYINT()),
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        db.session.close()
        print(APIEndpoint.__tablename__ + " seeded successfully!")

    except Exception as e:
        print(f"Error committing data: {e}")

# Example Seed Format
# nice_description can have """ and stores TEXT in the column.
# nice_category can be added to categorize endpoints.
"""     
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
             '___'
             '___'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="___",
                nice_description=
                "___",
                http_method="___",
                http_path='___'
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="___",
                nice_description=
                "___",
                http_method="___",
                http_path='___'
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))
"""
