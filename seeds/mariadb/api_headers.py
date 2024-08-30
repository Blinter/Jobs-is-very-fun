"""
API Headers

Seed file can be run
cd <base_dir>
PYTHONPATH=<base_dir> python3 <base_dir>/<file_name>.py

These need to be imported due to relationship of APIListURL.
APIEndpoint, APIEndpointParam, APIEndpointBody, APIEndpointHeader

Endpoints must be seeded first before this seed can be executed.
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
            APIHeader.__tablename__,
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

        # set apijobdev_s as apijobs.dev for convenience.
        apijobdev_s = 'apijobs.dev'
        # retrieve API Endpoints in order to reference API ID.
        api_job_dev_api_list = db.session.query(APIListURL).filter(
            APIListURL.host == apijobdev_s).all()

        # add all APIJob.dev required API key headers
        db.session.add_all([
            APIHeader(
                api_id=i.id,
                header='apikey',
                required=True,
                api_key_header=True,
            ) for i in api_job_dev_api_list
        ])
        db.session.commit()
        print("APIJob.dev header seeded successfully!")

        rapid_s = 'rapidapi.com'
        # retrieve API Endpoints in order to reference API ID.
        rapid_api_list = db.session.query(APIListURL).filter(
            APIListURL.host == rapid_s).all()

        # add all Rapid API required API key headers
        db.session.add_all([
            APIHeader(
                api_id=i.id,
                header='x-rapidapi-key',
                required=True,
                api_key_header=True,
            ) for i in rapid_api_list
        ])
        db.session.commit()
        print("Rapid API x-rapidapi-key header seeded successfully!")

        # Get a sample of the http_path that was stored in Endpoints in order
        # to produce a valid x-rapidapi-host.
        # Each RapidAPI follows the same format.
        # i.e. http_path (the URL for the endpoint) hostname
        rapid_api_endpoint_list = [
            db.session.query(APIEndpoint)
            .filter(APIEndpoint.api_id == i.id).first()
            for i in rapid_api_list
        ]

        api_job_dev_api_endpoint_list = [
            db.session.query(APIEndpoint)
            .filter(APIEndpoint.api_id == i.id).first()
            for i in api_job_dev_api_list
        ]

        for j, i in enumerate(rapid_api_endpoint_list +
                              api_job_dev_api_endpoint_list):
            if i is None:
                print("INVALID ENDPOINT")
                print(str(i) + " ID: " + str(j))
                raise ValueError("Invalid Endpoint: " + str(i) +
                                 " ID: " + str(j))
            else:
                pass
                # print("Valid: " + str(i) + " ID: " + str(j))

        # add all Rapid API required host key headers
        # Endpoints must be seeded first before this can be added.
        db.session.add_all([
            APIHeader(
                api_id=i.id,
                header='x-rapidapi-host',
                value=str(
                    j.http_path[:(j.http_path.index(rapid_s)+len(rapid_s))]
                    .replace("https://", "")
                ),
                required=True,
            ) for (i, j) in zip(rapid_api_list, rapid_api_endpoint_list)
        ])

        # attempt to accept response in JSON
        # Endpoints must be seeded first before this can be added.
        db.session.add_all([
            APIHeader(
                api_id=i.id,
                header='Accept',
                value='application/json',
                required=True,
            ) for (i, j) in zip(
                rapid_api_list + api_job_dev_api_list,
                rapid_api_endpoint_list + api_job_dev_api_endpoint_list
            )
        ])
        db.session.commit()
        print("Rapid API Headers seeded successfully!")

        db.session.close()
        print(APIHeader.__tablename__ + " seeded successfully!")

    except Exception as e:
        print(f"Error committing data: {e}")
        raise e
