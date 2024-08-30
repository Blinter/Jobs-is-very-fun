"""
jobisite | Job Search
Endpoint
Search Jobs
"""
from routines.parsing.find_location import (
    find_state,
    find_city,
    find_country,
    derive_locations,
    fix_city_name,
    delimit_string,
    two_letter_matches_string, three_letter_matches_string
)


def jobisite_job_search(dict_new, input_json):
    """
    jobisite | Job Search
    """
    job_locations = {}
    # print("count " + str(len(dict_new)), flush=True)
    for i in dict_new.keys():
        # print("processing key: " + str(i), flush=True)
        # print(str(dict_new[i]), flush=True)
        # print(str(dict_new[i].get('location')), flush=True)

        parsed_location_list = {
            'source__jobs': "jobisite | Job Search",
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
            'city': None
        }

        found_region = None
        found_subregion = None
        found_country = None
        found_state = None
        found_city = None

        # Country: "United States of America"
        # state: "New York"
        # city: "New York"
        parsed_location_list['location_original'] = {
            'country': dict_new[i].get('Country', None),
            'state': dict_new[i].get('state', None),
            'city': (fix_city_name(
                input_city=dict_new[i].get('city', ''),
                input_state=dict_new[i].get('state', ''),
                input_country=dict_new[i].get('Country', '')
            ) if dict_new[i].get('city', None) is not None else ''),
        }

        # print(str(parsed_location_list['location_original']['city']),
        #       flush=True)

        detailed_location: list = parsed_location_list.get('location_original')

        # Most likely a status message string
        if detailed_location is None:
            continue

        # possible input location
        # {"filter": "skill": "Software Engineer",
        # "location": "New York", "limit": 10}
        # search_filters = input_json.get("filters")
        # search_filters.get("location")

        search_parameters = input_json

        search_filters = search_parameters.get('filter')

        if (search_filters and
                isinstance(search_filters, dict) and
                search_filters.get('location') is not None):
            parsed_location_list['input_location_original'] = (
                search_filters.get('location'))

        # Default location as
        # length 3: City, State, Country
        # length 2: State, Country
        # length 1: Country
        temp_input_locations = []

        if (parsed_location_list.get('input_location_original') is not None):
            temp_input_locations: list = [(
                j.strip(" ")
                for j in parsed_location_list.get('input_location_original')
            )]

        temp_input_locations_dict = {}

        if isinstance(temp_input_locations, list):
            match len(temp_input_locations):
                case 0:
                    pass

                case 1:
                    temp_input_locations_dict['country'] = (
                        temp_input_locations[-1])

                case 2:
                    temp_input_locations_dict['country'] = (
                        temp_input_locations[-1])
                    temp_input_locations_dict['state'] = (
                        temp_input_locations[-2])

                case _:
                    temp_input_locations_dict['country'] = (
                        temp_input_locations[-1])
                    temp_input_locations_dict['state'] = (
                        temp_input_locations[-2])
                    temp_input_locations_dict['city'] = (
                        temp_input_locations[-3])

        # Attempt to fill in location list with priority over job details.
        detailed_location_list: list = [None, None, None]

        # Set Country
        if temp_input_locations_dict.get('country') is not None:
            detailed_location_list[-1] = temp_input_locations_dict.get(
                'country')

        if (parsed_location_list['location_original'].get('country') is
                not None):
            detailed_location_list[-1] = (
                parsed_location_list['location_original'].get('country')
            )

        # Set State
        if temp_input_locations_dict.get('state') is not None:
            detailed_location_list[-2] = temp_input_locations_dict.get('state')

        if (parsed_location_list['location_original'].get('state') is not None):
            detailed_location_list[-2] = (
                parsed_location_list['location_original'].get('state')
            )

        # Set City
        if parsed_location_list['location_original'].get('city', False):
            detailed_location_list[-3] = (
                parsed_location_list['location_original'].get('city')
            )

        if parsed_location_list['location_original'].get('city', False):
            parsed_location_list['location_original']['city'] = (
                parsed_location_list['location_original'].get('city')
            )
        if len(detailed_location_list) > 0:
            # Find country
            found_country = find_country(detailed_location_list[-1])

        if found_country is not None:
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

                elif len(detailed_location_list) >= 2:
                    parsed_location_list['state_original'] = (
                        detailed_location_list[-2])

                elif len(detailed_location_list) >= 3:
                    parsed_location_list['city_original'] = (
                        detailed_location_list[-3])

                parsed_location_list['combined_location_original'] = (
                    detailed_location_list)

            if temp_detailed_state.lower() == 'anywhere':
                # We will default back to remote.
                # print("Defaulting to remote location instead.", flush=True)
                parsed_location_list['remote'] = True

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
                length_combo=2,
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
            ) if (detailed_location_list is not None and
                  len(detailed_location_list) >= 3 and
                  detailed_location_list[-3] is not None and
                  len(detailed_location_list[-3]) != 0) else []

            parsed_location_list['city_stripped'] = detailed_address_city

            delimited_city: list = delimit_string(
                length_combo=2,
                input_string=detailed_address_city
            )

            parsed_location_list['city_delimited']: list = delimited_city
            # print(str(delimited_city), flush=True)

            found_city = find_city(
                country_id=found_country.id if found_country else -1,
                state_id=found_state.id if found_state else -1,
                city_string=str(detailed_address_city),
                delimited_string=[],
            )

            if found_city is None:
                found_city = find_city(
                    country_id=found_country.id if found_country else -1,
                    state_id=found_state.id if found_state else -1,
                    city_string=str(detailed_address_city),
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
