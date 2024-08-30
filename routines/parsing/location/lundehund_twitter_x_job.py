"""
Lundehund | Twitter X Job API
Endpoints:
Search Job
Get Job Detail

"""
from routines.parsing.location.misc.country_abbreviations import (
    country_abbreviations
)

from routines.parsing.find_location import (
    find_x_location_id,
    get_region_by_id,
    get_subregion_by_id,
    get_city_by_id,
    get_state_by_id,
    get_country_by_id,
    derive_locations
)


def lundehund_twitter_x_job_search_location(dict_new: dict):
    """
    Lundehund | Twitter X Job API
    Updates search location dictionary into a proper format to save
    """
    locations = dict_new.get('location_type_ahead', {})
    parsed_location_list = {}

    for i in locations:
        parsed_location_list[str(i.get('location_id'))] = (
            i.get("display_name"))

    return parsed_location_list


def lundehund_twitter_x_job_search_job(dict_new, input_json):
    """
    Lundehund | Twitter X Job API
    Endpoint
        Search Job
    Assume Job location is shown
    """
    location_id = input_json.get('location_id', None)
    if (location_id is None or
            len(str(location_id)) == 0):
        # print("Error: Cannot parse location data because "
        #       "location_id is not a parameter.", flush=True)
        return {"Error": "Cannot parse location data because "
                         "location_id is not a parameter."}

    location_id = int(location_id)
    location = find_x_location_id(location_id)

    found_region = None
    found_subregion = None
    found_country = None
    found_state = None
    found_city = None

    if location is not None:
        if location.region_id is not None:
            found_region = get_region_by_id(location.region_id)

        if location.subregion_id is not None:
            found_region = get_subregion_by_id(location.subregion_id)

        if location.country_id is not None:
            found_country = get_country_by_id(location.country_id)

        if location.state_id is not None:
            found_state = get_state_by_id(location.state_id)

        if location.city_id is not None:
            found_city = get_city_by_id(location.city_id)

    job_locations = {}
    # print("count " + str(len(dict_new)), flush=True)
    for i in dict_new.keys():
        # print("processing key: " + str(i), flush=True)
        detailed_location = dict_new[i].get('location', None)
        # Most likely a status message string
        if detailed_location is None:
            continue

        # print(str(dict_new[i]), flush=True)
        # print(str(dict_new[i].get('jobGeo')), flush=True)

        parsed_location_list = {
            'source__jobs': "Lundehund | Twitter X Job API",
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
            'location_original': dict_new[i].get('location', None)
        }

        # Location Example
        # United States, CA, San Francisco
        # Sunnyvale, CA
        # Las Vegas, NV
        # Seattle, WA
        # Menlo Park, CA
        # México D.F., CDMX, MX
        # Seattle, WA
        # Remote - Estonia
        # San Mateo, CA, USA
        # San Diego / Remote
        # Laurel, MD, United States
        # Bengaluru, KA, IN
        # Istanbul, Turkiye - Remote
        # Remote - India
        # San Jose, CA, US
        # Chennai, TN, IN
        # San Francisco, CA | New York City, NY | Seattle, WA
        # Remote - Armenia
        # Europe & US East Coast
        # Hursley, England, United Kingdom
        # AMER, EMEA
        # Atlanta, GA, us
        abbreviated_countries = ""

        for j in parsed_location_list['location_original'].split(","):
            j = j.strip(" ")

            if j in country_abbreviations.keys():
                for k in country_abbreviations.keys():
                    if j == k:
                        j = country_abbreviations[k]

            abbreviated_countries += j + ","

        if abbreviated_countries[-1] == ",":
            abbreviated_countries = abbreviated_countries[:-1]

        parsed_location_list['location_abbreviated'] = abbreviated_countries

        job_locations[i] = derive_locations(
            found_region=found_region,
            found_subregion=found_subregion,
            found_country=found_country,
            found_state=found_state,
            found_city=found_city,
            parsed_location_list=parsed_location_list
        )
    return job_locations
