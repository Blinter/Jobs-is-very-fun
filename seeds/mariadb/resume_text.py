"""
Resume Text

Seed file can be run
cd <base_dir>
PYTHONPATH=<base_dir> python3 <base_dir>/<file_name>.py
"""
from secrets_jobs.credentials import maria_information_login_details
from models.mariadb.resume_text import ResumeText
from app import create_app, db
import sqlalchemy as db2
from sqlalchemy_utils import database_exists, create_database
app = create_app()

engine = db2.create_engine(maria_information_login_details)
if not database_exists(engine.url):
    create_database(engine.url, encoding='UTF8')
with app.app_context():
    table = db.Table(
        ResumeText.__tablename__,
        bind_key="mariadb",
        autoload_with=engine)
    table.drop(engine, checkfirst=True)
    table.create(engine, checkfirst=True)
    try:
        db.session.add(ResumeText())
        db.session.commit()
    except db2.exc.IntegrityError as e:
        print(ResumeText.__tablename__ + " seeded successfully!")
    except Exception as e:
        print(f"Error committing data: {e}")
