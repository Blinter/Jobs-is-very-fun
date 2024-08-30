"""
API Keys

Seed file can be run
cd <base_dir>
PYTHONPATH=<base_dir> python3 <base_dir>/<file_name>.py
"""
from sqlalchemy import asc, select
from sqlalchemy.orm import load_only

from secrets_jobs.credentials import (maria_information_login_details,
                                      rapid_api_keys, api_jobs_api_keys)
from models.mariadb.api_keys import APIKey
from models.mariadb.api_list_url import APIListURL
from app import create_app, db
import sqlalchemy as db2
from sqlalchemy_utils import database_exists, create_database

app = create_app()

engine = db2.create_engine(maria_information_login_details)
if not database_exists(engine.url):
    create_database(engine.url, encoding='UTF8')

with app.app_context():
    table = db.Table(
        APIKey.__tablename__,
        bind_key="mariadb",
        autoload_with=engine)
    table.drop(engine, checkfirst=True)
    table.create(engine, checkfirst=True)
    try:
        # add Rapid API Keys from credentials file.
        rapid_api_url_list = (db.session.scalars(
            select(APIListURL.url)
            .filter(APIListURL.host == 'rapidapi.com')
            .order_by(asc(APIListURL.nice_name))
        ).all())

        db.session.add_all(
            [APIKey(
                url=i,
                key=j['key'],
                preferred_proxy=(j['preferred_proxy'] if 'preferred_proxy' in
                                 j.keys() else None)
            )
                for j in rapid_api_keys
                for i in rapid_api_url_list
             ]
        )

        db.session.commit()

        print(APIKey.__tablename__ + " RapidAPI keys seeded successfully!")

        # add APIJobs API Keys from credentials file.
        api_jobs_dev_url_list = (db.session.scalars(
            select(APIListURL.url)
            .filter(APIListURL.host == 'apijobs.dev')
            .order_by(asc(APIListURL.nice_name))
        ).all())

        db.session.add_all(
            [APIKey(
                url=i,
                key=j['key'],
                preferred_proxy=(j['preferred_proxy'] if 'preferred_proxy' in
                                 j.keys() else None)
            )
                for j in api_jobs_api_keys
                for i in api_jobs_dev_url_list
             ]
        )

        db.session.commit()

        print(APIKey.__tablename__ + " API Jobs seeded successfully!")

    except Exception as e:
        print(f"Error committing data: {e}")
