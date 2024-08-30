"""
Jobwiz | Job Search API
Endpoints:
searchJob
"""
from routines.parsing.find_location import (
    find_state,
    find_city,
    find_country,
    derive_locations,
    fix_city_name,
    two_letter_matches_string,
    delimit_string, three_letter_matches_string
)


def jobwiz_job_search_search_job(dict_new, input_json):
    """
    Jobwiz | Job Search API
    """
    job_locations = {}

    # print("count " + str(len(dict_new)), flush=True)
    for i in dict_new.keys():
        # print("processing key: " + str(i), flush=True)
        detailed_location = dict_new[i].get('location')

        # Most likely a status message string
        if detailed_location is None:
            continue
        # print(str(dict_new[i]), flush=True)
        # print(str(dict_new[i].get('location')), flush=True)

        parsed_location_list = {
            'source__jobs': "Jobwiz | Job Search API",
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
            'location_original': dict_new[i].get('location', None),
            'country_original': input_json.get('country', None),
            'city_original': input_json.get('city', None)
        }

        found_region = None
        found_subregion = None
        found_country = None
        found_state = None
        found_city = None

        if not parsed_location_list.get('city_original', False):
            parsed_location_list['city_original'] = fix_city_name(
                input_city=parsed_location_list.get('city_original'),
                input_state='',
                input_country=parsed_location_list.get(
                    'country_original', ''),
            )

        # Location Example
        # Jersey City, New Jersey
        # location input JSON parameter contains Country Name
        detailed_location_list: list = [
            j.strip(" ")
            for j in detailed_location.split(',')
        ]
        # print(str(detailed_location_list), flush=True)

        if len(detailed_location_list) != 3:
            # print("City, State, Country format not found", flush=True)
            # Likely an empty string, so we need to infer off the search
            # parameters instead. worst case scenario, tag location as remote.
            search_parameters = input_json
            searched_city = search_parameters.get('city', None)
            searched_country = search_parameters.get('country', None)
            remote_only_search = search_parameters.get('remoteOnly', None)
            location_string = (
                (searched_city + "," if searched_city is not None else "") +
                (searched_country if searched_country is not None else "")
            )

            if (remote_only_search or
                    location_string is None or
                    location_string.lower() == 'anywhere' or
                    searched_city.lower() == 'anywhere' or
                    searched_country.lower() == 'anywhere' or
                    'anywhere' in detailed_location_list or
                    'Anywhere' in detailed_location_list):
                # Likely no location.
                # print("City, State, Country format not found and input "
                #      "parameters indicates no string.", flush=True)
                # use search queries which have the same format if possible.

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

            # Try and split, add to end since location input from query would
            # be prioritized when working from the back of the location list.
            detailed_location_list: list = detailed_location_list + [
                j.strip(" ")
                for j in location_string.split(',')
                if (j is not None and
                    j != "" and
                    j not in detailed_location_list)
            ]
            # print("Detailed" + " " + str(detailed_location_list), flush=True)

        parsed_location_list['combined_location_original']: list = (
            detailed_location_list)
        # The detailed_location_list has been reset,
        # derive the City and State values from the listing details.

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

        if len(detailed_location_list) >= 3:
            # default to the last index for input
            found_country = find_country(
                detailed_location_list[-1]
            )

        if found_country:
            found_subregion = found_country.subregion
            found_region = found_country.region

            # Cleanup list if found_country is equal to iso2 or iso3.
            temp_detailed_state = detailed_location_list[-2]

            # print("Detailed State: " + str(temp_detailed_state), flush=True)
            if (temp_detailed_state.lower() == found_country.name.lower() or
                temp_detailed_state.lower() == found_country.iso2.lower() or
                    temp_detailed_state.lower() == found_country.iso3.lower()):
                # print("popping", flush=True)
                detailed_location_list.pop(-2)

                # update the list
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
                        input_state=parsed_location_list.get(
                            'state_original', ''),
                        input_country=parsed_location_list.get(
                            'country_original', ''),
                    )

                    if len(detailed_location_list) >= 3:
                        detailed_location_list[-3] = (
                            parsed_location_list.get('city_original'))

                parsed_location_list['combined_location_original'] = (
                    detailed_location_list)

            if temp_detailed_state.lower() == 'anywhere':
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
                detailed_location_list[-2]
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
                # length_combo=1,
                input_string=detailed_address_state
            )

            parsed_location_list['state_delimited']: list = delimited_state

            # Debug any delimited matches
            # print("Delimited: " + str(delimited_state), flush=True)

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
                # length_combo=1,
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

        if (found_country is None and
                found_state is None and
                found_city is None):
            # Attempt to  find a country
            while len(detailed_location_list) != 0:
                temp_locality = detailed_location_list.pop()

                temp_locality = (
                    temp_locality
                    .replace("()", "")
                    .replace("[]", "")
                    .strip(" ")
                )

                regex: list = (
                    two_letter_matches_string(temp_locality) + 
                    three_letter_matches_string(temp_locality)
                )

                delimited_locality: list = delimit_string(
                    input_string=temp_locality,
                    # length_combo=1
                )

                found_country = find_country(temp_locality)

                if not found_country:
                    found_state = find_state(
                        country_id=-1,
                        state_string=temp_locality,
                        regex_letter_code=regex,
                        delimited_string=[]
                    )

                    if found_state is None:
                        found_state = find_state(
                            country_id=-1,
                            state_string=temp_locality,
                            regex_letter_code=regex,
                            delimited_string=delimited_locality
                        )

                    if not found_state:
                        found_city = find_city(
                            country_id=-1,
                            state_id=-1,
                            city_string=temp_locality,
                            delimited_string=[]
                        )

                        if found_city is None:
                            found_city = find_city(
                                country_id=-1,
                                state_id=-1,
                                city_string=temp_locality,
                                delimited_string=delimited_locality
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
