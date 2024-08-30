"""
Job Type

Seed file can be run
cd <base_dir>
PYTHONPATH=<base_dir> python3 <base_dir>/<file_name>.py
"""


from sqlalchemy import inspect, text, MetaData
from sqlalchemy_utils import database_exists, create_database

from models.postgres.api_source import APISource
from models.postgres.company import Company
from models.postgres.job_type import JobType
from models.postgres.listed_job import ListedJob
from models.postgres.listed_job_job_type import ListedJobJobType
from models.postgres.profile import Profile
from models.postgres.survey import Survey
from models.postgres.survey_job_type import SurveyJobType
from models.postgres.user import User
from secrets_jobs.credentials import (
    postgres_information_login_details,
    postgres_database_name
)

from app import create_app, db
import sqlalchemy as db2

engine = db2.create_engine(postgres_information_login_details)
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


def table_exists(temp_db, table_name, schema=postgres_database_name):
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
    metadata = MetaData()

    table_survey_job_type = db.Table(
        SurveyJobType.__tablename__,
        metadata=metadata,
        bind_key="postgres",
        autoload_with=engine)

    if table_exists(db, table_survey_job_type.name):
        fk_names = get_foreign_key_constraint_names(
            table_survey_job_type,
            engine
        )
        for fk_name in fk_names:
            if fk_name:
                sql_text = (f'ALTER TABLE {table_survey_job_type.name} \
DROP FOREIGN KEY {fk_name}')
                db.session.execute(text(sql_text))

    table_listed_job_job_type = db.Table(
        ListedJobJobType.__tablename__,
        metadata=metadata,
        bind_key="postgres",
        autoload_with=engine)

    if table_exists(db, table_listed_job_job_type.name):
        fk_names = get_foreign_key_constraint_names(
            table_listed_job_job_type,
            engine
        )
        for fk_name in fk_names:
            if fk_name:
                sql_text = (f'ALTER TABLE {table_listed_job_job_type.name} \
DROP FOREIGN KEY {fk_name}')
                db.session.execute(text(sql_text))

    table_job_type = db.Table(
        JobType.__tablename__,
        metadata=metadata,
        bind_key="postgres",
        autoload_with=engine)

    if table_exists(db, table_job_type.name):
        fk_names = get_foreign_key_constraint_names(
            table_job_type,
            engine
        )
        for fk_name in fk_names:
            if fk_name:
                sql_text = (f'ALTER TABLE {table_job_type.name} \
DROP FOREIGN KEY {fk_name}')
                db.session.execute(text(sql_text))

    table_survey_job_type.drop(engine, checkfirst=True)
    table_listed_job_job_type.drop(engine, checkfirst=True)
    table_job_type.drop(engine, checkfirst=True)

    if not table_exists(db, User.__tablename__):
        table_user = db.Table(
            User.__tablename__,
            metadata=metadata,
            bind_key="postgres",
            autoload_with=engine)
        table_user.create(engine, checkfirst=True)

    if not table_exists(db, Profile.__tablename__):
        table_profile = db.Table(
            Profile.__tablename__,
            metadata=metadata,
            bind_key="postgres",
            autoload_with=engine)
        table_profile.create(engine, checkfirst=True)

    if not table_exists(db, Survey.__tablename__):
        table_survey = db.Table(
            Survey.__tablename__,
            metadata=metadata,
            bind_key="postgres",
            autoload_with=engine)
        table_survey.create(engine, checkfirst=True)

    if not table_exists(db, APISource.__tablename__):
        table_api_source = db.Table(
            APISource.__tablename__,
            metadata=metadata,
            bind_key="postgres",
            autoload_with=engine)
        table_api_source.create(engine, checkfirst=True)

    if not table_exists(db, Company.__tablename__):
        table_company = db.Table(
            Company.__tablename__,
            metadata=metadata,
            bind_key="postgres",
            autoload_with=engine)
        table_company.create(engine, checkfirst=True)

    if not table_exists(db, ListedJob.__tablename__):
        table_listed_job = db.Table(
            ListedJob.__tablename__,
            metadata=metadata,
            bind_key="postgres",
            autoload_with=engine)
        table_listed_job.create(engine, checkfirst=True)

    table_job_type.create(engine, checkfirst=True)
    table_listed_job_job_type.create(engine, checkfirst=True)
    table_survey_job_type.create(engine, checkfirst=True)

    try:
        # test_job_type = JobType()
        # db.session.add_all([
        #     test_job_type
        # ])
        db.session.commit()
        print(JobType.__tablename__ + " seeded successfully!")
    except Exception as e:
        print(f"Error committing data: {e}")
        raise e
