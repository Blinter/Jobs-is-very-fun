"""
letscrape | JSearch
Endpoint
Search

Note: latitude/longitude search is accurate but slow.
"""
from routines.parsing.find_location import (
    find_city_by_coordinates,
    derive_locations, find_city_by_coordinates_fast
)


def letscrape_jsearch(dict_new, input_json):
    """
    letscrape | JSearch
    Endpoint
    Search

    Note: latitude/longitude search is accurate but slow.
    """
    job_locations = {}

    # print("count " + str(len(dict_new)), flush=True)
    for i in dict_new.keys():
        # print("processing key: " + str(i), flush=True)

        parsed_location_list = {
            'source__jobs': "letscrape | JSearch",
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
            'latitude_original': dict_new[i].get('job_latitude', None),
            'longitude_original': dict_new[i].get('job_longitude', None),
            'location_input_original': input_json.get('location', None),
            'remote__jobs': dict_new[i].get('job_is_remote', "False") == "True",
            'latitude': dict_new[i].get('job_latitude', None),
            'longitude': dict_new[i].get('job_longitude', None)
        }

        if (parsed_location_list['latitude'] is None or
                parsed_location_list['longitude'] is None):
            parsed_location_list['remote__jobs'] = True
            continue

        latitude = float(parsed_location_list['latitude'])
        longitude = float(parsed_location_list['longitude'])

        if not (isinstance(latitude, float) or
                isinstance(longitude, float)):
            parsed_location_list['remote__jobs'] = True
            continue

        found_city = find_city_by_coordinates_fast(
            find_latitude=latitude,
            find_longitude=longitude,
        )

        # found_city = find_city_by_coordinates(
        #     find_latitude=latitude,
        #     find_longitude=longitude,
        # )

        job_locations[i] = derive_locations(
            found_city=found_city,
            parsed_location_list=parsed_location_list
        )

    return job_locations


"""
158s execution time
                found_country = get_country_by_id(found_city.country_id)
                if found_country:

                    parsed_location_list['country_id'] = (
                        # found_state.country.id)
                        found_country.id)
                    parsed_location_list['country_iso3'] = (
                        # found_state.country.iso3)
                        found_country.iso3)
                    parsed_location_list['country_iso2'] = (
                        # found_state.country.iso2)
                        found_country.iso2)
                    parsed_location_list['country'] = (
                        # found_state.country.name)
                        found_country.name)

                    found_subregion = get_subregion_by_id(
                        found_country.subregion_id)

                    if found_subregion:
                        parsed_location_list['subregion_id'] = (
                            # found_state.country.subregion_id)
                            found_subregion.id)
                        parsed_location_list['subregion'] = (
                            # found_state.country.name)
                            found_subregion.name)

                        found_region = get_region_by_id(found_country.region_id)

                        if found_region:
                            parsed_location_list['region_id'] = (
                                # found_state.country.region_id)
                                found_region.id)
                            parsed_location_list['region'] = (
                                # found_state.country.name)
                                found_region.name)
"""
