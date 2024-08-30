"""
avadataservices | Job Postings
Endpoint
/api/v2/Jobs/{slug}
"""
from routines.parsing.find_location import (
    find_state,
    find_city,
    find_country,
    parse_location_to_detailed_list,
    derive_locations,
    fix_city_name,
    delimit_string,
    two_letter_matches_string,
    delimit_two_letter_matches_string,
    three_letter_matches_string,
    delimit_three_letter_matches_string
)


def clean_string(input_string: str):
    """
    Cleans string from the location given in data from ava data services.
    """
    cleaned_string = input_string.strip()
    parts = [part.strip() for part in cleaned_string.split('\n')]
    unique_parts = list(dict.fromkeys(parts))
    cleaned_string = ' '.join(unique_parts)

    return cleaned_string


def ava_data_services_job_postings_job_slug(dict_new):
    """
    avadataservices | Job Postings
    """
    job_locations = {}
    # print("count " + str(len(dict_new)), flush=True)
    for i in dict_new.keys():
        # print("processing key: " + str(i), flush=True)
        # print(str(dict_new[i]), flush=True)
        parsed_location_list = {
            'location_original': dict_new[i].get('location'),
            'source__jobs': "avadataservices | Job Postings",
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

        detailed_location = clean_string(dict_new[i].get('location'))

        # Most likely a status message string
        if detailed_location is None:
            continue

        # print(detailed_location, flush=True)

        detailed_location_list: list = parse_location_to_detailed_list(
            detailed_location
        )

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

        found_region = None
        found_subregion = None
        found_country = None
        found_state = None
        found_city = None

        if isinstance(detailed_location_list, list):
            # start with State String
            if (detailed_location_list[1] is not None and
                    detailed_location_list[1] != ''):

                detailed_address_state = (
                    detailed_location_list[1]
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

                found_state = find_state(
                    country_id=-1,
                    state_string=detailed_location_list[1],
                    regex_letter_code=state_regex,
                    delimited_string=[],
                )

                if found_state is None:
                    found_state = find_state(
                        country_id=-1,
                        state_string=detailed_location_list[1],
                        regex_letter_code=state_regex,
                        delimited_string=delimited_state,
                    )

            if (detailed_location_list[2] is not None and
                    detailed_location_list[2] != ''):
                found_country = find_country(
                    country_string=detailed_location_list[2]
                )

            # Check again after finding State
            if (found_state is None and
                    detailed_location_list[1] is not None and
                    detailed_location_list[1] != ''):

                found_state = find_state(
                    country_id=found_country.id if found_country else -1,
                    state_string=detailed_location_list[1],
                    regex_letter_code=(
                        delimit_two_letter_matches_string(
                            detailed_location_list[1]) + 
                        delimit_three_letter_matches_string(
                                detailed_location_list[1])),
                    delimited_string=[],
                )

                if found_state is None:
                    found_state = find_state(
                        country_id=found_country.id if found_country else -1,
                        state_string=detailed_location_list[1],
                        regex_letter_code=(
                            delimit_two_letter_matches_string(
                                detailed_location_list[1]) +
                            delimit_three_letter_matches_string(
                                detailed_location_list[1])
                        ),
                        delimited_string=delimit_string(
                            length_combo=2,
                            input_string=detailed_location_list[1]
                        ),
                    )

            # Check for city
            if (detailed_location_list[0] is not None and
                    detailed_location_list[0] != ''):

                delimited_city: list = delimit_string(
                    length_combo=2,
                    input_string=detailed_location_list[0]
                )

                parsed_location_list['city_delimited'] = delimited_city
                # print(str(delimited_city), flush=True)

                found_city = find_city(
                    country_id=found_country.id if found_country else -1,
                    state_id=found_state.id if found_state else -1,
                    city_string=detailed_location_list[0],
                    delimited_string=[],
                )

                if found_city is None:
                    found_city = find_city(
                        country_id=found_country.id if found_country else -1,
                        state_id=found_state.id if found_state else -1,
                        city_string=detailed_location_list[0],
                        delimited_string=delimit_string(
                            length_combo=2,
                            input_string=detailed_location_list[0]
                        ),
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
