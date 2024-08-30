"""
Seed file

Seed file can be run
cd <base_dir>
PYTHONPATH=<base_dir> python3 <base_dir>/<file_name>.py
"""

from secrets_jobs.credentials import postgres_information_login_details
from models.postgres.user import User
from app import create_app, db
import sqlalchemy as db2
from sqlalchemy_utils import database_exists, create_database
app = create_app()

engine = db2.create_engine(postgres_information_login_details)
if not database_exists(engine.url):
    create_database(engine.url, encoding='UTF8')
with app.app_context():
    db.drop_all(bind_key="postgres")
    db.create_all(bind_key="postgres")
    try:
        test_user = User(
        )
        db.session.add_all([
            test_user
        ])
        db.session.commit()
        db.session.delete(test_user)
        db.session.commit()
        print("Database seeded successfully!")
    except Exception as e:
        print(f"Error committing data: {e}")
        raise e
