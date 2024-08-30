"""
States Seed #1 Template

Seed file can be run
cd <base_dir>
PYTHONPATH=<base_dir> python3 <base_dir>/<file_name>.py
"""
'''
from sqlalchemy import inspect, text, MetaData
from sqlalchemy_utils import database_exists, create_database
from secrets_jobs.credentials import (postgres_information_login_details,
                                      postgres_database_name)
from models.postgres.locations.regions import Region
from models.postgres.locations.subregions import Subregion
from models.postgres.locations.countries import Country
from models.postgres.locations.states import State
from models.postgres.locations.cities import City
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

    table_city.drop(engine, checkfirst=True)

    table_state.drop(engine, checkfirst=True)

    table_state.create(engine, checkfirst=True)
    table_city.create(engine, checkfirst=True)
    try:
        country_list = db.session.query(Country).all()
        list_of_states = []

        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                if i.name == (
                    "")][0]),
        ))
        db.session.add_all(list_of_states)
        db.session.commit()
        print("Database seeded successfully!")
    except Exception as e:
        print(f"Error committing data: {e}")

'''
