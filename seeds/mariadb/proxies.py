"""
Proxies

Seed file can be run
cd <base_dir>
PYTHONPATH=<base_dir> python3 <base_dir>/<file_name>.py
"""
from secrets_jobs.credentials import maria_information_login_details
from models.mariadb.proxies import Proxy
from app import create_app, db
import sqlalchemy as db2
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy_utils import database_exists, create_database
from secrets_jobs.current_proxy_list import CurrentProxyList
app = create_app()

engine = db2.create_engine(maria_information_login_details)
if not database_exists(engine.url):
    create_database(engine.url, encoding='UTF8')
with app.app_context():
    table = db.Table(
        Proxy.__tablename__,
        bind_key="mariadb",
        autoload_with=engine)
    table.drop(engine, checkfirst=True)
    table.create(engine, checkfirst=True)
    try:
        db.session.add_all(
            [Proxy(
                proxy_type=db.cast(i['proxy_type'], TINYINT),
                proxy_address=i['proxy_address'],
                auth_required=False)
                for i in CurrentProxyList if not i['auth_required']]
        )
        db.session.add_all(
            [Proxy(
                proxy_type=db.cast(i['proxy_type'], TINYINT),
                proxy_address=i['proxy_address'],
                proxy_username=i['proxy_username'],
                proxy_password=i['proxy_password'],
                auth_required=True)
                for i in CurrentProxyList if i['auth_required']]
        )
        db.session.commit()
        print(Proxy.__tablename__ + " seeded successfully!")
    except Exception as e:
        print(f"Error committing data: {e}")
