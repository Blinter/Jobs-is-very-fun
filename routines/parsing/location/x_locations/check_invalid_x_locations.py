"""
This file can be run
cd <this directory>
PYTHONPATH=<base_dir> python3 <file_name>.py
"""
from sqlalchemy import and_
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError
from app import create_app, db
from models.postgres.locations.cities import City
from models.postgres.locations.countries import Country
from models.postgres.locations.regions import Region
from models.postgres.locations.states import State
from models.postgres.locations.subregions import Subregion
from models.postgres.locations.x_location_id import XLocationID
from routines.parsing.find_location import (
    fix_city_name,
    find_country,
    find_state,
    find_city,
    delimit_string,
    delimit_two_letter_matches_string, delimit_three_letter_matches_string
)

app = create_app()

with app.app_context():
    try:

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

        invalid_locations: list = refresh_invalid_x_locations()

        if len(invalid_locations) != 0:
            print('Invalid Locations Count (' +
                  str(len(invalid_locations)) + ')', flush=True)

        still_invalid: list = []

        for j in refresh_invalid_x_locations():
            print(str(j.id) + ": " + str(j.name), flush=True)

            # Re-iterating using alternative method
            found_region: None = None
            found_subregion: None = None
            found_country: None = None
            found_state: None = None
            found_city: None = None
            detailed_location_list: list = [
                j.strip(" ")
                for j in j.name.split(',')
            ]

            # Attempt to find country, state, then city
            # Attempt to find state, then city
            # Attempt to find city
            # Then report invalid
            print(str(detailed_location_list), flush=True)

            while len(detailed_location_list) != 0:
                if len(detailed_location_list[0]) == 0:
                    detailed_location_list.pop(0)

                if found_country is None:
                    found_country: Country = find_country(
                        detailed_location_list[0]
                    )

                    if found_country is None:
                        print("Can't find country for " +
                              detailed_location_list[0] +
                              " looking up state", flush=True)
                        found_state: State = find_state(
                            country_id=-1,
                            state_string=detailed_location_list[0],
                            regex_letter_code=(
                                delimit_two_letter_matches_string(
                                    detailed_location_list[0]) + 
                                delimit_three_letter_matches_string(
                                    detailed_location_list[0]
                                )
                            ),
                            delimited_string=[]
                        )

                        if found_state is None:
                            found_state: State = find_state(
                                country_id=-1,
                                state_string=detailed_location_list[0],
                                regex_letter_code=(
                                    delimit_two_letter_matches_string(
                                        detailed_location_list[0]) + 
                                    delimit_three_letter_matches_string(
                                        detailed_location_list[0])
                                ),
                                delimited_string=delimit_string(
                                    length_combo=2,
                                    input_string=detailed_location_list[0],
                                )
                            )

                        if found_state is None:
                            print("Can't find state for " +
                                  detailed_location_list[0] +
                                  " looking up city", flush=True)
                            found_city: City = find_city(
                                country_id=-1,
                                state_id=-1,
                                city_string=fix_city_name(
                                    input_city=detailed_location_list[0],
                                    input_state='',
                                ),
                                delimited_string=[]
                            )

                            if found_city is None:
                                found_city: City = find_city(
                                    country_id=-1,
                                    state_id=-1,
                                    city_string=fix_city_name(
                                        input_city=detailed_location_list[0],
                                        input_state='',
                                    ),
                                    delimited_string=delimit_string(
                                        length_combo=2,
                                        input_string=fix_city_name(
                                            input_city=(
                                                detailed_location_list[0]),
                                            input_state='',
                                        )
                                    )
                                )

                            if found_city is None:
                                print("Can't find city for " +
                                      detailed_location_list[0], flush=True)
                                detailed_location_list.pop(0)
                                continue

                            else:
                                print("Found City for " +
                                      detailed_location_list[0], flush=True)
                                found_state: State = found_city.state
                                found_country: Country = found_city.country
                                found_subregion: Subregion = (
                                    found_city.subregion)
                                found_region: Region = found_city.region
                                detailed_location_list.pop(0)
                                continue

                        else:
                            print("Found state for " +
                                  detailed_location_list[0], flush=True)
                            found_country: Country = found_state.country
                            found_subregion: Subregion = (
                                found_state.country.subregion)
                            found_region: Region = found_state.country.region
                            detailed_location_list.pop(0)
                            continue

                    else:
                        print("Found Country for " +
                              detailed_location_list[0], flush=True)
                        found_subregion: Subregion = found_country.subregion
                        found_region: Region = found_country.region
                        detailed_location_list.pop(0)
                        continue

                elif found_state is None:
                    found_state: State = find_state(
                        country_id=-1,
                        state_string=detailed_location_list[0],
                        regex_letter_code=(
                            delimit_two_letter_matches_string(
                                detailed_location_list[0]) + 
                            delimit_three_letter_matches_string(
                                detailed_location_list[0])
                        ),
                        delimited_string=[]
                    )

                    if found_state is None:
                        found_state: State = find_state(
                            country_id=-1,
                            state_string=detailed_location_list[0],
                            regex_letter_code=(
                                delimit_two_letter_matches_string(
                                    detailed_location_list[0]) + 
                                delimit_three_letter_matches_string(
                                    detailed_location_list[0])
                            ),
                            delimited_string=delimit_string(
                                length_combo=2,
                                input_string=detailed_location_list[0],
                            )
                        )

                    if found_state is None:
                        print("Can't find state for " +
                              detailed_location_list[0] +
                              " looking up city", flush=True)

                        found_city: City = find_city(
                            country_id=-1,
                            state_id=-1,
                            city_string=fix_city_name(
                                input_city=detailed_location_list[0],
                                input_state='',
                            ),
                            delimited_string=[]
                        )

                        if found_city is None:
                            found_city: City = find_city(
                                country_id=-1,
                                state_id=-1,
                                city_string=fix_city_name(
                                    input_city=detailed_location_list[0],
                                    input_state='',
                                ),
                                delimited_string=delimit_string(
                                    length_combo=2,
                                    input_string=fix_city_name(
                                        input_city=detailed_location_list[0],
                                        input_state='',
                                    )
                                )
                            )

                        if found_city is None:
                            print("Can't find city for " +
                                  detailed_location_list[0], flush=True)
                            detailed_location_list.pop(0)
                            continue

                        else:
                            print("Found City for " +
                                  detailed_location_list[0], flush=True)
                            found_state = found_city.state
                            found_country = found_city.country
                            found_subregion = (
                                found_city.subregion)
                            found_region = found_city.state.region
                            detailed_location_list.pop(0)
                            continue

                elif found_city is None:
                    found_city: City = find_city(
                        country_id=-1,
                        state_id=-1,
                        city_string=fix_city_name(
                            input_city=detailed_location_list[0],
                            input_state='',
                        ),
                        delimited_string=[]
                    )

                    if found_city is None:
                        found_city: City = find_city(
                            country_id=-1,
                            state_id=-1,
                            city_string=fix_city_name(
                                input_city=detailed_location_list[0],
                                input_state='',
                            ),
                            delimited_string=delimit_string(
                                length_combo=2,
                                input_string=fix_city_name(
                                    input_city=detailed_location_list[0],
                                    input_state='',
                                )
                            )
                        )

                    if found_city is None:
                        print("Can't find city for " +
                              detailed_location_list[0], flush=True)
                        detailed_location_list.pop(0)
                        continue

                    else:
                        print("Found City for " +
                              detailed_location_list[0], flush=True)
                        found_state: State = found_city.state
                        found_country: Country = found_city.country
                        found_subregion: Subregion = (
                            found_city.subregion)
                        found_region: Region = found_city.region
                        detailed_location_list.pop(0)
                        continue

                else:
                    print("Found Country for " +
                          detailed_location_list[0], flush=True)
                    detailed_location_list.pop(0)

            if found_city is not None:
                j.city_id = found_city.id
                j.state_id = found_city.state.id
                j.country_id = found_city.country.id
                j.subregion_id = found_city.subregion.id
                j.region_id = found_city.region.id
                j.verified = True

            elif found_state is not None:
                j.state_id = found_state.id
                j.country_id = found_state.country.id
                j.subregion_id = found_state.subregion.id
                j.region_id = found_state.region.id
                j.verified = True

            elif found_country is not None:
                j.country_id = found_country.id
                j.subregion_id = found_country.subregion.id
                j.region_id = found_country.region.id
                j.verified = True

            elif found_subregion is not None:
                j.subregion_id = found_subregion.id
                j.region_id = found_subregion.region.id
                j.verified = True

            elif found_region is not None:
                j.region_id = found_region.id
                j.verified = True

            db.session.add(j)
            db.session.commit()
        # Step through parsing process

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
