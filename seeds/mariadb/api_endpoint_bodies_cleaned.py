"""
API Endpoint Bodies

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
            APIEndpointBody.__tablename__,
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

        # Seed Data here

        db.session.commit()

        db.session.close()
        print(APIEndpointBody.__tablename__ + " seeded successfully!")

    except Exception as e:
        print(f"Error committing data: {e}")

# Example Seed Format
# nice_description can have """ and stores TEXT in the column.
"""

        # HTTP_Path and Endpoint Nice_Name
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                '___'
                '___') and
            i.nice_name == '___')
        db.session.add_all([
            APIEndpointBody(
                api_endpoint_id=new_api_endpoint_id,
                key='___',
                key_description='___',
                value_hint_type='___',
                value_default='___',
                required=True
            ),
        ])
        db.session.commit()
        print(APIEndpointBody.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))
"""
