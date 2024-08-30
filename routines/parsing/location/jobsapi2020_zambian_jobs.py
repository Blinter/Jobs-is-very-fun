"""
JobsAPI2020 | Zambian Jobs API
Endpoint
httpsJobapiCoUkGet
"""
from routines.parsing.find_location import (
    find_state,
    find_city,
    find_country,
    derive_locations
)


def jobs_2020_zambian_jobs_https_job_co_uk_get(dict_new):
    """
    JobsAPI2020 | Zambian Jobs API
    """
    job_locations = {}
    # print("count " + str(len(dict_new)), flush=True)
    for i in dict_new.keys():
        parsed_location_list = {
            'source__jobs': "JobsAPI2020 | Zambian Jobs API",
            'locations_original': dict_new[i].get('location'),
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
        found_country = find_country("zambia")
        found_state = None
        found_city = None

        if found_country:
            found_subregion = found_country.subregion
            found_region = found_country.region

        parsed_location_list['cities'] = {}

        parsed_location_list['states'] = {}

        locations_list: list = [
            j.lower().replace("zambia", "").strip(" ")
            for j in dict_new[i].get('location').split(",")
            if j.lower() != "zambia"
        ]

        locations_list: list = [
            j for j in locations_list
            if j is not None and j != ''
        ]

        parsed_location_list['locations_original']: list = locations_list
        # print(str(locations_list), flush=True)

        # Add substrings when matching city from the longest combination to
        # shortest

        delimited_location_string = []

        # Split spaces into delimited location lists
        for k in locations_list:
            current_location = k.split(" ")

            if len(current_location) > 1:
                temp_delimited_location_string = []

                for j in range(1, len(current_location) + 1):
                    string_to_append = ' '.join(current_location[0:j])

                    if string_to_append not in current_location:
                        temp_delimited_location_string.append(string_to_append)

                # Keep original city and insert it in the beginning later.
                temp_delimited_location_string = current_location.pop(0)

                # redeclare and manually add shortest combinations first to the
                # delimited array because of Type errors when appending or
                # extending.
                for j in temp_delimited_location_string:
                    if j not in delimited_location_string:
                        delimited_location_string = [j] + current_location

                # Add back the original city to the beginning, with the
                # longest combinations following it.
                delimited_location_string: list = (
                        [temp_delimited_location_string] + current_location)

        temp_delimited_location_string: list = [
            j for j in delimited_location_string
            if (j != '[]' and
                j != '()')
        ]

        parsed_location_list['delimited_locations']: list = (
            temp_delimited_location_string)

        for j in temp_delimited_location_string:
            # print('Searching ' + str(j), flush=True)
            found_city = find_city(
                country_id=found_country.id if found_country else -1,
                state_id=-1,
                city_string=j,
                delimited_string=[]
            )

            if found_city is None:
                found_city = find_city(
                    country_id=found_country.id if found_country else -1,
                    state_id=-1,
                    city_string=j,
                    delimited_string=[j]
                )

            if (found_city is not None and
                    str(found_city.id) not in
                    parsed_location_list['cities'].keys()):
                parsed_location_list['cities'][str(found_city.id)] = (
                    {
                            'name': found_city.name,
                    })

                if (str(found_city.state.id) not in
                        parsed_location_list['states'].keys()):
                    parsed_location_list['states'][str(found_city.state.id)] = (
                        {
                            'name': found_city.state.name,
                            'state_code': found_city.state.state_code,
                        })

            else:
                found_state = find_state(
                    country_id=found_country.id if found_country else -1,
                    state_string=j,
                    regex_letter_code=[],
                    delimited_string=[]
                )

                if found_state is None:
                    found_state = find_state(
                        country_id=found_country.id if found_country else -1,
                        state_string=j,
                        regex_letter_code=[],
                        delimited_string=[j]
                    )

                if (found_state is not None and
                        str(found_state.id) not in
                        parsed_location_list['states'].keys()):
                    parsed_location_list['states'][str(found_state.id)] = (
                        {
                            'name': found_state.name,
                            'state_code': found_state.state_code,
                        })

        job_locations[i] = derive_locations(
            found_region=found_region,
            found_subregion=found_subregion,
            found_country=found_country,
            found_state=found_state,
            found_city=found_city,
            parsed_location_list=parsed_location_list
        )

    return job_locations
