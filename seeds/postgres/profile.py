"""
Profile

Seed file can be run
cd <base_dir>
PYTHONPATH=<base_dir> python3 <base_dir>/<file_name>.py
"""


from sqlalchemy import inspect, text, MetaData
from sqlalchemy_utils import database_exists, create_database

from models.postgres.experience_level import ExperienceLevel
from models.postgres.job_type import JobType
from models.postgres.locations.location import Location
from models.postgres.locations.survey_location import SurveyLocation
from models.postgres.resume import Resume
from models.postgres.saved_company import SavedCompany
from models.postgres.saved_job import SavedJob
from models.postgres.survey import Survey
from models.postgres.survey_experience_level import SurveyExperienceLevel
from models.postgres.survey_job_type import SurveyJobType
from secrets_jobs.credentials import (
    postgres_information_login_details,
    postgres_database_name
)

# Imports are required due to relationships
from models.postgres.profile import Profile
from models.postgres.user import User

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

    table_saved_jobs = db.Table(
        SavedJob.__tablename__,
        metadata=metadata,
        bind_key="postgres",
        autoload_with=engine)

    if table_exists(db, table_saved_jobs.name):
        fk_names = get_foreign_key_constraint_names(
            table_saved_jobs,
            engine
        )
        for fk_name in fk_names:
            if fk_name:
                sql_text = (f'ALTER TABLE {table_saved_jobs.name} \
DROP FOREIGN KEY {fk_name}')
                db.session.execute(text(sql_text))

    table_saved_companies = db.Table(
        SavedCompany.__tablename__,
        metadata=metadata,
        bind_key="postgres",
        autoload_with=engine)

    if table_exists(db, table_saved_companies.name):
        fk_names = get_foreign_key_constraint_names(
            table_saved_companies,
            engine
        )
        for fk_name in fk_names:
            if fk_name:
                sql_text = (f'ALTER TABLE {table_saved_companies.name} \
DROP FOREIGN KEY {fk_name}')
                db.session.execute(text(sql_text))

    table_profile = db.Table(
        Profile.__tablename__,
        metadata=metadata,
        bind_key="postgres",
        autoload_with=engine)

    if table_exists(db, table_profile.name):
        fk_names = get_foreign_key_constraint_names(
            table_profile,
            engine
        )
        for fk_name in fk_names:
            if fk_name:
                sql_text = (f'ALTER TABLE {table_profile.name} \
DROP FOREIGN KEY {fk_name}')
                db.session.execute(text(sql_text))

    table_resume = db.Table(
        Resume.__tablename__,
        metadata=metadata,
        bind_key="postgres",
        autoload_with=engine)

    if table_exists(db, table_resume.name):
        fk_names = get_foreign_key_constraint_names(
            table_resume,
            engine
        )
        for fk_name in fk_names:
            if fk_name:
                sql_text = (f'ALTER TABLE {table_resume.name} \
DROP FOREIGN KEY {fk_name}')
                db.session.execute(text(sql_text))

    table_survey_location = db.Table(
        SurveyLocation.__tablename__,
        metadata=metadata,
        bind_key="postgres",
        autoload_with=engine)

    if table_exists(db, table_survey_location.name):
        fk_names = get_foreign_key_constraint_names(
            table_survey_location,
            engine
        )
        for fk_name in fk_names:
            if fk_name:
                sql_text = (f'ALTER TABLE {table_survey_location.name} \
DROP FOREIGN KEY {fk_name}')
                db.session.execute(text(sql_text))

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

    table_survey_experience_level = db.Table(
        SurveyExperienceLevel.__tablename__,
        metadata=metadata,
        bind_key="postgres",
        autoload_with=engine)

    if table_exists(db, table_survey_experience_level.name):
        fk_names = get_foreign_key_constraint_names(
            table_survey_experience_level,
            engine
        )
        for fk_name in fk_names:
            if fk_name:
                sql_text = (f'ALTER TABLE {table_survey_experience_level.name} \
DROP FOREIGN KEY {fk_name}')
                db.session.execute(text(sql_text))

    table_survey = db.Table(
        Survey.__tablename__,
        metadata=metadata,
        bind_key="postgres",
        autoload_with=engine)

    if table_exists(db, table_survey.name):
        fk_names = get_foreign_key_constraint_names(
            table_survey,
            engine
        )
        for fk_name in fk_names:
            if fk_name:
                sql_text = (f'ALTER TABLE {table_survey.name} \
DROP FOREIGN KEY {fk_name}')
                db.session.execute(text(sql_text))

    table_saved_jobs.drop(engine, checkfirst=True)
    table_saved_companies.drop(engine, checkfirst=True)

    table_survey_location.drop(engine, checkfirst=True)
    table_survey_job_type.drop(engine, checkfirst=True)
    table_survey_experience_level.drop(engine, checkfirst=True)
    table_survey.drop(engine, checkfirst=True)

    table_resume.drop(engine, checkfirst=True)
    table_profile.drop(engine, checkfirst=True)

    if not table_exists(db, User.__tablename__):
        table_user = db.Table(
            User.__tablename__,
            metadata=metadata,
            bind_key="postgres",
            autoload_with=engine)
        table_user.create(engine, checkfirst=True)

    if not table_exists(db, JobType.__tablename__):
        table_job_type = db.Table(
            JobType.__tablename__,
            metadata=metadata,
            bind_key="postgres",
            autoload_with=engine)
        table_job_type.create(engine, checkfirst=True)

    if not table_exists(db, ExperienceLevel.__tablename__):
        table_experience_level = db.Table(
            ExperienceLevel.__tablename__,
            metadata=metadata,
            bind_key="postgres",
            autoload_with=engine)
        table_experience_level.create(engine, checkfirst=True)

    if not table_exists(db, Location.__tablename__):
        table_location = db.Table(
            Location.__tablename__,
            metadata=metadata,
            bind_key="postgres",
            autoload_with=engine)
        table_location.create(engine, checkfirst=True)

    table_profile.create(engine, checkfirst=True)
    table_resume.create(engine, checkfirst=True)

    table_survey.create(engine, checkfirst=True)
    table_survey_experience_level.create(engine, checkfirst=True)
    table_survey_job_type.create(engine, checkfirst=True)
    table_survey_location.create(engine, checkfirst=True)

    try:
        # test_profile = Profile()
        # db.session.add_all([
        #     test_profile
        # ])
        db.session.commit()
        print(Profile.__tablename__ + " seeded successfully!")
    except Exception as e:
        print(f"Error committing data: {e}")
        raise e
