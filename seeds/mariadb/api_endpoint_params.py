"""
API Endpoint Parameters

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
            APIEndpointParam.__tablename__,
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

        # retrieve API Endpoints in order to reference foreign keys.
        API_Endpoint_List = db.session.query(APIEndpoint).all()

        # Get Job by ID
        # APIJobs | Job Searching API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://apijob-job-searching-api.p.rapidapi.com'
                '/v1/job/') and
            i.nice_name == 'Get job by id')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='id',
                description='Detailed Information about a specific Job ID',
                hint_type='String',
                default_value='65d9c96f19e3a211a90b9f41',
                path_param=True,
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # /api/v2/Jobs/Latest
        # avadataservices | Job Postings
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://job-postings1.p.rapidapi.com'
                '/') and
            i.nice_name == '/api/v2/Jobs/Latest')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='PageNumber',
                description='Page Number',
                hint_type='Number',
                default_value='1',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='PageSize',
                description='Page Size',
                hint_type='Number',
                default_value='12',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # /api/v2/Jobs/{slug}
        # avadataservices | Job Postings
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://job-postings1.p.rapidapi.com'
                '/api/v2/Jobs/') and
            i.nice_name == '/api/v2/Jobs/{slug}')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='slug',
                description='Slug',
                hint_type='String',
                default_value='principal-cloud-solutions-architect-4674',
                path_param=True,
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # /api/v2/Jobs/Search
        # avadataservices | Job Postings
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://job-postings1.p.rapidapi.com'
                '/api/v2/Jobs/Search') and
            i.nice_name == '/api/v2/Jobs/Search')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='searchQuery',
                description='Search Query',
                hint_type='String',
                default_value='Software Engineer',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='PageSize',
                description='Page Size',
                hint_type='Number',
                default_value='12',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='PageNumber',
                description='Page Number',
                hint_type='Number',
                default_value='1',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # SearchOffers
        # Dodocr7 | Google Jobs
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://google-jobs.p.rapidapi.com'
                '/') and
            i.nice_name == 'SearchOffers')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='keyword',
                description='Search Keyword',
                hint_type='String',
                default_value='Software Engineer',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='location',
                description='Location of Posting',
                hint_type='String',
                default_value='United States',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='offset',
                description='Offset of Job (Pagination)',
                hint_type='Number',
                default_value='0',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='posted',
                description='Time Posted '
                            '(i.e. today, '
                            '3days, '
                            'week, '
                            'month, '
                            'all)',
                hint_type='String',
                default_value='all',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # OfferInfo
        # Dodocr7 | Google Jobs
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://google-jobs.p.rapidapi.com'
                '/') and
            i.nice_name == 'OfferInfo')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='joburl',
                description='URL of job search website',
                hint_type='String',
                default_value='https://www.google.com/search?ibp=htl%3Bjobs&q=d'
                              'eveloper+newyork&hl=en-US&kgs=e473f607e23ae72f&s'
                              'hndl=-1&source=sh%2Fx%2Fim%2Ftextlists%2Fdetail%'
                              '2F1&entrypoint=sh%2Fx%2Fim%2Ftextlists%2Fdetail&'
                              'mysharpfpstate=tldetail&htivrt=jobs&htiq=develop'
                              'er+newyork&htidocid=6ak4txGw4C4AAAAAAAAAAA%3D%3'
                              'D',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Jobs
        # Fantastic Jobs | Active Jobs DB
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://active-jobs-db.p.rapidapi.com'
                '/active-ats') and
            i.nice_name == 'Get Jobs')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='title',
                description="""\
SSearch on the job title. You can search like you search on Google, see the \
documentation for more info.\
""",
                hint_type='String',
                default_value='"Data Engineer"',
                required=False
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='location',
                description="""\
Filter on location. Please do not search on abbreviations like US, UK, NYC. \
Instead, search on full names like United States, New York, United Kingdom.\
""",
                hint_type='String',
                default_value='"United States"',
                required=False
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='organization',
                description="""\
Filter on Company, like \"Apple\".\
""",
                hint_type='String',
                default_value='',
                required=False
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='offset',
                description="""\
Offset allows you to paginate results. For example, if you want to retrieve \
300 jobs from our api you can send 3 requests with offset 0, 100, and 200.\
""",
                hint_type='Number',
                default_value='',
                required=False
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='description',
                description="""\
Description Type. Leave empty to return data without job description. \
Option 1: 'text' Option 2: 'html'
""",
                hint_type='String',
                default_value='text',
                required=False
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Usuarios
        # fernandelcapo | pizzaallapala | TEST
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://pizzaallapala.p.rapidapi.com'
                '/usuarios/') and
            i.nice_name == 'Usuarios')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='id',
                description='ID',
                hint_type='String',
                default_value='',
                path_param=True,
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Personal Profile
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-linkedin-profile') and
            i.nice_name == 'Get Personal Profile')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='linkedin_url',
                description='URL of LinkedIn Profile',
                hint_type='String',
                default_value='https://www.linkedin.com/in/cjfollini/',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='include_skills',
                description='Include Skills',
                hint_type='String Boolean',
                default_value='false',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='include_certifications',
                description='Include Certifications',
                hint_type='String Boolean',
                default_value='false',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='include_publications',
                description='Include Publications',
                hint_type='String Boolean',
                default_value='false',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='include_honors',
                description='Include Honors',
                hint_type='String Boolean',
                default_value='false',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='include_volunteers',
                description='Include Volunteers',
                hint_type='String Boolean',
                default_value='false',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='include_projects',
                description='Include Projects',
                hint_type='String Boolean',
                default_value='false',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='include_patents',
                description='Include Patents',
                hint_type='String Boolean',
                default_value='false',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='include_courses',
                description='Include Courses',
                hint_type='String Boolean',
                default_value='false',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='include_organizations',
                description='Include Organizations',
                hint_type='String Boolean',
                default_value='false',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Personal Profile
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-profile-posts') and
            i.nice_name == "Get Profile's Posts")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='linkedin_url',
                description='URL of LinkedIn Profile',
                hint_type='String',
                default_value='https://www.linkedin.com/in/williamhgates/',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='type',
                description='Type - \nPossible Values \n(posts: to scrape '
                            'posts from tab Posts -- posts or posts '
                            're-shared by the person) \n(comments: to scrape'
                            'posts from tab Comments -- posts the person'
                            'commented) \n(reactions: to scrape posts from '
                            'tab Reactions -- posts the person reacted)',
                hint_type='String',
                default_value='posts',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='start',
                description='Use this param to fetch posts of the next '
                            'result page: 0 for page 1, 50 for page 2, '
                            'etc.',
                hint_type='Number',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='pagination_token',
                description='Required when fetching the next result page. '
                            'Please use the token from the result of your '
                            'previous call.',
                hint_type='String',
                default_value='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Detect Activity Time
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-profile-recent-activity-time') and
            i.nice_name == "Detect Activity Time")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='linkedin_url',
                description='URL of LinkedIn Profile',
                hint_type='String',
                default_value='https://www.linkedin.com/in/williamhgates/',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Profile by Sales Nav URL
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-linkedin-profile-by-salesnavurl') and
            i.nice_name == "Get Profile by Sales Nav URL")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='linkedin_url',
                description='URL of LinkedIn Profile',
                hint_type='String',
                default_value='https://www.linkedin.com/sales/lead'
                              '/ACoAAABD0a4B2wblfHunfjGEN-uRLdg2MnWydmk,name,'
                              'zofi',
                required=True,
                disabled=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='include_skills',
                description='Include Skills',
                hint_type='String Boolean',
                default_value='false',
                required=False,
                disabled=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='include_certifications',
                description='Include Certifications',
                hint_type='String Boolean',
                default_value='false',
                required=False,
                disabled=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='include_publications',
                description='Include Publications',
                hint_type='String Boolean',
                default_value='false',
                required=False,
                disabled=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='include_honors',
                description='Include Honors',
                hint_type='String Boolean',
                default_value='false',
                required=False,
                disabled=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='include_volunteers',
                description='Include Volunteers',
                hint_type='String Boolean',
                default_value='false',
                required=False,
                disabled=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='include_projects',
                description='Include Projects',
                hint_type='String Boolean',
                default_value='false',
                required=False,
                disabled=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='include_patents',
                description='Include Patents',
                hint_type='String Boolean',
                default_value='false',
                required=False,
                disabled=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='include_courses',
                description='Include Courses',
                hint_type='String Boolean',
                default_value='false',
                required=False,
                disabled=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='include_organizations',
                description='Include Organizations',
                hint_type='String Boolean',
                default_value='false',
                required=False,
                disabled=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Company by URL
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-company-by-linkedinurl') and
            i.nice_name == "Get Company by URL")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='linkedin_url',
                description='URL of LinkedIn Company Profile',
                hint_type='String',
                default_value='https://www.linkedin.com/company/google/',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Company's Posts
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-company-posts') and
            i.nice_name == "Get Company's Posts")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='linkedin_url',
                description='URL of LinkedIn Company Profile',
                hint_type='String',
                default_value='https://www.linkedin.com/company/google/',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='start',
                description='Use this param to fetch posts of the next '
                            'result page: 0 for page 1, 50 for page 2, '
                            'etc.',
                hint_type='Number',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='pagination_token',
                description='Required when fetching the next result page. '
                            'Please use the token from the result of your '
                            'previous call.',
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='sort_by',
                description='Possible values: top, recent',
                hint_type='String',
                default_value='recent',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Company by Domain
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-company-by-domain') and
            i.nice_name == "Get Company by Domain")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='domain',
                description='URL of Company',
                hint_type='String',
                default_value='google.com',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Company by ID
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-company-by-id') and
            i.nice_name == "Get Company by ID")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='company_id',
                description='ID of Company',
                hint_type='String',
                default_value='162479',
                path_param=True,
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Company Jobs Count
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-company-jobs-count') and
            i.nice_name == "Get Company Jobs Count")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='company_id',
                description='ID of Company',
                hint_type='String',
                default_value='162479',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Crunchbase Details
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-company-details-from-crunchbase') and
            i.nice_name == "Get Crunchbase Details")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='crunchbase',
                description='Crunchbase URL',
                hint_type='String',
                default_value='https://www.crunchbase.com/organization/kinly'
                              '-c638',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Check Search Status
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/check-search-status') and
            i.nice_name == "Check Search Status")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='request_id',
                description='Request ID',
                hint_type='String',
                default_value='dd1b29063de8927b31fa523d36432b61',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Search Results
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-search-results') and
            i.nice_name == "Get Search Results")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='request_id',
                description='Request ID',
                hint_type='String',
                default_value='dd1b29063de8927b31fa523d36432b61',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='page',
                description='Page Number',
                hint_type='String',
                default_value='1',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Check Company Search Status
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/check-search-companies-status') and
            i.nice_name == "Check Company Search Status")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='request_id',
                description='Request ID',
                hint_type='String',
                default_value='ba072fac0b38d12378ef5023742f0184s34e1i8n2a7p0m9'
                              'o',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Companies
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-search-companies-results') and
            i.nice_name == "Get Companies")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='request_id',
                description='Request ID',
                hint_type='String',
                default_value='ba072fac0b38d12378ef5023742f0184s34e1i8n2a7p0m9'
                              'o',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='page',
                description='Page #',
                hint_type='String',
                default_value='1',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Job Details
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-job-details') and
            i.nice_name == "Get Job Details")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='job_url',
                description='Job URL',
                hint_type='String',
                default_value='https://www.linkedin.com/jobs/view/3766410207/',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='include_skills',
                description='Include Skills '
                            '**Including skills will cost 1 more credit**',
                hint_type='Boolean String',
                default_value='false',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Recommendation Given
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-recommendations-given') and
            i.nice_name == "Get Recommendation Given")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='linkedin_url',
                description='LinkedIn URL',
                hint_type='URL',
                default_value='https://www.linkedin.com/in/ajjames',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Recommendation Received
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-recommendations-received') and
            i.nice_name == "Get Recommendation Received")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='linkedin_url',
                description='LinkedIn URL',
                hint_type='URL',
                default_value='https://www.linkedin.com/in/ajjames',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Years of Experience
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-year-of-experiences') and
            i.nice_name == "Get Years of Experience")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='linkedin_url',
                description='LinkedIn URL',
                hint_type='URL',
                default_value='https://www.linkedin.com/in/ajjames',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Open to Work Status
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-opentowork-status') and
            i.nice_name == "Get Open to Work Status")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='linkedin_url',
                description='LinkedIn URL',
                hint_type='URL',
                default_value='https://www.linkedin.com/in/williamhgates/',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Open Profile Status
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-open-profile-status') and
            i.nice_name == "Get Open Profile Status")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='linkedin_url',
                description='LinkedIn URL',
                hint_type='URL',
                default_value='https://www.linkedin.com/in/williamhgates/',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Profile PDF CSV
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-profile-pdf-cv') and
            i.nice_name == "Get Profile PDF CSV")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='linkedin_url',
                description='LinkedIn URL',
                hint_type='URL',
                default_value='https://www.linkedin.com/in/williamhgates/',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Extra Profile Data
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-extra-profile-data') and
            i.nice_name == "Get Extra Profile Data")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='linkedin_url',
                description='LinkedIn URL',
                hint_type='URL',
                default_value='https://www.linkedin.com/in/ajjames/',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Company Ads Count
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-company-ads-count') and
            i.nice_name == "Get Company Ads Count")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='company_id',
                description='ID of Company (i.e. 162479)',
                hint_type='String',
                default_value='',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Job Details
        # Freshdata | Linkedin Jobs
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-jobs4.p.rapidapi.com'
                '/get-job-details') and
            i.nice_name == "Get Job Details")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='job_url',
                description='Job URL',
                hint_type='String',
                default_value='https://www.linkedin.com/jobs/view/3766410207/',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='include_skills',
                description='Include Skills **Including skills will cost 1 more'
                            ' credit**',
                hint_type='Boolean String',
                default_value='false',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Remote Jobs API
        # jobicy | Remote Jobs API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                    'https://jobicy.p.rapidapi.com'
                    '/api/v2/remote-jobs') and
            i.nice_name == "Remote Jobs API")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='count',
                description='Count - # of listings to return '
                            '(i.e. default is 50, range: 1-50)',
                hint_type='Number',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='tag',
                description='Tag - Search by Job Title and Description '
                            '(i.e. all jobs)',
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='geo',
                description='Geographic Location - Filter by job region - See '
                            'https://jobicy.com'
                            '/api/v2/remote-jobs?get=locations (i.e. usa)',
                hint_type='String',
                default_value='usa',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # estimateSalaryRange
        # Jobwiz | Job Descriptions API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://job-descriptions-api.p.rapidapi.com'
                '/v1/salary-range-estimate') and
            i.nice_name == 'estimateSalaryRange')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='company',
                description='Company Name',
                hint_type='String',
                default_value='Google',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='title',
                description='Title',
                hint_type='String',
                default_value='Software Engineer',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='city',
                description='City (i.e. New York)',
                hint_type='String',
                default_value='New York',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='country',
                description='Country (i.e. us)',
                hint_type='String',
                default_value='us',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # searchJob
        # Jobwiz | Job Search API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://job-search-api1.p.rapidapi.com'
                '/v1/job-description-search') and
            i.nice_name == 'searchJob')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='q',
                description='Keyword',
                hint_type='String',
                default_value='Software Engineer',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='page',
                description='Page # - First page index is 1',
                hint_type='String',
                default_value='1',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='country',
                description='Country - ISO 3166-1 alpha-2 country code '
                            'https://en.wikipedia.org/wiki/List_of_ISO_3166_cou'
                            'ntry_codes',
                hint_type='String',
                default_value='us',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='city',
                description='City',
                hint_type='String',
                default_value='New York',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Job Salary
        # letscrape | Job Salary Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://job-salary-data.p.rapidapi.com'
                '/job-salary') and
            i.nice_name == "Job Salary")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='job_title',
                description='Job Title for which to get salary estimation',
                hint_type='String',
                default_value='Software Engineer',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='location',
                description='Location - Free-text location/area in which to '
                            'get salary estimation',
                hint_type='String',
                default_value='New York, USA',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='radius',
                description='Radius - Search radius in km (measured from '
                            'location). Default: 200.',
                hint_type='String Number',
                default_value='200',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search
        # letscrape | JSearch
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://jsearch.p.rapidapi.com'
                '/search') and
            i.nice_name == "Search")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='query',
                description="""\
Free-form jobs search query. It is highly recommended to include job title \
and location as part of the query, see query examples below.\n \
Query examples\n \
web development in chicago\n\
marketing manager in new york via linkedin\n\
developer in germany 60306\n\
""",
                hint_type='String',
                default_value='Software Engineer in New York City, USA',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='page',
                description="""\
Page to return (each page includes up to 10 results). (i.e. 1-100) (default: 1)\
""",
                hint_type='Number',
                default_value='1',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='num_pages',
                description="""\
Number of pages to return, starting from page. Allowed values: 1-20. Default: 1\
\nNote: requests for more than one page and up to 10 pages are charged x2 and \
requests for more than 10 pages are charged 3x.\
""",
                hint_type='String',
                default_value='1',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='date_posted',
                description="""\
Find jobs posted within the time you specify. \
Allowed values: \
all, \
today, \
3days, \
week, \
month. \
Default: all.
""",
                hint_type='String',
                default_value='all',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='remote_jobs_only',
                description="""\
Find remote jobs only (work from home). \
Allowed values: \
true,\
false,\
Default: empty.\
""",
                hint_type='Boolean String',
                default_value='false',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='employment_types',
                description="""\
Find jobs of particular employment types, specified as a comma delimited list \
of the following values: \
(FULLTIME, \
CONTRACTOR, \
PARTTIME, \
INTERN)
""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='job_requirements',
                description="""\
Find jobs with specific requirements, specified as a comma delimited list of \
the following values: \
(under_3_years_experience, \
more_than_3_years_experience, \
no_experience, \
no_degree)""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='job_titles',
                description="""\
Find jobs with specific job titles - specified as a comma (,) separated list \
of job_titles filter values (i.e. filter value field) as returned by the \
Search Filters endpoint. \n\
Example: job_titles=c2VuaW9y,YXNzb2NpYXRl\
""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='company_types',
                description="""\
Find jobs posted by companies of certain types - specified as a comma (,) \
separated list of company_types filter values (i.e. filter value field) as \
returned by the Search Filters endpoint.\
\n\
Example: company_types=L2J1c2luZXNzL25haWNzMjAwNy81MjpGaW5hbmNl,L2J1c2luZXN\
zL25haWNzMjAwNy81MTpJbmZvcm1hdGlvbg==\
""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='employer',
                description="""\
Find jobs posted by specific employers - specified as a comma (,) separated \
list of employer filter values (i.e. filter value field) as returned by the\
 Search Filters endpoint.\
\
Example: employers=L2cvMTFoMTV4eHhydDpJbmZpbml0eSBDb25zdWx0aW5n,L2cvMTFmMDEzO\
XIxbjpDeWJlckNvZGVycw==\
""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='actively_hiring',
                description="""\
Find jobs at employers that are hiring a lot right now. Default: false.\
""",
                hint_type='Boolean String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='radius',
                description="""\
Return jobs within a certain distance from location as specified as part of \
the query (in km).\
""",
                hint_type='Number',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='exclude_job_publishers',
                description="""\
Exclude jobs published by specific publishers, specified as a comma (,) \
separated list of publishers to exclude.\
\n\
Example: exclude_job_publishers=BeeBe,Dice\
""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='categories',
                description="""\
[Deprecated] Find jobs in specific categories/industries - specified as a comma\
 (,) separated list of categories filter values (i.e. filter value field) as \
returned by the Search Filters endpoint. \
Example: categories=R0MxODpNYW5hZ2VtZW50,R0MwNTpBcnRGYXNoaW9uRGVzaWdu\
""",
                hint_type='String',
                default_value='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Filters
        # letscrape | JSearch
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
                i.http_path == (
                    'https://jsearch.p.rapidapi.com'
                    '/search-filters') and
                i.nice_name == "Search Filters")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='query',
                description="""\
Free-form jobs search query. It is highly recommended to include job title \
and location as part of the query, see query examples below.\n \
Query examples\n \
web development in chicago\n\
marketing manager in new york via linkedin\n\
developer in germany 60306\n\
""",
                hint_type='String',
                default_value='Software Engineer in New York City, USA',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='date_posted',
                description="""\
Find jobs posted within the time you specify. \
Allowed values: \
all, \
today, \
3days, \
week, \
month. \
Default: all.
""",
                hint_type='String',
                default_value='all',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='remote_jobs_only',
                description="""\
Find jobs posted within the time you specify. \
Allowed values: \
true,\
false,\
Default: empty.\
""",
                hint_type='Boolean String',
                default_value='false',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='employment_types',
                description="""\
Find jobs of particular employment types, specified as a comma delimited list \
of the following values: \
(FULLTIME, \
CONTRACTOR, \
PARTTIME, \
INTERN)
""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='job_requirements',
                description="""\
Find jobs with specific requirements, specified as a comma delimited list of \
the following values: \
(under_3_years_experience, \
more_than_3_years_experience, \
no_experience, \
no_degree)\
""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='radius',
                description="""\
Return jobs within a certain distance from location as specified as part of \
the query (in km).\
""",
                hint_type='Number',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='job_titles',
                description="""\
Find jobs with specific job titles - specified as a comma (,) separated list \
of job_titles filter values (i.e. filter value field) as returned by the \
Search Filters endpoint. \n\
Example: job_titles=c2VuaW9y,YXNzb2NpYXRl\
""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='company_types',
                description="""\
Find jobs posted by companies of certain types - specified as a comma (,) \
separated list of company_types filter values (i.e. filter value field) as \
returned by the Search Filters endpoint.\
\n\
Example: company_types=L2J1c2luZXNzL25haWNzMjAwNy81MjpGaW5hbmNl,L2J1c2luZXN\
zL25haWNzMjAwNy81MTpJbmZvcm1hdGlvbg==\
""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='employers',
                description="""\
Employers filter - specified as a comma (,) separated list of employers \
filter values (i.e. filter value field) as returned by a previous call \
to this endpoint.\
\n\
Example: employers= L2cvMTFoMTV4eHhydDpJbmZpbml0eSBDb25zdWx0aW5n,L2cvMTFmMDEzO\
XIxbjpDeWJlckNvZGVycw==\
""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='actively_hiring',
                description="""\
Find jobs at employers that are hiring a lot right now. Default: false.\
""",
                hint_type='Boolean String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='categories',
                description="""\
[Deprecated] Find jobs in specific categories/industries - specified as a comma\
 (,) separated list of categories filter values (i.e. filter value field) as \
returned by the Search Filters endpoint. \
Example: categories=R0MxODpNYW5hZ2VtZW50,R0MwNTpBcnRGYXNoaW9uRGVzaWdu\
""",
                hint_type='String',
                default_value='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Job Details
        # letscrape | JSearch
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://jsearch.p.rapidapi.com'
                '/job-details') and
            i.nice_name == "Job Details")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='job_id',
                description="""\
Job Id of the job for which to get details. Batching of up to 20 Job Ids is \
supported by separating multiple Job Ids by comma (,).\
\n\
Note that each Job Id in a batch request is counted as a request for quota \
calculation.\
""",
                hint_type='String',
                default_value='7oKm_SkxjLxpFtVuAAAAAA==',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='extended_publisher_details',
                description="""\
Return additional publisher details such as website url and favicon.\
""",
                hint_type='Boolean String',
                default_value='False',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Estimated Salary
        # letscrape | JSearch
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://jsearch.p.rapidapi.com'
                '/estimated-salary') and
            i.nice_name == "Estimated Salary")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='job_title',
                description="""\
Job title for which to get salary estimation.\
""",
                hint_type='String',
                default_value='Software Engineer',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='location',
                description="""\
Location in which to get salary estimation.\
""",
                hint_type='String',
                default_value='New-York, NY, USA',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='radius',
                description="""\
Search radius in km (measured from location). Default: 200.\
""",
                hint_type='Number',
                default_value='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Company Search
        # letscrape | Real-Time Glassdoor Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://real-time-glassdoor-data.p.rapidapi.com'
                '/company-search') and
            i.nice_name == "Company Search")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='query',
                description='Search Query or Company ID',
                hint_type='String',
                default_value='Google',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='limit',
                description='Maximum number of results to return (i.e. 1-100).',
                hint_type='Number',
                default_value='100',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Company Reviews
        # letscrape | Real-Time Glassdoor Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://real-time-glassdoor-data.p.rapidapi.com'
                '/company-reviews') and
            i.nice_name == "Company Reviews")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='company_id',
                description='Company ID',
                hint_type='Number',
                default_value='9079',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='page',
                description='The reviews page to return (Each page includes '
                            'up to 10 results).',
                hint_type='Number',
                default_value='1',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='sort',
                description='Return reviews in a specific sort '
                            'order. '
                            '(i.e. POPULAR, '
                            'MOST_RECENT, '
                            'HIGHEST_RATING, '
                            'LOWEST_RATING)',
                hint_type='String',
                default_value='MOST_RECENT',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='query',
                description='Return reviews matching a search query',
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='language',
                description='Return reviews written in a specific language. '
                            '(i.e. en, fr, nl, de, pt, es, it)',
                hint_type='String',
                default_value='en',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='employment_statuses',
                description='Return reviews written by employees with a '
                            'specific job type. Multiple values can be '
                            'specified as a comma delimited list of the '
                            'following values: REGULAR, INTERN, PART_TIME, '
                            'CONTRACT, FREELANCE. '
                            '(e.g. REGULAR, '
                            'CONTRACT, '
                            'FREELANCE)',
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='only_current_employees',
                description='Only return reviews written by current '
                            'employees (at the time of writing). '
                            '(e.g. true, false, empty),',
                hint_type='Boolean String',
                default_value='false',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='extended_rating_data',
                description='Include extended company rating data such as '
                            'rating breakdown and rating distributions.',
                hint_type='Boolean String',
                default_value='false',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Company Overview
        # letscrape | Real-Time Glassdoor Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://real-time-glassdoor-data.p.rapidapi.com'
                '/company-overview') and
            i.nice_name == "Company Overview")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='company_id',
                description='Company ID',
                hint_type='Number',
                default_value='1138',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get User Detail
        # Lundehund | Twitter X Job API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://twitter-x-api.p.rapidapi.com'
                '/api/user/detail') and
            i.nice_name == 'Get User Detail')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='username',
                description='Username',
                hint_type='String',
                default_value='taylorswift13',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get User Followers
        # Lundehund | Twitter X Job API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://twitter-x-api.p.rapidapi.com'
                '/api/user/followers') and
            i.nice_name == 'Get User Followers')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='user_id',
                description='User ID',
                hint_type='String',
                default_value='17919972',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='count',
                description='Count',
                hint_type='Number',
                default_value='20',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='cursor',
                description='Cursor',
                hint_type='String',
                default_value='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get User Verified Followers
        # Lundehund | Twitter X Job API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://twitter-x-api.p.rapidapi.com'
                '/api/user/followers/blue-verified') and
            i.nice_name == 'Get User Verified Followers')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='user_id',
                description='User ID',
                hint_type='String',
                default_value='17919972',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='count',
                description='Count',
                hint_type='Number',
                default_value='20',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='cursor',
                description='Cursor',
                hint_type='String',
                default_value='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get User Following
        # Lundehund | Twitter X Job API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://twitter-x-api.p.rapidapi.com'
                '/api/user/following') and
            i.nice_name == 'Get User Following')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='user_id',
                description='User ID',
                hint_type='String',
                default_value='44196397',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='count',
                description='Count',
                hint_type='Number',
                default_value='20',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='cursor',
                description='Cursor',
                hint_type='String',
                default_value='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get User Subscriptions
        # Lundehund | Twitter X Job API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://twitter-x-api.p.rapidapi.com'
                '/api/user/subscriptions') and
            i.nice_name == 'Get User Subscriptions')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='user_id',
                description='User ID',
                hint_type='String',
                default_value='44196397',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='count',
                description='Count',
                hint_type='Number',
                default_value='20',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='cursor',
                description='Cursor',
                hint_type='String',
                default_value='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get User Tweets
        # Lundehund | Twitter X Job API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://twitter-x-api.p.rapidapi.com'
                '/api/user/tweets') and
            i.nice_name == 'Get User Tweets')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='user_id',
                description='User ID',
                hint_type='String',
                default_value='17919972',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='count',
                description='Count',
                hint_type='Number',
                default_value='20',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='cursor',
                description='Cursor',
                hint_type='String',
                default_value='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get User Medias
        # Lundehund | Twitter X Job API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://twitter-x-api.p.rapidapi.com'
                '/api/user/medias') and
            i.nice_name == 'Get User Medias')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='user_id',
                description='User ID',
                hint_type='String',
                default_value='44196397',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='count',
                description='Count',
                hint_type='Number',
                default_value='20',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='cursor',
                description='Cursor',
                hint_type='String',
                default_value='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get User Likes
        # Lundehund | Twitter X Job API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://twitter-x-api.p.rapidapi.com'
                '/api/user/likes') and
            i.nice_name == 'Get User Likes')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='user_id',
                description='User ID',
                hint_type='String',
                default_value='44196397',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='count',
                description='Count',
                hint_type='Number',
                default_value='20',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='cursor',
                description='Cursor',
                hint_type='String',
                default_value='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get User Highlights
        # Lundehund | Twitter X Job API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://twitter-x-api.p.rapidapi.com'
                '/api/user/highlights') and
            i.nice_name == 'Get User Highlights')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='user_id',
                description='User ID',
                hint_type='String',
                default_value='44196397',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='count',
                description='Count',
                hint_type='Number',
                default_value='20',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='cursor',
                description='Cursor',
                hint_type='String',
                default_value='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Tweet Detail
        # Lundehund | Twitter X Job API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://twitter-x-api.p.rapidapi.com'
                '/api/tweet/detail') and
            i.nice_name == 'Get Tweet Detail')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='tweet_id',
                description='Tweet ID',
                hint_type='String',
                default_value='1781171613058097619',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Tweet Retweeters
        # Lundehund | Twitter X Job API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://twitter-x-api.p.rapidapi.com'
                '/api/tweet/retweeters') and
            i.nice_name == 'Get Tweet Retweeters')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='tweet_id',
                description='Tweet ID',
                hint_type='String',
                default_value='1781171613058097619',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='count',
                description='Count',
                hint_type='Number',
                default_value='20',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='cursor',
                description='Cursor',
                hint_type='String',
                default_value='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Tweet Retweets
        # Lundehund | Twitter X Job API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://twitter-x-api.p.rapidapi.com'
                '/api/tweet/quotes') and
            i.nice_name == 'Get Tweet Retweets')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='tweet_id',
                description='Tweet ID',
                hint_type='String',
                default_value='1781171613058097619',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='count',
                description='Count',
                hint_type='Number',
                default_value='20',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='cursor',
                description='Cursor',
                hint_type='String',
                default_value='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Tweet Likes
        # Lundehund | Twitter X Job API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://twitter-x-api.p.rapidapi.com'
                '/api/tweet/likes') and
            i.nice_name == 'Get Tweet Likes')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='tweet_id',
                description='Tweet ID',
                hint_type='String',
                default_value='1781171613058097619',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='count',
                description='Count',
                hint_type='Number',
                default_value='20',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='cursor',
                description='Cursor',
                hint_type='String',
                default_value='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Tweet Hidden Replies
        # Lundehund | Twitter X Job API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://twitter-x-api.p.rapidapi.com'
                '/api/tweet/hidden-replies') and
            i.nice_name == 'Get Tweet Hidden Replies')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='tweet_id',
                description='Tweet ID',
                hint_type='String',
                default_value='1795855230661439926',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='count',
                description='Count',
                hint_type='Number',
                default_value='20',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='cursor',
                description='Cursor',
                hint_type='String',
                default_value='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Top
        # Lundehund | Twitter X Job API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://twitter-x-api.p.rapidapi.com'
                '/api/search/top') and
            i.nice_name == 'Search Top')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='keyword',
                description='Keyword',
                hint_type='String',
                default_value='crypto',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='count',
                description='Count',
                hint_type='Number',
                default_value='20',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='cursor',
                description='Cursor',
                hint_type='String',
                default_value='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Latest
        # Lundehund | Twitter X Job API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://twitter-x-api.p.rapidapi.com'
                '/api/search/latest') and
            i.nice_name == 'Search Latest')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='keyword',
                description='Keyword',
                hint_type='String',
                default_value='Software Engineer Jobs',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='count',
                description='Count',
                hint_type='Number',
                default_value='20',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='cursor',
                description='Cursor',
                hint_type='String',
                default_value='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search People
        # Lundehund | Twitter X Job API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://twitter-x-api.p.rapidapi.com'
                '/api/search/people') and
            i.nice_name == 'Search People')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='keyword',
                description='Keyword',
                hint_type='String',
                default_value='crypto',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='count',
                description='Count',
                hint_type='Number',
                default_value='20',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='cursor',
                description='Cursor',
                hint_type='String',
                default_value='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Media
        # Lundehund | Twitter X Job API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://twitter-x-api.p.rapidapi.com'
                '/api/search/media') and
            i.nice_name == 'Search Media')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='keyword',
                description='Keyword',
                hint_type='String',
                default_value='crypto',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='count',
                description='Count',
                hint_type='Number',
                default_value='20',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='cursor',
                description='Cursor',
                hint_type='String',
                default_value='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Lists
        # Lundehund | Twitter X Job API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://twitter-x-api.p.rapidapi.com'
                '/api/search/lists') and
            i.nice_name == 'Search Lists')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='keyword',
                description='Keyword',
                hint_type='String',
                default_value='crypto',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='count',
                description='Count',
                hint_type='Number',
                default_value='20',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='cursor',
                description='Cursor',
                hint_type='String',
                default_value='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get List Tweets
        # Lundehund | Twitter X Job API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://twitter-x-api.p.rapidapi.com'
                '/api/list/tweets') and
            i.nice_name == 'Get List Tweets')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='list_id',
                description='List ID',
                hint_type='String',
                default_value='1590828215161036815',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='count',
                description='Count',
                hint_type='Number',
                default_value='20',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='cursor',
                description='Cursor',
                hint_type='String',
                default_value='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get List Followers
        # Lundehund | Twitter X Job API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://twitter-x-api.p.rapidapi.com'
                '/api/list/followers') and
            i.nice_name == 'Get List Followers')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='list_id',
                description='List ID',
                hint_type='String',
                default_value='1590828215161036815',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='count',
                description='Count',
                hint_type='Number',
                default_value='20',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='cursor',
                description='Cursor',
                hint_type='String',
                default_value='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get List Member
        # Lundehund | Twitter X Job API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://twitter-x-api.p.rapidapi.com'
                '/api/list/member') and
            i.nice_name == 'Get List Member')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='list_id',
                description='List ID',
                hint_type='String',
                default_value='1590828215161036815',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='count',
                description='Count',
                hint_type='Number',
                default_value='20',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='cursor',
                description='Cursor',
                hint_type='String',
                default_value='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Job Detail
        # Lundehund | Twitter X Job API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://twitter-x-api.p.rapidapi.com'
                '/api/job/detail') and
            i.nice_name == 'Get Job Detail')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='job_id',
                description='Job ID',
                hint_type='String',
                default_value='1795659227551375360',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Job
        # Lundehund | Twitter X Job API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://twitter-x-api.p.rapidapi.com'
                '/api/job/search') and
            i.nice_name == 'Search Job')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='keyword',
                description='Keyword',
                hint_type='String',
                default_value='Software Engineer',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='count',
                description='Count',
                hint_type='String',
                default_value='25',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='count',
                description='Count',
                hint_type='Number',
                default_value='20',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='location_id',
                description='Location ID',
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='job_location_type',
                description='Job Location Type',
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='seniority_level',
                description='Seniority Level',
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='employment_type',
                description='Employment Type',
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='company_name',
                description='Company Name',
                hint_type='String',
                default_value='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Location
        # Lundehund | Twitter X Job API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://twitter-x-api.p.rapidapi.com'
                '/api/job/search/location') and
            i.nice_name == 'Search Location')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='query',
                description='Query',
                hint_type='String',
                default_value='New York',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Company Details
        # mantiks | Glassdoor
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://glassdoor.p.rapidapi.com'
                '/company/') and
            i.nice_name == 'Company Details')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='company_id',
                description='Company ID - Use company search endpoint to '
                            'look for IDs',
                hint_type='Number',
                default_value='1651',
                path_param=True,
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Companies Search
        # mantiks | Glassdoor
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://glassdoor.p.rapidapi.com'
                '/companies/search') and
            i.nice_name == 'Companies Search')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='company_name',
                description='Company Name',
                hint_type='String',
                default_value='Google',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Job details
        # mantiks | Glassdoor
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://glassdoor.p.rapidapi.com'
                '/job/') and
            i.nice_name == 'Job details')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='job_id',
                description='Use Jobs Search endpoint to retrieve IDs',
                hint_type='String',
                default_value='',
                path_param=True,
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Jobs Search
        # mantiks | Glassdoor
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://glassdoor.p.rapidapi.com'
                '/jobs/search') and
            i.nice_name == 'Jobs Search')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='keyword',
                description='Keyword used to search jobs, could be job '
                            'title or any specific word',
                hint_type='String',
                default_value='Software Engineer',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='location_id',
                description="""\
Glassdoor's locations are represented by ID/Type. Those tuple could be found we\
 a locations search (see relation endpoint)""",
                hint_type='Number',
                default_value='1128808',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='location_type',
                description="""\
Glassdoor's locations are represented by ID/Type. The tuple could be found 
from a locations search (see relation endpoint). Here is the meaning of each 
value C: CITY, N: COUNTRY, M: METRO, S: STATE (Single capital letter only)\
""",
                hint_type='String',
                default_value='C',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='page_id',
                description='Default page_id is 0 (first page). Each page '
                            'return at most 30 jobs. You need to specify the '
                            'page_cursor for all page greater than 1',
                hint_type='Number',
                default_value='0',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='page_cursor',
                description='For all page_id greater than 1, you need to '
                            'specify this parameter. Each page provide the '
                            'page_cursor of the next page_id in its payload',
                hint_type='String',
                default_value='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Locations Search
        # mantiks | Glassdoor
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://glassdoor.p.rapidapi.com'
                '/locations/search') and
            i.nice_name == 'Locations Search')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='location_name',
                description='Location',
                hint_type='String',
                default_value='New York',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Job Details
        # mantiks | Indeed
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://indeed12.p.rapidapi.com'
                '/job/') and
            i.nice_name == 'Job details')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='locality',
                description="""\
Select the Indeed's country. Each value correspond to a specific indeed subdoma\
in. Default value if missing is 'us'\n
(e.g. us, ae, at, be, bh, ch, ch-fr, cz, de, dk, eg, es, fi, fr, gb, gr, hu, ie\
, il, in, it, kw, lu, ma, ng, nl, no, om, pk, pl, pt, qa, ro, ru, sa, se, tr, \
ua, za, au, ca, nz, id, ph, do not include\
""",
                hint_type='String',
                default_value='us',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='job_id',
                description="You can retrieve jobs ids from on jobs searches",
                hint_type='String',
                default_value='02eb3a9f080f10e7',
                path_param=True,
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Jobs Search
        # mantiks | Indeed
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://indeed12.p.rapidapi.com'
                '/jobs/search') and
            i.nice_name == 'Jobs Search')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='query',
                description='Keyword used to search jobs',
                hint_type='String',
                default_value='Software Engineer',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='location',
                description='Location',
                hint_type='String',
                default_value='New York',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='page_id',
                description='Page ID - Use to control the pagination of results'
                            '. If omitted return the first page',
                hint_type='Number',
                default_value='1',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='locality',
                description="""\
Select the Indeed's country. Each value correspond to a specific indeed subdoma\
in. Default value if missing is 'us'\n\
(e.g. us, ae, at, be, bh, ch, ch-fr, cz, de, dk, eg, es, fi, fr, gb, gr, hu, ie\
, il, in, it, kw, lu, ma, ng, nl, no, om, pk, pl, pt, qa, ro, ru, sa, se, tr, \
ua, za, au, ca, nz, id, ph, do not include\
""",
                hint_type='String',
                default_value='us',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='fromage',
                description="""\
Number of days. Filter jobs that was updated between now and fromage days.\
(e.g. 1, 3, 7, 14, do not include)\
""",
                hint_type='Number',
                default_value='1',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='radius',
                description="radius in km. Filter jobs that are in the given "
                            "radius",
                hint_type='Number',
                default_value='50',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='sort',
                description="""\
Sort results. Currently only support by 'date' to get the newest jobs. If null,\
 results are sorted by relevance\
(e.g.) date, do not include\
""",
                hint_type='String',
                default_value='date',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Company details
        # mantiks | Indeed
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://indeed12.p.rapidapi.com'
                '/company/') and
            i.nice_name == 'Company details')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='locality',
                description="""\
Select the Indeed's country. Each value correspond to a specific indeed subdoma\
in. Default value if missing is 'us'\n\
(e.g. us, ae, at, be, bh, ch, ch-fr, cz, de, dk, eg, es, fi, fr, gb, gr, hu, ie\
, il, in, it, kw, lu, ma, ng, nl, no, om, pk, pl, pt, qa, ro, ru, sa, se, tr, \
ua, za, au, ca, nz, id, ph, do not include\
""",
                hint_type='String',
                default_value='us',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='company_id',
                description='Company Name',
                hint_type='String',
                default_value='Google',
                path_param=True,
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Company Search
        # mantiks | Indeed
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://indeed12.p.rapidapi.com'
                '/companies/search') and
            i.nice_name == 'Company Search')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='company_name',
                description='Company Name',
                hint_type='String',
                default_value='Google',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='locality',
                description="""\
Select the Indeed's country. Each value correspond to a specific indeed subdoma\
in. Default value if missing is 'us'\n\
(e.g. us, ae, at, be, bh, ch, ch-fr, cz, de, dk, eg, es, fi, fr, gb, gr, hu, ie\
, il, in, it, kw, lu, ma, ng, nl, no, om, pk, pl, pt, qa, ro, ru, sa, se, tr, \
ua, za, au, ca, nz, id, ph, do not include\
""",
                hint_type='String',
                default_value='us',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Company Jobs
        # mantiks | Indeed
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://indeed12.p.rapidapi.com'
                '/company/') and
            i.nice_name == 'Company jobs')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='locality',
                description="""\
Select the Indeed's country. Each value correspond to a specific indeed subdoma\
in. Default value if missing is 'us'\n\
(e.g. us, ae, at, be, bh, ch, ch-fr, cz, de, dk, eg, es, fi, fr, gb, gr, hu, ie\
, il, in, it, kw, lu, ma, ng, nl, no, om, pk, pl, pt, qa, ro, ru, sa, se, tr, \
ua, za, au, ca, nz, id, ph, do not include\
""",
                hint_type='String',
                default_value='us',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='start',
                description='Page ID - Use to control the pagination of results'
                            '. If omitted return the first page',
                hint_type='Number',
                default_value='1',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='company_id',
                description='Company Name',
                hint_type='String',
                default_value='Google',
                path_param=True,
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Person Posts (WITH PAGINATION)
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/profile_updates') and
            i.nice_name == "Person Posts ( WITH PAGINATION )")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='profile_url',
                description='LinkedIn Profile URL',
                hint_type='URL',
                default_value='https://www.linkedin.com/in/ingmar-klein',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='page',
                description='Page Number',
                hint_type='Number',
                default_value='1',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='reposts',
                description='Reposts Number',
                hint_type='Number',
                default_value='1',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='comments',
                description='Comments Number',
                hint_type='Number',
                default_value='1',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='paginationToken',
                description='Pagination Token',
                hint_type='String',
                default_value='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Company Posts (WITH PAGINATION) /company_updates
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/company_updates') and
            i.nice_name == "Company Posts ( WITH PAGINATION ) "
                           "/company_updates")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='company_url',
                description='LinkedIn Company Profile URL',
                hint_type='URL',
                default_value='https://www.linkedin.com/company/huzzle-app',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='page',
                description='Page #',
                hint_type='Number',
                default_value='1',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='reposts',
                description='Reposts #',
                hint_type='Number',
                default_value='2',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='comments',
                description='Comments #',
                hint_type='Number',
                default_value='2',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Company Employee
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/company_employee') and
            i.nice_name == "Company Employee")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='page',
                description='Page #',
                hint_type='Number',
                default_value='1',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='companyId',
                description='LinkedIn Company ID',
                hint_type='String',
                default_value='1441',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='keywords',
                description='Keywords',
                hint_type='String',
                default_value='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Filter Function Suggestions
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/filter_function_suggestions') and
            i.nice_name == "Filter Function Suggestions")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='query',
                description='Query',
                hint_type='String',
                default_value='',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Filter Job Title Suggestions
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/filter_job_title_suggestions') and
            i.nice_name == "Filter Job Title Suggestions")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='query',
                description='Query',
                hint_type='String',
                default_value='Software Engineer',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Filter Company Suggestions
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/filter_company_suggestions') and
            i.nice_name == "Filter Company Suggestions")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='query',
                description='Query',
                hint_type='String',
                default_value='Google',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Filter Search Suggestions
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/filter_search_suggestions') and
            i.nice_name == "Filter Search Suggestions")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='query',
                description='Query',
                hint_type='String',
                default_value='Paul',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Filter Geography Location Suggestions
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/filter_geography_location_suggestions') and
            i.nice_name == "Filter Geography Location Suggestions")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='query',
                description='Query',
                hint_type='String',
                default_value='United States',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Filter Industry Suggestions
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/filter_industry_suggestions') and
            i.nice_name == "Filter Industry Suggestions")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='query',
                description='Query',
                hint_type='String',
                default_value='In',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Filter School Suggestions
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/filter_school_suggestions') and
            i.nice_name == "Filter School Suggestions")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='query',
                description='Query',
                hint_type='String',
                default_value='Uni',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Jobs (with filters)
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/search_jobs') and
            i.nice_name == "Search Jobs ( with filters )" and
            i.http_method == "GET")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='query',
                description='Query',
                hint_type='String',
                default_value='Software Engineer',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='location',
                description='Location',
                hint_type='String',
                default_value='United States',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='page',
                description='Page Number',
                hint_type='Number',
                default_value='1',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='easyApply',
                description='Easy Apply (i.e. true or false)',
                hint_type='Boolean String',
                default_value='false',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='experience',
                description='''\
experience : experience refers to the experience level required for a specific\
 job. It could be one or more of (1, 2, 3, 4, 5, 6). 1 = Internship, 2 = Entry \
level, 3 = Associate, 4 = Mid senior level, 5=Director, 6=Executive. For \
example experience=2,5 means experience=Entry level,Director\
''',
                hint_type='String',
                default_value='2',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='jobType',
                description='''\
jobType : Linkedin Job Type filter. It could one or more of F,P,C,T,V,I,O. \
F=Full time, P=Part time, C=Contract, T=Temporary, V=Volunteer, I=Internship,\
 O=Other.\
''',
                hint_type='String',
                default_value='F',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='postedAgo',
                description='''\
postedAgo : Time jobs was posted ago. It should be in seconds. e.g \
postedAgo=3600 means all jobs from past 1 hour and so on.\
''',
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='workplaceType',
                description='''\
workplaceType - No Description\
''',
                hint_type='String',
                default_value='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Suggestion Service Category
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/suggestion_service_catagory') and
            i.nice_name == "Suggestion Service Category")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='query',
                description='Query',
                hint_type='String',
                default_value='Ad',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Suggestion School
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/suggestion_school') and
            i.nice_name == "Suggestion School")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='query',
                description='Query',
                hint_type='String',
                default_value='Uni',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Suggestion Company
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/suggestion_company') and
            i.nice_name == "Suggestion Company")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='query',
                description='Query',
                hint_type='String',
                default_value='App',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Suggestion Industry
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/suggestion_industry') and
            i.nice_name == "Suggestion Industry")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='query',
                description='Query',
                hint_type='String',
                default_value='Ad',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Suggestion Location
        # mgujjargamingm | LinkedIn Data Scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-scraper.p.rapidapi.com'
                '/suggestion_location') and
            i.nice_name == "Suggestion Location")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='query',
                description='Query',
                hint_type='String',
                default_value='United States',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Jobs
        # mgujjargamingm | Linkedin BULK data scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-bulk-data-scraper.p.rapidapi.com'
                '/search_jobs') and
            i.nice_name == "Search Jobs" and
            i.http_method == "GET")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='query',
                description='Query',
                hint_type='String',
                default_value='Software Engineer',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='page',
                description='Page Number',
                hint_type='String',
                default_value='1',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='searchLocationId',
                description='''\
Details: https://rapidapi.com/mgujjargamingm/api/linkedin-data-scraper/\
tutorials/search-jobs-with-filters-(-get-endpoint-)''',
                hint_type='String',
                default_value='103644278',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='easyApply',
                description='Either True or False',
                hint_type='Boolean String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='experience',
                description='''\
experience refers to the experience level required for a specific job. \
It could be one or more of (1,2,3,4,5,6). \
1 = Internship, \
2 = Entry level, \
3 = Associate, \
4 = Mid senior level, \
5=Director, \
6=Executive. \
For example experience=2,5 means experience=Entry level,Director''',
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='jobType',
                description='''\
jobType : Linkedin Job Type filter. It could one or more of F,P,C,T,V,I,O. \
F=Full time, P=Part time, C=Contract, T=Temporary, V=Volunteer, I=Internship, \
O=Other.\
For example experience=2,5 means experience=Entry level,Director''',
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='postedAgo',
                description='''\
Time jobs was posted ago. It should be in seconds. \
e.g postedAgo=3600 means all jobs from past 1 hour and so on.\
 Default time: 1 month = 2,629,746 seconds''',
                hint_type='String',
                default_value='2629746',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='workplaceType',
                description='''\
It could be one more of 1,2,3. 1=On-Site, 2=Remote, 3=Hybrid''',
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='sortBy',
                description='''\
Could be either DD ( most recent ) or R ( most relevant )''',
                hint_type='String',
                default_value='most recent',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='companyIdsList',
                description='''\
List of companies id separated by comma. \
To find a company's id using keyword, Note : "urn" is the id \
https://rapidapi.com/mgujjargamingm/api/linkedin-bulk-data-scraper/\
playground/apiendpoint_4a836c00-f4fa-45ef-93c0-bc0c60b67448''',
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='industryIdsList',
                description='''\
List of industries separated by comma. \
To find a industry's id using keyword,Follow this. Note : "urn" is the id\
https://rapidapi.com/mgujjargamingm/api/linkedin-bulk-data-scraper/\
playground/apiendpoint_e91c6b16-8496-49e4-98ec-2ab6ac15abc6''',
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='functionIdsList',
                description='''\
List of funtions separated by comma. \
To find a funtion's id using keyword,Follow this. Note : "urn" is the id\
https://rapidapi.com/mgujjargamingm/api/linkedin-bulk-data-scraper/\
playground/apiendpoint_d8327853-8c23-484d-b422-119f8e089a5c''',
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='titleIdsList',
                description='''\
List of job titles separated by comma. \
To find a job title's id using keyword, Follow this. Note : "urn" is the id\
https://rapidapi.com/mgujjargamingm/api/linkedin-data-scraper/\
playground/apiendpoint_c5ab8f19-3d68-4663-a5ad-1a5dcf2cc578''',
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='locationIdsList',
                description='''\
List of location ids of cities/states of specified searchLocationId country. \
To get the ids of cities/states using keywords, \
Follow this. Note : "urn" is the id\
https://rapidapi.com/mgujjargamingm/api/linkedin-bulk-data-scraper/\
playground/apiendpoint_d037e73e-d19a-4f3b-8ae8-d3b9b00f6df0''',
                hint_type='String',
                default_value='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Job Details
        # mgujjargamingm | Linkedin BULK data scraper
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-bulk-data-scraper.p.rapidapi.com'
                '/job_details') and
            i.nice_name == "Job Details" and
            i.http_method == "GET")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='jobPostingUrn',
                description='Job Posting URN (ID)',
                hint_type='String',
                default_value='3887887137',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get all freelancers in specific page
        # omarmohamed0 | Jobs API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://freelancer-api.p.rapidapi.com'
                '/find-freelancers/') and
            i.nice_name == 'Get all freelancers in specific page')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='page_number',
                description='Page Number',
                hint_type='String',
                default_value='1',
                path_param=True,
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get all jobs in specific page
        # omarmohamed0 | Jobs API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://freelancer-api.p.rapidapi.com'
                '/api/find-job/') and
            i.nice_name == 'Get all jobs in specific page')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='page_number',
                description='Page #',
                hint_type='String',
                default_value='1',
                path_param=True,
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # List Jobs
        # Pat92 | Jobs API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://jobs-api14.p.rapidapi.com'
                '/list') and
            i.nice_name == "List Jobs")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='query',
                description='Search Query - Keywords, Job Title, Company Name '
                            'or any other relevant search-query.',
                hint_type='String',
                default_value='Software Engineer',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='location',
                description='Location - City, country, or any other locations.',
                hint_type='String',
                default_value='United States',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='distance',
                description='Distance (i.e. -1.0 Distance to the '
                            'location in kilometers)',
                hint_type='Decimal',
                default_value='-1.0',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='language',
                description="""\
Sets the language of the following return fields (location, employmentType, \
datePosted and salaryRange), but does not filter by language.
Important: If you want the values in english, either don't use this field or \
use 'en_GB', other variants will not work.\
""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='remoteOnly',
                description='Remote Only? Filter by only remote job postings.',
                hint_type='Boolean String',
                default_value='false',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='datePosted',
                description='Date Posted - Only receive job postings that are '
                            'newer than the date given, takes all job postings '
                            'if not set. (i.e. month, week, today, 3days)',
                hint_type='String',
                default_value='month',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='employmentTypes',
                description='Employment Types: Only receive job postings with '
                            'the specific employment types. You can use '
                            'multiple types and separate them with semicolons '
                            '(parttime;internship) (i.e. '
                            'fulltime;parttime;intern;contractor)',
                hint_type='String',
                default_value='fulltime',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='allowedJobProviders',
                description='Allowed Job Providers - Only receive job postings '
                            'from specific job-providers. You can use multiple '
                            'providers and separate them with semicolons '
                            '(i.e. ziprecruiter;indeed;linkedin) '
                            'Note: It currently works only with bigger '
                            'providers like indeed, linkedin, etc.',
                hint_type='String CSV',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='index',
                description='Index of the search, per request you will get a '
                            'maximum of 10 jobs. If you have received a total '
                            'of 10 jobs, you can increase the index by 1 to get'
                            ' the next results.',
                hint_type='Number',
                default_value='0',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Salary Range
        # Pat92 | Jobs API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://jobs-api14.p.rapidapi.com'
                '/salary/getSalaryRange') and
            i.nice_name == "Get salary range")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='jobTitle',
                description='Job Title - The job title you want the salary '
                            'range from. use Get job titles for valid titles.',
                hint_type='String',
                default_value='Software Engineer',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='countryCode',
                description='Country Code - The country you want the salary '
                            'range from. (i.e DE, US, CH)',
                hint_type='String',
                default_value='US',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Job Titles
        # Pat92 | Jobs API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://jobs-api14.p.rapidapi.com'
                '/salary/getJobTitles') and
            i.nice_name == "Get job titles")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='query',
                description='Find job titles from your query to use in Get '
                            'salary range',
                hint_type='String',
                default_value='Software Engineer',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='countryCode',
                description='Find job titles for a specific country. '
                            '(i.e. DE, US, CH)',
                hint_type='String',
                default_value='US',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # list_jobs_jobs_get
        # qurazor1 | Remoote Job Search
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://remoote-job-search1.p.rapidapi.com'
                '/remoote/jobs') and
            i.nice_name == "list_jobs_jobs_get")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='search_id',
                description='Search ID (?)',
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='exclude_skill_ids',
                description="Exclude Skill ID's",
                hint_type='Array',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='skill_ids',
                description="Skill ID's",
                hint_type='Array',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='titles',
                description='Titles',
                hint_type='Array',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='limit',
                description='Limit',
                hint_type='Number',
                default_value='10',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='country_id',
                description='Country ID '
                            '(i.e. '
                            'US: 236, '
                            'Canada: 41, '
                            'United Kingdom: 235'
                            ')',
                hint_type='Number',
                default_value='236',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
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
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='id',
                description='id',
                hint_type='Number',
                default_value='',
                path_param=True,
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # get_job_jobs__int_id__get
        # qurazor1 | Remoote Job Search
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://remoote-job-search1.p.rapidapi.com'
                '/remoote/jobs/') and
            i.nice_name == "get_job_jobs__int_id__get")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='id',
                description='id',
                hint_type='Number',
                default_value='',
                path_param=True,
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Token
        # Relu Consultancy | Arbeitsagentur
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://arbeitsagentur-employement-agency.p.rapidapi.com'
                '/get-token') and
            i.nice_name == "Get Token")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='email',
                description='Email',
                hint_type='String',
                default_value='',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Jobs
        # Relu Consultancy | Arbeitsagentur
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://arbeitsagentur-employement-agency.p.rapidapi.com'
                '/search') and
            i.nice_name == "Search Jobs")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='token',
                description='Token from Step 1',
                hint_type='String',
                default_value='',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='keyword',
                description='Keyword',
                hint_type='String',
                default_value='Software Engineer',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='location',
                description='Location',
                hint_type='String',
                default_value='United States',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='radius',
                description='Radius (i.e. 10)',
                hint_type='Number',
                default_value='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Token
        # Relu Consultancy | Indeed Scraper API - Germany
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://indeed-scraper-api-germany.p.rapidapi.com'
                '/get-token') and
            i.nice_name == "Get Token")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='email',
                description='Email',
                hint_type='String',
                default_value='',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Jobs
        # Relu Consultancy | Indeed Scraper API - Germany
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://indeed-scraper-api-germany.p.rapidapi.com'
                '/search') and
            i.nice_name == "Search Jobs")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='token',
                description='Token from Step 1',
                hint_type='String',
                default_value='',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='keyword',
                description='Keyword',
                hint_type='String',
                default_value='Software Engineer',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='location',
                description='Location',
                hint_type='String',
                default_value='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Job View
        # Relu Consultancy | Indeed Scraper API - Germany
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://indeed-scraper-api-germany.p.rapidapi.com'
                '/jobview') and
            i.nice_name == "Job View")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='token',
                description='Token from Step 1',
                hint_type='String',
                default_value='',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='jobkey',
                description='Job Key',
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='joburl',
                description='Job URL',
                hint_type='String',
                default_value='',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Employees
        # RockAPIs | Linkedin API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-api8.p.rapidapi.com'
                '/search-employees') and
            i.nice_name == "Search Employees")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='companyId',
                description='Company ID',
                hint_type='String',
                default_value='1441',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='start',
                description='Start (i.e. 0, 25, 50, 75, 100, etc.)',
                hint_type='String',
                default_value='0',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Company Details
        # RockAPIs | Linkedin API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-api8.p.rapidapi.com'
                '/get-company-details') and
            i.nice_name == "Get Company Details")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='username',
                description='Username',
                hint_type='String',
                default_value='google',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Company By Domain (BETA)
        # RockAPIs | Linkedin API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-api8.p.rapidapi.com'
                '/get-company-by-domain') and
            i.nice_name == "Get Company By Domain (BETA)")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='domain',
                description='Domain',
                hint_type='String',
                default_value='google.com',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Company Insights [PREMIUM] (Beta)
        # RockAPIs | Linkedin API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-api8.p.rapidapi.com'
                '/get-company-insights') and
            i.nice_name == "Get Company Insights [PREMIUM] (Beta)")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='username',
                description='Username',
                hint_type='String',
                default_value='google',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Company Jobs Count
        # RockAPIs | Linkedin API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-api8.p.rapidapi.com'
                '/get-company-jobs-count') and
            i.nice_name == "Get Company Jobs Count")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='companyId',
                description='Company ID',
                hint_type='String',
                default_value='1441',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Company Pages People Also Viewed
        # RockAPIs | Linkedin API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-api8.p.rapidapi.com'
                '/get-company-pages-people-also-viewed') and
            i.nice_name == "Get Company Pages People Also Viewed")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='username',
                description='Username',
                hint_type='String',
                default_value='google',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Company's Post
        # RockAPIs | Linkedin API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-api8.p.rapidapi.com'
                '/get-company-posts') and
            i.nice_name == "Get Company's Post")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='username',
                description='Username',
                hint_type='String',
                default_value='google',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Company Post Comments
        # RockAPIs | Linkedin API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-api8.p.rapidapi.com'
                '/get-company-post-comments') and
            i.nice_name == "Get Company Post Comments")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='urn',
                description='Post URN Value',
                hint_type='String',
                default_value='7179144327430844416',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='sort',
                description='Sort - it could be one of these'
                            ' (i.e. mostRelevant, mostRecent)',
                hint_type='String',
                default_value='mostRecent',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Job Details
        # RockAPIs | Linkedin API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-api8.p.rapidapi.com'
                '/get-job-details') and
            i.nice_name == "Get Job Details")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='id',
                description='ID',
                hint_type='String',
                default_value='3738360408',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Jobs
        # RockAPIs | Linkedin API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-api8.p.rapidapi.com'
                '/search-jobs') and
            i.nice_name == "Search Jobs")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='keywords',
                description='Keywords',
                hint_type='String',
                default_value='Software Engineer',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='locationId',
                description="""Location ID \
https://rapidapi.com/rockapis-rockapis-default/api/linkedin-api8/tutorials/how\
-to-find-a-location-id-on-linkedin%3F""",
                hint_type='Number',
                default_value='103644278',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='companyIds',
                description="Company ID's"
                            "https://rapidapi.com/rockapis-rockapis-default"
                            "/api/linkedin-api8/tutorials/how-to-find-a-com"
                            "pany-id-on-linkedin%3F",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='datePosted',
                description="""Date Posted - it could be one of these: \
(i.e. anyTime, pastMonth, pastWeek, past24Hours)""",
                hint_type='String',
                default_value='anyTime',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='salary',
                description="""Salary \
(i.e. 40k+, 60k+, \
80k+, 100k+, 120k+, \
140k+, 160k+, 180k+, \
200k+ (i.e. 80k+))""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='jobType',
                description="""Job Type - it could be one of these: \
fullTime, partTime, contract, internship (i.e. contract)""",
                hint_type='String',
                default_value='fullTime',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='experienceLevel',
                description="""Experience Level: \
internship, associate, director, entryLevel, midSeniorLevel. executive \
(i.e. executive)""",
                hint_type='String',
                default_value='entryLevel',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='titleIds',
                description="""\
Title ID's - https://rapidapi.com/rockapis-rockapis-default/api/linkedin-api8\
/tutorials/how-to-find-a-title-id-on-linkedin%3F\
""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='functionIds',
                description="""\
Function ID's - https://rapidapi.com/rockapis-rockapis-default/api/linkedin-ap\
i8/tutorials/how-to-find-a-function-id-on-linkedin%3F\
""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='start',
                description="""\
Start: (i.e. 0, 25, 50, 75, 100)\
""",
                hint_type='String',
                default_value='0',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='industryIds',
                description="""\
Industry ID's \
https://rapidapi.com/rockapis-rockapis-default/api/linkedin-api8/tutorials/how\
-to-find-a-industry-id-on-linkedin%3F\
""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='onsiteRemote',
                description="""On-Site or Remote or Hybrid\
it could be one of these: onSite, remote, hybrid \
(i.e. remote)""",
                hint_type='String',
                default_value='remote',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='sort',
                description="""Sort: mostRelevant, mostRecent""",
                hint_type='String',
                default_value='mostRelevant',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Jobs V2
        # RockAPIs | Linkedin API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-api8.p.rapidapi.com'
                '/search-jobs-v2') and
            i.nice_name == "Search Jobs V2")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='keywords',
                description='Keywords',
                hint_type='String',
                default_value='Software Engineer',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='locationId',
                description="""Location ID \
https://rapidapi.com/rockapis-rockapis-default/api/linkedin-api8/tutorials/how\
-to-find-a-location-id-on-linkedin%3F""",
                hint_type='Number',
                default_value='103644278',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='companyIds',
                description="Company ID's"
                            "https://rapidapi.com/rockapis-rockapis-default"
                            "/api/linkedin-api8/tutorials/how-to-find-a-com"
                            "pany-id-on-linkedin%3F",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='datePosted',
                description="""Date Posted - it could be one of these \
(i.e. anyTime, pastMonth, pastWeek, past24Hours)""",
                hint_type='String',
                default_value='anyTime',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='salary',
                description="""Salary \
(i.e. 40k+, 60k+, \
80k+, 100k+, 120k+, \
140k+, 160k+, 180k+, \
200k+ (i.e.: 80k+))""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='jobType',
                description="""Job Type (i.e. \
fullTime, partTime, contract, internship (i.e. contract))""",
                hint_type='String',
                default_value='fullTime',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='experienceLevel',
                description="""Experience Level: \
internship, associate, director, entryLevel, midSeniorLevel. executive \
(i.e. executive)""",
                hint_type='String',
                default_value='entryLevel',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='titleIds',
                description="""\
Title ID's - https://rapidapi.com/rockapis-rockapis-default/api/linkedin-api8\
/tutorials/how-to-find-a-title-id-on-linkedin%3F\
""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='functionIds',
                description="""\
Function ID's - https://rapidapi.com/rockapis-rockapis-default/api/linkedin-ap\
i8/tutorials/how-to-find-a-function-id-on-linkedin%3F\
""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='start',
                description="""Start \
(i.e. 0, 25, 50, 75, 100)\
""",
                hint_type='String',
                default_value='0',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='industryIds',
                description="""\
Industry ID's \
https://rapidapi.com/rockapis-rockapis-default/api/linkedin-api8/tutorials/how\
-to-find-a-industry-id-on-linkedin%3F\
""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='onsiteRemote',
                description="""On-Site or Remote or Hybrid\
it could be one of these: onSite, remote, hybrid \
(i.e. remote)""",
                hint_type='String',
                default_value='remote',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='sort',
                description="""Sort: mostRelevant, mostRecent""",
                hint_type='String',
                default_value='mostRelevant',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Hiring Team
        # RockAPIs | Linkedin API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-api8.p.rapidapi.com'
                '/get-hiring-team') and
            i.nice_name == "Get Hiring Team")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='id',
                description='ID - LinkedIn Job ID',
                hint_type='String',
                default_value='3903094332',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='url',
                description='URL of Job',
                hint_type='String',
                default_value='https://www.linkedin.com/jobs/view/3903094332/',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Locations
        # RockAPIs | Linkedin API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-api8.p.rapidapi.com'
                '/search-locations') and
            i.nice_name == "Search Locations")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='keyword',
                description='Keyword (Location)',
                hint_type='String',
                default_value='United States',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Employees
        # RockAPIs | Rapid LinkedIn Data API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-api.p.rapidapi.com'
                '/search-employees') and
            i.nice_name == "Search Employees")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='companyId',
                description='Company ID',
                hint_type='String',
                default_value='1441',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='start',
                description='Start - (i.e. 0, 25, 50, 75, '
                            '100, etc. 0 = 1st page 25 = 2nd page 50 = 3rd '
                            'page, etc.)',
                hint_type='String',
                default_value='0',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Company Details
        # RockAPIs | Rapid LinkedIn Data API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-api.p.rapidapi.com'
                '/get-company-details') and
            i.nice_name == "Get Company Details")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='username',
                description='Username',
                hint_type='String',
                default_value='google',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Company By Domain (BETA)
        # RockAPIs | Rapid LinkedIn Data API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-api.p.rapidapi.com'
                '/get-company-by-domain') and
            i.nice_name == "Get Company By Domain (BETA)")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='domain',
                description='Domain',
                hint_type='String',
                default_value='google.com',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Company Insights [PREMIUM] (Beta)
        # RockAPIs | Rapid LinkedIn Data API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-api.p.rapidapi.com'
                '/get-company-insights') and
            i.nice_name == "Get Company Insights [PREMIUM] (Beta)")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='username',
                description='Username',
                hint_type='String',
                default_value='google',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Company Jobs Count
        # RockAPIs | Rapid LinkedIn Data API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-api.p.rapidapi.com'
                '/get-company-jobs-count') and
            i.nice_name == "Get Company Jobs Count")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='companyId',
                description='Company ID',
                hint_type='String',
                default_value='1441',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Company Pages People Also Viewed
        # RockAPIs | Rapid LinkedIn Data API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-api.p.rapidapi.com'
                '/get-company-pages-people-also-viewed') and
            i.nice_name == "Get Company Pages People Also Viewed")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='username',
                description='Username',
                hint_type='String',
                default_value='google',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Company's Post
        # RockAPIs | Rapid LinkedIn Data API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-api.p.rapidapi.com'
                '/get-company-posts') and
            i.nice_name == "Get Company's Post")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='username',
                description='Username',
                hint_type='String',
                default_value='google',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Company Post Comments
        # RockAPIs | Rapid LinkedIn Data API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-api.p.rapidapi.com'
                '/get-company-post-comments') and
            i.nice_name == "Get Company Post Comments")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='urn',
                description='Post URN Value',
                hint_type='String',
                default_value='7179144327430844416',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='sort',
                description='Sort - (i.e. mostRelevant, mostRecent)',
                hint_type='String',
                default_value='mostRecent',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Jobs
        # RockAPIs | Rapid LinkedIn Data API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-api.p.rapidapi.com'
                '/search-jobs') and
            i.nice_name == "Search Jobs")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='keywords',
                description='Keywords',
                hint_type='String',
                default_value='Software Engineer',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='locationId',
                description="""Location ID \
https://rapidapi.com/rockapis-rockapis-default/api/linkedin-data-api/tutorials\
/how-to-find-a-location-id-on-linkedin%3F\
""",
                hint_type='Number',
                default_value='103644278',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='companyIds',
                description="Company ID's"
                            "https://rapidapi.com/rockapis-rockapis-default"
                            "/api/linkedin-data-api/tutorials/how-to-find-a"
                            "-company-id-on-linkedin%3F",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='datePosted',
                description="""Date Posted - \
(i.e. anyTime, pastMonth, pastWeek, past24Hours""",
                hint_type='String',
                default_value='anyTime',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='salary',
                description="""Salary - \
(i.e. 40k+, 60k+, \
80k+, 100k+, 120k+, \
140k+, 160k+, 180k+, \
200k+ (i.e. 80k+))""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='jobType',
                description="""Job Type - (i.e. \
fullTime, partTime, contract, internship (i.e. contract))""",
                hint_type='String',
                default_value='fullTime',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='experienceLevel',
                description="""Experience Level: \
internship, associate, director, entryLevel, midSeniorLevel. executive \
(example: executive)""",
                hint_type='String',
                default_value='entryLevel',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='titleIds',
                description="""\
Title ID's - https://rapidapi.com/rockapis-rockapis-default/api/linkedin-data-a\
pi/tutorials/how-to-find-a-title-id-on-linkedin%3F\
""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='functionIds',
                description="""\
Function ID's - https://rapidapi.com/rockapis-rockapis-default/api/linkedin-dat\
a-api/tutorials/how-to-find-a-function-id-on-linkedin%3F\
""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='start',
                description="""Start: \
Should be one of: 0, 25, 50, 75, 100, etc.\
""",
                hint_type='String',
                default_value='0',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='industryIds',
                description="""\
Industry ID's \
https://rapidapi.com/rockapis-rockapis-default/api/linkedin-data-api/tutorials/\
how-to-find-a-industry-id-on-linkedin%3F\
""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='onsiteRemote',
                description="""On-Site or Remote or Hybrid\
(i.e. onSite, remote, hybrid) \
Example: remote""",
                hint_type='String',
                default_value='remote',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='sort',
                description="""Sort (i.e. mostRelevant, mostRecent)""",
                hint_type='String',
                default_value='mostRecent',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Job Details
        # RockAPIs | Rapid LinkedIn Data API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-api.p.rapidapi.com'
                '/get-job-details') and
            i.nice_name == "Get Job Details")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='id',
                description='ID',
                hint_type='String',
                default_value='3738360408',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Jobs V2
        # RockAPIs | Rapid LinkedIn Data API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-api.p.rapidapi.com'
                '/search-jobs-v2') and
            i.nice_name == "Search Jobs V2")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='keywords',
                description='Keywords',
                hint_type='String',
                default_value='Software Engineer',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='locationId',
                description="""Location ID \
https://rapidapi.com/rockapis-rockapis-default/api/linkedin-data-api/tutorials/\
how-to-find-a-location-id-on-linkedin%3F""",
                hint_type='Number',
                default_value='103644278',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='companyIds',
                description="Company ID's"
                            "https://rapidapi.com/rockapis-rockapis-default"
                            "/api/linkedin-data-api/tutorials/how-to-find-a"
                            "-company-id-on-linkedin%3F",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='datePosted',
                description="""Date Posted \
(i.e. anyTime, pastMonth, pastWeek, past24Hours)""",
                hint_type='String',
                default_value='anyTime',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='salary',
                description="""Salary \
(i.e. 40k+, 60k+, \
80k+, 100k+, 120k+, \
140k+, 160k+, 180k+, \
200k+) (i.e. 80k+)""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='jobType',
                description="""Job Type (i.e. \
fullTime, partTime, contract, internship) (i.e. contract)""",
                hint_type='String',
                default_value='fullTime',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='experienceLevel',
                description="""Experience Level: \
internship, associate, director, entryLevel, midSeniorLevel. executive \
(i.e. executive)""",
                hint_type='String',
                default_value='entryLevel',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='titleIds',
                description="""\
Title ID's - https://rapidapi.com/rockapis-rockapis-default/api/linkedin-data-a\
pi/tutorials/how-to-find-a-title-id-on-linkedin%3F\
""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='functionIds',
                description="""\
Function ID's - https://rapidapi.com/rockapis-rockapis-default/api/linkedin-dat\
a-api/tutorials/how-to-find-a-function-id-on-linkedin%3F\
""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='start',
                description="""\
Start: (i.e. 0, 25, 50, 75, 100)\
""",
                hint_type='String',
                default_value='0',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='industryIds',
                description="""\
Industry ID's \
https://rapidapi.com/rockapis-rockapis-default/api/linkedin-data-api/tutorials/\
how-to-find-a-industry-id-on-linkedin%3F\
""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='onsiteRemote',
                description="""On-Site or Remote or Hybrid\
(i.e. onSite, remote, hybrid) \
Example: remote""",
                hint_type='String',
                default_value='remote',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='sort',
                description="""Sort (i.e. mostRelevant, mostRecent)""",
                hint_type='String',
                default_value='mostRecent',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Hiring Team
        # RockAPIs | Rapid LinkedIn Data API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-api.p.rapidapi.com'
                '/get-hiring-team') and
            i.nice_name == "Get Hiring Team")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='id',
                description='ID - LinkedIn Job ID',
                hint_type='String',
                default_value='3903094332',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='url',
                description='URL of Job',
                hint_type='String',
                default_value='https://www.linkedin.com/jobs/view/3903094332/',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Locations
        # RockAPIs | Rapid LinkedIn Data API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://linkedin-data-api.p.rapidapi.com'
                '/search-locations') and
            i.nice_name == "Search Locations")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='keyword',
                description='Keyword (Location)',
                hint_type='String',
                default_value='United States',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Jobs
        # RockAPIs | Rapid Linkedin Jobs API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://rapid-linkedin-jobs-api.p.rapidapi.com'
                '/search-jobs') and
            i.nice_name == "Search Jobs")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='keywords',
                description='Keywords',
                hint_type='String',
                default_value='Software Engineer',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='locationId',
                description="""Location ID \
https://rapidapi.com/rockapis-rockapis-default/api/linkedin-data-api/tutorials\
/how-to-find-a-location-id-on-linkedin%3F\
""",
                hint_type='Number',
                default_value='103644278',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='companyIds',
                description="Company ID's "
                            "https://rapidapi.com/rockapis-rockapis-default"
                            "/api/linkedin-data-api/tutorials/how-to-find-a"
                            "-company-id-on-linkedin%3F",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='datePosted',
                description="""Date Posted \
(i.e. anyTime, pastMonth, pastWeek, past24Hours)""",
                hint_type='String',
                default_value='anyTime',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='salary',
                description="""Salary \
(i.e. 40k+, 60k+, \
80k+, 100k+, 120k+, \
140k+, 160k+, 180k+, \
200k+) (i.e. 80k+)""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='jobType',
                description="""Job Type (i.e. \
fullTime, partTime, contract, internship) (i.e. contract)""",
                hint_type='String',
                default_value='fullTime',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='experienceLevel',
                description="""Experience Level \
(i.e. internship, associate, director, entryLevel, midSeniorLevel. executive) \
(i.e. executive)""",
                hint_type='String',
                default_value='entryLevel',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='titleIds',
                description="""\
Title ID's - https://rapidapi.com/rockapis-rockapis-default/api/linkedin-data-a\
pi/tutorials/how-to-find-a-title-id-on-linkedin%3F\
""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='functionIds',
                description="""\
Function ID's - https://rapidapi.com/rockapis-rockapis-default/api/linkedin-dat\
a-api/tutorials/how-to-find-a-function-id-on-linkedin%3F\
""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='start',
                description="""Start: \
Should be one of: 0, 25, 50, 75, 100, etc.\
""",
                hint_type='String',
                default_value='0',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='industryIds',
                description="""\
Industry ID's \
https://rapidapi.com/rockapis-rockapis-default/api/linkedin-data-api/tutorials/\
how-to-find-a-industry-id-on-linkedin%3F\
""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='onsiteRemote',
                description="""On-Site or Remote or Hybrid\
(i.e. onSite, remote, hybrid) \
(i.e. remote)""",
                hint_type='String',
                default_value='remote',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='sort',
                description="""Sort (i.e. mostRelevant, mostRecent)""",
                hint_type='String',
                default_value='mostRecent',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Job Details
        # RockAPIs | Rapid Linkedin Jobs API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://rapid-linkedin-jobs-api.p.rapidapi.com'
                '/get-job-details') and
            i.nice_name == "Get Job Details")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='id',
                description='ID',
                hint_type='String',
                default_value='3738360408',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Jobs V2
        # RockAPIs | Rapid Linkedin Jobs API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://rapid-linkedin-jobs-api.p.rapidapi.com'
                '/search-jobs-v2') and
            i.nice_name == "Search Jobs V2")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='keywords',
                description='Keywords',
                hint_type='String',
                default_value='Software Engineer',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='locationId',
                description="""Location ID \
https://rapidapi.com/rockapis-rockapis-default/api/rapid-linkedin-jobs-api/tuto\
rials/how-to-find-a-location-id-on-linkedin%3F""",
                hint_type='Number',
                default_value='103644278',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='companyIds',
                description="Company ID's "
                            "https://rapidapi.com/rockapis-rockapis-default"
                            "/api/rapid-linkedin-jobs-api/tutorials/how-to-"
                            "find-a-company-id-on-linkedin%3F-1",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='datePosted',
                description="""Date Posted \
(i.e. anyTime, pastMonth, pastWeek, past24Hours)""",
                hint_type='String',
                default_value='anyTime',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='salary',
                description="""Salary \
(i.e. 40k+, 60k+, \
80k+, 100k+, 120k+, \
140k+, 160k+, 180k+, \
200k+) (i.e. 80k+)""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='jobType',
                description="""Job Type \
(i.e. fullTime, partTime, contract, internship Example: contract""",
                hint_type='String',
                default_value='fullTime',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='experienceLevel',
                description="""Experience Level \
(i.e. internship, associate, director, entryLevel, midSeniorLevel, executive) \
(example: executive)""",
                hint_type='String',
                default_value='entryLevel',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='titleIds',
                description="""\
Title ID's \
https://rapidapi.com/rockapis-rockapis-default/api/rapid-linkedin-jobs-api/tuto\
rials/how-to-find-a-title-id-on-linkedin%3F\
""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='functionIds',
                description="""\
Function ID's \
https://rapidapi.com/rockapis-rockapis-default/api/rapid-linkedin-jobs-api/tuto\
rials/how-to-find-a-function-id-on-linkedin%3F\
""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='start',
                description="""\
Start: (i.e. 0, 50, 100, 150, 200, etc.)\
""",
                hint_type='String',
                default_value='0',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='industryIds',
                description="""\
Industry ID's \
https://rapidapi.com/rockapis-rockapis-default/api/rapid-linkedin-jobs-api/tuto\
rials/how-to-find-a-industry-id-on-linkedin%3F\
""",
                hint_type='String',
                default_value='',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='onsiteRemote',
                description="""On-Site or Remote or Hybrid \
(i.e. onSite, remote, hybrid) \
Example: remote""",
                hint_type='String',
                default_value='remote',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='sort',
                description="""Sort (i.e. mostRelevant, mostRecent)""",
                hint_type='String',
                default_value='mostRecent',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Hiring Team
        # RockAPIs | Rapid Linkedin Jobs API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://rapid-linkedin-jobs-api.p.rapidapi.com'
                '/get-hiring-team') and
            i.nice_name == "Get Hiring Team")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='id',
                description='ID - LinkedIn Job ID',
                hint_type='String',
                default_value='3903094332',
                required=False,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='url',
                description='URL of Job',
                hint_type='String',
                default_value='https://www.linkedin.com/jobs/view/3903094332/',
                required=False,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # SearchJobs
        # vuesdata | Indeed Jobs - Sweden
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://indeed-jobs-api-sweden.p.rapidapi.com'
                '/indeed-se/') and
            i.nice_name == "SearchJobs")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='offset',
                description='Offset',
                hint_type='Number',
                default_value='0',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='keyword',
                description='Keyword',
                hint_type='String',
                default_value='Software Engineer',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='location',
                description='Location',
                hint_type='String',
                default_value='Sweden',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +

              str(new_api_endpoint_nice_name))

        # SearchJobs
        # vuesdata | Indeed Jobs API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://indeed-jobs-api.p.rapidapi.com'
                '/indeed-us/') and
            i.nice_name == "SearchJobs")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='offset',
                description='Offset',
                hint_type='Number',
                default_value='0',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='keyword',
                description='Keyword',
                hint_type='String',
                default_value='Software Engineer',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='location',
                description='Location',
                hint_type='String',
                default_value='United States',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # SearchJobs
        # vuesdata | Indeed Jobs API - Denmark
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://indeed-jobs-api-denmark.p.rapidapi.com'
                '/indeed-dk/') and
            i.nice_name == "SearchJobs")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='offset',
                description='Offset',
                hint_type='Number',
                default_value='0',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='keyword',
                description='Keyword',
                hint_type='String',
                default_value='Software Engineer',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='location',
                description='Location',
                hint_type='String',
                default_value='Denmark',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # SearchJobs
        # vuesdata | Indeed Jobs API - Finland
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://indeed-jobs-api-finland.p.rapidapi.com'
                '/indeed-fi/') and
            i.nice_name == "SearchJobs")
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='offset',
                description='Offset',
                hint_type='Number',
                default_value='0',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='keyword',
                description='Keyword',
                hint_type='String',
                default_value='Software Engineer',
                required=True,
            ),
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='location',
                description='Location',
                hint_type='String',
                default_value='Finland',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Job by ID
        # apijobs | apijobs
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List if
            i.http_path == (
                'https://api.apijobs.dev'
                '/v1/job/') and
            i.nice_name == 'Get Job by ID')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='id',
                description='''\
Detailed Information about a specific Job ID - \
This route retrieves detailed information about a specific job using its unique\
 ID. When you send a GET request with a job ID, the route provides you with all\
 the relevant job details in response. If there's an issue with your request, \
 you'll receive an error message.''',
                hint_type='String',
                default_value='65d9c96f19e3a211a90b9f41',
                path_param=True,
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        db.session.close()
        print(APIEndpointParam.__tablename__ + " seeded successfully!")

    except Exception as e:
        print(f"Error committing data: {e}")

# Example Seed Format
# nice_description can have """ and stores TEXT in the column.
"""
        # endpoint_name
        # api_endpoint_nice_name
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                '___'
                '___') and
            i.nice_name == '___')
        db.session.add_all([
            APIEndpointParam(
                api_endpoint_id=new_api_endpoint_id,
                param='___',
                description='___',
                hint_type='___',
                default_value='___',
                required=True,
            ),
        ])
        db.session.commit()
        print(APIEndpointParam.__tablename__ + " seeded " + 
              str(new_api_endpoint_nice_name))
"""
