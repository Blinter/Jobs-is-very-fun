from sqlalchemy import exists, and_
from extensions_sql import db

from models.postgres.locations.location import Location
from models.postgres.locations.regions import Region
from models.postgres.locations.subregions import Subregion
from models.postgres.locations.countries import Country
from models.postgres.locations.states import State
from models.postgres.locations.cities import City
from routines.parsing.find_location import (
    find_city_and_state,
    fix_city_name,
    delimit_two_letter_matches_string,
    delimit_string,
    find_country,
    find_state,
    parse_location_to_detailed_list,
    find_city,
    derive_locations,
    cleanup_locations, 
    delimit_three_letter_matches_string
)


def shift_to_end(lst: list) -> list:
    if len(lst) != 3:
        return lst

    if (lst[0] != '' and
            lst[1] == '' and
            lst[2] == ''):
        return ['', '', lst[0]]

    elif (lst[0] != '' and
            lst[1] == '' and
            lst[2] != ''):
        return ['', lst[0], lst[2]]

    elif (lst[0] != '' and
            lst[1] != '' and
            lst[2] == ''):
        return ['', lst[0], lst[1]]

    else:
        return lst


def shift_to_middle(lst: list) -> list:
    if len(lst) != 3:
        return lst

    if (lst[0] != '' and
            lst[1] == '' and
            lst[2] == ''):
        return ['', lst[0], '']

    elif (lst[0] == '' and
            lst[1] == '' and
            lst[2] != ''):
        return ['', lst[2], '']

    elif (lst[0] != '' and
            lst[1] != '' and
            lst[2] == ''):
        return ['', lst[0], lst[1]]

    else:
        return lst


def string_to_location(
        string_to_parse: str,
        remote_flag: bool = False,
        attempt_as_city: bool = False,
        attempt_as_state: bool = False) -> Location:

    # print(string_to_parse + " !", flush=True)
    if remote_flag:
        lower_str = string_to_parse.lower()
        while "remote" in lower_str:
            index = lower_str.find('remote')
            if index == -1:
                break
            # Remove 'remote' from both the lower and original strings
            lower_str = (
                    lower_str[:index] +
                    lower_str[index + len('remote'):]
            ).strip()
            string_to_parse = (
                    string_to_parse[:index] +
                    string_to_parse[index + len('remote'):]
            ).strip()
    if len(string_to_parse) == 0:
        print("Returning remote flag True with no other location query",
              flush=True)
        return Location(remote=remote_flag)

    # print("STRING: (" + string_to_parse + ")", flush=True)

    location_count = 0
    if (string_to_parse is not None and
            len(string_to_parse) != 0):
        location_count = len(
            [i for i in string_to_parse.split(',')
                if i.strip() != '']
        )

    detailed_location_list: list = parse_location_to_detailed_list(
        location_str=str(string_to_parse),
        score=0.5
    )

    # detailed_location_list: list = []

    # print(str(detailed_location_list), flush=True)

    test_locations = len([
        i for i in detailed_location_list
        if i.strip() != ''])

    if location_count != test_locations:
        # print("pelias parser is missing data from the string for " +
        #       str(string_to_parse) + " reverting to string parse", flush=True)
        detailed_location_list = string_to_parse.strip().split(',')
        detailed_location_list = [
            i.strip() for i in detailed_location_list
            if i != '']
        if len(detailed_location_list) < 3:
            if not attempt_as_city:
                for i in range(3 - len(detailed_location_list)):
                    detailed_location_list = [''] + detailed_location_list
            else:
                for i in range(3 - len(detailed_location_list)):
                    detailed_location_list.append('')

    elif (isinstance(detailed_location_list, list) and
          len(detailed_location_list[0]) == 0 and
          len(detailed_location_list[1]) == 0 and
          len(detailed_location_list[2]) == 0):
        # print("string_to_location failed parser for " +
        #       str(string_to_parse) + " reverting to string parse", flush=True)
        detailed_location_list = string_to_parse.strip().split(',')
        detailed_location_list = [i for i in detailed_location_list
                                  if i != '']
        if len(detailed_location_list) < 3:
            for i in range(3 - len(detailed_location_list)):
                detailed_location_list = [''] + detailed_location_list

    # print(str(detailed_location_list), flush=True)

    if attempt_as_state:
        detailed_location_list = shift_to_middle(detailed_location_list)

    elif not attempt_as_city:
        # manual fix to revert to US based city
        if 'san francisco' in detailed_location_list[0].lower():
            if detailed_location_list[2] == '':
                detailed_location_list[2] = "USA"
            if detailed_location_list[1] == '':
                detailed_location_list[1] = "California"
        else:
            detailed_location_list = shift_to_end(detailed_location_list)

    # print(str(detailed_location_list), flush=True)

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
                    detailed_location_list[2])

            found_state: State = find_state(
                country_id=found_country.id
                if found_country is not None
                else -1,
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
                    if found_country is not None
                    else -1,
                    state_string=detailed_location_list[1],
                    regex_letter_code=(
                        delimit_two_letter_matches_string(
                            detailed_location_list[1]) +
                        delimit_three_letter_matches_string(
                            detailed_location_list[1])
                    ),
                    delimited_string=(
                        delimit_string(input_string=detailed_location_list[1])
                    ),
                )

            if found_state is not None:
                found_country: Country = found_state.country
                found_subregion: Subregion = (
                    found_state.country.subregion)
                found_region: Region = found_country.region

        if (detailed_location_list[2] is not None and
                detailed_location_list[2] != ''):
            found_country: Country = find_country(
                country_string=detailed_location_list[2]
            )

            if found_country is not None:
                found_subregion: Subregion = (
                    found_country.subregion)
                found_region: Region = found_country.region

        # Check again after finding State
        if (found_state is None and
                isinstance(detailed_location_list, list) and
                len(detailed_location_list) > 1 and
                detailed_location_list[1] is not None and
                detailed_location_list[1] != ''):

            found_state: State = find_state(
                country_id=found_country.id
                if found_country is not None
                else -1,
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
                    if found_country is not None
                    else -1,
                    state_string=detailed_location_list[1],
                    regex_letter_code=(
                        delimit_two_letter_matches_string(
                            detailed_location_list[1]) + 
                        delimit_three_letter_matches_string(
                            detailed_location_list[1])
                    ),
                    delimited_string=(
                        delimit_string(input_string=detailed_location_list[1])
                    ),
                )

            if found_state is not None:
                found_country: Country = found_state.country
                found_subregion: Subregion = (
                    found_state.country.subregion)
                found_region: Region = found_country.region

        # Check for city
        if (isinstance(detailed_location_list, list) and
                len(detailed_location_list) > 0 and
                detailed_location_list[0] is not None and
                detailed_location_list[0] != ''):

            found_city: City = find_city(
                country_id=found_country.id
                if found_country is not None
                else -1,

                state_id=found_state.id
                if found_state is not None
                else -1,

                city_string=fix_city_name(
                    input_city=detailed_location_list[0],

                    input_state=found_state.name
                    if found_state is not None
                    else '',

                    input_country=found_country.name
                    if found_country is not None
                    else '',

                ),
                delimited_string=[],
            )
            if not found_city:
                found_city: City = find_city(
                    country_id=found_country.id
                    if found_country is not None
                    else -1,

                    state_id=found_state.id
                    if found_state is not None
                    else -1,

                    city_string=fix_city_name(
                        input_city=detailed_location_list[0],

                        input_state=found_state.name
                        if found_state is not None
                        else '',

                        input_country=found_country.name
                        if found_country is not None
                        else '',

                    ),
                    delimited_string=delimit_string(
                        input_string=detailed_location_list[0]
                    ),
                )

            if found_city is not None:
                # print("Found city", flush=True)
                # print(str(found_city), flush=True)
                found_state: State = found_city.state
                found_country: Country = found_state.country
                found_subregion: Subregion = found_country.subregion
                found_region: Region = found_country.region

            elif (found_city is None and
                  isinstance(detailed_location_list, list) and

                  detailed_location_list[0] is not None and
                  detailed_location_list[0] != '' and
                  len(detailed_location_list[0]) > 0 and

                  detailed_location_list[1] is not None and
                  detailed_location_list[1] != '' and
                  len(detailed_location_list[1]) > 0):
                found_city: City = (
                    find_city_and_state(
                        city_string=fix_city_name(
                            input_city=detailed_location_list[0],

                            input_state=found_state.name
                            if found_state is not None
                            else '',

                            input_country=found_country.name
                            if found_country is not None
                            else '',
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

                        delimited_state_string=(
                            delimit_string(
                                input_string=detailed_location_list[1]
                            )
                        )
                    )
                )
                if found_city is not None:
                    # print("Found city", flush=True)
                    found_state: State = found_city.state
                    found_country: Country = found_state.country
                    found_subregion: Subregion = (
                        found_country.subregion)
                    found_region: Region = found_country.region

        if found_country is None:
            pass
            # print("No country found", flush=True)
        # else:
        #     print('found_country', flush=True)
        #     print(found_country, flush=True)

        new_location: dict = cleanup_locations(
            derive_locations(
                {},
                found_region=found_region,
                found_subregion=found_subregion,
                found_country=found_country,
                found_state=found_state,
                found_city=found_city,
            )
        )

        # print(str(new_location), flush=True)
        new_location: Location = Location(
            region_id=new_location.get('region_id'),
            subregion_id=new_location.get('subregion_id'),
            country_id=new_location.get('country_id'),
            state_id=new_location.get('state_id'),
            city_id=new_location.get('city_id'),
            latitude=new_location.get('latitude'),
            longitude=new_location.get('longitude'),
            remote=remote_flag,
        )

        # print(str(new_location), flush=True)

        # print("CHECK REDO " + str(detailed_location_list), flush=True)
        # print("CHECK REDO " + str(attempt_as_city), flush=True)

        # Shift to the right and attempt to find country instead
        if (not attempt_as_city and
                not attempt_as_state and
                new_location is None or
                (new_location is not None and
                 new_location.latitude is None and
                 new_location.longitude is None) and
                detailed_location_list[0] == '' and
                detailed_location_list[2] != ''):
            # print("Attempting parse without shifting to right", flush=True)
            return string_to_location(
                str(string_to_parse),
                remote_flag,
                attempt_as_city=True)
        elif (attempt_as_city and
              new_location is None or
              (new_location is not None and
               new_location.latitude is None and
               new_location.longitude is None) and
              detailed_location_list[0] != '' and
              detailed_location_list[2] == ''):
            # print("Attempting parse as state only", flush=True)
            return string_to_location(
                str(string_to_parse),
                remote_flag,
                attempt_as_state=True)

        return new_location if new_location is not None else None


def look_for_location(location_to_find: Location):
    if (Location.longitude is None and
            Location.latidue is None):
        return Location

    if (db.session.query(
            exists().where(
                and_(
                    ((Location.region_id == location_to_find.region_id)
                     if location_to_find.region_id is not None
                     else True),
                    
                    ((Location.subregion_id == location_to_find.subregion_id)
                     if location_to_find.subregion_id is not None
                     else True),

                    ((Location.country_id == location_to_find.country_id)
                     if location_to_find.country_id is not None
                     else True),

                    ((Location.state_id == location_to_find.state_id)
                     if location_to_find.state_id is not None
                     else True),

                    ((Location.city_id == location_to_find.city_id)
                     if location_to_find.city_id is not None
                     else True),

                    ((Location.latitude == location_to_find.latitude)
                     if location_to_find.latitude is not None
                     else True),

                    ((Location.longitude == location_to_find.longitude)
                     if location_to_find.longitude is not None
                     else True),

                    ((Location.remote == location_to_find.remote)
                     if location_to_find.remote is not None
                     else True),
                )
            )
    ).scalar()):
        selected_location: Location = (
            db.session.query(Location).filter(
                and_(
                    ((Location.region_id == location_to_find.region_id)
                     if location_to_find.region_id is not None
                     else True),

                    ((Location.subregion_id == location_to_find.subregion_id)
                     if location_to_find.subregion_id is not None
                     else True),

                    ((Location.country_id == location_to_find.country_id)
                     if location_to_find.country_id is not None
                     else True),

                    ((Location.state_id == location_to_find.state_id)
                     if location_to_find.state_id is not None
                     else True),

                    ((Location.city_id == location_to_find.city_id)
                     if location_to_find.city_id is not None
                     else True),

                    ((Location.latitude == location_to_find.latitude)
                     if location_to_find.latitude is not None
                     else True),

                    ((Location.longitude == location_to_find.longitude)
                     if location_to_find.longitude is not None
                     else True),

                    ((Location.remote == location_to_find.remote)
                     if location_to_find.remote is not None
                     else True),
                )
            ).first()
        )

        return selected_location

    return None
