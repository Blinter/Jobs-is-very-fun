"""
Fantastic Jobs | Active Jobs DB
"""
import json
from routines.parsing.find_location import (
    find_state,
    find_city,
    find_country,
    derive_locations,
    fix_city_name,
    delimit_string,
    two_letter_matches_string, three_letter_matches_string
)


def escape_double_quotes(json_string):
    return json_string.replace('"', '\\"').replace('\\\\"', '\\"')
    # Ensure already escaped quotes are not double-escaped


def fantastic_jobs_active_jobs_db_get_jobs_text(dict_new):
    """
    Fantastic Jobs | Active Jobs DB
    Requires more address parsing

    Cases:
        460561137
        address_original
            @type	"PostalAddress"
            addressCountry	"United States of America"
            addressLocality	"PA - Philadelphia, 1800 Arch St"
    ---
        460929163
            address_original
                @type	"PostalAddress"
                addressCountry	"United States of America"
                addressLocality	"New Jersey Office - 210 Hudson Street"
        461097352
            address_original
                @type	"PostalAddress"
                addressCountry	null
                addressLocality	"San Diego, California, United States"
                addressRegion	"CA"
                postalCode	null
        461607740
        address_original
            @type	"PostalAddress"
            addressCountry	"United States of America"
            addressLocality	"Austin IT Innovation Center North - Austin IT
                Innovation Center North"
    """
    job_locations = {}
    for i in dict_new.keys():
        detailed_location = dict_new[i].get('locations_raw', None)

        if not isinstance(detailed_location, dict):
            # print('locations_raw is not a dict', flush=True)
            if len(detailed_location) == 0:
                # print('locations_raw length is 0', flush=True)
                continue

            try:
                detailed_location = (
                    detailed_location
                    .replace(": None,", ": null,")
                    .replace(": None", ": null")
                    .replace("'", '"')
                    # hard fix
                    .replace('''O"fallon''', "O'fallon")
                    .replace('''O"Fallon''', "O'Fallon")
                    .replace('''Mary"s''', "Mary's")
                    # hard fix
                    .replace('''""Field""''', '''"Field"''')
                    # hard fix
                    .replace('''Land O" Lakes''', '''Land O' Lakes''')
                    .replace('''River"s Edge''', '''River's Edge''')
                    .replace('''Peter"s Lane''', '''Peter's Lane''')
                    .replace('''Nicoletta"s''', '''Nicoletta's''')
                    .replace('''Joseph"s Candler Drive''',
                             '''Joseph's Candler Drive''')
                )

                detailed_location = json.loads(detailed_location)[0]
                # print("corrected locations_raw as " + str(detailed_location),
                #       flush=True)
            # except json.decoder.JSONDecodeError as e:
            except json.decoder.JSONDecodeError:
                # print("error decoding (" + str(e) + ")", flush=True)
                # print(str(len(detailed_location)), flush=True)
                # print("Attempting fix", flush=True)
                str_ending = detailed_location.rfind("}}]")
                str_beginning_find = '''"addressLocality": "'''
                str_beginning = detailed_location.find(str_beginning_find)

                if str_beginning != 1 and str_ending != -1:
                    fix_str = detailed_location[
                     str_beginning + len(str_beginning_find): str_ending-1]
                    # print("fix_str " + str(fix_str), flush=True)

                    # Fix quotes within string
                    fix_str = (escape_double_quotes(fix_str)
                               .replace('\\"@', '"@')
                               .replace('@\\"', '@"')
                               .replace('\\"}', '"}')
                               .replace('{\\"', '{"'))
                    # print("fix_str escaped " + str(fix_str), flush=True)

                    # Add string without ending quote
                    detailed_location = (
                            detailed_location[:(str_beginning +
                                                len(str_beginning_find))] +
                            fix_str +
                            detailed_location[str_ending-1:]
                    )

                # print("--" + str(detailed_location) + "--", flush=True)
                # print("Str: " + str(isinstance(detailed_location, str)),
                #       flush=True)
                # print("List: " + str(isinstance(detailed_location, list)),
                #       flush=True)
                # print("Dict: " + str(isinstance(detailed_location, dict)),
                #       flush=True)
                # print("Attempting again", flush=True)
                try:
                    detailed_location = json.loads(detailed_location)[0]

                except Exception as e:
                    print("Attempt to fix failed - " +
                          str(detailed_location), flush=True)
                    print(str(e), flush=True)
                    raise e

            except Exception as e:
                print("Other Error", flush=True)
                print(str(e), flush=True)
                raise e

            # print("Processed List: ", flush=True)
            # print(detailed_location, flush=True)
        parsed_location_list = {
            'source__jobs': "APIJobs | Job Searching API",
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
            'address_original': None,
            'country_original': None,
            'locality_original': None
        }

        found_region = None
        found_subregion = None
        found_country = None
        found_state = None
        found_city = None

        detailed_location_type = detailed_location.get('@type')

        if (detailed_location_type and
                detailed_location_type == 'Place'):
            detailed_address = detailed_location.get('address', {})

            parsed_location_list['address_original'] = (
                detailed_location.get('address'))

            if not isinstance(detailed_address, dict):
                # print('detailed_address is not a dict', flush=True)
                break

            detailed_address_country = None

            detailed_address_type = detailed_address.get('@type')

            if detailed_address_type == "PostalAddress":
                detailed_address_country = detailed_address.get(
                    'addressCountry')

            if (detailed_address_country != "" and
                    detailed_address_country is not None and
                    isinstance(detailed_address_country, str)):
                parsed_location_list['country_original'] = (
                    detailed_address.get('addressCountry'))

                if isinstance(detailed_address_country, dict):
                    print(str(detailed_address_country) +
                          " instead of string", flush=True)
                    continue

                found_country = find_country(str(detailed_address_country))

                if found_country:
                    found_subregion = found_country.subregion
                    found_region = found_country.region

                    detailed_address_locality = detailed_address.get(
                        'addressLocality', "")

                    if (detailed_address_locality != "" and
                            detailed_address_locality is not None):
                        parsed_location_list['locality_original'] = (
                            detailed_address.get('addressLocality', "")
                        )

                        detailed_address_locality = (
                            detailed_address_locality
                            .replace(found_country.name, "")

                            .replace(" " + found_country.name, "")
                            .replace(found_country.iso3 + " ", "")

                            .replace(" " + found_country.iso2, "")
                            .replace(found_country.iso2 + " ", "")

                            .replace("()", "")
                            .replace("[]", "")
                            .strip(" ")
                        )

                    detailed_address_region = detailed_address.get(
                        'addressRegion', ""
                    )

                    if (detailed_address_region != "" and
                            detailed_address_region) is not None:

                        parsed_location_list['region_original'] = (
                            detailed_address.get('addressRegion', "")
                        )

                        detailed_address_region = (
                            detailed_address_region
                            .replace(found_country.name, "")
                            .replace(found_country.iso3, "")
                            .replace(found_country.iso2, "")
                            .replace("()", "")
                            .replace("[]", "")
                            .strip(" ")
                        )

                    if (detailed_address_locality is not None and
                            isinstance(detailed_address_locality, str) and
                            detailed_address_locality != ''):
                        parsed_location_list['locality_original'] = (
                            detailed_address_locality
                        )

                    if (detailed_address_region is not None and
                            isinstance(detailed_address_region, str) and
                            detailed_address_region != ''):
                        parsed_location_list['region_original'] = (
                            detailed_address_region
                        )

                    two_letter_region_locality_matches: list = (
                        two_letter_matches_string(detailed_address_region)
                        if detailed_address_region is not None else [] +
                        two_letter_matches_string(detailed_address_locality)
                        if detailed_address_locality is not None else []
                    )

                    three_letter_region_locality_matches: list = (
                        three_letter_matches_string(detailed_address_region)
                        if detailed_address_region is not None else [] +
                        three_letter_matches_string(detailed_address_locality)
                        if detailed_address_locality is not None else []
                    )

                    parsed_location_list['region_locality_regex']: list = (
                        two_letter_region_locality_matches + 
                        three_letter_region_locality_matches
                    )

                    delimited_list: list = (
                            delimit_string(
                                input_string=detailed_address_region) +
                            delimit_string(
                                input_string=detailed_address_locality)
                    )

                    parsed_location_list['region_locality_delimited']: list = (
                        delimited_list)

                    # Debug any delimited matches
                    # print(str(delimited_list), flush=True)
                    if ((detailed_address_locality is not None and
                         isinstance(detailed_address_locality, str) and
                         detailed_address_locality != "") or
                        (detailed_address_region is not None and
                         isinstance(detailed_address_region, str) and
                         detailed_address_region != "")):
                        found_state = find_state(
                            country_id=(
                                parsed_location_list.get('country_id', -1)),
                            state_string=detailed_address_locality,
                            regex_letter_code=(
                                two_letter_region_locality_matches + 
                                three_letter_region_locality_matches
                            ),
                            delimited_string=[],
                        )

                        if found_state is None:
                            found_state = find_state(
                                country_id=(
                                    parsed_location_list.get(
                                        'country_id', -1)),
                                state_string=detailed_address_locality,
                                regex_letter_code=(
                                    two_letter_region_locality_matches + 
                                    three_letter_region_locality_matches
                                ),
                                delimited_string=delimited_list,
                            )

                    if ((detailed_address_locality is not None and
                        isinstance(detailed_address_locality, str) and
                        detailed_address_locality != "") or
                            (detailed_address_region is not None and
                             isinstance(detailed_address_region, str) and
                             detailed_address_region != "")):

                        found_city = find_city(
                            country_id=(
                                found_country.id if found_country else -1),
                            state_id=found_state.id if found_state else -1,
                            city_string=fix_city_name(
                                input_city=detailed_address_locality,
                                input_state=found_state.name
                                if found_state else '',
                                input_country=found_country.name
                                if found_country else ''
                            ),
                            delimited_string=[],
                        )

                        if found_city is None:
                            found_city = find_city(
                                country_id=(
                                    found_country.id if found_country else -1),
                                state_id=found_state.id if found_state else -1,
                                city_string=fix_city_name(
                                    input_city=detailed_address_locality,
                                    input_state=found_state.name
                                    if found_state else '',
                                    input_country=found_country.name
                                    if found_country else ''
                                ),
                                delimited_string=delimited_list,
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
