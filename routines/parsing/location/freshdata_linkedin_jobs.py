"""
Freshdata | Linkedin Jobs
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
    two_letter_matches_string,
    find_city_and_state,
    find_linkedin_geourn_id, three_letter_matches_string
)

from routines.parsing.location.misc.linkedin_job_types import (
    linkedin_job_types_list
)


def freshdata_search_jobs(dict_new, input_json):
    """
    Freshdata | Linkedin Jobs
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
            'source__jobs': "Freshdata | Linkedin Jobs",
            'remote__jobs': dict_new[i].get('remote', '').lower() == 'remote',
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
            'location_country_id_original': input_json.get('country')
        }

        found_region = None
        found_subregion = None
        found_country = None
        found_state = None
        found_city = None

        # Location Example
        # Jersey City, New Jersey
        # location input JSON parameter contains Country Name
        detailed_location_list: list = [
            j.strip(" ")
            for j in detailed_location.split(',')
        ]

        # print(str(detailed_location_list), flush=True)

        if len(detailed_location_list) != 3:
            search_parameters = input_json
            searched_country = search_parameters.get('geo_code')

            if searched_country.lower() == 'anywhere':
                parsed_location_list['remote__jobs'] = True

            # Match GeoUrn ID to ISO2
            if searched_country is not None:
                try:
                    searched_country = int(searched_country)
                except Exception as e:
                    print(str(e), flush=True)
                    raise e

                searched_country = (
                    find_linkedin_geourn_id(int(searched_country))
                )
                if searched_country is not None:
                    searched_country = searched_country.country.iso2

            location_string = (
                (searched_country if searched_country is not None else "")
            )

            if not isinstance(detailed_location_list, list):
                detailed_location_list: list = []

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

        # Parse Job Type within location
        # example
        # Mequon, WI (Hybrid), US
        # print(str(detailed_location_list[-2].lower()), flush=True)
        # print(str(linkedin_job_types_list.keys()), flush=True)
        if (len(detailed_location_list) >= 3 and
                detailed_location_list[-2] is not None):

            for j in linkedin_job_types_list.keys():
                if detailed_location_list[-2].lower().find(str(j)) != -1:
                    parsed_location_list['job_type'] = (
                        linkedin_job_types_list[j]
                    )

                    # Strip from string
                    detailed_location_list[-2] = (
                        detailed_location_list[-2]
                        .lower()
                        .replace(str(j), "")
                        .strip(" ")
                    )

                    # print("Setting detailed_location_list[-2] to " +
                    #       str(detailed_location_list[-2]), flush=True)
                    break

        # Reset remote status if the newly set job_type is not Remote.
        if (parsed_location_list.get('job_type', None) is not None and
                parsed_location_list.get('job_type') != "Remote"):
            parsed_location_list['remote__jobs'] = False

        parsed_location_list['combined_location_original'] = (
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
                input_state=parsed_location_list.get(
                    'state_original', ''),
                input_country=parsed_location_list.get(
                    'country_original', ''),
            )

            if len(detailed_location_list) >= 3:
                detailed_location_list[-3] = (
                    parsed_location_list.get('city_original'))

        if (len(detailed_location_list) >= 3 and
                parsed_location_list.get('country_original', None) is not None):
            # default to the last index for input
            found_country = find_country(parsed_location_list.get(
                'country_original'))

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

            else:
                # Fallback to City
                found_city = find_city(
                    country_id=found_country.id if found_country else -1,
                    state_id=-1,
                    city_string=detailed_address_state,
                    delimited_string=[]
                )

                if found_city is None:
                    found_city = find_city(
                        country_id=found_country.id if found_country else -1,
                        state_id=-1,
                        city_string=detailed_address_state,
                        delimited_string=delimited_state
                    )

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
                input_string=detailed_address_city,
                length_combo=2
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

        if (found_country is None and
                found_state is None and
                found_city is None):
            # Attempt to  find a country
            while len(detailed_location_list) != 0:
                temp_locality = detailed_location_list.pop()
                found_country = find_country(temp_locality)

                if not found_country:
                    found_state = find_state(
                        country_id=-1,
                        state_string=temp_locality,
                        regex_letter_code=list(),
                        delimited_string=list()
                    )

                    if not found_state:
                        found_city = find_city(
                            country_id=-1,
                            state_id=-1,
                            city_string=temp_locality,
                            delimited_string=list()
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


def freshdata_get_job_details(dict_new):
    """
    Freshdata | Linkedin Jobs
    """
    job_locations = {}
    # print("count " + str(len(dict_new)), flush=True)
    for i in dict_new.keys():
        # print("processing key: " + str(i), flush=True)
        detailed_location = dict_new[i].get('job_location', '')
        # Most likely a status message string
        if detailed_location is None:
            continue

        # print(str(dict_new[i]), flush=True)
        # print(str(dict_new[i].get('location')), flush=True)

        parsed_location_list = {
            'source__jobs': "Freshdata | Linkedin Jobs",
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
            'location_original': dict_new[i].get('job_location', '')
        }

        found_region = None
        found_subregion = None
        found_country = None
        found_state = None
        found_city = None

        # Location Example
        # Jersey City, New Jersey
        # location input JSON parameter contains Country Name
        detailed_location_list: list = [
            j.strip(" ")
            for j in detailed_location.split(',')
        ]

        # print(str(detailed_location_list), flush=True)

        # print("Detailed" + " " + str(detailed_location_list), flush=True)

        # Parse Job Type within location
        # example
        # Mequon, WI (Hybrid), US
        # print(str(detailed_location_list[-2].lower()), flush=True)

        # Reset remote status if the newly set job_type is not Remote.
        if (parsed_location_list.get('job_type', None) is not None and
                parsed_location_list.get('job_type') != "Remote"):
            parsed_location_list['remote__jobs'] = False

        parsed_location_list['combined_location_original'] = (
            detailed_location_list)

        # The detailed_location_list has been reset,
        # derive the City and State values from the listing details.

        # save originals
        if len(detailed_location_list) >= 1:
            detailed_address_state = detailed_location_list[-1]
            parsed_location_list['state_original'] = (
                detailed_location_list[-1])

            # Test country first
            found_country = find_country(parsed_location_list['state_original'])

            if found_country is not None:
                found_subregion = found_country.subregion
                found_region = found_country.region

            # Test for state
            parsed_location_list['state_stripped'] = detailed_address_state

            state_regex = (
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
            if (detailed_address_state is not None and
                    detailed_address_state != ''):

                # Test country first
                found_country = find_country(detailed_address_state)

                if found_country is None:
                    found_state = find_state(
                        country_id=-1,
                        state_string=detailed_address_state,
                        regex_letter_code=state_regex,
                        delimited_string=[],
                    )

                    if found_state is None:
                        found_state = find_state(
                            country_id=-1,
                            state_string=detailed_address_state,
                            regex_letter_code=state_regex,
                            delimited_string=delimited_state,
                        )

            if found_state is None:
                # Fallback to City
                found_city = find_city(
                    country_id=-1,
                    state_id=-1,
                    city_string=detailed_address_state,
                    delimited_string=[]
                )

                if found_city is None:
                    found_city = find_city(
                        country_id=-1,
                        state_id=-1,
                        city_string=detailed_address_state,
                        delimited_string=delimited_state
                    )

        if len(detailed_location_list) >= 2:
            # Fix city naming for Geo database
            parsed_location_list['city_original'] = fix_city_name(
                input_city=detailed_location_list[-2],
                input_state=parsed_location_list.get(
                    'state_original', ''),
                input_country=parsed_location_list.get(
                    'country_original', ''),
            )

            if len(detailed_location_list) >= 2:
                detailed_location_list[0] = (
                    parsed_location_list.get('city_original'))

            detailed_address_state = (
                detailed_location_list[-1]
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
            if (detailed_address_state is not None and
                    detailed_address_state != ''):

                # Test country first
                found_country = find_country(detailed_address_state)

                if found_country is None:
                    found_state = find_state(
                        country_id=-1,
                        state_string=detailed_address_state,
                        regex_letter_code=state_regex,
                        delimited_string=[],
                    )

                    if found_state is None:
                        found_state = find_state(
                            country_id=-1,
                            state_string=detailed_address_state,
                            regex_letter_code=state_regex,
                            delimited_string=delimited_state,
                        )

            if found_state is None:
                # Fallback to City
                found_city = find_city(
                    country_id=-1,
                    state_id=-1,
                    city_string=detailed_address_state,
                    delimited_string=[]
                )

                if found_city is None:
                    found_city = find_city(
                        country_id=-1,
                        state_id=-1,
                        city_string=detailed_address_state,
                        delimited_string=delimited_state
                    )

            # Default: 3rd to last location input
            # save original search string
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

            detailed_address_city = (
                detailed_location_list[0]
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
            found_city = find_city_and_state(
                city_string=detailed_address_city,
                delimited_city_string=delimited_city,
                state_string=detailed_address_state,
                regex_letters_state=state_regex,
                delimited_state_string=delimited_state,
            )

            if not found_city:
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


def freshdata_get_company(dict_new):
    """
    Freshdata | Linkedin Jobs
    Endpoint
    Get Company By Domain (BETA)
    """
    company_locations = []
    for j in dict_new.keys():
        location_list = dict_new[j].get('locations', '')
        # print("count " + str(len(location_list)), flush=True)
        for i in location_list:
            # print("processing: " + str(i), flush=True)
            parsed_location_list = {
                'source__jobs': "Freshdata | Linkedin Jobs",
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
                'location_original': [
                    i.get('city', ''),
                    i.get('geographicArea', ''),
                    i.get('country', ''),
                ],
                'country_original': i.get('country', ''),
                'state_original': i.get('geographicArea', ''),
                'city_original': fix_city_name(
                    input_city=i.get('city', ''),
                    input_state=i.get('geographicArea', ''),
                    input_country=i.get('country', '')
                )
            }

            found_region = None
            found_subregion = None
            found_country = None
            found_state = None
            found_city = None
            # print(str(detailed_location_list), flush=True)

            # print("Detailed" + " " +
            #       str(parsed_location_list['location_original']), flush=True)

            parsed_location_list['country_stripped'] = (
                parsed_location_list['country_original']
                .replace("()", "")
                .replace("[]", "")
                .strip(" ")
            )

            parsed_location_list['state_stripped'] = (
                parsed_location_list['state_original']
                .replace("()", "")
                .replace("[]", "")
                .strip(" ")
            )

            parsed_location_list['city_stripped'] = (
                parsed_location_list['city_original']
                .replace("()", "")
                .replace("[]", "")
                .strip(" ")
            )

            parsed_location_list['state_regex']: list = (
                two_letter_matches_string(
                    parsed_location_list['state_stripped']
                )
            )

            parsed_location_list['state_delimited']: list = delimit_string(
                length_combo=2,
                input_string=parsed_location_list['state_stripped']
            )

            parsed_location_list['city_delimited']: list = delimit_string(
                length_combo=2,
                input_string=parsed_location_list['state_stripped']
            )
            if parsed_location_list['country_stripped'] is not None:
                found_country = find_country(
                    parsed_location_list['country_stripped']
                )

            if (parsed_location_list['state_stripped'] is not None and
                    parsed_location_list['city_stripped'] is not None):

                found_city = find_city_and_state(
                    city_string=parsed_location_list['city_stripped'],
                    delimited_city_string=parsed_location_list[
                        'city_delimited'],
                    state_string=parsed_location_list['state_stripped'],
                    regex_letters_state=parsed_location_list['state_regex'],
                    delimited_state_string=parsed_location_list[
                        'state_delimited'],
                )

            if (not found_city and
                    parsed_location_list['state_stripped'] is not None):
                found_state = find_state(
                    country_id=found_country.id if found_country else -1,
                    state_string=parsed_location_list['state_stripped'],
                    regex_letter_code=parsed_location_list['state_regex'],
                    delimited_string=[],
                )

                if found_state is None:
                    found_state = find_state(
                        country_id=found_country.id if found_country else -1,
                        state_string=parsed_location_list['state_stripped'],
                        regex_letter_code=parsed_location_list['state_regex'],
                        delimited_string=(
                            parsed_location_list['state_delimited']),
                    )

            company_locations.append(
                derive_locations(
                    found_region=found_region,
                    found_subregion=found_subregion,
                    found_country=found_country,
                    found_state=found_state,
                    found_city=found_city,
                    parsed_location_list=parsed_location_list
                )
            )

    return company_locations
