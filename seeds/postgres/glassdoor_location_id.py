"""
Glassdoor Location ID

Seed file can be run
cd <base_dir>
PYTHONPATH=<base_dir> python3 <base_dir>/<file_name>.py
"""
from models.postgres.locations.glassdoor_location_id import GlassdoorLocationID
from sqlalchemy import inspect, text, MetaData
from app import create_app, db
from sqlalchemy_utils import database_exists, create_database
from secrets_jobs.credentials import (
    postgres_information_login_details,
    postgres_database_name
)
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
    with app.app_context():
        inspector = inspect(temp_connection)
        fks = inspector.get_foreign_keys(temp_table.name,
                                         schema=temp_table.schema)
        return [fk['name'] for fk in fks]


def table_exists(temp_db, table_name, schema=postgres_database_name):
    """
    Query information_schema and check if table exists.
    """

    with app.app_context():
        query = text(f"""\
    SELECT COUNT(*) FROM information_schema.TABLES \
    WHERE TABLE_SCHEMA = '{schema}' AND TABLE_NAME = '{table_name}'\
    """)
        result = temp_db.session.execute(query)
        return result.scalar() > 0


with app.app_context():
    metadata = MetaData()
    glassdoor_location_ids = db.Table(
        GlassdoorLocationID.__tablename__,
        metadata=metadata,
        bind_key="postgres",
        autoload_with=engine)

    if table_exists(db, glassdoor_location_ids.name):
        fk_names = get_foreign_key_constraint_names(
            glassdoor_location_ids,
            engine
        )
        for fk_name in fk_names:
            if fk_name:
                sql_text = (f'ALTER TABLE {glassdoor_location_ids.name} '
                            'DROP FOREIGN KEY '
                            f'{fk_name}')
                db.session.execute(text(sql_text))

    glassdoor_location_ids.drop(engine, checkfirst=True)
    glassdoor_location_ids.create(engine, checkfirst=True)
    try:
        # db.session.add_all([
        #     GlassdoorLocationID()
        # ])
        db.session.commit()
        print(GlassdoorLocationID.__tablename__ +
              " seeded successfully!")
    except Exception as e:
        print(f"Error committing data: {e}")
        raise e
