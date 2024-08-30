"""
letscrape | Real-Time Glassdoor Data
Endpoints:
Company Search
"""
from routines.parsing.find_location import (
    find_city,
    derive_locations,
    delimit_string,
)


def letscrape_real_time_glassdoor_data(dict_new):
    """
    letscrape | Real-Time Glassdoor Data
    Endpoints:
    Company Search

    Headquarters Location
    Location string needs more refinement

    "Wayne, PA"
    "Denver, CO" (State letters)
    """
    company_locations = {}
    # print("count " + str(len(dict_new)), flush=True)
    for i in dict_new.keys():
        # print("processing key: " + str(i), flush=True)
        detailed_location = dict_new[i].get('headquarters_location', None)
        # Most likely a status message string
        if detailed_location is None:
            continue
        # print(str(dict_new[i]), flush=True)
        # print(str(dict_new[i].get('location')), flush=True)

        parsed_location_list = {
            'source__jobs': "letscrape | Real-Time Glassdoor Data",
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
            'location_original': dict_new[i].get('headquarters_location', None)
        }

        found_region = None
        found_subregion = None
        found_country = None
        found_state = None
        found_city = None

        detailed_location_list: list = [
            j.strip(" ")
            for j in detailed_location.split(',')
        ]
        # print(str(detailed_location_list), flush=True)

        parsed_location_list['combined_location_original']: list = (
            detailed_location_list
        )
        # The detailed_location_list has been reset,
        # derive the City and State values from the listing details.

        while len(detailed_location_list) != 0:
            # Check for country
            if found_city is None:
                found_city = find_city(
                    country_id=-1,
                    state_id=-1,
                    city_string=detailed_location_list[-1],
                    delimited_string=[],
                )

                if found_city is None:
                    found_city = find_city(
                        country_id=-1,
                        state_id=-1,
                        city_string=detailed_location_list[-1],
                        delimited_string=delimit_string(
                            input_string=detailed_location_list[-1]
                        ),
                    )

                if found_state is None:
                    found_city = find_city(
                        country_id=-1,
                        state_id=-1,
                        city_string=detailed_location_list[-1],
                        delimited_string=[],
                    )

                    if found_city is None:
                        found_city = find_city(
                            country_id=-1,
                            state_id=-1,
                            city_string=detailed_location_list[-1],
                            delimited_string=delimit_string(
                                input_string=detailed_location_list[-1]
                            ),
                        )

            detailed_location_list.pop()

        # save originals
        company_locations[i] = derive_locations(
            found_region=found_region,
            found_subregion=found_subregion,
            found_country=found_country,
            found_state=found_state,
            found_city=found_city,
            parsed_location_list=parsed_location_list
        )

    return company_locations
