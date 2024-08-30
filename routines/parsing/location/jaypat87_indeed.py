"""
jaypat87 | Indeed
Endpoint
Search
"""
import re

from routines.parsing.find_location import (
    find_state,
    find_city,
    find_country,
    derive_locations,
    fix_city_name,
    two_letter_matches_string,
    delimit_string, three_letter_matches_string
)


def jaypat87_indeed_search(dict_new, input_json):
    """
    jaypat87 | Indeed
    """
    job_locations = {}
    # print("count " + str(len(dict_new)), flush=True)
    for i in dict_new.keys():
        # print("processing key: " + str(i), flush=True)
        detailed_location = dict_new[i].get('location', None)
        # Most likely a status message string
        if detailed_location is None:
            continue
        # print(str(dict_new[i]), flush=True)
        # print(str(dict_new[i].get('location')), flush=True)

        parsed_location_list = {
            'source__jobs': "jaypat87 | Indeed + Job Search",
            'remote__jobs': False,
            'region_id': None,
            'region': None,
            'subregion_id': None,
            'subregion': None,
            'country_id': None,
            'country': None,
            'country_iso3': None,
            'country_iso2': None,
            'state_id': None,
            'state': None,
            'state_code': None,
            'city_id': None,
            'city': None,
            'location_original': dict_new[i].get('location', None)
        }

        found_region = None
        found_subregion = None
        found_country = None
        found_state = None
        found_city = None

        # check if job location is listed as remote
        if ((parsed_location_list.get('location_original') is not None and
             parsed_location_list.get('location_original').lower()
             == 'anywhere' or
            parsed_location_list.get('location_original').lower()
             == 'none' or
            parsed_location_list.get('location_original').lower()
             == 'remote') or
                (dict_new[i].get('is_remote', None) is not None and
                 dict_new[i].get('is_remote', None))):
            parsed_location_list['remote__jobs'] = True

        # Regex zip code

        found_zip_code: list = (
            re.findall(r'\b\d{5}(?:-\d{4})?$', (
                parsed_location_list.get('location_original', '')))
            if parsed_location_list.get('location_original', None) else None
        )

        # Remove zip code from the location
        if (found_zip_code is not None and
                isinstance(found_zip_code, str) and
                len(found_zip_code) != 0):
            parsed_location_list['location_original_zip'] = found_zip_code[0]
            parsed_location_list['location_original'] = (
                parsed_location_list.get('location_original')
                .replace(found_zip_code[0], "")
                .strip(" ")
            )

        # Location Example
        # Jersey City, New Jersey, United States
        detailed_location_list: list = [
            j.strip(" ")
            for j in parsed_location_list.get('location_original')
            .split(',')
        ]

        '''
        print("Location Original: " + str(parsed_location_list.get(
            'location_original')), flush=True)
        '''
        # print(str(detailed_location_list), flush=True)

        if len(detailed_location_list) != 3:
            # print("City, State, Country format not found", flush=True)
            # raise KeyError('City, State, Country format not found')
            # Likely an empty string, so we need to infer off the search
            # parameters instead. worst case scenario, tag location as remote.
            location_string = input_json.get('location', '')

            if (location_string is None and
                    location_string != ''):
                # No location, which is a required string for this endpoint.

                # set as remote or debug
                # We will default back to remote.
                # print("Defaulting to remote location instead.", flush=True)
                parsed_location_list['remote__jobs'] = True

                job_locations[i] = derive_locations(
                    found_region=found_region,
                    found_subregion=found_subregion,
                    found_country=found_country,
                    found_state=found_state,
                    found_city=found_city,
                    parsed_location_list=parsed_location_list
                )

                continue
                # raise KeyError('City, State, Country format
                # and locations in input parameter not found.')
            # extend
            if len(location_string) != 0:
                detailed_location_list.extend([
                    j.strip(" ")
                    for j in location_string.split(',')
                ])

        # print(str(detailed_location_list), flush=True)
        # save originals
        if len(detailed_location_list) >= 1:
            parsed_location_list['country_original'] = (
                detailed_location_list[-1])

        if len(detailed_location_list) >= 2:
            parsed_location_list['state_original'] = (
                detailed_location_list[-2])

        if len(detailed_location_list) >= 3:
            # Fix city naming for Geo database
            parsed_location_list['city_original'] = fix_city_name(
                input_city=detailed_location_list[-3],
                input_state=parsed_location_list.get('state_original', ''),
                input_country=parsed_location_list.get('country_original', ''),
            )
            if len(detailed_location_list) >= 3:
                detailed_location_list[-3] = (
                    parsed_location_list.get('city_original'))

        # print(str(detailed_location_list), flush=True)

        if len(detailed_location_list) >= 3:
            # default to the last index for input
            found_country = find_country(detailed_location_list[-1])

        # Default: 2nd to last location input
        if len(detailed_location_list) == 1:
            # Can't go any further

            job_locations[i] = derive_locations(
                found_region=found_region,
                found_subregion=found_subregion,
                found_country=found_country,
                found_state=found_state,
                found_city=found_city,
                parsed_location_list=parsed_location_list
            )
            continue

        detailed_address_state = (
            parsed_location_list.get('state_original', '')
            .replace("()", "")
            .replace("[]", "")
            .strip(" ")
        )

        # print(detailed_address_state, flush=True)
        # save stripped state string
        parsed_location_list['state_stripped'] = detailed_address_state

        state_regex: list = (
            two_letter_matches_string(detailed_address_state) + 
            three_letter_matches_string(detailed_address_state)
        )

        parsed_location_list['state_regex']: list = state_regex

        delimited_state: list = delimit_string(
            length_combo=2,
            input_string=detailed_address_state
        )

        parsed_location_list['state_delimited']: list = delimited_state

        # Debug any delimited matches
        # print(str(delimited_list_string), flush=True)

        found_state = None

        if detailed_address_state:
            found_state = find_state(
                country_id=found_country.id if found_country else -1,
                state_string=detailed_address_state,
                regex_letter_code=state_regex,
                delimited_string=[],
            )

            if found_state is None:
                found_state = find_state(
                    country_id=found_country.id if found_country else -1,
                    state_string=detailed_address_state,
                    regex_letter_code=state_regex,
                    delimited_string=delimited_state,
                )

        if found_state is not None:
            found_country = found_state.country
            found_subregion = found_state.country.subregion
            found_region = found_state.country.region

        # Default: 3rd to last location input
        # save original search string
        if len(detailed_location_list) == 2:
            # Can't go any further

            job_locations[i] = derive_locations(
                found_region=found_region,
                found_subregion=found_subregion,
                found_country=found_country,
                found_state=found_state,
                found_city=found_city,
                parsed_location_list=parsed_location_list
            )

            continue

        detailed_address_city = (
            detailed_location_list[-3]
            .replace("()", "")
            .replace("[]", "")
            .strip(" ")
        )

        parsed_location_list['city_stripped'] = detailed_address_city

        delimited_city: list = delimit_string(
            input_string=detailed_address_city
        )

        parsed_location_list['city_delimited']: list = delimited_city
        # print(str(delimited_city), flush=True)

        found_city = find_city(
            country_id=found_country.id if found_country else -1,
            state_id=found_state.id if found_state else -1,
            city_string=detailed_address_city,
            delimited_string=[],
        )

        if found_city is None:
            found_city = find_city(
                country_id=found_country.id if found_country else -1,
                state_id=found_state.id if found_state else -1,
                city_string=detailed_address_city,
                delimited_string=delimited_city,
            )

        job_locations[i] = derive_locations(
            found_region=found_region,
            found_subregion=found_subregion,
            found_country=found_country,
            found_state=found_state,
            found_city=found_city,
            parsed_location_list=parsed_location_list
        )

    return job_locations
