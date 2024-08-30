"""
sohailglt | Linkedin Live Data
Endpoints:
Company Search
"""

from routines.parsing.find_location import (
    find_country,
    derive_locations,
    find_state,
    fix_city_name,
    two_letter_matches_string,
    delimit_string,
    find_city, three_letter_matches_string
)


def sohailglt_linkedin_live_data_company_search(dict_new):
    """
    sohailglt | Linkedin Live Data
    Endpoint: Company Search
    """
    company_locations = {}
    # print("count " + str(len(dict_new)), flush=True)
    for i in dict_new.keys():
        # print("processing key: " + str(i), flush=True)
        # print(str(dict_new[i]), flush=True)
        # print(str(dict_new[i].get('location')), flush=True)

        parsed_location_list = {
            'source__jobs': "sohailglt | Linkedin Live Data",
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
            'location_original': dict_new[i].get('location_country', None)
        }

        found_region = None
        found_subregion = None
        found_country = None
        found_state = None
        found_city = None

        if parsed_location_list['location_original'] is not None:
            found_country = find_country(
                parsed_location_list['location_original'])

        company_locations[i] = derive_locations(
            found_region=found_region,
            found_subregion=found_subregion,
            found_country=found_country,
            found_state=found_state,
            found_city=found_city,
            parsed_location_list=parsed_location_list
        )

    return company_locations


def sohailglt_linkedin_live_data_company_details(dict_new):
    """
    sohailglt | Linkedin Live Data
    Endpoint: Company Details
    """
    company_locations = {}
    # print("count " + str(len(dict_new)), flush=True)
    for main_key in dict_new.keys():
        # print("processing key: " + str(main_key), flush=True)
        # print(str(dict_new[main_key]), flush=True)
        company_locations[main_key] = {}
        locations_dict = dict_new[main_key].get('locations', None)
        for i in locations_dict.keys():
            if isinstance(locations_dict[i], list):
                company_locations[main_key][i] = []
                for k, m in enumerate(locations_dict[i]):
                    # print(str(dict_new[i].get('location')), flush=True)

                    parsed_location_list = {
                        'source__jobs': "sohailglt | Linkedin Live Data",
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

                    parsed_location_list['country_original']: str = (
                        m.get('country', None))

                    if parsed_location_list['country_original'] is not None:
                        parsed_location_list['country_stripped'] = (
                            parsed_location_list['country_original']
                            .replace("()", "")
                            .replace("[]", "")
                            .strip(" ")
                        )

                    parsed_location_list['state_original'] = (
                        m.get('geographic_area', None))

                    if parsed_location_list['state_original'] is not None:
                        parsed_location_list['state_stripped'] = (
                            parsed_location_list['state_original']
                            .replace("()", "")
                            .replace("[]", "")
                            .strip(" ")
                        )

                        parsed_location_list['state_regex']: list = (
                            two_letter_matches_string(
                                parsed_location_list['state_stripped']) + 
                            three_letter_matches_string(
                                parsed_location_list['state_stripped'])
                        )

                        parsed_location_list[
                            'state_delimited']: list = delimit_string(
                            input_string=parsed_location_list['state_stripped']
                        )

                    parsed_location_list['city_original'] = fix_city_name(
                        input_city=m.get('city', ''),
                        input_state=parsed_location_list.get(
                            'state_stripped',
                            ''),
                        input_country=parsed_location_list.get(
                            'country_stripped', ''),
                    )

                    if parsed_location_list['city_original'] is not None:
                        parsed_location_list['city_stripped'] = (
                            parsed_location_list['city_original']
                            .replace("()", "")
                            .replace("[]", "")
                            .strip(" ")
                        )

                        parsed_location_list[
                            'city_delimited']: list = delimit_string(
                            input_string=parsed_location_list['city_stripped']
                        )

                    if parsed_location_list['country_original'] is not None:
                        found_country = find_country(
                            parsed_location_list['country_original'])

                    if parsed_location_list['state_original'] is not None:
                        found_state = find_state(
                            country_id=(
                                found_country.id
                                if found_country else -1),
                            state_string=(
                                parsed_location_list['state_stripped']),
                            regex_letter_code=parsed_location_list[
                                'state_regex'],
                            delimited_string=[]
                        )

                        if found_state is None:
                            found_state = find_state(
                                country_id=(
                                    found_country.id
                                    if found_country else -1),
                                state_string=(
                                    parsed_location_list['state_stripped']),
                                regex_letter_code=parsed_location_list[
                                    'state_regex'],
                                delimited_string=parsed_location_list[
                                    'state_delimited']
                            )

                    if parsed_location_list['city_original'] is not None:
                        found_city = find_city(
                            country_id=found_country.id if found_country else
                            -1,
                            state_id=found_state.id if found_state else -1,
                            city_string=parsed_location_list['city_stripped'],
                            delimited_string=[]
                        )

                        if found_city is None:
                            found_city = find_city(
                                country_id=found_country.id
                                if found_country
                                else -1,
                                state_id=found_state.id if found_state else -1,
                                city_string=(
                                    parsed_location_list['city_stripped']),
                                delimited_string=parsed_location_list[
                                    'city_delimited']
                            )

                    company_locations[main_key][i].append(derive_locations(
                        found_region=found_region,
                        found_subregion=found_subregion,
                        found_country=found_country,
                        found_state=found_state,
                        found_city=found_city,
                        parsed_location_list=parsed_location_list
                    ))
            else:
                # print(str(dict_new[i].get('location')), flush=True)

                parsed_location_list = {
                    'source__jobs': "sohailglt | Linkedin Live Data",
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
                    'location_original': (
                        locations_dict[i].get('location_country', None)
                    )
                }

                found_region = None
                found_subregion = None
                found_country = None
                found_state = None
                found_city = None

                parsed_location_list['country_original']: str = (
                    locations_dict[i].get('country', None))

                if parsed_location_list['country_original'] is not None:
                    parsed_location_list['country_stripped'] = (
                        parsed_location_list['country_original']
                        .replace("()", "")
                        .replace("[]", "")
                        .strip(" ")
                    )

                parsed_location_list['state_original'] = (
                    locations_dict[i].get('geographic_area', None))

                if parsed_location_list['state_original'] is not None:
                    parsed_location_list['state_stripped'] = (
                        parsed_location_list['state_original']
                        .replace("()", "")
                        .replace("[]", "")
                        .strip(" ")
                    )

                    parsed_location_list['state_regex']: list = (
                        two_letter_matches_string(
                            parsed_location_list['state_stripped']) + 
                        three_letter_matches_string(
                            parsed_location_list['state_stripped'])
                    )

                    parsed_location_list[
                        'state_delimited']: list = delimit_string(
                        input_string=parsed_location_list['state_stripped']
                    )

                parsed_location_list['city_original']: str = fix_city_name(
                    input_city=locations_dict[i].get('city', ''),
                    input_state=parsed_location_list.get('state_stripped', ''),
                    input_country=parsed_location_list.get(
                        'country_stripped', ''),
                )

                if parsed_location_list['city_original'] is not None:
                    parsed_location_list['city_stripped'] = (
                        parsed_location_list['city_original']
                        .replace("()", "")
                        .replace("[]", "")
                        .strip(" ")
                    )

                    parsed_location_list[
                        'city_delimited']: list = delimit_string(
                        input_string=parsed_location_list['city_stripped']
                    )

                if parsed_location_list['country_original'] is not None:
                    found_country = find_country(
                        parsed_location_list['country_original'])

                if parsed_location_list['state_original'] is not None:
                    found_state = find_state(
                        country_id=found_country.id if found_country else -1,
                        state_string=parsed_location_list['state_stripped'],
                        regex_letter_code=parsed_location_list['state_regex'],
                        delimited_string=[]
                    )
                    if found_state is None:
                        found_state = find_state(
                            country_id=(
                                found_country.id if found_country else -1),
                            state_string=(
                                parsed_location_list['state_stripped']),
                            regex_letter_code=(
                                parsed_location_list['state_regex']),
                            delimited_string=(
                                parsed_location_list['state_delimited'])
                        )

                if parsed_location_list['city_original'] is not None:
                    found_city = find_city(
                        country_id=found_country.id if found_country else -1,
                        state_id=found_state.id if found_state else -1,
                        city_string=parsed_location_list['city_stripped'],
                        delimited_string=[]
                    )
                    if found_city is None:
                        found_city = find_city(
                            country_id=(
                                found_country.id if found_country else -1),
                            state_id=found_state.id if found_state else -1,
                            city_string=parsed_location_list['city_stripped'],
                            delimited_string=(
                                parsed_location_list['city_delimited'])
                        )

                company_locations[main_key][i] = derive_locations(
                    found_region=found_region,
                    found_subregion=found_subregion,
                    found_country=found_country,
                    found_state=found_state,
                    found_city=found_city,
                    parsed_location_list=parsed_location_list
                )

    return company_locations
