"""
API List URL

Seed file can be run
cd <base_dir>
PYTHONPATH=<base_dir> python3 <base_dir>/<file_name>.py

Table drop and creation must also drop
    APIEndpoints and APIEndpointParams due to FK restraints
"""
from sqlalchemy import asc, text, MetaData, inspect

from secrets_jobs.credentials import (maria_information_login_details,
                                      mariadb_database_name)
from models.mariadb.api_list_url import APIListURL
from models.mariadb.api_endpoints import APIEndpoint
from models.mariadb.api_endpoint_params import APIEndpointParam
from app import create_app, db
import sqlalchemy as db2
from sqlalchemy_utils import database_exists, create_database


# Function to get the names of foreign key constraints
def get_foreign_key_constraint_names(table, temp_connection):
    """
    Inspect table and get foreign key restraints.
    """
    inspector = inspect(temp_connection)
    fks = inspector.get_foreign_keys(table.name, schema=table.schema)
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
    table1 = db.Table(
        APIListURL.__tablename__,
        bind_key="mariadb",
        autoload_with=engine)

    metadata = MetaData()
    table2 = db.Table(
        APIEndpoint.__tablename__,
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

    table3 = db.Table(
        APIEndpointParam.__tablename__,
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

    table3.drop(engine, checkfirst=True)
    table2.drop(engine, checkfirst=True)
    table1.drop(engine, checkfirst=True)
    table1.create(engine, checkfirst=True)
    table2.create(engine, checkfirst=True)
    table3.create(engine, checkfirst=True)
    try:
        db.session.add_all([
            APIListURL(
                nice_name='fernandelcapo | pizzaallapala | TEST',
                host='rapidapi.com',
                url='https://rapidapi.com'
                    '/fernandelcapo/api/pizzaallapala',
                sub_required=True,
                month_limit=500000,
                hour_limit=1000),
        ])
        db.session.commit()
        print(APIListURL.__tablename__ + " seeded successfully!")
    except Exception as e:
        print(f"Error committing data: {e}")

# Example Seed Row
"""
            # Example API List URL shown here
            APIListURL(
                nice_name='___',
                host='___',
                url='___',
                sub_required=True,
                month_limit=___,
                hour_limit=___),
"""
