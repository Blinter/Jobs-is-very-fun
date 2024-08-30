"""
This file can be run
cd <this directory>
PYTHONPATH=<base_dir> python3 <file_name>.py
"""
from bson import ObjectId
from sqlalchemy import and_, asc, not_, or_
from sqlalchemy.orm import load_only
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError
from app import create_app, db
from extensions_mongo import fs_mongo
from models.mariadb.mongo_storage import MongoStorage
from models.postgres.locations.glassdoor_location_id import GlassdoorLocationID

from routines.parsing.conversions import convert_bytes_to_dict_raw

from routines.parsing.location.mantiks_glassdoor import (
    mantiks_glassdoor_locations_search
)

app = create_app()

with app.app_context():
    try:
        def refresh_glassdoor_locations():
            """
            Access Database and retrieve Glassdoor Location Table
            """
            return db.session.query(GlassdoorLocationID).all()

        def refresh_loaded_glassdoor_locations():
            return (
                db.session.query(MongoStorage)
                .filter(
                    not_(
                        or_(
                            MongoStorage.object_id.is_(None),
                            MongoStorage.input_json.is_(None),
                            MongoStorage.code.is_(None),
                            MongoStorage.length.is_(None),
                            MongoStorage.data_truncated.is_(None),
                            MongoStorage.code.is_(None),
                            MongoStorage.query_time.is_(None),
                            MongoStorage.proxy.is_(None),
                            MongoStorage.api_key.is_(None),
                        )
                    ),
                    and_(
                        MongoStorage.url == """\
https://glassdoor.p.rapidapi.com/locations/search""",
                        MongoStorage.endpoint_nice_name == """\
Locations Search""",
                        MongoStorage.code == '200',
                    )
                )
                .options(
                    load_only(
                        MongoStorage.id,
                        MongoStorage.object_id,
                        MongoStorage.input_json
                    )
                )
                .order_by(asc(MongoStorage.query_time))
                .all()
            )

        # Load Glassdoor Locations
        glassdoor_locations_table = refresh_glassdoor_locations()

        # Load Glassdoor rows and insert into database
        scraped_location_id_list = refresh_loaded_glassdoor_locations()

        # Work through locations list and improve filters over time
        for scraped_data in scraped_location_id_list:

            if scraped_data.id is None:
                continue

            # Load data
            dict_new = mantiks_glassdoor_locations_search(
                dict_new=convert_bytes_to_dict_raw(
                    fs_mongo.get(
                        file_id=ObjectId(scraped_data.object_id)
                    ).read()
                    .decode()
                ),
            )

            for location_id in dict_new.keys():
                if dict_new[location_id] is None:
                    continue

                found_row = db.session.query(
                    db.session.query(GlassdoorLocationID.id).filter(
                        GlassdoorLocationID.id == int(location_id)).exists()
                ).scalar()

                if not found_row:
                    found_row = GlassdoorLocationID(
                        id=int(location_id),
                        name=str(dict_new[location_id].get('long_name')),
                        region_id=dict_new[location_id].get('region_id'),
                        subregion_id=(
                            dict_new[str(location_id)].get('subregion_id')
                        ),
                        country_id=(
                            dict_new[str(location_id)].get('country_id')
                        ),
                        state_id=dict_new[str(location_id)].get('state_id'),
                        city_id=dict_new[str(location_id)].get('city_id')
                    )

                    db.session.add(found_row)

                else:
                    found_row = db.session.query(GlassdoorLocationID).filter(
                        GlassdoorLocationID.id == int(location_id)).first()

                    if dict_new[str(location_id)].get('region_id', False):
                        found_row.region_id = (
                            dict_new[str(location_id)].get('region_id'))
                        found_row.verified = True

                    if dict_new[str(location_id)].get('subregion_id', False):
                        found_row.subregion_id = (
                            dict_new[str(location_id)].get('subregion_id'))
                        found_row.verified = True

                    if dict_new[str(location_id)].get('country_id', False):
                        found_row.country_id = (
                            dict_new[str(location_id)].get('country_id'))
                        found_row.verified = True

                    if dict_new[str(location_id)].get('state_id', False):
                        found_row.state_id = (
                            dict_new[str(location_id)].get('state_id'))
                        found_row.verified = True

                    if dict_new[location_id].get('city_id', False):
                        found_row.city_id = (
                            dict_new[str(location_id)].get('city_id'))
                        found_row.verified = True

        db.session.commit()
        db.session.close()

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.rollback()
        db.session.close()
        print(f"IntegrityError: {e}", flush=True)
        raise e

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.rollback()
        db.session.close()
        print(f"OperationalError: {e}", flush=True)
        raise e

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.rollback()
        db.session.close()
        print(f"SQLAlchemyError: {e}", flush=True)
        raise e

    # Other Errors
    except Exception as e:
        db.session.rollback()
        db.session.close()
        print(f"Error: {e}", flush=True)
        raise e
