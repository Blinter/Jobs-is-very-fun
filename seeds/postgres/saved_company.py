"""
Saved Job

Seed file can be run
cd <base_dir>
PYTHONPATH=<base_dir> python3 <base_dir>/<file_name>.py
"""


from sqlalchemy import inspect, text, MetaData
from sqlalchemy_utils import database_exists, create_database

from secrets_jobs.credentials import (
    postgres_information_login_details,
    postgres_database_name
)

# Imports are required due to relationships
from models.postgres.saved_company import SavedCompany
from models.postgres.company import Company
from models.postgres.profile import Profile

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

    table_saved_company = db.Table(
        SavedCompany.__tablename__,
        metadata=metadata,
        bind_key="postgres",
        autoload_with=engine)

    if table_exists(db, table_saved_company.name):
        fk_names = get_foreign_key_constraint_names(
            table_saved_company,
            engine
        )
        for fk_name in fk_names:
            if fk_name:
                sql_text = (
                    f'ALTER TABLE {table_saved_company.name} \
DROP FOREIGN KEY {fk_name}')
                db.session.execute(text(sql_text))

    table_saved_company.drop(engine, checkfirst=True)

    if not table_exists(db, Profile.__tablename__):
        table_profile = db.Table(
            Profile.__tablename__,
            metadata=metadata,
            bind_key="postgres",
            autoload_with=engine)
        table_profile.create(engine, checkfirst=True)

    if not table_exists(db, Company.__tablename__):
        table_company = db.Table(
            Company.__tablename__,
            metadata=metadata,
            bind_key="postgres",
            autoload_with=engine)
        table_company.create(engine, checkfirst=True)

    table_saved_company.create(engine, checkfirst=True)

    try:
        # test_saved_company = SavedCompany()
        # db.session.add_all([
        #     test_saved_company
        # ])
        db.session.commit()
        print(SavedCompany.__tablename__ + " seeded successfully!")
    except Exception as e:
        print(f"Error committing data: {e}")
        raise e
