"""
Regions

Seed file can be run
cd <base_dir>
PYTHONPATH=<base_dir> python3 <base_dir>/<file_name>.py
"""


from sqlalchemy import inspect, text, MetaData
from sqlalchemy_utils import database_exists, create_database

from models.postgres.locations.glassdoor_location_id import GlassdoorLocationID
from models.postgres.locations.linkedin_geourn_id import LinkedInGeoURNID
from models.postgres.user import User
from models.postgres.survey import Survey
from models.postgres.profile import Profile
from models.postgres.api_source import APISource
from models.postgres.company import Company
from models.postgres.listed_job import ListedJob
from models.postgres.locations.listed_job_location import ListedJobLocation
from models.postgres.locations.location import Location
from models.postgres.locations.survey_location import SurveyLocation
from secrets_jobs.credentials import (
    postgres_information_login_details,
    postgres_database_name
)

from models.postgres.locations.regions import Region
from models.postgres.locations.subregions import Subregion
from models.postgres.locations.countries import Country
from models.postgres.locations.states import State
from models.postgres.locations.cities import City
from models.postgres.locations.x_location_id import XLocationID
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

    table_region = db.Table(
        Region.__tablename__,
        metadata=metadata,
        bind_key="postgres",
        autoload_with=engine)

    if table_exists(db, table_region.name):
        fk_names = get_foreign_key_constraint_names(table_region, engine)
        for fk_name in fk_names:
            if fk_name:
                sql_text = (f'ALTER TABLE {table_region.name} DROP FOREIGN KEY '
                            f'{fk_name}')
                db.session.execute(text(sql_text))

    table_subregion = db.Table(
        Subregion.__tablename__,
        metadata=metadata,
        bind_key="postgres",
        autoload_with=engine)

    if table_exists(db, table_subregion.name):
        fk_names = get_foreign_key_constraint_names(table_subregion, engine)
        for fk_name in fk_names:
            if fk_name:
                sql_text = (
                    f'ALTER TABLE {table_subregion.name} DROP FOREIGN KEY '
                    f'{fk_name}')
                db.session.execute(text(sql_text))

    table_country = db.Table(
        Country.__tablename__,
        metadata=metadata,
        bind_key="postgres",
        autoload_with=engine)

    if table_exists(db, table_country.name):
        fk_names = get_foreign_key_constraint_names(table_country, engine)
        for fk_name in fk_names:
            if fk_name:
                sql_text = (
                    f'ALTER TABLE {table_country.name} DROP FOREIGN KEY '
                    f'{fk_name}')
                db.session.execute(text(sql_text))

    table_state = db.Table(
        State.__tablename__,
        metadata=metadata,
        bind_key="postgres",
        autoload_with=engine)

    if table_exists(db, table_state.name):
        fk_names = get_foreign_key_constraint_names(table_state, engine)
        for fk_name in fk_names:
            if fk_name:
                sql_text = (f'ALTER TABLE {table_state.name} DROP FOREIGN KEY '
                            f'{fk_name}')
                db.session.execute(text(sql_text))

    table_city = db.Table(
        City.__tablename__,
        metadata=metadata,
        bind_key="postgres",
        autoload_with=engine)

    if table_exists(db, table_city.name):
        fk_names = get_foreign_key_constraint_names(table_city, engine)
        for fk_name in fk_names:
            if fk_name:
                sql_text = (f'ALTER TABLE {table_city.name} DROP FOREIGN KEY '
                            f'{fk_name}')
                db.session.execute(text(sql_text))

    table_x_location_ids = db.Table(
        XLocationID.__tablename__,
        metadata=metadata,
        bind_key="postgres",
        autoload_with=engine)

    if table_exists(db, table_x_location_ids.name):
        fk_names = get_foreign_key_constraint_names(
            table_x_location_ids, engine
        )
        for fk_name in fk_names:
            if fk_name:
                sql_text = (f'ALTER TABLE {table_x_location_ids.name} '
                            f'DROP FOREIGN KEY '
                            f'{fk_name}')
                db.session.execute(text(sql_text))

    table_glassdoor_location_ids = db.Table(
        GlassdoorLocationID.__tablename__,
        metadata=metadata,
        bind_key="postgres",
        autoload_with=engine)

    if table_exists(db, table_glassdoor_location_ids.name):
        fk_names = get_foreign_key_constraint_names(
            table_glassdoor_location_ids, engine
        )
        for fk_name in fk_names:
            if fk_name:
                sql_text = (f'ALTER TABLE {table_glassdoor_location_ids.name} '
                            f'DROP FOREIGN KEY '
                            f'{fk_name}')
                db.session.execute(text(sql_text))

    table_linkedin_geo_urn_ids = db.Table(
        LinkedInGeoURNID.__tablename__,
        metadata=metadata,
        bind_key="postgres",
        autoload_with=engine)

    if table_exists(db, table_linkedin_geo_urn_ids.name):
        fk_names = get_foreign_key_constraint_names(
            table_linkedin_geo_urn_ids,
            engine
        )
        for fk_name in fk_names:
            if fk_name:
                sql_text = (f'ALTER TABLE {table_linkedin_geo_urn_ids.name} '
                            'DROP FOREIGN KEY '
                            f'{fk_name}')
                db.session.execute(text(sql_text))

    table_location_ids = db.Table(
        Location.__tablename__,
        metadata=metadata,
        bind_key="postgres",
        autoload_with=engine)

    if table_exists(db, table_location_ids.name):
        fk_names = get_foreign_key_constraint_names(
            table_location_ids, engine
        )
        for fk_name in fk_names:
            if fk_name:
                sql_text = (f'ALTER TABLE {table_location_ids.name} '
                            f'DROP FOREIGN KEY '
                            f'{fk_name}')
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
                sql_text = (
                    f'ALTER TABLE {table_survey.name} \
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
                sql_text = (
                    f'ALTER TABLE {table_profile.name} \
    DROP FOREIGN KEY {fk_name}')
                db.session.execute(text(sql_text))

    table_users = db.Table(
        User.__tablename__,
        metadata=metadata,
        bind_key="postgres",
        autoload_with=engine)

    if table_exists(db, table_users.name):
        fk_names = get_foreign_key_constraint_names(
            table_users,
            engine
        )
        for fk_name in fk_names:
            if fk_name:
                sql_text = (
                    f'ALTER TABLE {table_users.name} \
    DROP FOREIGN KEY {fk_name}')
                db.session.execute(text(sql_text))

    table_listed_job = db.Table(
        ListedJob.__tablename__,
        metadata=metadata,
        bind_key="postgres",
        autoload_with=engine)

    if table_exists(db, table_listed_job.name):
        fk_names = get_foreign_key_constraint_names(
            table_listed_job,
            engine
        )
        for fk_name in fk_names:
            if fk_name:
                sql_text = (
                    f'ALTER TABLE {table_listed_job.name} \
    DROP FOREIGN KEY {fk_name}')
                db.session.execute(text(sql_text))

    table_company = db.Table(
        Company.__tablename__,
        metadata=metadata,
        bind_key="postgres",
        autoload_with=engine)

    if table_exists(db, table_company.name):
        fk_names = get_foreign_key_constraint_names(
            table_company,
            engine
        )
        for fk_name in fk_names:
            if fk_name:
                sql_text = (
                    f'ALTER TABLE {table_company.name} \
    DROP FOREIGN KEY {fk_name}')
                db.session.execute(text(sql_text))

    table_api_source = db.Table(
        APISource.__tablename__,
        metadata=metadata,
        bind_key="postgres",
        autoload_with=engine)

    if table_exists(db, table_api_source.name):
        fk_names = get_foreign_key_constraint_names(
            table_api_source,
            engine
        )
        for fk_name in fk_names:
            if fk_name:
                sql_text = (
                    f'ALTER TABLE {table_api_source.name} \
    DROP FOREIGN KEY {fk_name}')
                db.session.execute(text(sql_text))

    table_listed_job_location = db.Table(
        ListedJobLocation.__tablename__,
        metadata=metadata,
        bind_key="postgres",
        autoload_with=engine)

    if table_exists(db, table_listed_job_location.name):
        fk_names = get_foreign_key_constraint_names(
            table_listed_job_location,
            engine
        )
        for fk_name in fk_names:
            if fk_name:
                sql_text = (
                    f'ALTER TABLE {table_listed_job_location.name} \
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

    table_survey_location.drop(engine, checkfirst=True)

    table_listed_job_location.drop(engine, checkfirst=True)
    table_location_ids.drop(engine, checkfirst=True)
    table_linkedin_geo_urn_ids.drop(engine, checkfirst=True)
    table_glassdoor_location_ids.drop(engine, checkfirst=True)
    table_x_location_ids.drop(engine, checkfirst=True)

    table_survey.drop(engine, checkfirst=True)
    table_profile.drop(engine, checkfirst=True)
    table_users.drop(engine, checkfirst=True)
    table_listed_job.drop(engine, checkfirst=True)
    table_company.drop(engine, checkfirst=True)
    table_api_source.drop(engine, checkfirst=True)

    table_city.drop(engine, checkfirst=True)
    table_state.drop(engine, checkfirst=True)
    table_country.drop(engine, checkfirst=True)
    table_subregion.drop(engine, checkfirst=True)
    table_region.drop(engine, checkfirst=True)

    # Create

    table_region.create(engine, checkfirst=True)
    table_subregion.create(engine, checkfirst=True)
    table_country.create(engine, checkfirst=True)
    table_state.create(engine, checkfirst=True)
    table_city.create(engine, checkfirst=True)

    table_api_source.create(engine, checkfirst=True)
    table_company.create(engine, checkfirst=True)
    table_listed_job.create(engine, checkfirst=True)
    table_users.create(engine, checkfirst=True)
    table_profile.create(engine, checkfirst=True)
    table_survey.create(engine, checkfirst=True)

    table_x_location_ids.create(engine, checkfirst=True)
    table_glassdoor_location_ids.create(engine, checkfirst=True)
    table_linkedin_geo_urn_ids.create(engine, checkfirst=True)

    table_location_ids.create(engine, checkfirst=True)
    table_listed_job_location.create(engine, checkfirst=True)
    table_survey_location.create(engine, checkfirst=True)

    try:
        db.session.add_all([
            Region(
                name="Africa",
                latitude=-8.7832,
                longitude=34.5085
            ),
            Region(
                name="Americas",
                latitude=54.526,
                longitude=-105.2551,
            ),
            Region(
                name="Asia",
                latitude=34.0479,
                longitude=100.6197,
            ),
            Region(
                name="Europe",
                latitude=54.526,
                longitude=15.2551,
            ),
            Region(
                name="Oceania",
                latitude=-22.7359,
                longitude=140.0188,
            ),
            Region(
                name="Polar",
                latitude=76.2506,
                longitude=-100.114,
            ),
        ])
        db.session.commit()
        print(Region.__tablename__ + " seeded successfully!")
    except Exception as e:
        print(f"Error committing data: {e}")
        raise e
