"""
APIJobs | Job Searching API
APIJobs.dev | API Jobs
SearchJobs
"""
import re

from routines.parsing.find_location import (
    find_state,
    find_city,
    find_country,
    derive_locations,
    fix_city_name,
    delimit_string,
    two_letter_matches_string,
    find_city_and_state,
    find_city_contains, three_letter_matches_string
)


def api_jobs_search_jobs(dict_new: dict):
    """
    vuesdata | Indeed Jobs API
    """
    job_locations = {}
    # print("count " + str(len(dict_new)), flush=True)
    for i in dict_new.keys():
        # print("processing key: " + str(i), flush=True)
        detailed_location = ['', '', '']

        remote_jobs_test = False

        detailed_location[2] = dict_new[i].get(
            'locationAddressCountry',
            dict_new[i].get('country', '')
        )
        if (detailed_location[2] is not None and
                isinstance(detailed_location[2], str) and
                detailed_location[2] != ''):
            count = 0
            for j in detailed_location[2]:
                if ',' == j:
                    count += 1
            if count > 1:
                detailed_location[0] = detailed_location[2]
                detailed_location[1] = ''
                detailed_location[2] = ''

        detailed_location[1] = dict_new[i].get(
            'region',
            dict_new[i].get('locationAddressRegion', '')
        )

        if (detailed_location[1] is not None and
                isinstance(detailed_location[1], str) and
                detailed_location[1] != ''):
            count = 0
            for j in detailed_location[1]:
                if ',' == j:
                    count += 1
            if count > 1:
                detailed_location[0] = detailed_location[1]
                detailed_location[1] = ''
                detailed_location[2] = ''

        detailed_location[0] = dict_new[i].get(
            'locationAddressLocality',
            dict_new[i].get('city', '')
        )

        for j in detailed_location:
            if (j is not None and
                    isinstance(j, str) and
                    j != '' and
                    'remote' in j.lower()):
                remote_jobs_test = True

        if (dict_new.get('title') is not None and
                'remote' in dict_new.get('title')):
            remote_jobs_test = True

        # print(str(dict_new[i]), flush=True)
        # print(str(dict_new[i].get('job_location')), flush=True)

        parsed_location_list = {
            'source__jobs': "APIJobs | Job Searching API",
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
            'location_original': detailed_location
        }

        found_region = None
        found_subregion = None
        found_country = None
        found_state = None
        found_city = None

        if (detailed_location[1] == '' and
                detailed_location[2] == '' and
                ',' in detailed_location[0]):
            new_location = detailed_location[0].strip().split(',')
            while len(new_location) < 3:
                new_location = [''] + new_location

            detailed_location = new_location

        if detailed_location[2] != '':
            found_country = find_country(detailed_location[2])

        if detailed_location[1] != '':
            found_state = find_state(
                country_id=found_country.id
                if found_country is not None else -1,
                state_string=detailed_location[1],
                regex_letter_code=(
                        two_letter_matches_string(detailed_location[1]) +
                        three_letter_matches_string(detailed_location[1])
                ),
                delimited_string=delimit_string(
                    input_string=detailed_location[1]
                ),
            )

        if detailed_location[0] != '':
            found_city = find_city(
                country_id=found_country.id
                if found_country is not None else -1,
                state_id=found_state.id
                if found_state is not None else -1,
                city_string=detailed_location[0],
                delimited_string=delimit_string(
                    input_string=detailed_location[0]
                ),
            )
            # Try without state match
            if found_city is None:
                found_city = find_city(
                    country_id=found_country.id
                    if found_country is not None else -1,
                    state_id=-1,
                    city_string=detailed_location[0],
                    delimited_string=delimit_string(
                        input_string=detailed_location[0]
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
