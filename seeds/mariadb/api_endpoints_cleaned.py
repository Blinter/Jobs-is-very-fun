"""
API Endpoints

Seed file can be run
cd <base_dir>
PYTHONPATH=<base_dir> python3 <base_dir>/<file_name>.py

Table drop and creation must also drop:
    APIEndpointParams, APIEndpointHeaders, APIEndpointBodies due to FK
    restraints

APIHeader needs to be imported due to APIListURL relationship.
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

        # APIEndpoint
        table = db.Table(
            APIEndpoint.__tablename__,
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

        # APIEndpointParam
        table2 = db.Table(
            APIEndpointParam.__tablename__,
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

        # APIEndpointHeader
        table3 = db.Table(
            APIEndpointHeader.__tablename__,
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

        # APIEndpointBody
        table4 = db.Table(
            APIEndpointBody.__tablename__,
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

        table4.drop(engine, checkfirst=True)
        table3.drop(engine, checkfirst=True)
        table2.drop(engine, checkfirst=True)
        table.drop(engine, checkfirst=True)

        table.create(engine, checkfirst=True)
        table2.create(engine, checkfirst=True)
        table3.create(engine, checkfirst=True)
        table4.create(engine, checkfirst=True)

        # retrieve API List URL's in order to reference foreign keys.
        API_list = db.session.query(APIListURL).all()

        # Example API Endpoint shown here

        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
                'https://rapidapi.com'
                '/fernandelcapo/api/pizzaallapala'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Producto Promo",
                http_method="GET",
                http_path='https://pizzaallapala.p.rapidapi.com'
                          '/productos-promo'
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Productos",
                http_method="GET",
                http_path='https://pizzaallapala.p.rapidapi.com'
                          '/productos'
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Get Tags",
                http_method="GET",
                http_path='https://pizzaallapala.p.rapidapi.com'
                          '/tags'
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="Usuarios",
                http_method="GET",
                http_path='https://pizzaallapala.p.rapidapi.com'
                          '/usuarios/'
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))

        db.session.close()
        print(APIEndpoint.__tablename__ + " seeded successfully!")
    except Exception as e:
        print(f"Error committing data: {e}")

# Example Seed Format
# nice_description can have """ and stores TEXT in the column.
# nice_category can be added to categorize endpoints.
"""
        new_api_id, new_api_nice_name = next(
            (i.id, i.nice_name) for i in API_list if i.url == (
             '___'
             '___'))
        db.session.add_all([
            APIEndpoint(
                api_id=new_api_id,
                nice_name="___",
                nice_description=
                "___",
                http_method="___",
                http_path='___'
            ),
            APIEndpoint(
                api_id=new_api_id,
                nice_name="___",
                nice_description=
                "___",
                http_method="___",
                http_path='___'
            ),
        ])
        db.session.commit()
        print(APIEndpoint.__tablename__ + " seeded " + str(new_api_nice_name))
"""
