"""
jobicy | Remote Jobs API
Endpoints:
Remote Jobs API
"""
from routines.parsing.location.misc.country_abbreviations import (
    country_abbreviations
)
from routines.parsing.find_location import find_country


def jobicy_remote_jobs_remote_jobs(dict_new, input_json):
    """
    jobicy | Remote Jobs API
    """
    job_locations = {}
    # print("count " + str(len(dict_new)), flush=True)
    for i in dict_new.keys():
        # print("processing key: " + str(i), flush=True)
        detailed_location = dict_new[i].get('jobGeo')
        # Most likely a status message string

        if detailed_location is None:
            continue
        # print(str(dict_new[i]), flush=True)
        # print(str(dict_new[i].get('jobGeo')), flush=True)

        parsed_location_list = {
            'source__jobs': "jobicy | Remote Jobs API",
            'remote__jobs': False,
            'location_original': dict_new[i].get('jobGeo', None),
            'location_country_geo_slug_input': input_json.get('geo', None),
            'regions': {},
            'subregions': {},
            'countries': {}
        }

        # check if job location is listed as remote
        if ((parsed_location_list.get('location_original') is not None and
             parsed_location_list.get('location_original').lower()
             == 'anywhere' or
             parsed_location_list.get('location_original').lower()
             == 'None') or
                (dict_new[i].get('is_remote', None) is not None and
                 dict_new[i].get('is_remote', None))):
            parsed_location_list['remote__jobs'] = True

        # Location Example
        # jobGeo: "Anywhere"
        # jobGeo: "LATAM"
        # jobGeo: APAC, EMEA, Canada, USA
        # jobGeo: Canada,
        # Convert LATAM to Latin America Countries
        # Convert APAC to Asia Pacific
        abbreviated_countries = ""
        for j in parsed_location_list['location_original'].split(","):
            j = j.strip(" ")
            if j in country_abbreviations.keys():
                for k in country_abbreviations.keys():
                    if j == k:
                        j = country_abbreviations[k]

            abbreviated_countries += j + ", "

        parsed_location_list['location_original'] = abbreviated_countries

        for j in parsed_location_list['location_original'].split(","):
            found_country = find_country(str(j.strip(" ")))

            if found_country:
                if (str(found_country.id) not
                        in parsed_location_list['countries'].keys()):
                    parsed_location_list['countries'][str(found_country.id)] = (
                        {
                            "name": found_country.name,
                            "iso3": found_country.iso3,
                            "iso2": found_country.iso2,
                        }
                    )

                if (str(found_country.subregion.id) not
                        in parsed_location_list['subregions'].keys()):
                    parsed_location_list['subregions'][
                        str(found_country.id)] = (
                        {"name": found_country.subregion.name}
                    )

                if (str(found_country.region.id) not
                        in parsed_location_list['regions'].keys()):
                    parsed_location_list['regions'][str(
                        found_country.region.id)] = (
                        {"name": found_country.region.name}
                    )

        job_locations[i] = parsed_location_list

    return job_locations


jobicy_geo_slug_list = {
    "446": {
        "geoSlug": "apac",
        "geoName": "APAC"
    },
    "449": {
        "geoSlug": "emea",
        "geoName": "EMEA"
    },
    "572": {
        "geoSlug": "latam",
        "geoName": "LATAM"
    },
    "3804": {
        "geoSlug": "argentina",
        "geoName": "Argentina"
    },
    "447": {
        "geoSlug": "australia",
        "geoName": "Australia"
    },
    "3827": {
        "geoSlug": "austria",
        "geoName": "Austria"
    },
    "3819": {
        "geoSlug": "belgium",
        "geoName": "Belgium"
    },
    "1664": {
        "geoSlug": "brazil",
        "geoName": "Brazil"
    },
    "3815": {
        "geoSlug": "bulgaria",
        "geoName": "Bulgaria"
    },
    "448": {
        "geoSlug": "canada",
        "geoName": "Canada"
    },
    "3826": {
        "geoSlug": "china",
        "geoName": "China"
    },
    "3820": {
        "geoSlug": "costa-rica",
        "geoName": "Costa Rica"
                   ""},
    "3823": {
        "geoSlug": "croatia",
        "geoName": "Croatia"
    },
    "3821": {
        "geoSlug": "cyprus",
        "geoName": "Cyprus"
    },
    "3824": {
        "geoSlug": "czechia",
        "geoName": "Czechia"
    },
    "3833": {
        "geoSlug": "denmark",
        "geoName": "Denmark"
    },
    "3831": {
        "geoSlug": "estonia",
        "geoName": "Estonia"
    },
    "450": {
        "geoSlug": "europe",
        "geoName": "Europe"
    },
    "3810": {
        "geoSlug": "finland",
        "geoName": "Finland"
    },
    "1663": {
        "geoSlug": "france",
        "geoName": "France"
    },
    "1378": {
        "geoSlug": "germany",
        "geoName": "Germany"
    },
    "3808": {
        "geoSlug": "greece",
        "geoName": "Greece"
    },
    "3809": {
        "geoSlug": "hungary",
        "geoName": "Hungary"
    },
    "3811": {
        "geoSlug": "ireland",
        "geoName": "Ireland"
    },
    "3822": {
        "geoSlug": "israel",
        "geoName": "Israel"
    },
    "3719": {
        "geoSlug": "italy",
        "geoName": "Italy"
    },
    "3828": {
        "geoSlug": "japan",
        "geoName": "Japan"
    },
    "3829": {
        "geoSlug": "latvia",
        "geoName": "Latvia"
    },
    "3813": {
        "geoSlug": "lithuania",
        "geoName": "Lithuania"
    },
    "3718": {
        "geoSlug": "mexico",
        "geoName": "Mexico"
    },
    "3690": {
        "geoSlug": "netherlands",
        "geoName": "Netherlands"
    },
    "3817": {
        "geoSlug": "new-zealand",
        "geoName": "New Zealand"
                   ""},
    "3818": {
        "geoSlug": "norway",
        "geoName": "Norway"
    },
    "3835": {
        "geoSlug": "philippines",
        "geoName": "Philippines"
    },
    "3803": {
        "geoSlug": "poland",
        "geoName": "Poland"
    },
    "3802": {
        "geoSlug": "portugal",
        "geoName": "Portugal"
    },
    "3801": {
        "geoSlug": "romania",
        "geoName": "Romania"
    },
    "3806": {
        "geoSlug": "singapore",
        "geoName": "Singapore"
    },
    "3812": {
        "geoSlug": "slovakia",
        "geoName": "Slovakia"
    },
    "3830": {
        "geoSlug": "slovenia",
        "geoName": "Slovenia"
    },
    "3825": {
        "geoSlug": "south-korea",
        "geoName": "South Korea"
    },
    "671": {
        "geoSlug": "spain",
        "geoName": "Spain"
    },
    "3805": {
        "geoSlug": "sweden",
        "geoName": "Sweden"
    },
    "3816": {
        "geoSlug": "switzerland",
        "geoName": "Switzerland"
    },
    "3807": {
        "geoSlug": "thailand",
        "geoName": "Thailand"
    },
    "3799": {
        "geoSlug": "turkiye",
        "geoName": "Tu00fc rkiye"
    },
    "444": {
        "geoSlug": "uk",
        "geoName": "UK"
    },
    "3800": {
        "geoSlug": "united-arab-emirates",
        "geoName": "United Arab Emirates"
    },
    "445": {
        "geoSlug": "usa",
        "geoName": "USA"
    },
    "3814": {
        "geoSlug": "vietnam",
        "geoName": "Vietnam"
    }
}
