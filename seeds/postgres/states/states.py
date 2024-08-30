"""
States Seed #1

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

    # Create

    table_state.create(engine, checkfirst=True)
    table_city.create(engine, checkfirst=True)

    table_x_location_ids.create(engine, checkfirst=True)
    table_glassdoor_location_ids.create(engine, checkfirst=True)
    table_linkedin_geo_urn_ids.create(engine, checkfirst=True)

    table_location_ids.create(engine, checkfirst=True)
    table_listed_job_location.create(engine, checkfirst=True)
    table_survey_location.create(engine, checkfirst=True)

    try:
        country_list = db.session.query(Country).all()
        list_of_states = []
        list_of_states.append(State(
            name="'Adan",
            state_code="AD",
            latitude=12.8257481,
            longitude=44.7943804,
            country_id=([i.id for i in country_list if i.name == "Yemen"][0]),
        ))
        list_of_states.append(State(
            name="'Amran",
            state_code="AM",
            latitude=16.2569214,
            longitude=43.9436788,
            country_id=([i.id for i in country_list if i.name == "Yemen"][0]),
        ))
        list_of_states.append(State(
            name="'Asir",
            state_code="14",
            latitude=19.0969062,
            longitude=42.8637875,
            country_id=([i.id for i in country_list if i.name == "Saudi "
                                                                 "Arabia"][0]),
        ))
        list_of_states.append(State(
            name="A Coruña",
            state_code="C",
            latitude=43.361904,
            longitude=-8.4301932,
            country_id=([i.id for i in country_list if i.name == "Spain"][0]),
        ))
        list_of_states.append(State(
            name="A'ana",
            state_code="AA",
            latitude=-13.898418,
            longitude=-171.9752995,
            country_id=([i.id for i in country_list if i.name == "Samoa"][0]),
        ))
        list_of_states.append(State(
            name="Aargau",
            state_code="AG",
            latitude=47.3876664,
            longitude=8.2554295,
            country_id=([i.id for i in country_list if i.name == (
                "Switzerland")][0]),
        ))
        list_of_states.append(State(
            name="Aberdeen",
            state_code="ABE",
            latitude=57.149717,
            longitude=-2.094278,
            country_id=([i.id for i in country_list if i.name == (
                "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Aberdeenshire",
            state_code="ABD",
            latitude=57.2868723,
            longitude=-2.3815684,
            country_id=([i.id for i in country_list if i.name == (
                "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Abia",
            state_code="AB",
            latitude=5.4527354,
            longitude=7.5248414,
            country_id=([i.id for i in country_list if i.name == "Nigeria"][0]),
        ))
        list_of_states.append(State(
            name="Abidjan",
            state_code="AB",
            latitude=5.3599517,
            longitude=-4.0082563,
            country_id=([i.id for i in country_list if i.name == (
                "Cote D'Ivoire (Ivory Coast)")][0]),
        ))
        list_of_states.append(State(
            name="Abim District",
            state_code="314",
            latitude=2.706698,
            longitude=33.6595337,
            country_id=([i.id for i in country_list if i.name == "Uganda"][0]),
        ))
        list_of_states.append(State(
            name="Abkhazia",
            state_code="AB",
            latitude=43.0015544,
            longitude=41.023407,
            country_id=([i.id for i in country_list if i.name == "Georgia"][0]),
        ))
        list_of_states.append(State(
            name="Abra",
            state_code="ABR",
            latitude=42.497083,
            longitude=-96.38441,
            country_id=([i.id for i in country_list if i.name == "Philippines"][
                0]),
        ))
        list_of_states.append(State(
            name="Abruzzo",
            state_code="65",
            latitude=42.1920119,
            longitude=13.7289167,
            country_id=([i.id for i in country_list if i.name == "Italy"][0]),
        ))
        list_of_states.append(State(
            name="Absheron District",
            state_code="ABS",
            latitude=40.3629693,
            longitude=49.2736815,
            country_id=([i.id for i in country_list if i.name == "Azerbaijan"][
                0]),
        ))
        list_of_states.append(State(
            name="Abu Dhabi Emirate",
            state_code="AZ",
            latitude=24.453884,
            longitude=54.3773438,
            country_id=([i.id for i in country_list if i.name == (
                "United Arab Emirates")][0]),
        ))
        list_of_states.append(State(
            name="Abuja Federal Capital Territory",
            state_code="FC",
            latitude=8.8940691,
            longitude=7.1860402,
            country_id=([i.id for i in country_list if i.name == "Nigeria"][0]),
        ))
        list_of_states.append(State(
            name="Abyan",
            state_code="AB",
            latitude=13.6343413,
            longitude=46.0563212,
            country_id=([i.id for i in country_list if i.name == "Yemen"][0]),
        ))
        list_of_states.append(State(
            name="Aceh",
            state_code="AC",
            latitude=4.695135,
            longitude=96.7493993,
            country_id=([i.id for i in country_list if i.name == "Indonesia"][
                0]),
        ))
        list_of_states.append(State(
            name="Achaea Regional Unit",
            state_code="13",
            latitude=38.1158729,
            longitude=21.9522491,
            country_id=([i.id for i in country_list if i.name == "Greece"][0]),
        ))
        list_of_states.append(State(
            name="Acklins",
            state_code="AK",
            latitude=22.3657708,
            longitude=-74.0535126,
            country_id=([i.id for i in country_list if i.name == "The Bahamas"][
                                                             0]),
        ))
        list_of_states.append(State(
            name="Acklins and Crooked Islands",
            state_code="AC",
            latitude=22.3657708,
            longitude=-74.0535126,
            country_id=([i.id for i in country_list if i.name == "The Bahamas"][
                                                             0]),
        ))
        list_of_states.append(State(
            name="Açores",
            state_code="20",
            latitude=37.7412488,
            longitude=-25.6755944,
            country_id=([i.id for i in country_list if i.name == "Portugal"][
                0]),
        ))
        list_of_states.append(State(
            name="Acquaviva",
            state_code="01",
            latitude=41.8671597,
            longitude=14.7469479,
            country_id=([i.id for i in country_list if i.name == "San Marino"][
                0]),
        ))
        list_of_states.append(State(
            name="Acre",
            state_code="AC",
            latitude=-9.023796,
            longitude=-70.811995,
            country_id=([i.id for i in country_list if i.name == "Brazil"][0]),
        ))
        list_of_states.append(State(
            name="Ad Dakhiliyah",
            state_code="DA",
            latitude=22.8588758,
            longitude=57.5394356,
            country_id=([i.id for i in country_list if i.name == "Oman"][0]),
        ))
        list_of_states.append(State(
            name="Ad Dhahirah",
            state_code="ZA",
            latitude=23.2161674,
            longitude=56.4907444,
            country_id=([i.id for i in country_list if i.name == "Oman"][0]),
        ))
        list_of_states.append(State(
            name="Adamawa",
            state_code="AD",
            latitude=9.3264751,
            longitude=12.3983853,
            country_id=([i.id for i in country_list if i.name == "Cameroon"][
                0]),
        ))
        list_of_states.append(State(
            name="Adamawa",
            state_code="AD",
            latitude=9.3264751,
            longitude=12.3983853,
            country_id=([i.id for i in country_list if i.name == "Nigeria"][0]),
        ))
        list_of_states.append(State(
            name="Adana",
            state_code="01",
            latitude=37.2612315,
            longitude=35.3905046,
            country_id=([i.id for i in country_list if i.name == "Turkey"][0]),
        ))
        list_of_states.append(State(
            name="Addis Ababa",
            state_code="AA",
            latitude=8.9806034,
            longitude=38.7577605,
            country_id=([i.id for i in country_list if i.name == "Ethiopia"][
                0]),
        ))
        list_of_states.append(State(
            name="Addu Atoll",
            state_code="01",
            latitude=-0.6300995,
            longitude=73.1585626,
            country_id=([i.id for i in country_list if i.name == "Maldives"][
                0]),
        ))
        list_of_states.append(State(
            name="Adıyaman",
            state_code="02",
            latitude=37.9078291,
            longitude=38.4849923,
            country_id=([i.id for i in country_list if i.name == "Turkey"][0]),
        ))
        list_of_states.append(State(
            name="Adjara",
            state_code="AJ",
            latitude=41.6005626,
            longitude=42.0688383,
            country_id=([i.id for i in country_list if i.name == "Georgia"][0]),
        ))
        list_of_states.append(State(
            name="Adjumani District",
            state_code="301",
            latitude=3.2548527,
            longitude=31.7195459,
            country_id=([i.id for i in country_list if i.name == "Uganda"][0]),
        ))
        list_of_states.append(State(
            name="Adjuntas",
            state_code="001",
            latitude=18.1634848,
            longitude=-66.723158,
            country_id=([i.id for i in country_list if i.name == "Puerto Rico"][
                                                             0]),
        ))
        list_of_states.append(State(
            name="Adrar",
            state_code="01",
            latitude=26.418131,
            longitude=-0.6014717,
            country_id=([i.id for i in country_list if i.name == "Algeria"][0]),
        ))
        list_of_states.append(State(
            name="Adrar",
            state_code="07",
            latitude=19.8652176,
            longitude=-12.8054753,
            country_id=([i.id for i in country_list if i.name == "Mauritania"][
                0]),
        ))
        list_of_states.append(State(
            name="Aerodrom Municipality",
            state_code="01",
            latitude=41.9464363,
            longitude=21.4931713,
            country_id=([i.id for i in country_list if i.name == (
                "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Aetolia-Acarnania Regional Unit",
            state_code="01",
            latitude=38.7084386,
            longitude=21.3798928,
            country_id=([i.id for i in country_list if i.name == "Greece"][0]),
        ))
        list_of_states.append(State(
            name="Afar Region",
            state_code="AF",
            latitude=11.7559388,
            longitude=40.958688,
            country_id=([i.id for i in country_list if i.name == "Ethiopia"][
                0]),
        ))
        list_of_states.append(State(
            name="Afyonkarahisar",
            state_code="03",
            latitude=38.7391099,
            longitude=30.7120023,
            country_id=([i.id for i in country_list if i.name == "Turkey"][0]),
        ))
        list_of_states.append(State(
            name="Agadez Region",
            state_code="1",
            latitude=20.6670752,
            longitude=12.0718281,
            country_id=([i.id for i in country_list if i.name == "Niger"][0]),
        ))
        list_of_states.append(State(
            name="Agadir-Ida-Ou-Tanane",
            state_code="AGD",
            latitude=30.6462091,
            longitude=-9.8339061,
            country_id=([i.id for i in country_list if i.name == "Morocco"][0]),
        ))
        list_of_states.append(State(
            name="Agago District",
            state_code="322",
            latitude=2.925082,
            longitude=33.3486147,
            country_id=([i.id for i in country_list if i.name == "Uganda"][0]),
        ))
        list_of_states.append(State(
            name="Agalega Islands",
            state_code="AG",
            latitude=-10.4,
            longitude=56.6166667,
            country_id=([i.id for i in country_list if i.name == "Mauritius"][
                0]),
        ))
        list_of_states.append(State(
            name="Agdam District",
            state_code="AGM",
            latitude=39.9931853,
            longitude=46.9949562,
            country_id=([i.id for i in country_list if i.name == "Azerbaijan"][
                0]),
        ))
        list_of_states.append(State(
            name="Agdash District",
            state_code="AGS",
            latitude=40.6335427,
            longitude=47.467431,
            country_id=([i.id for i in country_list if i.name == "Azerbaijan"][
                0]),
        ))
        list_of_states.append(State(
            name="Agder",
            state_code="42",
            latitude=58.7406934,
            longitude=6.7531521,
            country_id=([i.id for i in country_list if i.name == "Norway"][0]),
        ))
        list_of_states.append(State(
            name="Aghjabadi District",
            state_code="AGC",
            latitude=28.7891841,
            longitude=77.5160788,
            country_id=([i.id for i in country_list if i.name == "Azerbaijan"][
                0]),
        ))
        list_of_states.append(State(
            name="Aglona Municipality",
            state_code="001",
            latitude=56.1089006,
            longitude=27.1286227,
            country_id=([i.id for i in country_list if i.name == "Latvia"][0]),
        ))
        list_of_states.append(State(
            name="Agnéby",
            state_code="16",
            latitude=5.3224503,
            longitude=-4.3449529,
            country_id=([i.id for i in country_list if i.name == (
                "Cote D'Ivoire (Ivory Coast)")][0]),
        ))
        list_of_states.append(State(
            name="Ağrı",
            state_code="04",
            latitude=39.6269218,
            longitude=43.0215965,
            country_id=([i.id for i in country_list if i.name == "Turkey"][0]),
        ))
        list_of_states.append(State(
            name="Agrigento",
            state_code="AG",
            latitude=37.3105202,
            longitude=13.5857978,
            country_id=([i.id for i in country_list if i.name == "Italy"][0]),
        ))
        list_of_states.append(State(
            name="Agstafa District",
            state_code="AGA",
            latitude=41.2655933,
            longitude=45.5134291,
            country_id=([i.id for i in country_list if i.name == "Azerbaijan"][
                0]),
        ))
        list_of_states.append(State(
            name="Agsu District",
            state_code="AGU",
            latitude=40.5283339,
            longitude=48.3650835,
            country_id=([i.id for i in country_list if i.name == "Azerbaijan"][
                0]),
        ))
        list_of_states.append(State(
            name="Aguada",
            state_code="003",
            latitude=18.3801579,
            longitude=-67.188704,
            country_id=([i.id for i in country_list if i.name == "Puerto Rico"][
                                                             0]),
        ))
        list_of_states.append(State(
            name="Aguadilla",
            state_code="005",
            latitude=18.4274454,
            longitude=-67.1540698,
            country_id=([i.id for i in country_list if i.name == "Puerto Rico"][
                                                             0]),
        ))
        list_of_states.append(State(
            name="Aguas Buenas",
            state_code="007",
            latitude=18.2568989,
            longitude=-66.1029442,
            country_id=([i.id for i in country_list if i.name == "Puerto Rico"][
                                                             0]),
        ))
        list_of_states.append(State(
            name="Aguascalientes",
            state_code="AGU",
            latitude=21.8852562,
            longitude=-102.2915677,
            country_id=([i.id for i in country_list if i.name == "Mexico"][0]),
        ))
        list_of_states.append(State(
            name="Agusan del Norte",
            state_code="AGN",
            latitude=8.9456259,
            longitude=125.5319234,
            country_id=([i.id for i in country_list if i.name == "Philippines"][
                                                             0]),
        ))
        list_of_states.append(State(
            name="Agusan del Sur",
            state_code="AGS",
            latitude=8.0463888,
            longitude=126.0615384,
            country_id=([i.id for i in country_list if i.name == "Philippines"][
                                                             0]),
        ))
        list_of_states.append(State(
            name="Ahafo",
            state_code="AF",
            latitude=7.5821372,
            longitude=-2.5497463,
            country_id=([i.id for i in country_list if i.name == "Ghana"][0]),
        ))
        list_of_states.append(State(
            name="Ahal Region",
            state_code="A",
            latitude=38.6399398,
            longitude=59.4720904,
            country_id=([i.id for i in country_list if i.name == (
                "Turkmenistan")][0]),
        ))
        list_of_states.append(State(
            name="Ahuachapán Department",
            state_code="AH",
            latitude=13.8216148,
            longitude=-89.9253233,
            country_id=([i.id for i in country_list if i.name == (
                "El Salvador")][0]),
        ))
        list_of_states.append(State(
            name="Aibonito",
            state_code="009",
            latitude=18.1399594,
            longitude=-66.2660016,
            country_id=([i.id for i in country_list if i.name == (
                "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Aichi Prefecture",
            state_code="23",
            latitude=35.0182505,
            longitude=137.2923893,
            country_id=([i.id for i in country_list if i.name == "Japan"][0]),
        ))
        list_of_states.append(State(
            name="Aiga-i-le-Tai",
            state_code="AL",
            latitude=-13.8513791,
            longitude=-172.0325401,
            country_id=([i.id for i in country_list if i.name == "Samoa"][0]),
        ))
        list_of_states.append(State(
            name="Aileu municipality",
            state_code="AL",
            latitude=-8.7043994,
            longitude=125.6095474,
            country_id=([i.id for i in country_list if i.name == "Timor-Leste"][
                                                             0]),
        ))
        list_of_states.append(State(
            name="Aimeliik",
            state_code="002",
            latitude=7.4455859,
            longitude=134.5030878,
            country_id=([i.id for i in country_list if i.name == "Palau"][0]),
        ))
        list_of_states.append(State(
            name="Ain",
            state_code="01",
            latitude=46.065086,
            longitude=4.888615,
            country_id=([i.id for i in country_list if i.name == "France"][0]),
        ))
        list_of_states.append(State(
            name="Aïn Defla",
            state_code="44",
            latitude=36.2509429,
            longitude=1.9393815,
            country_id=([i.id for i in country_list if i.name == "Algeria"][0]),
        ))
        list_of_states.append(State(
            name="Aïn Témouchent",
            state_code="46",
            latitude=35.2992698,
            longitude=-1.1392792,
            country_id=([i.id for i in country_list if i.name == "Algeria"][0]),
        ))
        list_of_states.append(State(
            name="Ainaro Municipality",
            state_code="AN",
            latitude=-9.0113171,
            longitude=125.5220012,
            country_id=([i.id for i in country_list if i.name == "Timor-Leste"][
                                                             0]),
        ))
        list_of_states.append(State(
            name="Airai",
            state_code="004",
            latitude=7.3966118,
            longitude=134.5690225,
            country_id=([i.id for i in country_list if i.name == "Palau"][0]),
        ))
        list_of_states.append(State(
            name="Aisén del General Carlos Ibañez del Campo",
            state_code="AI",
            latitude=-46.378345,
            longitude=-72.3007623,
            country_id=([i.id for i in country_list if i.name == "Chile"][0]),
        ))
        list_of_states.append(State(
            name="Aisne",
            state_code="02",
            latitude=49.4528921,
            longitude=3.0465111,
            country_id=([i.id for i in country_list if i.name == "France"][0]),
        ))
        list_of_states.append(State(
            name="Aiwo District",
            state_code="01",
            latitude=-0.5340012,
            longitude=166.9138873,
            country_id=([i.id for i in country_list if i.name == "Nauru"][0]),
        ))
        list_of_states.append(State(
            name="Aizkraukle Municipality",
            state_code="002",
            latitude=56.646108,
            longitude=25.2370854,
            country_id=([i.id for i in country_list if i.name == "Latvia"][0]),
        ))
        list_of_states.append(State(
            name="Aizpute Municipality",
            state_code="003",
            latitude=56.7182596,
            longitude=21.6072759,
            country_id=([i.id for i in country_list if i.name == "Latvia"][0]),
        ))
        list_of_states.append(State(
            name="Ajdovščina Municipality",
            state_code="001",
            latitude=45.8870776,
            longitude=13.9042818,
            country_id=([i.id for i in country_list if i.name == "Slovenia"][
                0]),
        ))
        list_of_states.append(State(
            name="Ajloun",
            state_code="AJ",
            latitude=32.3325584,
            longitude=35.7516844,
            country_id=([i.id for i in country_list if i.name == "Jordan"][0]),
        ))
        list_of_states.append(State(
            name="Ajman Emirate",
            state_code="AJ",
            latitude=25.4052165,
            longitude=55.5136433,
            country_id=([i.id for i in country_list if i.name == (
                "United Arab Emirates")][0]),
        ))
        list_of_states.append(State(
            name="Akita Prefecture",
            state_code="05",
            latitude=40.1376293,
            longitude=140.334341,
            country_id=([i.id for i in country_list if i.name == "Japan"][0]),
        ))
        list_of_states.append(State(
            name="Akkar",
            state_code="AK",
            latitude=34.5328763,
            longitude=36.1328132,
            country_id=([i.id for i in country_list if i.name == "Lebanon"][0]),
        ))
        list_of_states.append(State(
            name="Aklan",
            state_code="AKL",
            latitude=11.8166109,
            longitude=122.0941541,
            country_id=([i.id for i in country_list if i.name == "Philippines"][
                                                             0]),
        ))
        list_of_states.append(State(
            name="Akmenė District Municipality",
            state_code="01",
            latitude=56.2455029,
            longitude=22.7471169,
            country_id=([i.id for i in country_list if i.name == "Lithuania"][
                0]),
        ))
        list_of_states.append(State(
            name="Akmola Region",
            state_code="AKM",
            latitude=51.916532,
            longitude=69.4110494,
            country_id=([i.id for i in country_list if i.name == "Kazakhstan"][
                0]),
        ))
        list_of_states.append(State(
            name="Aknīste Municipality",
            state_code="004",
            latitude=56.1613037,
            longitude=25.7484827,
            country_id=([i.id for i in country_list if i.name == "Latvia"][0]),
        ))
        list_of_states.append(State(
            name="Aksaray",
            state_code="68",
            latitude=38.3352043,
            longitude=33.9750018,
            country_id=([i.id for i in country_list if i.name == "Turkey"][0]),
        ))
        list_of_states.append(State(
            name="Aktobe Region",
            state_code="AKT",
            latitude=48.7797078,
            longitude=57.9974378,
            country_id=([i.id for i in country_list if i.name == "Kazakhstan"][
                0]),
        ))
        list_of_states.append(State(
            name="Akwa Ibom",
            state_code="AK",
            latitude=4.9057371,
            longitude=7.8536675,
            country_id=([i.id for i in country_list if i.name == "Nigeria"][0]),
        ))
        list_of_states.append(State(
            name="Al Ahmadi",
            state_code="AH",
            latitude=28.5745125,
            longitude=48.1024743,
            country_id=([i.id for i in country_list if i.name == "Kuwait"][0]),
        ))
        list_of_states.append(State(
            name="Al Anbar",
            state_code="AN",
            latitude=32.5597614,
            longitude=41.9196471,
            country_id=([i.id for i in country_list if i.name == "Iraq"][0]),
        ))
        list_of_states.append(State(
            name="Al Bahah",
            state_code="11",
            latitude=20.2722739,
            longitude=41.441251,
            country_id=([i.id for i in country_list if i.name == (
                "Saudi Arabia")][0]),
        ))
        list_of_states.append(State(
            name="Al Batinah North",
            state_code="BS",
            latitude=24.3419846,
            longitude=56.7298904,
            country_id=([i.id for i in country_list if i.name == "Oman"][0]),
        ))
        list_of_states.append(State(
            name="Al Batinah Region",
            state_code="BA",
            latitude=24.3419846,
            longitude=56.7298904,
            country_id=([i.id for i in country_list if i.name == "Oman"][0]),
        ))
        list_of_states.append(State(
            name="Al Batinah South",
            state_code="BJ",
            latitude=23.4314903,
            longitude=57.4239796,
            country_id=([i.id for i in country_list if i.name == "Oman"][0]),
        ))
        list_of_states.append(State(
            name="Al Bayda'",
            state_code="BA",
            latitude=14.3588662,
            longitude=45.4498065,
            country_id=([i.id for i in country_list if i.name == "Yemen"][0]),
        ))
        list_of_states.append(State(
            name="Al Buraimi",
            state_code="BU",
            latitude=24.1671413,
            longitude=56.1142253,
            country_id=([i.id for i in country_list if i.name == "Oman"][0]),
        ))
        list_of_states.append(State(
            name="Al Daayen",
            state_code="ZA",
            latitude=25.5784559,
            longitude=51.4821387,
            country_id=([i.id for i in country_list if i.name == "Qatar"][0]),
        ))
        list_of_states.append(State(
            name="Al Farwaniyah",
            state_code="FA",
            latitude=29.273357,
            longitude=47.9400154,
            country_id=([i.id for i in country_list if i.name == "Kuwait"][0]),
        ))
        list_of_states.append(State(
            name="Al Haouz",
            state_code="HAO",
            latitude=31.2956729,
            longitude=-7.87216,
            country_id=([i.id for i in country_list if i.name == "Morocco"][0]),
        ))
        list_of_states.append(State(
            name="Al Hoceïma",
            state_code="HOC",
            latitude=35.2445589,
            longitude=-3.9317468,
            country_id=([i.id for i in country_list if i.name == "Morocco"][0]),
        ))
        list_of_states.append(State(
            name="Al Hudaydah",
            state_code="HU",
            latitude=15.3053072,
            longitude=43.0194897,
            country_id=([i.id for i in country_list if i.name == "Yemen"][0]),
        ))
        list_of_states.append(State(
            name="Al Jahra",
            state_code="JA",
            latitude=29.9931831,
            longitude=47.7634731,
            country_id=([i.id for i in country_list if i.name == "Kuwait"][0]),
        ))
        list_of_states.append(State(
            name="Al Jawf",
            state_code="12",
            latitude=29.887356,
            longitude=39.3206241,
            country_id=([i.id for i in country_list if i.name == (
                "Saudi Arabia")][0]),
        ))
        list_of_states.append(State(
            name="Al Jawf",
            state_code="JA",
            latitude=16.7901819,
            longitude=45.2993862,
            country_id=([i.id for i in country_list if i.name == "Yemen"][0]),
        ))
        list_of_states.append(State(
            name="Al Jazirah",
            state_code="GZ",
            latitude=14.8859611,
            longitude=33.438353,
            country_id=([i.id for i in country_list if i.name == "Sudan"][0]),
        ))
        list_of_states.append(State(
            name="Al Khor",
            state_code="KH",
            latitude=25.6804078,
            longitude=51.4968502,
            country_id=([i.id for i in country_list if i.name == "Qatar"][0]),
        ))
        list_of_states.append(State(
            name="Al Madinah",
            state_code="03",
            latitude=24.8403977,
            longitude=39.3206241,
            country_id=([i.id for i in country_list if i.name == (
                "Saudi Arabia")][0]),
        ))
        list_of_states.append(State(
            name="Al Mahrah",
            state_code="MR",
            latitude=16.5238423,
            longitude=51.6834275,
            country_id=([i.id for i in country_list if i.name == "Yemen"][0]),
        ))
        list_of_states.append(State(
            name="Al Mahwit",
            state_code="MW",
            latitude=15.3963229,
            longitude=43.5606946,
            country_id=([i.id for i in country_list if i.name == "Yemen"][0]),
        ))
        list_of_states.append(State(
            name="Al Muthanna",
            state_code="MU",
            latitude=29.9133171,
            longitude=45.2993862,
            country_id=([i.id for i in country_list if i.name == "Iraq"][0]),
        ))
        list_of_states.append(State(
            name="Al Qadarif",
            state_code="GD",
            latitude=14.024307,
            longitude=35.3685679,
            country_id=([i.id for i in country_list if i.name == "Sudan"][0]),
        ))
        list_of_states.append(State(
            name="Al Rayyan Municipality",
            state_code="RA",
            latitude=25.2522551,
            longitude=51.4388713,
            country_id=([i.id for i in country_list if i.name == "Qatar"][0]),
        ))
        list_of_states.append(State(
            name="Al Wahat District",
            state_code="WA",
            latitude=29.0466808,
            longitude=21.8568586,
            country_id=([i.id for i in country_list if i.name == "Libya"][0]),
        ))
        list_of_states.append(State(
            name="Al Wakrah",
            state_code="WA",
            latitude=25.1659314,
            longitude=51.5975524,
            country_id=([i.id for i in country_list if i.name == "Qatar"][0]),
        ))
        list_of_states.append(State(
            name="Al Wusta",
            state_code="WU",
            latitude=19.9571078,
            longitude=56.2756846,
            country_id=([i.id for i in country_list if i.name == "Oman"][0]),
        ))
        list_of_states.append(State(
            name="Al-Hasakah",
            state_code="HA",
            latitude=36.405515,
            longitude=40.7969149,
            country_id=([i.id for i in country_list if i.name == "Syria"][0]),
        ))
        list_of_states.append(State(
            name="Al-Qādisiyyah",
            state_code="QA",
            latitude=32.043691,
            longitude=45.1494505,
            country_id=([i.id for i in country_list if i.name == "Iraq"][0]),
        ))
        list_of_states.append(State(
            name="Al-Qassim",
            state_code="05",
            latitude=26.207826,
            longitude=43.483738,
            country_id=([i.id for i in country_list if i.name == (
                "Saudi Arabia")][0]),
        ))
        list_of_states.append(State(
            name="Al-Raqqah",
            state_code="RA",
            latitude=35.9594106,
            longitude=38.9981052,
            country_id=([i.id for i in country_list if i.name == "Syria"][0]),
        ))
        list_of_states.append(State(
            name="Al-Shahaniya",
            state_code="SH",
            latitude=25.4106386,
            longitude=51.1846025,
            country_id=([i.id for i in country_list if i.name == "Qatar"][0]),
        ))
        list_of_states.append(State(
            name="Alabama",
            state_code="AL",
            latitude=32.3182314,
            longitude=-86.902298,
            country_id=([i.id for i in country_list if i.name == (
                "United States")][0]),
        ))
        list_of_states.append(State(
            name="Alagoas",
            state_code="AL",
            latitude=-9.5713058,
            longitude=-36.7819505,
            country_id=([i.id for i in country_list if i.name == "Brazil"][0]),
        ))
        list_of_states.append(State(
            name="Alajuela Province",
            state_code="A",
            latitude=10.391583,
            longitude=-84.4382721,
            country_id=([i.id for i in country_list if i.name == (
                "Costa Rica")][0]),
        ))
        list_of_states.append(State(
            name="Åland Islands",
            state_code="01",
            latitude=60.1785247,
            longitude=19.9156105,
            country_id=([i.id for i in country_list if i.name == "Finland"][0]),
        ))
        list_of_states.append(State(
            name="Alaska",
            state_code="AK",
            latitude=64.2008413,
            longitude=-149.4936733,
            country_id=([i.id for i in country_list if i.name == (
                "United States")][0]),
        ))
        list_of_states.append(State(
            name="Alba",
            state_code="AB",
            latitude=44.7009153,
            longitude=8.0356911,
            country_id=([i.id for i in country_list if i.name == "Romania"][0]),
        ))
        list_of_states.append(State(
            name="Albacete",
            state_code="AB",
            latitude=38.9922312,
            longitude=-1.8780989,
            country_id=([i.id for i in country_list if i.name == "Spain"][0]),
        ))
        list_of_states.append(State(
            name="Albay",
            state_code="ALB",
            latitude=13.1774827,
            longitude=123.5280072,
            country_id=([i.id for i in country_list if i.name == "Philippines"][
                                                             0]),
        ))
        list_of_states.append(State(
            name="Alberta",
            state_code="AB",
            latitude=53.9332706,
            longitude=-116.5765035,
            country_id=([i.id for i in country_list if i.name == "Canada"][0]),
        ))
        list_of_states.append(State(
            name="Alborz",
            state_code="30",
            latitude=35.9960467,
            longitude=50.9289246,
            country_id=([i.id for i in country_list if i.name == "Iran"][0]),
        ))
        list_of_states.append(State(
            name="Alebtong District",
            state_code="323",
            latitude=2.2545773,
            longitude=33.3486147,
            country_id=([i.id for i in country_list if i.name == "Uganda"][0]),
        ))
        list_of_states.append(State(
            name="Aleppo",
            state_code="HL",
            latitude=36.2262393,
            longitude=37.4681396,
            country_id=([i.id for i in country_list if i.name == "Syria"][0]),
        ))
        list_of_states.append(State(
            name="Alessandria",
            state_code="AL",
            latitude=44.8175587,
            longitude=8.7046627,
            country_id=([i.id for i in country_list if i.name == "Italy"][0]),
        ))
        list_of_states.append(State(
            name="Alexandria",
            state_code="ALX",
            latitude=30.8760568,
            longitude=29.742604,
            country_id=([i.id for i in country_list if i.name == "Egypt"][0]),
        ))
        list_of_states.append(State(
            name="Algiers",
            state_code="16",
            latitude=36.6997294,
            longitude=3.0576199,
            country_id=([i.id for i in country_list if i.name == "Algeria"][0]),
        ))
        list_of_states.append(State(
            name="Ali Sabieh Region",
            state_code="AS",
            latitude=11.1928973,
            longitude=42.941698,
            country_id=([i.id for i in country_list if i.name == "Djibouti"][
                0]),
        ))
        list_of_states.append(State(
            name="Alibori Department",
            state_code="AL",
            latitude=10.9681093,
            longitude=2.7779813,
            country_id=([i.id for i in country_list if i.name == "Benin"][0]),
        ))
        list_of_states.append(State(
            name="Alicante",
            state_code="A",
            latitude=38.3579546,
            longitude=-0.5425634,
            country_id=([i.id for i in country_list if i.name == "Spain"][0]),
        ))
        list_of_states.append(State(
            name="Alif Alif Atoll",
            state_code="02",
            latitude=4.085,
            longitude=72.8515479,
            country_id=([i.id for i in country_list if i.name == "Maldives"][
                0]),
        ))
        list_of_states.append(State(
            name="Alif Dhaal Atoll",
            state_code="00",
            latitude=3.6543302,
            longitude=72.8042797,
            country_id=([i.id for i in country_list if i.name == "Maldives"][
                0]),
        ))
        list_of_states.append(State(
            name="Allier",
            state_code="03",
            latitude=46.3670863,
            longitude=2.5808277,
            country_id=([i.id for i in country_list if i.name == "France"][0]),
        ))
        list_of_states.append(State(
            name="Almaty",
            state_code="ALA",
            latitude=43.2220146,
            longitude=76.8512485,
            country_id=([i.id for i in country_list if i.name == "Kazakhstan"][
                0]),
        ))
        list_of_states.append(State(
            name="Almaty Region",
            state_code="ALM",
            latitude=45.0119227,
            longitude=78.4229392,
            country_id=([i.id for i in country_list if i.name == "Kazakhstan"][
                0]),
        ))
        list_of_states.append(State(
            name="Almeria",
            state_code="AL",
            latitude=36.8415268,
            longitude=-2.4746261,
            country_id=([i.id for i in country_list if i.name == "Spain"][0]),
        ))
        list_of_states.append(State(
            name="Aloja Municipality",
            state_code="005",
            latitude=57.767136,
            longitude=24.8770839,
            country_id=([i.id for i in country_list if i.name == "Latvia"][0]),
        ))
        list_of_states.append(State(
            name="Alpes-de-Haute-Provence",
            state_code="04",
            latitude=44.1637752,
            longitude=5.672478,
            country_id=([i.id for i in country_list if i.name == "France"][0]),
        ))
        list_of_states.append(State(
            name="Alpes-Maritimes",
            state_code="06",
            latitude=43.920417,
            longitude=6.6167822,
            country_id=([i.id for i in country_list if i.name == "France"][0]),
        ))
        list_of_states.append(State(
            name="Alsace",
            state_code="6AE",
            latitude=48.3181795,
            longitude=7.4416241,
            country_id=([i.id for i in country_list if i.name == "France"][0]),
        ))
        list_of_states.append(State(
            name="Alsunga Municipality",
            state_code="006",
            latitude=56.9828531,
            longitude=21.5555919,
            country_id=([i.id for i in country_list if i.name == "Latvia"][0]),
        ))
        list_of_states.append(State(
            name="Alta Verapaz Department",
            state_code="AV",
            latitude=15.5942883,
            longitude=-90.1494988,
            country_id=([i.id for i in country_list if i.name == "Guatemala"][
                0]),
        ))
        list_of_states.append(State(
            name="Altai Krai",
            state_code="ALT",
            latitude=51.7936298,
            longitude=82.6758596,
            country_id=([i.id for i in country_list if i.name == "Russia"][0]),
        ))
        list_of_states.append(State(
            name="Altai Republic",
            state_code="AL",
            latitude=50.6181924,
            longitude=86.2199308,
            country_id=([i.id for i in country_list if i.name == "Russia"][0]),
        ))
        list_of_states.append(State(
            name="Alto Paraguay Department",
            state_code="16",
            latitude=-20.0852508,
            longitude=-59.4720904,
            country_id=([i.id for i in country_list if i.name == "Paraguay"][
                0]),
        ))
        list_of_states.append(State(
            name="Alto Paraná Department",
            state_code="10",
            latitude=-25.6075546,
            longitude=-54.9611836,
            country_id=([i.id for i in country_list if i.name == "Paraguay"][
                0]),
        ))
        list_of_states.append(State(
            name="Alūksne Municipality",
            state_code="007",
            latitude=57.4254485,
            longitude=27.0424968,
            country_id=([i.id for i in country_list if i.name == "Latvia"][0]),
        ))
        list_of_states.append(State(
            name="Alytus City Municipality",
            state_code="02",
            latitude=54.3962938,
            longitude=24.0458761,
            country_id=([i.id for i in country_list if i.name == "Lithuania"][
                0]),
        ))
        list_of_states.append(State(
            name="Alytus County",
            state_code="AL",
            latitude=54.2000214,
            longitude=24.1512634,
            country_id=([i.id for i in country_list if i.name == "Lithuania"][
                0]),
        ))
        list_of_states.append(State(
            name="Alytus District Municipality",
            state_code="03",
            latitude=54.3297496,
            longitude=24.1960931,
            country_id=([i.id for i in country_list if i.name == "Lithuania"][
                0]),
        ))
        list_of_states.append(State(
            name="Amambay Department",
            state_code="13",
            latitude=-22.5590272,
            longitude=-56.0249982,
            country_id=([i.id for i in country_list if i.name == "Paraguay"][
                0]),
        ))
        list_of_states.append(State(
            name="Amanat Al Asimah",
            state_code="SA",
            latitude=15.3694451,
            longitude=44.1910066,
            country_id=([i.id for i in country_list if i.name == "Yemen"][0]),
        ))
        list_of_states.append(State(
            name="Amapá",
            state_code="AP",
            latitude=0.9019925,
            longitude=-52.0029565,
            country_id=([i.id for i in country_list if i.name == "Brazil"][0]),
        ))
        list_of_states.append(State(
            name="Amasya",
            state_code="05",
            latitude=40.6516608,
            longitude=35.9037966,
            country_id=([i.id for i in country_list if i.name == "Turkey"][0]),
        ))
        list_of_states.append(State(
            name="Amata Municipality",
            state_code="008",
            latitude=56.9938726,
            longitude=25.2627675,
            country_id=([i.id for i in country_list if i.name == "Latvia"][0]),
        ))
        list_of_states.append(State(
            name="Amazonas",
            state_code="AM",
            latitude=-3.07,
            longitude=-61.66,
            country_id=([i.id for i in country_list if i.name == "Brazil"][0]),
        ))
        list_of_states.append(State(
            name="Amazonas",
            state_code="AMA",
            latitude=-1.4429123,
            longitude=-71.5723953,
            country_id=([i.id for i in country_list if i.name == "Colombia"][
                0]),
        ))
        list_of_states.append(State(
            name="Amazonas",
            state_code="AMA",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list if i.name == "Peru"][0]),
        ))
        list_of_states.append(State(
            name="Amazonas",
            state_code="Z",
            latitude=-3.4168427,
            longitude=-65.8560646,
            country_id=([i.id for i in country_list if i.name == "Venezuela"][
                0]),
        ))
        list_of_states.append(State(
            name="American Samoa",
            state_code="AS",
            latitude=-14.270972,
            longitude=-170.132217,
            country_id=([i.id for i in country_list if i.name == (
                "United States")][0]),
        ))
        list_of_states.append(State(
            name="Amhara Region",
            state_code="AM",
            latitude=11.3494247,
            longitude=37.9784585,
            country_id=([i.id for i in country_list if i.name == (
                "Ethiopia")][0]),
        ))
        list_of_states.append(State(
            name="Amman",
            state_code="AM",
            latitude=31.9453633,
            longitude=35.9283895,
            country_id=([i.id for i in country_list if i.name == "Jordan"][0]),
        ))
        list_of_states.append(State(
            name="Amnat Charoen",
            state_code="37",
            latitude=15.8656783,
            longitude=104.6257774,
            country_id=([i.id for i in country_list if i.name == (
                "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Amolatar District",
            state_code="315",
            latitude=1.6054402,
            longitude=32.8084496,
            country_id=([i.id for i in country_list if i.name == "Uganda"][0]),
        ))
        list_of_states.append(State(
            name="Ampara District",
            state_code="52",
            latitude=7.2911685,
            longitude=81.6723761,
            country_id=([i.id for i in country_list if i.name == (
                "Sri Lanka")][0]),
        ))
        list_of_states.append(State(
            name="Amudat District",
            state_code="324",
            latitude=1.7916224,
            longitude=34.906551,
            country_id=([i.id for i in country_list if i.name == "Uganda"][0]),
        ))
        list_of_states.append(State(
            name="Amur Oblast",
            state_code="AMU",
            latitude=54.6035065,
            longitude=127.4801721,
            country_id=([i.id for i in country_list if i.name == "Russia"][0]),
        ))
        list_of_states.append(State(
            name="Amuria District",
            state_code="216",
            latitude=2.03017,
            longitude=33.6427533,
            country_id=([i.id for i in country_list if i.name == "Uganda"][0]),
        ))
        list_of_states.append(State(
            name="Amuru District",
            state_code="316",
            latitude=2.9667878,
            longitude=32.0837445,
            country_id=([i.id for i in country_list if i.name == "Uganda"][0]),
        ))
        list_of_states.append(State(
            name="An Giang",
            state_code="44",
            latitude=10.5215836,
            longitude=105.1258955,
            country_id=([i.id for i in country_list if i.name == "Vietnam"][0]),
        ))
        list_of_states.append(State(
            name="Anabar District",
            state_code="02",
            latitude=-0.5133517,
            longitude=166.9484624,
            country_id=([i.id for i in country_list if i.name == "Nauru"][0]),
        ))
        list_of_states.append(State(
            name="Anambra",
            state_code="AN",
            latitude=6.2208997,
            longitude=6.9369559,
            country_id=([i.id for i in country_list if i.name == "Nigeria"][0]),
        ))
        list_of_states.append(State(
            name="Añasco",
            state_code="011",
            latitude=18.2854476,
            longitude=-67.1402935,
            country_id=([i.id for i in country_list if i.name == "Puerto Rico"][
                                                             0]),
        ))
        list_of_states.append(State(
            name="Áncash",
            state_code="ANC",
            latitude=-9.3250497,
            longitude=-77.5619419,
            country_id=([i.id for i in country_list if i.name == "Peru"][0]),
        ))
        list_of_states.append(State(
            name="Ancona",
            state_code="AN",
            latitude=43.5493245,
            longitude=13.2663479,
            country_id=([i.id for i in country_list if i.name == "Italy"][0]),
        ))
        list_of_states.append(State(
            name="Andaman and Nicobar Islands",
            state_code="AN",
            latitude=11.7400867,
            longitude=92.6586401,
            country_id=([i.id for i in country_list if i.name == "India"][0]),
        ))
        list_of_states.append(State(
            name="Andhra Pradesh",
            state_code="AP",
            latitude=15.9128998,
            longitude=79.7399875,
            country_id=([i.id for i in country_list if i.name == "India"][0]),
        ))
        list_of_states.append(State(
            name="Andijan Region",
            state_code="AN",
            latitude=40.7685941,
            longitude=72.236379,
            country_id=([i.id for i in country_list if i.name == "Uzbekistan"][
                0]),
        ))
        list_of_states.append(State(
            name="Andorra la Vella",
            state_code="07",
            latitude=42.5063174,
            longitude=1.5218355,
            country_id=([i.id for i in country_list if i.name == "Andorra"][0]),
        ))
        list_of_states.append(State(
            name="Andrijevica Municipality",
            state_code="01",
            latitude=42.7362477,
            longitude=19.7859556,
            country_id=([i.id for i in country_list if i.name == "Montenegro"][
                0]),
        ))
        list_of_states.append(State(
            name="Anenii Noi District",
            state_code="AN",
            latitude=46.8795663,
            longitude=29.2312175,
            country_id=([i.id for i in country_list if i.name == "Moldova"][0]),
        ))
        list_of_states.append(State(
            name="Anetan District",
            state_code="03",
            latitude=-0.5064343,
            longitude=166.9427006,
            country_id=([i.id for i in country_list if i.name == "Nauru"][0]),
        ))
        list_of_states.append(State(
            name="Ang Thong",
            state_code="15",
            latitude=14.5896054,
            longitude=100.455052,
            country_id=([i.id for i in country_list if i.name == "Thailand"][
                0]),
        ))
        list_of_states.append(State(
            name="Angaur",
            state_code="010",
            latitude=6.909223,
            longitude=134.1387934,
            country_id=([i.id for i in country_list if i.name == "Palau"][0]),
        ))
        list_of_states.append(State(
            name="Angus",
            state_code="ANS",
            latitude=37.2757886,
            longitude=-95.6501033,
            country_id=([i.id for i in country_list if i.name == (
                "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Anhui",
            state_code="AH",
            latitude=30.6006773,
            longitude=117.9249002,
            country_id=([i.id for i in country_list if i.name == "China"][0]),
        ))
        list_of_states.append(State(
            name="Anibare District",
            state_code="04",
            latitude=-0.5294758,
            longitude=166.9513432,
            country_id=([i.id for i in country_list if i.name == "Nauru"][0]),
        ))
        list_of_states.append(State(
            name="Anjouan",
            state_code="A",
            latitude=-12.2138145,
            longitude=44.4370606,
            country_id=([i.id for i in country_list if i.name == "Comoros"][0]),
        ))
        list_of_states.append(State(
            name="Ankara",
            state_code="06",
            latitude=39.7805245,
            longitude=32.7181375,
            country_id=([i.id for i in country_list if i.name == "Turkey"][0]),
        ))
        list_of_states.append(State(
            name="Ankaran Municipality",
            state_code="213",
            latitude=45.578451,
            longitude=13.7369174,
            country_id=([i.id for i in country_list if i.name == "Slovenia"][
                0]),
        ))
        list_of_states.append(State(
            name="Annaba",
            state_code="23",
            latitude=36.8020508,
            longitude=7.5247243,
            country_id=([i.id for i in country_list if i.name == "Algeria"][0]),
        ))
        list_of_states.append(State(
            name="Annobón Province",
            state_code="AN",
            latitude=-1.4268782,
            longitude=5.6352801,
            country_id=([i.id for i in country_list if i.name == (
                "Equatorial Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Anse Boileau",
            state_code="02",
            latitude=-4.7047268,
            longitude=55.4859363,
            country_id=([i.id for i in country_list if i.name == "Seychelles"][
                0]),
        ))
        list_of_states.append(State(
            name="Anse la Raye Quarter",
            state_code="01",
            latitude=13.9459424,
            longitude=-61.0369468,
            country_id=([i.id for i in country_list if i.name == (
                "Saint Lucia")][0]),
        ))
        list_of_states.append(State(
            name="Anse Royale",
            state_code="05",
            latitude=-4.7407988,
            longitude=55.5081012,
            country_id=([i.id for i in country_list if i.name == (
                "Seychelles")][0]),
        ))
        list_of_states.append(State(
            name="Anse-aux-Pins",
            state_code="01",
            latitude=-4.6900443,
            longitude=55.5150289,
            country_id=([i.id for i in country_list if i.name == "Seychelles"][
                0]),
        ))
        list_of_states.append(State(
            name="Anseba Region",
            state_code="AN",
            latitude=16.4745531,
            longitude=37.8087693,
            country_id=([i.id for i in country_list if i.name == "Eritrea"][0]),
        ))
        list_of_states.append(State(
            name="Antalya",
            state_code="07",
            latitude=37.0951672,
            longitude=31.0793705,
            country_id=([i.id for i in country_list if i.name == "Turkey"][0]),
        ))
        list_of_states.append(State(
            name="Antananarivo Province",
            state_code="T",
            latitude=-18.7051474,
            longitude=46.8252838,
            country_id=([i.id for i in country_list if i.name == "Madagascar"][
                0]),
        ))
        list_of_states.append(State(
            name="Antioquia",
            state_code="ANT",
            latitude=7.1986064,
            longitude=-75.3412179,
            country_id=([i.id for i in country_list if i.name == "Colombia"][
                0]),
        ))
        list_of_states.append(State(
            name="Antique",
            state_code="ANT",
            latitude=37.0358695,
            longitude=-95.6361694,
            country_id=([i.id for i in country_list if i.name == "Philippines"][
                                                             0]),
        ))
        list_of_states.append(State(
            name="Antofagasta",
            state_code="AN",
            latitude=-23.8369104,
            longitude=-69.2877535,
            country_id=([i.id for i in country_list if i.name == "Chile"][0]),
        ))
        list_of_states.append(State(
            name="Antrim",
            state_code="ANT",
            latitude=54.7195338,
            longitude=-6.2072498,
            country_id=([i.id for i in country_list if i.name == (
                "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Antrim and Newtownabbey",
            state_code="ANN",
            latitude=54.6956887,
            longitude=-5.9481069,
            country_id=([i.id for i in country_list if i.name == (
                "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Antsiranana Province",
            state_code="D",
            latitude=-13.771539,
            longitude=49.5279996,
            country_id=([i.id for i in country_list if i.name == "Madagascar"][
                0]),
        ))
        list_of_states.append(State(
            name="Antwerp",
            state_code="VAN",
            latitude=51.2194475,
            longitude=4.4024643,
            country_id=([i.id for i in country_list if i.name == "Belgium"][0]),
        ))
        list_of_states.append(State(
            name="Anuradhapura District",
            state_code="71",
            latitude=8.3318305,
            longitude=80.4029017,
            country_id=([i.id for i in country_list if i.name == "Sri Lanka"][
                0]),
        ))
        list_of_states.append(State(
            name="Anzoátegui",
            state_code="B",
            latitude=8.5913073,
            longitude=-63.9586111,
            country_id=([i.id for i in country_list if i.name == "Venezuela"][
                0]),
        ))
        list_of_states.append(State(
            name="Aomori Prefecture",
            state_code="02",
            latitude=40.7657077,
            longitude=140.9175879,
            country_id=([i.id for i in country_list if i.name == "Japan"][0]),
        ))
        list_of_states.append(State(
            name="Aosta Valley",
            state_code="23",
            latitude=45.7388878,
            longitude=7.4261866,
            country_id=([i.id for i in country_list if i.name == "Italy"][0]),
        ))
        list_of_states.append(State(
            name="Aousserd (EH)",
            state_code="AOU",
            latitude=22.5521538,
            longitude=-14.3297353,
            country_id=([i.id for i in country_list if i.name == "Morocco"][0]),
        ))
        list_of_states.append(State(
            name="Apac District",
            state_code="302",
            latitude=1.8730263,
            longitude=32.6277455,
            country_id=([i.id for i in country_list if i.name == "Uganda"][0]),
        ))
        list_of_states.append(State(
            name="Apayao",
            state_code="APA",
            latitude=18.0120304,
            longitude=121.1710389,
            country_id=([i.id for i in country_list if i.name == "Philippines"][
                                                             0]),
        ))
        list_of_states.append(State(
            name="Ape Municipality",
            state_code="009",
            latitude=57.5392697,
            longitude=26.6941649,
            country_id=([i.id for i in country_list if i.name == "Latvia"][0]),
        ))
        list_of_states.append(State(
            name="Appenzell Ausserrhoden",
            state_code="AR",
            latitude=47.366481,
            longitude=9.3000916,
            country_id=([i.id for i in country_list if i.name == "Switzerland"][
                                                             0]),
        ))
        list_of_states.append(State(
            name="Appenzell Innerrhoden",
            state_code="AI",
            latitude=47.3161925,
            longitude=9.4316573,
            country_id=([i.id for i in country_list if i.name == "Switzerland"][
                                                             0]),
        ))
        list_of_states.append(State(
            name="Apulia",
            state_code="75",
            latitude=40.7928393,
            longitude=17.1011931,
            country_id=([i.id for i in country_list if i.name == "Italy"][0]),
        ))
        list_of_states.append(State(
            name="Apure",
            state_code="C",
            latitude=6.9269483,
            longitude=-68.5247149,
            country_id=([i.id for i in country_list if i.name == "Venezuela"][
                0]),
        ))
        list_of_states.append(State(
            name="Apurímac",
            state_code="APU",
            latitude=-14.0504533,
            longitude=-73.087749,
            country_id=([i.id for i in country_list if i.name == "Peru"][0]),
        ))
        list_of_states.append(State(
            name="Aqaba",
            state_code="AQ",
            latitude=29.532086,
            longitude=35.0062821,
            country_id=([i.id for i in country_list if i.name == "Jordan"][0]),
        ))
        list_of_states.append(State(
            name="Araba",
            state_code="VI",
            latitude=42.8395119,
            longitude=-3.8423774,
            country_id=([i.id for i in country_list if i.name == "Spain"][0]),
        ))
        list_of_states.append(State(
            name="Aračinovo Municipality",
            state_code="02",
            latitude=42.0247381,
            longitude=21.5766407,
            country_id=([i.id for i in country_list if i.name == (
                "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Arad County",
            state_code="AR",
            latitude=46.2283651,
            longitude=21.6597819,
            country_id=([i.id for i in country_list if i.name == "Romania"][0]),
        ))
        list_of_states.append(State(
            name="Aragatsotn Region",
            state_code="AG",
            latitude=40.3347301,
            longitude=44.3748296,
            country_id=([i.id for i in country_list if i.name == "Armenia"][0]),
        ))
        list_of_states.append(State(
            name="Aragua",
            state_code="D",
            latitude=10.0635758,
            longitude=-67.2847875,
            country_id=([i.id for i in country_list if i.name == "Venezuela"][
                0]),
        ))
        list_of_states.append(State(
            name="Ararat Province",
            state_code="AR",
            latitude=39.9139415,
            longitude=44.7200004,
            country_id=([i.id for i in country_list if i.name == "Armenia"][0]),
        ))
        list_of_states.append(State(
            name="Arauca",
            state_code="ARA",
            latitude=6.547306,
            longitude=-71.0022311,
            country_id=([i.id for i in country_list if i.name == "Colombia"][
                0]),
        ))
        list_of_states.append(State(
            name="Arcadia Prefecture",
            state_code="12",
            latitude=37.5557825,
            longitude=22.3337769,
            country_id=([i.id for i in country_list if i.name == "Greece"][0]),
        ))
        list_of_states.append(State(
            name="Archipiélago de San Andrés, Providencia y Santa Catalina",
            state_code="SAP",
            latitude=12.5567324,
            longitude=-81.7185253,
            country_id=([i.id for i in country_list if i.name == "Colombia"][
                0]),
        ))
        list_of_states.append(State(
            name="Ardabil",
            state_code="24",
            latitude=38.4853276,
            longitude=47.8911209,
            country_id=([i.id for i in country_list if i.name == "Iran"][0]),
        ))
        list_of_states.append(State(
            name="Ardahan",
            state_code="75",
            latitude=41.1112964,
            longitude=42.7831674,
            country_id=([i.id for i in country_list if i.name == "Turkey"][0]),
        ))
        list_of_states.append(State(
            name="Ardèche",
            state_code="07",
            latitude=44.8148695,
            longitude=3.8133483,
            country_id=([i.id for i in country_list if i.name == "France"][0]),
        ))
        list_of_states.append(State(
            name="Ardennes",
            state_code="08",
            latitude=49.6975951,
            longitude=4.1489576,
            country_id=([i.id for i in country_list if i.name == "France"][0]),
        ))
        list_of_states.append(State(
            name="Ards",
            state_code="ARD",
            latitude=42.1391851,
            longitude=-87.8614972,
            country_id=([i.id for i in country_list if i.name == (
                "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Ards and North Down",
            state_code="AND",
            latitude=54.5899645,
            longitude=-5.5984972,
            country_id=([i.id for i in country_list if i.name == (
                "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Arecibo",
            state_code="013",
            latitude=18.4705137,
            longitude=-66.7218472,
            country_id=([i.id for i in country_list if i.name == "Puerto Rico"][
                                                             0]),
        ))
        list_of_states.append(State(
            name="Arecibo",
            state_code="AR",
            latitude=18.47055556,
            longitude=-66.72083333,
            country_id=([i.id for i in country_list if i.name == "Puerto Rico"][
                                                             0]),
        ))
        list_of_states.append(State(
            name="Arequipa",
            state_code="ARE",
            latitude=-16.4090474,
            longitude=-71.537451,
            country_id=([i.id for i in country_list if i.name == "Peru"][0]),
        ))
        db.session.add_all(list_of_states)
        db.session.commit()
        print(State.__tablename__ + " seeded successfully! (1/21)")
    except Exception as e:
        print(f"Error committing data: {e}")
        raise e
