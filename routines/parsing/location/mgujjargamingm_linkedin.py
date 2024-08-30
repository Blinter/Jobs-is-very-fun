"""
mgujjargamingm | LinkedIn Data Scraper
Endpoint
Search Jobs
"""
import re

from routines.parsing.find_location import (
    find_state,
    find_city,
    find_country,
    derive_locations,
    fix_city_name,
    two_letter_matches_string,
    delimit_string,
    three_letter_matches_string, find_linkedin_geourn_id, get_country_by_id
)


def mgujjargamingm_linkedin_search_jobs(dict_new, input_json=None):
    """
    mgujjargamingm | LinkedIn Data Scraper
    fixed for location with Bulk data scraper
    """
    job_locations = {}
    # print("count " + str(len(dict_new)), flush=True)
    for i in dict_new.keys():
        # print("processing key: " + str(i), flush=True)
        detailed_location = dict_new[i].get(
            'formattedLocation',
            dict_new[i].get('secondaryDescription')
        )

        # Most likely a status message string
        if detailed_location is None:
            continue

        # print(str(dict_new[i]), flush=True)
        # print(str(dict_new[i].get('formattedLocation')), flush=True)

        remote_jobs_test = dict_new[i].get('workplaceTypes', False)
        if isinstance(remote_jobs_test, list):
            for j in remote_jobs_test:
                if 'remote' in j.lower():
                    remote_jobs_test = True

        if not remote_jobs_test:
            if dict_new[i].get('jobPostingTitle') is not None:
                if 'remote' in dict_new[i].get('jobPostingTitle').lower():
                    remote_jobs_test = True

        if not remote_jobs_test:
            if dict_new[i].get('secondaryDescription') is not None:
                if 'remote' in dict_new[i].get('secondaryDescription').lower():
                    remote_jobs_test = True

        if not remote_jobs_test:
            if dict_new[i].get('title') is not None:
                if 'remote' in dict_new[i].get('title').lower():
                    remote_jobs_test = True

        if not isinstance(remote_jobs_test, bool):
            remote_jobs_test = False

        parsed_location_list = {
            'source__jobs': "mgujjargamingm | LinkedIn Data Scraper",
            'remote__jobs': remote_jobs_test,
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
            'location_original': dict_new[i].get(
                'formattedLocation', dict_new[i].get('secondaryDescription')
            )
        }

        found_region = None
        found_subregion = None
        found_country = None
        found_state = None
        found_city = None

        # Regex zip code

        found_zip_code: list = (
            re.findall(r'\b\d{5}(?:-\d{4})?$', (
                parsed_location_list.get('location_original')
            ))
            if parsed_location_list.get('location_original', None)
            else None
        )

        # Remove zip code from the location
        if found_zip_code is not None and len(found_zip_code) != 0:
            parsed_location_list['location_original_zip'] = found_zip_code[0]
            parsed_location_list['location_original'] = (
                parsed_location_list.get('location_original').replace(
                    found_zip_code[0], "").strip(" "))

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

        if (input_json is not None and
                len(detailed_location_list) <= 3):
            # print("City, State, Country format not found", flush=True)
            # raise KeyError('City, State, Country format not found')
            # Likely an empty string, so we need to infer off the search
            # parameters instead. worst case scenario, tag location as remote.
            search_parameters = input_json

            location_string = search_parameters.get('location')

            if location_string is None:
                if search_parameters.get('searchLocationId') is not None:
                    location_string = find_linkedin_geourn_id(
                        int(search_parameters.get('searchLocationId').strip())
                    )
                    if location_string is not None:
                        location_string = get_country_by_id(
                            location_string.country_id
                        )
                        location_string = location_string.name

            if location_string is None:
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
            detailed_location_list.extend([
                j.strip(" ")
                for j in location_string.split(',')
            ])
            # print(str(detailed_location_list), flush=True)

        # Clean detailed_location_list
        temp_location_list = []

        for j in detailed_location_list:
            if j not in temp_location_list:
                temp_location_list.append(j)
        detailed_location_list: list = temp_location_list

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

        if parsed_location_list.get('country_original', False):
            # default to the last index for input
            # print("Find Country: " + str(detailed_location_list[-1]),
            #       flush=True)
            # print(str(len(detailed_location_list)), flush=True)
            found_country = find_country(
                parsed_location_list.get('country_original')
            )

        if found_country:
            # print(str(i) + " Find Country Found: " +
            #       str(detailed_location_list[-1]), flush=True)

            # Default: 2nd to last location input
            if (not parsed_location_list.get('state_original', False) and
                    not parsed_location_list.get('city_original', False)):
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
            # print(str(delimited_state), flush=True)

            found_state = None

            if parsed_location_list.get('state_stripped'):
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

                    # Attempt city parse instead
                    if found_city is None:
                        found_city = find_city(
                            country_id=found_country.id
                            if found_country else -1,
                            state_id=-1,
                            city_string=detailed_address_state,
                            delimited_string=[],
                        )
                        if found_city is None:
                            found_city = find_city(
                                country_id=found_country.id
                                if found_country else -1,
                                state_id=-1,
                                city_string=detailed_address_state,
                                delimited_string=delimited_state,
                            )

            if not parsed_location_list.get('city_original', False):
                # Can't go any further
                # print(str(detailed_location_list), flush=True)
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
                parsed_location_list.get('city_original', '')
                .replace("()", "")
                .replace("[]", "")
                .strip(" ")
            )

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
