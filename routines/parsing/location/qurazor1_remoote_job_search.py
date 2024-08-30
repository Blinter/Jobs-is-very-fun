"""
qurazor1 | Remoote Job Search
Endpoints:
list_jobs_jobs_get

Note:
  Most of the job listings are remote, if there are listing that are not
  remote then filtering can be done later.
"""
import ast


def qurazor1_remoote_job_search_list_jobs_jobs_get(dict_new, input_json):
    """
    qurazor1 | Remoote Job Search
    """
    job_locations = {}
    # print("count " + str(len(dict_new)), flush=True)
    for i in dict_new.keys():
        # print("processing key: " + str(i), flush=True)
        detailed_location = dict_new[i].get('geo_raw', None)
        # Most likely a status message string
        if detailed_location is None:
            continue

        # print(str(dict_new[i]), flush=True)
        # print(str(dict_new[i].get('geo_raw')), flush=True)

        parsed_location_list = {
            'source__jobs': "qurazor1 | Remoote Job Search",
            'remote__jobs': False,
            'location_original': dict_new[i].get('geo_raw', None),
            'location_country_original': dict_new[i].get('countries', None),
            'location_country_id_input': input_json.get('countries', None),
            'regions': [],
            'subregions': [],
            'countries': [],
            'states': [],
            'cities': []
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
        # countries" "[{'alpha2': 'PL', 'id': 178, 'name': 'Poland'}]"
        # geo_raw: "Białystok, Warszawa, Gdańsk"
        # geo_raw: "Anywhere in Europe"
        # geo_raw: "Any Location"
        # geo_raw: "Wroclaw"
        # geo_raw: "Anywhere"
        # geo_raw: "Only Latam"
        # geo_raw: "None"
        # location input JSON parameter may contain country ID
        # extract countries from countries list:
        # countries: "[{'alpha2': 'PL', 'id': 178, 'name': 'Poland'}]"
        country_id_list = []

        parse_country = parsed_location_list.get('location_country_original')

        # print(str(parse_country), flush=True)
        if (parse_country is not None and
                len(parse_country) > 0):

            if isinstance(parse_country, str):

                try:
                    parse_country = ast.literal_eval(parse_country)
                    # Fix parsed_location_list['location_country_original']
                    parsed_location_list['location_country_original'] = (
                        parse_country)

                except Exception as e:
                    print(str(e), flush=True)
                    raise e

            for j in parse_country:
                if not isinstance(j, dict):
                    continue

                # Extract id from countries
                extracted_country_id = j.get('id', None)

                if extracted_country_id:
                    country_id_list.append(str(extracted_country_id))

        parsed_location_list['location_country_list'] = (
            country_id_list)

        job_locations[i] = parsed_location_list

    return job_locations


qurazor1_country_id_list = {
    "1": {
        "alpha2": "AF",
        "name": "Afghanistan"
    },
    "2": {
        "alpha2": "AX",
        "name": "\u00c5land Islands"
    },
    "3": {
        "alpha2": "AL",
        "name": "Albania"
    },
    "4": {
        "alpha2": "DZ",
        "name": "Algeria"
    },
    "5": {
        "alpha2": "AS",
        "name": "American Samoa"
    },
    "6": {
        "alpha2": "AD",
        "name": "Andorra"
    },
    "7": {
        "alpha2": "AO",
        "name": "Angola"
    },
    "8": {
        "alpha2": "AI",
        "name": "Anguilla"
    },
    "9": {
        "alpha2": "AQ",
        "name": "Antarctica"
    },
    "10": {
        "alpha2": "AG",
        "name": "Antigua and Barbuda"
    },
    "11": {
        "alpha2": "AR",
        "name": "Argentina"
    },
    "12": {
        "alpha2": "AM",
        "name": "Armenia"
    },
    "13": {
        "alpha2": "AW",
        "name": "Aruba"
    },
    "14": {
        "alpha2": "AU",
        "name": "Australia"
    },
    "15": {
        "alpha2": "AT",
        "name": "Austria"
    },
    "16": {
        "alpha2": "AZ",
        "name": "Azerbaijan"
    },
    "17": {
        "alpha2": "BS",
        "name": "Bahamas"
    },
    "18": {
        "alpha2": "BH",
        "name": "Bahrain"
    },
    "19": {
        "alpha2": "BD",
        "name": "Bangladesh"
    },
    "20": {
        "alpha2": "BB",
        "name": "Barbados"
    },
    "21": {
        "alpha2": "BY",
        "name": "Belarus"
    },
    "22": {
        "alpha2": "BE",
        "name": "Belgium"
    },
    "23": {
        "alpha2": "BZ",
        "name": "Belize"
    },
    "24": {
        "alpha2": "BJ",
        "name": "Benin"
    },
    "25": {
        "alpha2": "BM",
        "name": "Bermuda"
    },
    "26": {
        "alpha2": "BT",
        "name": "Bhutan"
    },
    "27": {
        "alpha2": "BO",
        "name": "Bolivia"
    },
    "28": {
        "alpha2": "BQ",
        "name": "Bonaire, Sint Eustatius and Saba"
    },
    "29": {
        "alpha2": "BA",
        "name": "Bosnia and Herzegovina"
    },
    "30": {
        "alpha2": "BW",
        "name": "Botswana"
    },
    "31": {
        "alpha2": "BV",
        "name": "Bouvet Island"
    },
    "32": {
        "alpha2": "BR",
        "name": "Brazil"
    },
    "33": {
        "alpha2": "IO",
        "name": "British Indian Ocean Territory"
    },
    "34": {
        "alpha2": "BN",
        "name": "Brunei Darussalam"
    },
    "35": {
        "alpha2": "BG",
        "name": "Bulgaria"
    },
    "36": {
        "alpha2": "BF",
        "name": "Burkina Faso"
    },
    "37": {
        "alpha2": "BI",
        "name": "Burundi"
    },
    "38": {
        "alpha2": "CV",
        "name": "CaboVerde"
    },
    "39": {
        "alpha2": "KH",
        "name": "Cambodia"
    },
    "40": {
        "alpha2": "CM",
        "name": "Cameroon"
    },
    "41": {
        "alpha2": "CA",
        "name": "Canada"
    },
    "42": {
        "alpha2": "KY",
        "name": "Cayman Islands"
    },
    "43": {
        "alpha2": "CF",
        "name": "Central African Republic"
    },
    "44": {
        "alpha2": "TD",
        "name": "Chad"
    },
    "45": {
        "alpha2": "CL",
        "name": "Chile"
    },
    "46": {
        "alpha2": "CN",
        "name": "China"
    },
    "47": {
        "alpha2": "CX",
        "name": "Christmas Island"
    },
    "48": {
        "alpha2": "CC",
        "name": "Cocos (Keeling) Islands"
    },
    "49": {
        "alpha2": "CO",
        "name": "Colombia"
    },
    "50": {
        "alpha2": "KM",
        "name": "Comoros"
    },
    "51": {
        "alpha2": "CG",
        "name": "Congo"
    },
    "52": {
        "alpha2": "CD",
        "name": "Congo, Democratic Republic of the"
    },
    "53": {
        "alpha2": "CK",
        "name": "Cook Islands"
    },
    "54": {
        "alpha2": "CR",
        "name": "Costa Rica"
    },
    "55": {
        "alpha2": "CI",
        "name": "C\u00f4te d'Ivoire"
    },
    "56": {
        "alpha2": "HR",
        "name": "Croatia"
    },
    "57": {
        "alpha2": "CU",
        "name": "Cuba"
    },
    "58": {
        "alpha2": "CW",
        "name": "Cura\u00e7ao"
    },
    "59": {
        "alpha2": "CY",
        "name": "Cyprus"
    },
    "60": {
        "alpha2": "CZ",
        "name": "Czechia"
    },
    "61": {
        "alpha2": "DK",
        "name": "Denmark"
    },
    "62": {
        "alpha2": "DJ",
        "name": "Djibouti"
    },
    "63": {
        "alpha2": "DM",
        "name": "Dominica"
    },
    "64": {
        "alpha2": "DO",
        "name": "Dominican Republic"
    },
    "65": {
        "alpha2": "EC",
        "name": "Ecuador"
    },
    "66": {
        "alpha2": "EG",
        "name": "Egypt"
    },
    "67": {
        "alpha2": "SV",
        "name": "El Salvador"
    },
    "68": {
        "alpha2": "GQ",
        "name": "Equatorial Guinea"
    },
    "69": {
        "alpha2": "ER",
        "name": "Eritrea"
    },
    "70": {
        "alpha2": "EE",
        "name": "Estonia"
    },
    "71": {
        "alpha2": "SZ",
        "name": "Eswatini"
    },
    "72": {
        "alpha2": "ET",
        "name": "Ethiopia"
    },
    "73": {
        "alpha2": "FK",
        "name": "Falkland Islands(Malvinas)"
    },
    "74": {
        "alpha2": "FO",
        "name": "Faroe Islands"
    },
    "75": {
        "alpha2": "FJ",
        "name": "Fiji"
    },
    "76": {
        "alpha2": "FI",
        "name": "Finland"
    },
    "77": {
        "alpha2": "FR",
        "name": "France"
    },
    "78": {
        "alpha2": "GF",
        "name": "French Guiana"
    },
    "79": {
        "alpha2": "PF",
        "name": "French Polynesia"
    },
    "80": {
        "alpha2": "TF",
        "name": "French Southern Territories"
    },
    "81": {
        "alpha2": "GA",
        "name": "Gabon"
    },
    "82": {
        "alpha2": "GM",
        "name": "Gambia"
    },
    "83": {
        "alpha2": "GE",
        "name": "Georgia"
    },
    "84": {
        "alpha2": "DE",
        "name": "Germany"
    },
    "85": {
        "alpha2": "GH",
        "name": "Ghana"
    },
    "86": {
        "alpha2": "GI",
        "name": "Gibraltar"
    },
    "87": {
        "alpha2": "GR",
        "name": "Greece"
    },
    "88": {
        "alpha2": "GL",
        "name": "Greenland"
    },
    "89": {
        "alpha2": "GD",
        "name": "Grenada"
    },
    "90": {
        "alpha2": "GP",
        "name": "Guadeloupe"
    },
    "91": {
        "alpha2": "GU",
        "name": "Guam"
    },
    "92": {
        "alpha2": "GT",
        "name": "Guatemala"
    },
    "93": {
        "alpha2": "GG",
        "name": "Guernsey"
    },
    "94": {
        "alpha2": "GN",
        "name": "Guinea"
    },
    "95": {
        "alpha2": "GW",
        "name": "Guinea-Bissau"
    },
    "96": {
        "alpha2": "GY",
        "name": "Guyana"
    },
    "97": {
        "alpha2": "HT",
        "name": "Haiti"
    },
    "98": {
        "alpha2": "HM",
        "name": "Heard Island and McDonald Islands"
    },
    "99": {
        "alpha2": "VA",
        "name": "Holy See"
    },
    "100": {
        "alpha2": "HN",
        "name": "Honduras"
    },
    "101": {
        "alpha2": "HK",
        "name": "HongKong"
    },
    "102": {
        "alpha2": "HU",
        "name": "Hungary"
    },
    "103": {
        "alpha2": "IS",
        "name": "Iceland"
    },
    "104": {
        "alpha2": "IN",
        "name": "India"
    },
    "105": {
        "alpha2": "ID",
        "name": "Indonesia"
    },
    "106": {
        "alpha2": "IR",
        "name": "Iran"
    },
    "107": {
        "alpha2": "IQ",
        "name": "Iraq"
    },
    "108": {
        "alpha2": "IE",
        "name": "Ireland"
    },
    "109": {
        "alpha2": "IM",
        "name": "Isle of Man"
    },
    "110": {
        "alpha2": "IL",
        "name": "Israel"
    },
    "111": {
        "alpha2": "IT",
        "name": "Italy"
    },
    "112": {
        "alpha2": "JM",
        "name": "Jamaica"
    },
    "113": {
        "alpha2": "JP",
        "name": "Japan"
    },
    "114": {
        "alpha2": "JE",
        "name": "Jersey"
    },
    "115": {
        "alpha2": "JO",
        "name": "Jordan"
    },
    "116": {
        "alpha2": "KZ",
        "name": "Kazakhstan"
    },
    "117": {
        "alpha2": "KE",
        "name": "Kenya"
    },
    "118": {
        "alpha2": "KI",
        "name": "Kiribati"
    },
    "119": {
        "alpha2": "KP",
        "name": "Korea"
    },
    "120": {
        "alpha2": "KR",
        "name": "Korea, Republic of"
    },
    "121": {
        "alpha2": "KW",
        "name": "Kuwait"
    },
    "122": {
        "alpha2": "KG",
        "name": "Kyrgyzstan"
    },
    "123": {
        "alpha2": "LA",
        "name": "Lao People's Democratic Republic"
    },
    "124": {
        "alpha2": "LV",
        "name": "Latvia"
    },
    "125": {
        "alpha2": "LB",
        "name": "Lebanon"
    },
    "126": {
        "alpha2": "LS",
        "name": "Lesotho"
    },
    "127": {
        "alpha2": "LR",
        "name": "Liberia"
    },
    "128": {
        "alpha2": "LY",
        "name": "Libya"
    },
    "129": {
        "alpha2": "LI",
        "name": "Liechtenstein"
    },
    "130": {
        "alpha2": "LT",
        "name": "Lithuania"
    },
    "131": {
        "alpha2": "LU",
        "name": "Luxembourg"
    },
    "132": {
        "alpha2": "MO",
        "name": "Macao"
    },
    "133": {
        "alpha2": "MG",
        "name": "Madagascar"
    },
    "134": {
        "alpha2": "MW",
        "name": "Malawi"
    },
    "135": {
        "alpha2": "MY",
        "name": "Malaysia"
    },
    "136": {
        "alpha2": "MV",
        "name": "Maldives"
    },
    "137": {
        "alpha2": "ML",
        "name": "Mali"
    },
    "138": {
        "alpha2": "MT",
        "name": "Malta"
    },
    "139": {
        "alpha2": "MH",
        "name": "Marshall Islands"
    },
    "140": {
        "alpha2": "MQ",
        "name": "Martinique"
    },
    "141": {
        "alpha2": "MR",
        "name": "Mauritania"
    },
    "142": {
        "alpha2": "MU",
        "name": "Mauritius"
    },
    "143": {
        "alpha2": "YT",
        "name": "Mayotte"
    },
    "144": {
        "alpha2": "MX",
        "name": "Mexico"
    },
    "145": {
        "alpha2": "FM",
        "name": "Micronesia"
    },
    "146": {
        "alpha2": "MD",
        "name": "Moldova"
    },
    "147": {
        "alpha2": "MC",
        "name": "Monaco"
    },
    "148": {
        "alpha2": "MN",
        "name": "Mongolia"
    },
    "149": {
        "alpha2": "ME",
        "name": "Montenegro"
    },
    "150": {
        "alpha2": "MS",
        "name": "Montserrat"
    },
    "151": {
        "alpha2": "MA",
        "name": "Morocco"
    },
    "152": {
        "alpha2": "MZ",
        "name": "Mozambique"
    },
    "153": {
        "alpha2": "MM",
        "name": "Myanmar"
    },
    "154": {
        "alpha2": "NA",
        "name": "Namibia"
    },
    "155": {
        "alpha2": "NR",
        "name": "Nauru"
    },
    "156": {
        "alpha2": "NP",
        "name": "Nepal"
    },
    "157": {
        "alpha2": "NL",
        "name": "Netherlands"
    },
    "158": {
        "alpha2": "NC",
        "name": "New Caledonia"
    },
    "159": {
        "alpha2": "NZ",
        "name": "New Zealand"
    },
    "160": {
        "alpha2": "NI",
        "name": "Nicaragua"
    },
    "161": {
        "alpha2": "NE",
        "name": "Niger"
    },
    "162": {
        "alpha2": "NG",
        "name": "Nigeria"
    },
    "163": {
        "alpha2": "NU",
        "name": "Niue"
    },
    "164": {
        "alpha2": "NF",
        "name": "Norfolk Island"
    },
    "165": {
        "alpha2": "MK",
        "name": "NorthMacedonia"
    },
    "166": {
        "alpha2": "MP",
        "name": "Northern MarianaIslands"
    },
    "167": {
        "alpha2": "NO",
        "name": "Norway"
    },
    "168": {
        "alpha2": "OM",
        "name": "Oman"
    },
    "169": {
        "alpha2": "PK",
        "name": "Pakistan"
    },
    "170": {
        "alpha2": "PW",
        "name": "Palau"
    },
    "171": {
        "alpha2": "PS",
        "name": "Palestine, State of"
    },
    "172": {
        "alpha2": "PA",
        "name": "Panama"
    },
    "173": {
        "alpha2": "PG",
        "name": "Papua New Guinea"
    },
    "174": {
        "alpha2": "PY",
        "name": "Paraguay"
    },
    "175": {
        "alpha2": "PE",
        "name": "Peru"
    },
    "176": {
        "alpha2": "PH",
        "name": "Philippines"
    },
    "177": {
        "alpha2": "PN",
        "name": "Pitcairn"
    },
    "178": {
        "alpha2": "PL",
        "name": "Poland"
    },
    "179": {
        "alpha2": "PT",
        "name": "Portugal"
    },
    "180": {
        "alpha2": "PR",
        "name": "Puerto Rico"
    },
    "181": {
        "alpha2": "QA",
        "name": "Qatar"
    },
    "182": {
        "alpha2": "RE",
        "name": "R\u00e9union"
    },
    "183": {
        "alpha2": "RO",
        "name": "Romania"
    },
    "184": {
        "alpha2": "RU",
        "name": "Russian Federation"
    },
    "185": {
        "alpha2": "RW",
        "name": "Rwanda"
    },
    "186": {
        "alpha2": "BL",
        "name": "Saint Barth\u00e9lemy"
    },
    "187": {
        "alpha2": "SH",
        "name": "Saint Helena, Ascension and Tristan daCunha"
    },
    "188": {
        "alpha2": "KN",
        "name": "Saint Kitts and Nevis"
    },
    "189": {
        "alpha2": "LC",
        "name": "Saint Lucia"
    },
    "190": {
        "alpha2": "MF",
        "name": "Saint Martin (French part)"
    },
    "191": {
        "alpha2": "PM",
        "name": "Saint Pierre and Miquelon"
    },
    "192": {
        "alpha2": "VC",
        "name": "Saint Vincent and the Grenadines"
    },
    "193": {
        "alpha2": "WS",
        "name": "Samoa"
    },
    "194": {
        "alpha2": "SM",
        "name": "San Marino"
    },
    "195": {
        "alpha2": "ST",
        "name": "Sao Tome and Principe"
    },
    "196": {
        "alpha2": "SA",
        "name": "Saudi Arabia"
    },
    "197": {
        "alpha2": "SN",
        "name": "Senegal"
    },
    "198": {
        "alpha2": "RS",
        "name": "Serbia"
    },
    "199": {
        "alpha2": "SC",
        "name": "Seychelles"
    },
    "200": {
        "alpha2": "SL",
        "name": "Sierra Leone"
    },
    "201": {
        "alpha2": "SG",
        "name": "Singapore"
    },
    "202": {
        "alpha2": "SX",
        "name": "Sint Maarten (Dutch part)"
    },
    "203": {
        "alpha2": "SK",
        "name": "Slovakia"
    },
    "204": {
        "alpha2": "SI",
        "name": "Slovenia"
    },
    "205": {
        "alpha2": "SB",
        "name": "Solomon Islands"
    },
    "206": {
        "alpha2": "SO",
        "name": "Somalia"
    },
    "207": {
        "alpha2": "ZA",
        "name": "South Africa"
    },
    "208": {
        "alpha2": "GS",
        "name": "South Georgiaand the South Sandwich Islands"
    },
    "209": {
        "alpha2": "SS",
        "name": "South Sudan"
    },
    "210": {
        "alpha2": "ES",
        "name": "Spain"
    },
    "211": {
        "alpha2": "LK",
        "name": "Sri Lanka"
    },
    "212": {
        "alpha2": "SD",
        "name": "Sudan"
    },
    "213": {
        "alpha2": "SR",
        "name": "Suriname"
    },
    "214": {
        "alpha2": "SJ",
        "name": "Svalbard and Jan Mayen"
    },
    "215": {
        "alpha2": "SE",
        "name": "Sweden"
    },
    "216": {
        "alpha2": "CH",
        "name": "Switzerland"
    },
    "217": {
        "alpha2": "SY",
        "name": "Syrian Arab Republic"
    },
    "218": {
        "alpha2": "TW",
        "name": "Taiwan, Province of China"
    },
    "219": {
        "alpha2": "TJ",
        "name": "Tajikistan"
    },
    "220": {
        "alpha2": "TZ",
        "name": "Tanzania, United Republic of"
    },
    "221": {
        "alpha2": "TH",
        "name": "Thailand"
    },
    "222": {
        "alpha2": "TL",
        "name": "Timor-Leste"
    },
    "223": {
        "alpha2": "TG",
        "name": "Togo"
    },
    "224": {
        "alpha2": "TK",
        "name": "Tokelau"
    },
    "225": {
        "alpha2": "TO",
        "name": "Tonga"
    },
    "226": {
        "alpha2": "TT",
        "name": "Trinidad and Tobago"
    },
    "227": {
        "alpha2": "TN",
        "name": "Tunisia"
    },
    "228": {
        "alpha2": "TR",
        "name": "Turkey"
    },
    "229": {
        "alpha2": "TM",
        "name": "Turkmenistan"
    },
    "230": {
        "alpha2": "TC",
        "name": "Turks and Caicos Islands"
    },
    "231": {
        "alpha2": "TV",
        "name": "Tuvalu"
    },
    "232": {
        "alpha2": "UG",
        "name": "Uganda"
    },
    "233": {
        "alpha2": "UA",
        "name": "Ukraine"
    },
    "234": {
        "alpha2": "AE",
        "name": "United Arab Emirates"
    },
    "235": {
        "alpha2": "GB",
        "name": "United Kingdom"
    },
    "236": {
        "alpha2": "US",
        "name": "United States of America"
    },
    "237": {
        "alpha2": "UM",
        "name": "United States Minor Outlying Islands"
    },
    "238": {
        "alpha2": "UY",
        "name": "Uruguay"
    },
    "239": {
        "alpha2": "UZ",
        "name": "Uzbekistan"
    },
    "240": {
        "alpha2": "VU",
        "name": "Vanuatu"
    },
    "241": {
        "alpha2": "VE",
        "name": "Venezuela"
    },
    "242": {
        "alpha2": "VN",
        "name": "Viet Nam"
    },
    "243": {
        "alpha2": "VG",
        "name": "Virgin Islands (British)"
    },
    "244": {
        "alpha2": "VI",
        "name": "Virgin Islands(U.S.)"
    },
    "245": {
        "alpha2": "WF",
        "name": "Wallis and Futuna"
    },
    "246": {
        "alpha2": "EH",
        "name": "Western Sahara"
    },
    "247": {
        "alpha2": "YE",
        "name": "Yemen"
    },
    "248": {
        "alpha2": "ZM",
        "name": "Zambia"
    },
    "249": {
        "alpha2": "ZW",
        "name": "Zimbabwe"
    }
}
