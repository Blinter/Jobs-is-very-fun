"""
Dodocr7 | Google Jobs
Endpoint
OfferInfo
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


def dodocr7_google_jobs_offer_info(job_info):
    """
    Dodocr7 | Google Jobs
    """
    job_locations = {}

    # Quick fix for parsing
    if len(job_info) == 1:
        job_info = job_info[list(job_info.keys())[0]]

    else:
        print("Parsing Offer info Error.", flush=True)
        raise ValueError("Parsing Offer info Error.")

    key_name = job_info.get('googleUrl')
    detailed_location = job_info.get('location')
    # Most likely a status message string
    if detailed_location is None:
        return
    # print(str(job_info), flush=True)
    # print(str(job_info.get('job_location')), flush=True)

    parsed_location_list = {
        'source__jobs': "Dodocr7 | Google Jobs",
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
        'location_original': job_info.get('location', None)
    }

    found_region = None
    found_subregion = None
    found_country = None
    found_state = None
    found_city = None

    # check if job location is listed as remote
    if ((parsed_location_list.get('location_original') is not None and
         parsed_location_list.get('location_original').lower() == 'anywhere' or
        parsed_location_list.get('location_original').lower() == 'none' or
        parsed_location_list.get('location_original').lower() == 'remote') or
            (job_info.get('is_remote', None) is not None and
             job_info.get('is_remote', None))):
        parsed_location_list['remote__jobs'] = True

    # Regex zip code
    found_zip_code: list = (
        re.findall(r'\b\d{5}(?:-\d{4})?$', (
            parsed_location_list.get('location_original')))
        if parsed_location_list.get('location_original') is not None
        else None
    )

    # Remove zip code from the location
    if found_zip_code is not None and len(found_zip_code) != 0:
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
        for j in parsed_location_list.get('location_original').split(',')
    ]

    '''
    print("Location Original: " + str(parsed_location_list.get(
        'location_original')), flush=True)
    '''

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

    if found_country is not None:
        found_subregion = found_country.subregion
        found_region = found_country.region

        # Default: 2nd to last location input
        if len(detailed_location_list) == 1:
            # Can't go any further
            job_locations[key_name] = derive_locations(
                found_region=found_region,
                found_subregion=found_subregion,
                found_country=found_country,
                found_state=found_state,
                found_city=found_city,
                parsed_location_list=parsed_location_list
            )

            return job_locations

        detailed_address_state = (
            detailed_location_list[-2]
            .replace("()", "")
            .replace("[]", "")
            .strip(" ")
        )

        # save stripped state string
        parsed_location_list['state_stripped'] = detailed_address_state

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

        # Default: 3rd to last location input
        # save original search string
        if len(detailed_location_list) == 2:
            # Can't go any further
            job_locations[key_name] = derive_locations(
                found_region=found_region,
                found_subregion=found_subregion,
                found_country=found_country,
                found_state=found_state,
                found_city=found_city,
                parsed_location_list=parsed_location_list
            )

            return job_locations

        detailed_address_city = (
            parsed_location_list.get('city_original', '')
            .replace("()", "")
            .replace("[]", "")
            .strip(" ")
        )

        parsed_location_list['city_stripped'] = detailed_address_city

        delimited_city_string: list = delimit_string(
            length_combo=2,
            input_string=detailed_address_city
        )

        parsed_location_list['city_delimited']: list = delimited_city_string
        # print(str(delimited_city_string), flush=True)

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
                delimited_string=delimited_city_string,
            )

    job_locations[key_name] = derive_locations(
            found_region=found_region,
            found_subregion=found_subregion,
            found_country=found_country,
            found_state=found_state,
            found_city=found_city,
            parsed_location_list=parsed_location_list
        )

    return job_locations
