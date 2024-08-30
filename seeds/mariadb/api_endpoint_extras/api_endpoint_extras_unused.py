"""
API Endpoint Extras
This does not delete the table before seeding.

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

with app.app_context():
    try:

        # retrieve API Endpoints in order to reference foreign keys.
        API_Endpoint_List = db.session.query(APIEndpoint).all()

        db.session.close()
        print(APIEndpointExtra.__tablename__ + " seeded successfully!")

    except Exception as e:
        print(f"Error committing data: {e}")

# Example Seed Format
# extra_documentation stores LONGTEXT in the column.
"""
        # API Endpoint Nice Name
        # API List URL Nice Name,
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List
            if i.http_path == (
                '') and
            i.nice_name == "")
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
\
""",
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))
"""
