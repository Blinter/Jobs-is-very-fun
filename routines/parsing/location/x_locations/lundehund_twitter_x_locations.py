"""
This file can be run
cd <this directory>
PYTHONPATH=<base_dir> python3 <file_name>.py


REQUIRES NODE.JS/NPM
npm install pelias-parser
Edit ~/node_modules/pelias-parser/server/http.js

Find "const HOST = process.env.HOST || undefined"
    Modify to edit and configure to listen on "localhost"
node ./node_modules/pelias-parser/server/http.js

Pelias Parser running on localhost at port 3000

Extra Links
https://www.npmjs.com/package/pelias-parser
"""
from bson import ObjectId
from sqlalchemy import and_, asc, not_, or_
from sqlalchemy.orm import load_only
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError
from app import create_app, db
from extensions_mongo import fs_mongo
from models.mariadb.mongo_storage import MongoStorage
from models.postgres.locations.cities import City
from models.postgres.locations.countries import Country
from models.postgres.locations.regions import Region
from models.postgres.locations.states import State
from models.postgres.locations.subregions import Subregion
from models.postgres.locations.x_location_id import XLocationID
from routines.parsing.conversions import convert_bytes_to_dict_raw
from routines.parsing.location import lundehund_twitter_x_job_search_location
from routines.parsing.find_location import (
    parse_location_to_detailed_list,
    find_country,
    find_city,
    find_state,
    delimit_two_letter_matches_string,
    delimit_string,
    find_city_and_state,
    find_x_location_id,
    fix_city_name, delimit_three_letter_matches_string
)

app = create_app()

with app.app_context():
    try:
        def refresh_x_locations():
            """
            Refresh X Locations from XLocationID Table
            """
            return db.session.query(XLocationID).all()

        def refresh_invalid_x_locations():
            """
            Refresh X Locations from XLocationID Table
            """
            return (
                db.session.query(XLocationID)
                .filter(
                    and_(
                        XLocationID.region_id.is_(None),
                        XLocationID.subregion_id.is_(None),
                        XLocationID.country_id.is_(None),
                        XLocationID.state_id.is_(None),
                        XLocationID.city_id.is_(None),
                    )
                )
                .all()
            )

        def refresh_loaded_x_locations():
            """
            Access MongoStorage and refresh the X Location results
            """
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
https://twitter-x-api.p.rapidapi.com/api/job/search/location""",
                        MongoStorage.endpoint_nice_name == """\
Search Location""",
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
        # Load X Locations
        x_locations_table: list = refresh_x_locations()

        # Load X rows and insert into database
        scraped_location_id_list: list = refresh_loaded_x_locations()

        low_scoring_names = {}
        failed_scoring_names = {}

        # Work through locations list and improve filters over time
        for scraped_data in scraped_location_id_list:

            if (scraped_data is None or
                    scraped_data.id is None):
                continue

            # Load data
            dict_new: dict = lundehund_twitter_x_job_search_location(
                dict_new=convert_bytes_to_dict_raw(
                    fs_mongo.get(
                        file_id=ObjectId(scraped_data.object_id)
                    ).read()
                    .decode()
                ),
            )

            for location_id in dict_new.keys():

                if (location_id is None or
                        dict_new[location_id] is None):
                    continue

                detailed_location_list: list = parse_location_to_detailed_list(
                    dict_new[location_id])

                if (isinstance(detailed_location_list, list) and
                        len(detailed_location_list[0]) == 0 and
                        len(detailed_location_list[1]) == 0 and
                        len(detailed_location_list[2]) == 0):
                    print("Failed parser for " +
                          str(dict_new[location_id]))
                    failed_scoring_names[str(scraped_data.id)] = (
                        dict_new[location_id]
                    )

                found_region: None = None
                found_subregion: None = None
                found_country: None = None
                found_state: None = None
                found_city: None = None

                if isinstance(detailed_location_list, list):
                    # start with State String
                    if (detailed_location_list[1] is not None and
                            detailed_location_list[1] != ''):

                        if len(detailed_location_list[2]) > 0:
                            found_country: Country = find_country(
                                detailed_location_list[2]
                            )

                        found_state: State = find_state(
                            country_id=found_country.id
                            if found_country is not None else -1,
                            state_string=detailed_location_list[1],
                            regex_letter_code=(
                                delimit_two_letter_matches_string(
                                    detailed_location_list[1]) + 
                                delimit_three_letter_matches_string(
                                    detailed_location_list[1])

                            ),
                            delimited_string=[],
                        )
                        if found_state is None:
                            found_state: State = find_state(
                                country_id=found_country.id
                                if found_country is not None else -1,
                                state_string=detailed_location_list[1],
                                regex_letter_code=(
                                    delimit_two_letter_matches_string(
                                        detailed_location_list[1]) + 
                                    delimit_three_letter_matches_string(
                                        detailed_location_list[1])
                                ),
                                delimited_string=(
                                    delimit_string(
                                        input_string=detailed_location_list[1]
                                    )
                                ),
                            )

                        if found_state is not None:
                            # noinspection PyUnresolvedReferences
                            found_country: Country = found_state.country
                            # noinspection PyUnresolvedReferences
                            found_subregion: Subregion = (
                                found_state.country.subregion)
                            # noinspection PyUnresolvedReferences
                            found_region: Region = found_country.region

                    if (detailed_location_list[2] is not None and
                            detailed_location_list[2] != ''):
                        found_country: Country = find_country(
                            country_string=detailed_location_list[2]
                        )

                        if found_country is not None:
                            # noinspection PyUnresolvedReferences
                            found_subregion: Subregion = found_country.subregion
                            # noinspection PyUnresolvedReferences
                            found_region: Region = found_country.region

                    # Check again after finding State
                    if (found_state is None and
                            isinstance(detailed_location_list, list) and
                            len(detailed_location_list) > 1 and
                            detailed_location_list[1] is not None and
                            detailed_location_list[1] != ''):

                        found_state: State = find_state(
                            country_id=found_country.id
                            if found_country is not None else -1,
                            state_string=detailed_location_list[1],
                            regex_letter_code=(
                                delimit_two_letter_matches_string(
                                    detailed_location_list[1]) + 
                                delimit_three_letter_matches_string(
                                    detailed_location_list[1])
                            ),
                            delimited_string=[],
                        )
                        if found_state is None:
                            found_state: State = find_state(
                                country_id=found_country.id
                                if found_country is not None else -1,
                                state_string=detailed_location_list[1],
                                regex_letter_code=(
                                    delimit_two_letter_matches_string(
                                        detailed_location_list[1]) + 
                                    delimit_three_letter_matches_string(
                                        detailed_location_list[1])
                                ),
                                delimited_string=(
                                    delimit_string(
                                        input_string=detailed_location_list[1]
                                    )
                                ),
                            )

                        if found_state is not None:
                            # noinspection PyUnresolvedReferences
                            found_country: Country = found_state.country
                            # noinspection PyUnresolvedReferences
                            found_subregion: Subregion = (
                                found_state.country.subregion)
                            # noinspection PyUnresolvedReferences
                            found_region: Region = found_country.region

                    # Check for city
                    if (isinstance(detailed_location_list, list) and
                            len(detailed_location_list) > 0 and
                            detailed_location_list[0] is not None and
                            detailed_location_list[0] != ''):

                        # noinspection PyUnresolvedReferences
                        found_city: City = find_city(
                            country_id=found_country.id
                            if found_country is not None else -1,

                            state_id=found_state.id
                            if found_state is not None else -1,

                            city_string=fix_city_name(
                                input_city=detailed_location_list[0],

                                input_state=found_state.name
                                if found_state is not None else '',

                                input_country=found_country.name
                                if found_country is not None else '',

                            ),
                            delimited_string=[],
                        )

                        if found_city is None:
                            # noinspection PyUnresolvedReferences
                            found_city: City = find_city(
                                country_id=found_country.id
                                if found_country is not None else -1,

                                state_id=found_state.id
                                if found_state is not None else -1,

                                city_string=fix_city_name(
                                    input_city=detailed_location_list[0],

                                    input_state=found_state.name
                                    if found_state is not None else '',

                                    input_country=found_country.name
                                    if found_country is not None else '',

                                ),
                                delimited_string=delimit_string(
                                    input_string=detailed_location_list[0]
                                ),
                            )

                        if found_city is not None:
                            # noinspection PyUnresolvedReferences
                            found_state: State = found_city.state
                            # noinspection PyUnresolvedReferences
                            found_country: Country = found_state.country
                            # noinspection PyUnresolvedReferences
                            found_subregion: Subregion = found_country.subregion
                            # noinspection PyUnresolvedReferences
                            found_region: Region = found_country.region

                        elif (found_city is None and
                              isinstance(detailed_location_list, list) and

                              detailed_location_list[0] is not None and
                              detailed_location_list[0] != '' and
                              len(detailed_location_list[0]) > 0 and

                              detailed_location_list[1] is not None and
                              detailed_location_list[1] != '' and
                              len(detailed_location_list[1]) > 0):
                            # noinspection PyUnresolvedReferences
                            found_city: City = (
                                find_city_and_state(
                                    city_string=fix_city_name(
                                        input_city=detailed_location_list[0],

                                        input_state=found_state.name
                                        if found_state is not None else '',

                                        input_country=found_country.name
                                        if found_country is not None else '',
                                    ),

                                    delimited_city_string=delimit_string(
                                        length_combo=2,
                                        input_string=detailed_location_list[0]
                                    ),

                                    state_string=detailed_location_list[1],
                                    regex_letters_state=(
                                        delimit_two_letter_matches_string(
                                            detailed_location_list[1]
                                        )
                                    ),

                                    delimited_state_string=delimit_string(
                                        length_combo=2,
                                        input_string=detailed_location_list[1]
                                    )
                                )
                            )
                            if found_city is not None:
                                # noinspection PyUnresolvedReferences
                                found_state: State = found_city.state
                                # noinspection PyUnresolvedReferences
                                found_country: Country = found_state.country
                                # noinspection PyUnresolvedReferences
                                found_subregion: Subregion = (
                                    found_country.subregion)
                                # noinspection PyUnresolvedReferences
                                found_region: Region = found_country.region

                if not db.session.query(
                        db.session.query(XLocationID.id).filter(
                            XLocationID.id == int(location_id)).exists()
                ).scalar():
                    # noinspection PyUnresolvedReferences
                    found_row: XLocationID = XLocationID(
                        id=int(location_id),
                        name=str(dict_new[location_id]),

                        region_id=found_region.id
                        if found_region else None,

                        subregion_id=found_subregion.id
                        if found_subregion else None,

                        country_id=found_country.id
                        if found_country else None,

                        state_id=found_state.id
                        if found_state else None,

                        city_id=found_city.id
                        if found_city else None
                    )

                    db.session.add(found_row)

                else:
                    found_row = find_x_location_id(int(location_id))

                    if found_region is not None:
                        # noinspection PyUnresolvedReferences
                        found_row.region_id = found_region.id
                        found_row.verified = True

                    if found_subregion is not None:
                        # noinspection PyUnresolvedReferences
                        found_row.subregion_id = found_subregion.id
                        found_row.verified = True

                    if found_country is not None:
                        # noinspection PyUnresolvedReferences
                        found_row.country_id = found_country.id
                        found_row.verified = True

                    if found_state is not None:
                        # noinspection PyUnresolvedReferences
                        found_row.state_id = found_state.id
                        found_row.verified = True

                    if found_city is not None:
                        # noinspection PyUnresolvedReferences
                        found_row.city_id = found_city.id
                        found_row.verified = True

                # print(
                #     "ID: " + str(location_id) + " " +
                #     "Name: " + str(dict_new[location_id]) + " " +
                #     ("Region: " + str(found_region.name) + " "
                #      if found_region is not None else '') +
                #     ("Subregion: " + str(found_subregion.name) + " "
                #      if found_subregion is not None else '') +
                #     ("Country: " + str(found_country.name) + " "
                #      if found_country is not None else '') +
                #     ("State: " + str(found_state.name) + " "
                #      if found_state is not None else '') +
                #     ("City: " + str(found_city.name) + " "
                #      if found_city is not None else '')
                # )
        db.session.commit()

        if len(failed_scoring_names.keys()) != 0:
            print('failed_scoring_names Count (' +
                  str(len(failed_scoring_names.keys())) + ')', flush=True)

            for j in failed_scoring_names.keys():
                print(str(j) + " " + str(failed_scoring_names[j]), flush=True)

            print('--------')

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
