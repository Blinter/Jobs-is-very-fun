"""
mantiks | Glassdoor
Endpoints:
Locations Search
Jobs Search
Job details
"""
import re

from routines.parsing.find_location import (
    find_country,
    find_city,
    find_state,
    get_glassdoor_location_from_id,
    get_country_by_id,
    get_city_by_id,
    get_state_by_id,
    find_city_and_state,
    derive_locations,
    fix_city_name,
    delimit_string,
    two_letter_matches_string, three_letter_matches_string
)


def mantiks_glassdoor_locations_search(dict_new: dict):
    """
    mantiks | Glassdoor
    Endpoint: Locations Search
    Updates search location dictionary into a proper format to save
    """
    job_locations = {}
    # print("count " + str(len(dict_new)), flush=True)
    for i in dict_new.keys():
        """
        Example Data
        "country_name": "United States",
        "full_type": "CITY",
        "id": "1147401",
        "long_name": "San Francisco, CA (US)",
        "name": "San Francisco, CA (US)",
        "type": "C"
        """
        # print("processing key: " + str(i), flush=True)

        # Get country name, set country ID
        parsed_location_list = {
            'id': str(i),
            'type': dict_new[str(i)].get("type", None),
            'name': dict_new[str(i)].get("long_name", None),
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
            'country_original': dict_new[i].get('job_country', None),
            'state_original': dict_new[i].get('job_state', None),
            'city_original': dict_new[i].get('job_city', None),
            'latitude_original':  dict_new[i].get('job_latitude', None),
            'longitude_original': dict_new[i].get('job_longitude', None)
        }

        found_region = None
        found_subregion = None
        found_country = None
        found_state = None
        found_city = None

        # Possible values:
        # C: City
        # N: Country
        # M: Metro
        # S: State
        parsed_location_list['full_type'] = dict_new[str(i)].get("full_type")

        parsed_location_list['country_name'] = (
            dict_new[str(i)].get("country_name"))

        parsed_location_list['long_name'] = dict_new[str(i)].get("long_name")

        # Get location then strip two-letter ISO from long_name, then find
        # State_Code in -1 after splitting
        location_detailed_list = [
            j.strip(' ') for j in
            dict_new[str(i)].get('long_name', '').split(',')
            if j.strip(' ') is not None]

        if not parsed_location_list.get('country_name', False):
            job_locations[i] = derive_locations(
                found_region=found_region,
                found_subregion=found_subregion,
                found_country=found_country,
                found_state=found_state,
                found_city=found_city,
                parsed_location_list=parsed_location_list
            )

            continue

        found_country = find_country(parsed_location_list.get('country_name')
        )

        if found_country is not None:
            found_subregion = found_country.subregion
            found_region = found_country.region

            # Clean up location_detailed_list
            for j in range(0, len(location_detailed_list)):
                location_detailed_list[j] = (
                    location_detailed_list[j]
                    .replace("[", "")
                    .replace("]", "")
                    .replace("(", "")
                    .replace(")", "")
                ).strip(" ")

                if (location_detailed_list[j].lower()
                        == found_country.iso3.lower() or
                        location_detailed_list[j].lower()
                        == found_country.iso2.lower() or
                        location_detailed_list[j].lower()
                        == found_country.name.lower()):
                    location_detailed_list[j] = ''

            location_detailed_list = [
                j for j in location_detailed_list
                if j != ''
            ]

            # print("List: " + str(location_detailed_list), flush=True)

        if (len(location_detailed_list) == 0 or
                not parsed_location_list.get('full_type', False) or
                parsed_location_list.get('full_type', 'N') == 'N'):

            job_locations[i] = derive_locations(
                found_region=found_region,
                found_subregion=found_subregion,
                found_country=found_country,
                found_state=found_state,
                found_city=found_city,
                parsed_location_list=parsed_location_list
            )

            continue

            # Add substrings when matching city from the longest combination to
            # shortest

        two_letter_state_matches: list = (
            re.findall(r'\b['r'A-Z]{2}\b', dict_new[str(i)].get('long_name', '')
            )
        )

        three_letter_state_matches: list = (
            re.findall(r'\b['r'A-Z]{3}\b', dict_new[str(i)].get('long_name', '')
            )
        )

        pattern = r' - |,'

        delimited_state: list = (
            re.split(
                pattern,
                str(two_letter_state_matches) + str(three_letter_state_matches)
                .replace("[", "")
                .replace("]", "")
                .replace("(", "")
                .replace(")", "")
                .lower())
        )

        delimited_state = [
            j for j in delimited_state
            if (found_country is None or
                (j.lower() == found_country.iso3.lower() or
                 j.lower() == found_country.iso2.lower() or
                 j.lower() == found_country.name.lower()))
        ]

        for j in str(dict_new[str(i)].get('long_name', '')).lower(
        ).split(' '):
            if (j is not None and
                    j not in delimited_state):
                delimited_state.append(j)

        delimited_state = [
            j.strip(" ").replace('-', '')
            for j in delimited_state
            if j is not None
        ]

        delimited_state = [
            j.lower() for j in delimited_state
            if (j != '[]' and
                j != '()' and
                j is not None)
        ]

        parsed_location_list['state_delimited'] = delimited_state

        temp_delimited_state = []

        for j in range(0, len(delimited_state) + 1):
            string_to_append = ' '.join(delimited_state[0:j])
            if string_to_append not in delimited_state:
                temp_delimited_state.append(string_to_append)

        # Keep original state and insert it in the beginning later.
        if len(delimited_state) != 0:
            first_delimited_state = delimited_state.pop(0)

        else:
            first_delimited_state = None

        # redeclare and manually add shortest combinations first to the
        # delimited array because of Type errors when appending or
        # extending.
        for j in temp_delimited_state:
            if j not in delimited_state:
                delimited_state = [j] + delimited_state

        # Add back the original city to the beginning, with the
        # longest combinations following it.
        if first_delimited_state is not None:
            delimited_state = [first_delimited_state] + delimited_state

        delimited_state = [
            j for j in delimited_state
            if (j != '[]' and
                j != '()' and
                j is not None)
        ]

        parsed_location_list['state_delimited'] = delimited_state

        # print(str(delimited_state), flush=True)

        found_city = None
        found_state = find_state(
            country_id=found_country.id if found_country else -1,
            state_string=location_detailed_list[-1],
            regex_letter_code=(two_letter_state_matches +
                               three_letter_state_matches),
            delimited_string=[]
        )

        if found_state is None:
            found_state = find_state(
                country_id=found_country.id if found_country else -1,
                state_string=location_detailed_list[-1],
                regex_letter_code=(two_letter_state_matches +
                                   three_letter_state_matches),
                delimited_string=delimited_state
            )

        if found_state is None:
            found_city = find_city(
                country_id=found_country.id if found_country else -1,
                state_id=found_state.id if found_state else -1,
                city_string=location_detailed_list[-1],
                delimited_string=[]
            )

            if found_city is None:
                found_city = find_city(
                    country_id=found_country.id if found_country else -1,
                    state_id=found_state.id if found_state else -1,
                    city_string=location_detailed_list[-1],
                    delimited_string=[]
                )

                if not found_city:
                    location_detailed_list.pop()

        else:
            location_detailed_list.pop()

        if (found_city is None and
                len(location_detailed_list) != 0):
            found_city = find_city(
                country_id=found_country.id if found_country else -1,
                state_id=found_state.id if found_state else -1,
                city_string=(location_detailed_list[-1]),
                delimited_string=[]
            )

            if found_city is None:
                found_city = find_city(
                    country_id=found_country.id if found_country else -1,
                    state_id=found_state.id if found_state else -1,
                    city_string=(location_detailed_list[-1]),
                    delimited_string=location_detailed_list[-1].split(" ")
                )

            if found_city is None:
                if len(location_detailed_list) != 0:
                    location_detailed_list.pop()

        job_locations[i] = derive_locations(
            found_region=found_region,
            found_subregion=found_subregion,
            found_country=found_country,
            found_state=found_state,
            found_city=found_city,
            parsed_location_list=parsed_location_list
        )

    return job_locations


def mantiks_glassdoor_jobs_search(dict_new, input_json):
    """
    mantiks | Glassdoor
    Endpoint: Jobs Search
    Uses search by location ID:
    from input_json, derive the location data and return the format.
    """
    locations_to_lookup = []
    locations_to_search = []
    searched_location_id = None

    if (input_json is not None and
            isinstance(input_json, dict) and
            input_json.get('location_id', False)):
        searched_location_id = input_json.get('location_id', -1)
        print("Searched Location ID: " + str(searched_location_id), flush=True)

    searched_country = None
    searched_state = None
    searched_city = None

    found_location = (
        get_glassdoor_location_from_id(int(searched_location_id))
        if searched_location_id != -1
        else None
    )

    if found_location is not None:
        if found_location.country_id is not None:
            searched_country = get_country_by_id(found_location.country_id)
            # print("Preset Country: " + str(searched_country.name), flush=True)

        if found_location.state_id is not None:
            searched_state = get_state_by_id(found_location.state_id)

        if found_location.city_id is not None:
            searched_city = get_city_by_id(found_location.city_id)

    else:
        locations_to_lookup.append(searched_location_id)

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

        parsed_location_list = {'source__jobs': "mantiks | Glassdoor"}

        if searched_country is None:
            parsed_location_list['region_id'] = None
            parsed_location_list['region'] = None

            parsed_location_list['subregion_id'] = None
            parsed_location_list['subregion'] = None

            parsed_location_list['country_id'] = None
            parsed_location_list['country'] = None
            parsed_location_list['country_iso3'] = None
            parsed_location_list['country_iso2'] = None

        else:
            parsed_location_list['region_id'] = searched_country.region.id
            parsed_location_list['region'] = searched_country.region.name

            parsed_location_list['subregion_id'] = (
                searched_country.subregion.id)
            parsed_location_list['subregion'] = searched_country.subregion.name

            parsed_location_list['country_id'] = searched_country.id
            parsed_location_list['country'] = searched_country.name
            parsed_location_list['country_iso3'] = searched_country.iso3
            parsed_location_list['country_iso2'] = searched_country.iso2

        if searched_state is None:
            parsed_location_list['state_id'] = None
            parsed_location_list['state'] = None
            parsed_location_list['state_code'] = None

        else:
            parsed_location_list['state_id'] = searched_state.id
            parsed_location_list['state'] = searched_state.name
            parsed_location_list['state_code'] = searched_state.state_code

        if searched_city is None:
            parsed_location_list['city_id'] = None
            parsed_location_list['city'] = None

        else:
            parsed_location_list['city_id'] = searched_city.id
            parsed_location_list['city'] = searched_city.name

        found_region = None
        found_subregion = None
        found_country = None
        found_state = None
        found_city = None

        parsed_location_list['location_original'] = dict_new[i].get('location')

        # Location Example
        # Jersey City, New Jersey
        # location input JSON parameter contains Country Name
        detailed_location_list: list = [
            j.strip(" ")
            for j in detailed_location.split(',')
        ]

        # print(str(detailed_location_list), flush=True)

        if (len(detailed_location_list) != 3 and
                searched_country is None):

            search_parameters = input_json
            search_parameters = search_parameters.get('location', None)

            location_string = (
                search_parameters
                if search_parameters is not None
                else ""
            )

            if (location_string is None or
                    location_string.lower() == 'anywhere'):

                parsed_location_list['remote__jobs'] = True

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
        if (len(detailed_location_list) >= 1 and
                searched_country is not None):
            parsed_location_list['country_original'] = (
                detailed_location_list[-1])

        if (searched_state is None and
                ((len(detailed_location_list) >= 2 and
                  searched_country is not None) or
                 (len(detailed_location_list) >= 1 and
                  searched_country is None))):
            parsed_location_list['state_original'] = (
                detailed_location_list[(
                    -1 if searched_country is None else -2)])

        if (searched_city is None and
                ((len(detailed_location_list) >= 3 and
                  searched_state is None and
                  searched_country is not None) or
                 (len(detailed_location_list) >= 2 and
                  searched_country is None))):
            parsed_location_list['city_original'] = (
                detailed_location_list[(
                    -2 if searched_country is None else -3)])

        if searched_country is None:
            # print("SEARCHED COUNTRY IS NONE", flush=True)
            # print(str(searched_country), flush=True)

            if len(detailed_location_list) >= 3:
                # default to the last index for input
                found_country = find_country(detailed_location_list[-1])

            if found_country:

                if len(detailed_location_list) == 1:

                    job_locations[i] = derive_locations(
                        found_region=found_region,
                        found_subregion=found_subregion,
                        found_country=found_country,
                        found_state=found_state,
                        found_city=found_city,
                        parsed_location_list=parsed_location_list
                    )

                    continue

                # Cleanup list if found_country is equal to iso2 or iso3.
                temp_detailed_state = detailed_location_list[(
                    -1 if found_country is None else -2)]
                # print("Detailed State: " + str(temp_detailed_state),
                #       flush=True)

                if (temp_detailed_state.lower()
                        == found_country.name.lower() or
                        temp_detailed_state.lower()
                        == found_country.iso2.lower() or
                        temp_detailed_state.lower()
                        == found_country.iso3.lower()):
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
                    # print("Defaulting to remote location instead.",
                    #       flush=True)

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

            if searched_city is None:
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
                        country_id=(
                            parsed_location_list.get('country_id', -1)),
                        state_string=detailed_address_state,
                        regex_letter_code=state_regex,
                        delimited_string=[],
                    )

                    if found_state is None:
                        found_state = find_state(
                            country_id=(
                                parsed_location_list.get('country_id', -1)),
                            state_string=detailed_address_state,
                            regex_letter_code=state_regex,
                            delimited_string=delimited_state,
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

            if searched_city is None:
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
                    country_id=(
                        parsed_location_list.get('country_id', -1)),
                    state_id=(
                        parsed_location_list.get('state_id', -1)),
                    city_string=str(detailed_address_city),
                    delimited_string=[],
                )

                if found_city is None:
                    found_city = find_city(
                        country_id=(
                            parsed_location_list.get('country_id', -1)),
                        state_id=(
                            parsed_location_list.get('state_id', -1)),
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

    if len(locations_to_lookup) != 0:
        print("lookup this location ID since database does not contain data",
              flush=True)
        print(str(locations_to_lookup), flush=True)

    if len(locations_to_search) != 0:
        print("lookup this location name since there are no ID's populated.",
              flush=True)
        print(str(locations_to_search), flush=True)

    return job_locations


def mantiks_glassdoor_company_jobs(dict_new, input_json):
    """
    mantiks | Glassdoor
    Endpoint:
        Job details
    Retrieves details based on Job ID

    derive location data from City and State only.
    key name provided from input_json's job_id key.
    """
    job_locations = {}

    found_country = input_json.get('locality')

    if found_country is not None:
        found_country = find_country(found_country)

    found_subregion = found_country.subregion
    found_region = found_country.region

    # print("Preset Country: " + str(searched_country.name), flush=True)

    # print("count " + str(len(dict_new)), flush=True)
    for i in dict_new.keys():
        detailed_location = dict_new[i].get('location')

        # Location Example
        # Country is not included.
        detailed_location_list: list = [
            j.strip(" ")
            for j in detailed_location.split(',')
        ]

        # Jersey City, New Jersey
        # Emeryville, CA
        # San Francisco, CA

        # print("Detailed" + " " + str(detailed_location_list), flush=True)
        # The detailed_location_list has been reset,
        # derive the City and State values from the listing details.

        # Derive 0 as City and 1 as State (if length is 2)

        parsed_location_list = {
            'source__jobs': "mantiks | Glassdoor",
            'remote__jobs': False,
            'region_id': found_country.region.id,
            'region': found_country.region.name,
            'subregion_id': found_country.subregion.id,
            'subregion': found_country.subregion.name,
            'location_original': detailed_location,
            'country_id': found_country.id,
            'country': found_country.name,
            'country_iso3': found_country.iso3,
            'country_iso2': found_country.iso2,
            'state_id': None,
            'state': None,
            'state_code': None,
            'city_id': None,
            'city': None,
            'combined_location_original': detailed_location_list
        }

        found_state = None
        found_city = None

        # Delimit City String
        # Delimit State String
        if (detailed_location_list is None or
                len(detailed_location_list) == 0):
            parsed_location_list['remote__jobs'] = True

        else:
            detailed_address_state = (
                detailed_location_list[1]
                .replace("()", "")
                .replace("[]", "")
                .strip(" ")
            )

            # save stripped state string
            parsed_location_list['state_stripped'] = detailed_address_state

            state_regex: list = two_letter_matches_string(
                detailed_address_state
            )

            parsed_location_list['state_regex']: list = state_regex

            delimited_state: list = delimit_string(
                length_combo=2,
                input_string=detailed_address_state
            )

            parsed_location_list['state_delimited']: list = delimited_state

            detailed_address_city = fix_city_name(
                input_city=(detailed_location_list[0]
                            .replace("()", "")
                            .replace("[]", "")
                            .strip(" ")),
                input_state='',
                input_country=found_country.name
                if found_country
                else ''
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
                delimited_state_string=delimited_state
            )

            # Override country when city found
            if found_city is not None:
                found_state = found_city.state
                found_country = found_city.state.country
                found_subregion = found_city.state.country.subregion
                found_country = found_city.state.country.region

        job_locations[str(i)] = derive_locations(
                found_region=found_region,
                found_subregion=found_subregion,
                found_country=found_country,
                found_state=found_state,
                found_city=found_city,
                parsed_location_list=parsed_location_list
            )

    return job_locations


def mantiks_glassdoor_job_details(dict_new):
    """
        mantiks | Glassdoor
        Endpoint:
            Job details
        Retrieves details based on Job ID

        derive location data from City and State only.
        key name provided from input_json's job_id key.
        """
    job_locations = {}

    for i in dict_new.keys():
        # print("Preset Country: " + str(searched_country.name), flush=True)

        # print("count " + str(len(dict_new)), flush=True)

        detailed_location = dict_new[str(i)].get('location')

        # Location Example
        # Country is not included.
        detailed_location_list: list = [
            j.strip(" ")
            for j in detailed_location.split(',')
        ]
        # Jersey City, New Jersey
        # Emeryville, CA
        # San Francisco, CA

        # print("Detailed" + " " + str(detailed_location_list), flush=True)

        # The detailed_location_list has been reset,
        # derive the City and State values from the listing details.

        # Derive 0 as City and 1 as State (if length is 2)

        parsed_location_list = {
            'source__jobs': "mantiks | Glassdoor",
            'remote__jobs': False,
            'location_original': detailed_location,
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
            'combined_location_original': detailed_location_list
        }

        found_region = None
        found_subregion = None
        found_country = None
        found_state = None
        found_city = None

        # Delimit City String
        # Delimit State String
        if (detailed_location_list is None or
                len(detailed_location_list) == 0):
            parsed_location_list['remote__jobs'] = True

        elif len(detailed_location_list) == 1:
            detailed_country = detailed_location_list[0]
            found_country = find_country(detailed_country)

        elif len(detailed_location_list) > 1:
            detailed_address_state = (
                detailed_location_list[1]
                .replace("()", "")
                .replace("[]", "")
                .strip(" ")
            ) if len(detailed_location_list) > 0 else None

            # save stripped state string
            parsed_location_list['state_stripped'] = detailed_address_state

            state_regex: list = two_letter_matches_string(
                detailed_address_state
            )

            parsed_location_list['state_regex']: list = state_regex

            delimited_state: list = delimit_string(
                length_combo=2,
                input_string=detailed_address_state
            )

            parsed_location_list['state_delimited']: list = delimited_state

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
                delimited_state_string=delimited_state
            )
        job_locations[str(i)] = derive_locations(
            found_region=found_region,
            found_subregion=found_subregion,
            found_country=found_country,
            found_state=found_state,
            found_city=found_city,
            parsed_location_list=parsed_location_list
        )

    return job_locations
