"""
API List URL

Seed file can be run
cd <base_dir>
PYTHONPATH=<base_dir> python3 <base_dir>/<file_name>.py

Table drop and creation must also drop:
    APIHeaders,APIEndpointParams, APIEndpointHeaders, APIEndpointBodies due
    to FK restraints

"""
from sqlalchemy import asc, text, MetaData, inspect

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
from sqlalchemy_utils import database_exists, create_database


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


engine = db2.create_engine(maria_information_login_details)
if not database_exists(engine.url):
    create_database(engine.url, encoding='UTF8')


app = create_app()

with app.app_context():

    # APIListURL
    table1 = db.Table(
        APIListURL.__tablename__,
        bind_key="mariadb",
        autoload_with=engine)

    # APIHeader
    metadata = MetaData()
    table2 = db.Table(
        APIHeader.__tablename__,
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

    # APIEndpoint
    table3 = db.Table(
        APIEndpoint.__tablename__,
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

    # APIEndpointParam
    table4 = db.Table(
        APIEndpointParam.__tablename__,
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

    # APIEndpointHeader
    table5 = db.Table(
        APIEndpointHeader.__tablename__,
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

    # APIEndpointBody
    table6 = db.Table(
        APIEndpointBody.__tablename__,
        metadata=metadata,
        bind_key="mariadb",
        autoload_with=engine)
    if table_exists(db, table6.name):
        fk_names = get_foreign_key_constraint_names(table6, engine)
        for fk_name in fk_names:
            if fk_name:
                sql_text = (f'ALTER TABLE {table6.name} DROP FOREIGN KEY '
                            f'{fk_name}')
                db.session.execute(text(sql_text))

    # APIEndpointExtra
    table7 = db.Table(
        APIEndpointExtra.__tablename__,
        metadata=metadata,
        bind_key="mariadb",
        autoload_with=engine)
    if table_exists(db, table7.name):
        fk_names = get_foreign_key_constraint_names(table7, engine)
        for fk_name in fk_names:
            if fk_name:
                sql_text = (f'ALTER TABLE {table7.name} DROP FOREIGN KEY '
                            f'{fk_name}')
                db.session.execute(text(sql_text))

    table7.drop(engine, checkfirst=True)
    table6.drop(engine, checkfirst=True)
    table5.drop(engine, checkfirst=True)
    table4.drop(engine, checkfirst=True)
    table3.drop(engine, checkfirst=True)
    table2.drop(engine, checkfirst=True)
    table1.drop(engine, checkfirst=True)
    table1.create(engine, checkfirst=True)
    table2.create(engine, checkfirst=True)
    table3.create(engine, checkfirst=True)
    table4.create(engine, checkfirst=True)
    table5.create(engine, checkfirst=True)
    table6.create(engine, checkfirst=True)
    table7.create(engine, checkfirst=True)
    try:
        db.session.add_all([
            APIListURL(
                nice_name='APIJobs | Job Searching API',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/apijobs-apijobs-default/api/apijob-job-searching-api/',
                sub_required=True,
                daily_limit=100,
                hour_limit=1000,
                minute_limit=100),
            APIListURL(
                nice_name='avadataservices | Job Postings',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/avadataservices-avadataservices-default'
                    '/api/job-postings1/',
                sub_required=True,
                month_limit=1000,
                hour_limit=1000),
            APIListURL(
                nice_name='bareq | Remote Jobs API',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/bareq/api/remote-jobs-api1/',
                sub_required=True,
                daily_limit=10,
                hour_limit=1000),
            APIListURL(
                nice_name='Bebity | Linkedin Jobs Scraper API',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/bebity-bebity-default/api/linkedin-jobs-scraper-api/',
                sub_required=True,
                month_limit=25,
                hour_limit=1000),
            APIListURL(
                nice_name='Betoalien | USA Jobs for IT',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/betoalien/api/usa-jobs-for-it/',
                sub_required=True,
                month_limit=20,
                hour_limit=1000),
            APIListURL(
                nice_name='Dodocr7 | Google Jobs',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/dodocr7/api/google-jobs/',
                sub_required=True,
                month_limit=25,
                hour_limit=1000,
                second_limit_per=1),
            APIListURL(
                nice_name='Fantastic Jobs | Active Jobs DB',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/fantastic-jobs-fantastic-jobs-default'
                    '/api/active-jobs-db/',
                sub_required=True,
                month_limit=25,
                hour_limit=1000),
            APIListURL(
                nice_name='fernandelcapo | pizzaallapala | TEST',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/fernandelcapo/api/pizzaallapala',
                sub_required=True,
                month_limit=500000,
                hour_limit=1000,
                disabled=True),
            APIListURL(
                nice_name='Flatroy | Jobs from Remoteok',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/Flatroy/api/jobs-from-remoteok/',
                sub_required=True,
                daily_limit=24,
                hour_limit=5),
            APIListURL(
                nice_name='Freshdata | Fresh Linkedin Profile Data',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/freshdata-freshdata-default/api/'
                    'fresh-linkedin-profile-data/',
                sub_required=True,
                month_limit=10,
                hour_limit=1000),
            APIListURL(
                nice_name='Freshdata | Linkedin Jobs',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/freshdata-freshdata-default/api/linkedin-jobs4/',
                sub_required=True,
                month_limit=10,
                hour_limit=1000,
                disabled=True),
            APIListURL(
                nice_name='jaypat87 | Indeed',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/jaypat87/api/indeed11/',
                sub_required=True,
                month_limit=15,
                hour_limit=1000,
                second_limit_per=1),
            APIListURL(
                nice_name='jaypat87 | Job Search',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/jaypat87/api/job-search15',
                sub_required=True,
                month_limit=50,
                hour_limit=1000,
                minute_limit=7),
            APIListURL(
                nice_name='jaypat87 | Linkedin Jobs Search',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/jaypat87/api/linkedin-jobs-search/',
                sub_required=True,
                month_limit=100,
                hour_limit=1000),
            APIListURL(
                nice_name='jobicy | Remote Jobs API',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/jobicy-jobicy-default/api/jobicy/',
                sub_required=True,
                month_limit=500000,
                hour_limit=1000),
            APIListURL(
                nice_name='jobisite | Job Search',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/jobisite/api/job-search38/',
                sub_required=True,
                month_limit=500000,
                hour_limit=1000),
            APIListURL(
                nice_name='JobsAPI2020 | Zambian Jobs API',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/JobsAPI2020/api/zambian-jobs-api1/',
                sub_required=True,
                month_limit=500000,
                hour_limit=1000),
            APIListURL(
                nice_name='Jobwiz | Job Descriptions API',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/jobwiz-jobwiz-default/api/job-descriptions-api/',
                sub_required=True,
                month_limit=100000,
                hour_limit=1000,
                special_restrictions=True),
            APIListURL(
                nice_name='Jobwiz | Job Search API',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/jobwiz-jobwiz-default/api/job-search-api1/',
                sub_required=True,
                month_limit=20,
                hour_limit=1000),
            APIListURL(
                nice_name='letscrape | Job Salary Data',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/letscrape-6bRBa3QguO5/api/job-salary-data/',
                sub_required=True,
                month_limit=50,
                hour_limit=1000),
            APIListURL(
                nice_name='letscrape | JSearch',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/letscrape-6bRBa3QguO5/api/jsearch/',
                sub_required=True,
                month_limit=200,
                hour_limit=1000),
            APIListURL(
                nice_name='letscrape | Real-Time Glassdoor Data',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/letscrape-6bRBa3QguO5/api/real-time-glassdoor-data/',
                sub_required=True,
                month_limit=50,
                hour_limit=1000),
            APIListURL(
                nice_name='Lundehund | Twitter X Job API',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/Lundehund/api/twitter-x-api',
                sub_required=True,
                month_limit=500000,
                hour_limit=1000,
                disabled=True),
            APIListURL(
                nice_name='mantiks | Glassdoor',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/mantiks-mantiks-default/api/glassdoor/',
                sub_required=True,
                month_limit=25,
                hour_limit=1000),
            APIListURL(
                nice_name='mantiks | Indeed',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/mantiks-mantiks-default/api/indeed12/',
                sub_required=True,
                month_limit=25,
                hour_limit=1000),
            APIListURL(
                nice_name='mgujjargamingm | LinkedIn Data Scraper',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/mgujjargamingm/api/linkedin-data-scraper/',
                sub_required=True,
                month_limit=50,
                hour_limit=1000),
            APIListURL(
                nice_name='mgujjargamingm | Linkedin BULK data scraper',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/mgujjargamingm/api/linkedin-bulk-data-scraper',
                sub_required=True,
                month_limit=150,
                hour_limit=1000,
                second_limit_per=1),
            APIListURL(
                nice_name='omarmohamed0 | Jobs API',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/omarmohamed0/api/freelancer-api/',
                sub_required=True,
                month_limit=500000,
                hour_limit=1000),
            APIListURL(
                nice_name='Pat92 | Jobs API',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/Pat92/api/jobs-api14/',
                sub_required=True,
                month_limit=50,
                hour_limit=1000),
            APIListURL(
                nice_name='qurazor1 | Remoote Job Search',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/qurazor1/api/remoote-job-search1/',
                sub_required=True,
                month_limit=50,
                hour_limit=1000),
            APIListURL(
                nice_name='Relu Consultancy | Arbeitsagentur',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/relu-consultancy-relu-consultancy-default/api/'
                    'arbeitsagentur-employement-agency/',
                sub_required=True,
                daily_limit=10,
                hour_limit=1000),
            APIListURL(
                nice_name='Relu Consultancy | Indeed Scraper API - Germany',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/relu-consultancy-relu-consultancy-default/api/'
                    'indeed-scraper-api-germany/',
                sub_required=True,
                daily_limit=10,
                hour_limit=1000),
            APIListURL(
                nice_name='RockAPIs | Linkedin API',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/rockapis-rockapis-default/api/linkedin-api8/',
                sub_required=True,
                month_limit=50,
                hour_limit=1000,
                disabled=True),
            APIListURL(
                nice_name='RockAPIs | Rapid LinkedIn Data API',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/rockapis-rockapis-default/api/linkedin-data-api/',
                sub_required=True,
                month_limit=50,
                hour_limit=1000,
                disabled=True),
            APIListURL(
                nice_name='RockAPIs | Rapid Linkedin Jobs API',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/rockapis-rockapis-default/api/rapid-linkedin-jobs-api/',
                sub_required=True,
                month_limit=50,
                hour_limit=1000,
                disabled=True),
            APIListURL(
                nice_name='sohailglt | Linkedin Live Data',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/sohailglt/api/linkedin-live-data/',
                sub_required=True,
                month_limit=5,
                hour_limit=1000,
                second_limit_per=1),
            APIListURL(
                nice_name='vuesdata | Indeed Jobs - Sweden',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/vuesdata/api/indeed-jobs-api-sweden/',
                sub_required=True,
                month_limit=10,
                hour_limit=1000,
                minute_limit=1),
            APIListURL(
                nice_name='vuesdata | Indeed Jobs API',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/vuesdata/api/indeed-jobs-api/',
                sub_required=True,
                month_limit=20,
                hour_limit=1000,
                minute_limit=1),
            APIListURL(
                nice_name='vuesdata | Indeed Jobs API - Denmark',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/vuesdata/api/indeed-jobs-api-denmark/',
                sub_required=True,
                month_limit=10,
                hour_limit=1000,
                minute_limit=1),
            APIListURL(
                nice_name='vuesdata | Indeed Jobs API - Finland',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/vuesdata/api/indeed-jobs-api-finland/',
                sub_required=True,
                month_limit=20,
                hour_limit=1000,
                minute_limit=1),
            APIListURL(
                nice_name='apijobs',
                host='apijobs.dev',
                url='https://app.apijobs.dev/',
                sub_required=True,
                month_limit=250),
        ])
        db.session.commit()
        db.session.close()
        print(APIListURL.__tablename__ + " seeded successfully!")
    except Exception as e:
        print(f"Error committing data: {e}")
        raise e
