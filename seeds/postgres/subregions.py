"""
Subregions

Seed file can be run
cd <base_dir>
PYTHONPATH=<base_dir> python3 <base_dir>/<file_name>.py
"""
from sqlalchemy import inspect, text, MetaData
from sqlalchemy_utils import database_exists, create_database

from models.postgres.locations.glassdoor_location_id import GlassdoorLocationID
from models.postgres.locations.linkedin_geourn_id import LinkedInGeoURNID
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

    table_city.drop(engine, checkfirst=True)
    table_state.drop(engine, checkfirst=True)
    table_country.drop(engine, checkfirst=True)
    table_subregion.drop(engine, checkfirst=True)

    # Create

    table_subregion.create(engine, checkfirst=True)
    table_country.create(engine, checkfirst=True)
    table_state.create(engine, checkfirst=True)
    table_city.create(engine, checkfirst=True)

    table_x_location_ids.create(engine, checkfirst=True)
    table_glassdoor_location_ids.create(engine, checkfirst=True)
    table_linkedin_geo_urn_ids.create(engine, checkfirst=True)

    table_location_ids.create(engine, checkfirst=True)
    table_listed_job_location.create(engine, checkfirst=True)
    table_survey_location.create(engine, checkfirst=True)

    try:
        all_regions = db.session.query(Region).all()
        africa = [i.id for i in all_regions if i.name == "Africa"][0]
        americas = [i.id for i in all_regions if i.name == "Americas"][0]
        asia = [i.id for i in all_regions if i.name == "Asia"][0]
        europe = [i.id for i in all_regions if i.name == "Europe"][0]
        oceania = [i.id for i in all_regions if i.name == "Oceania"][0]
        polar = [i.id for i in all_regions if i.name == "Polar"][0]
        db.session.add_all([
            Subregion(
                name="Eastern Africa",
                region_id=africa,
                latitude=1.9577,
                longitude=37.2972),
            Subregion(
                name="Middle Africa",
                region_id=africa,
                latitude=2.3185,
                longitude=19.5687),
            Subregion(
                name="Northern Africa",
                region_id=africa,
                latitude=26.0198,
                longitude=32.2778),
            Subregion(
                name="Southern Africa",
                region_id=africa,
                latitude=-24.3571,
                longitude=19.5687),
            Subregion(
                name="Western Africa",
                region_id=africa,
                latitude=13.5317,
                longitude=-2.4604),
            Subregion(
                name="Caribbean",
                region_id=americas,
                latitude=21.4691,
                longitude=-78.6569),
            Subregion(
                name="Central America",
                region_id=americas,
                latitude=12.769,
                longitude=-85.6024),
            Subregion(
                name="Northern America",
                region_id=americas,
                latitude=54.526,
                longitude=-105.2551),
            Subregion(
                name="South America",
                region_id=americas,
                latitude=-8.7832,
                longitude=-55.4915),
            Subregion(
                name="Central Asia",
                region_id=asia,
                latitude=45.4507,
                longitude=68.8319),
            Subregion(
                name="Eastern Asia",
                region_id=asia,
                latitude=38.7946,
                longitude=106.5348),
            Subregion(
                name="South-Eastern Asia",
                region_id=asia,
                latitude=-2.218,
                longitude=115.6628),
            Subregion(
                name="Southern Asia",
                region_id=asia,
                latitude=25.0376,
                longitude=76.4563),
            Subregion(
                name="Western Asia",
                region_id=asia,
                latitude=28.995,
                longitude=49.25),
            Subregion(
                name="Eastern Europe",
                region_id=europe,
                latitude=52.0055,
                longitude=37.9587),
            Subregion(
                name="Northern Europe",
                region_id=europe,
                latitude=62.2786,
                longitude=12.3402),
            Subregion(
                name="Southern Europe",
                region_id=europe,
                latitude=41.2745,
                longitude=-1.2121),
            Subregion(
                name="Western Europe",
                region_id=europe,
                latitude=46.2022,
                longitude=1.2644),
            Subregion(
                name="Australia and New Zealand",
                region_id=oceania,
                latitude=-35.936944,
                longitude=162.766389),
            Subregion(
                name="Melanesia",
                region_id=oceania,
                latitude=-8.1902,
                longitude=152.8265),
            Subregion(
                name="Micronesia",
                region_id=oceania,
                latitude=7.4256,
                longitude=150.5508),
            Subregion(
                name="Polynesia",
                region_id=oceania,
                latitude=-16.8395,
                longitude=-148.3717),
        ])
        db.session.commit()
        print(Subregion.__tablename__ + " seeded successfully!")
    except Exception as e:
        print(f"Error committing data: {e}")
        raise e
