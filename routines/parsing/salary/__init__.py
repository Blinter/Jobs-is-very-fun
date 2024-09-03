"""
Get Job Salary
main function that parses API Job Salaries
"""
import ast
import decimal
import re
from decimal import Decimal, InvalidOperation

from extensions_salaries import convert_str_to_int
from routines import (
    extract_value_from_dict,
    extract_values_from_dict
)


def get_job_salaries(
        api_url: str,
        nice_name: str,
        dict_new: dict,
        input_json: dict):
    """
    Converts a jobs dictionary to a parsed Salary dictionary
    """
    if (not isinstance(dict_new, dict) or
            dict_new.get('error') is not None):
        return {}
    match api_url:

        # APIJobs | Job Searching API
        # APIJobs.dev | API Jobs
        # Search jobs
        # Search Jobs
        case ("https://apijob-job-searching-api.p.rapidapi.com"
              "/v1/job/search" |
              "https://api.apijobs.dev"
              "/v1/job/search"):
            if (nice_name == "Search jobs" or
                    nice_name == "Search Jobs"):
                return {"error": "Data from API does not include salary data."}

        # APIJobs | Job Searching API
        # Search organization
        case ("https://apijob-job-searching-api.p.rapidapi.com"
              "/v1/organization/search"):
            if nice_name == "Search organization":
                return {"error": "Data from API does not include salary data."}

        # APIJobs | Job Searching API
        # Get job by id
        case ("https://apijob-job-searching-api.p.rapidapi.com"
              "/v1/job/"):
            if nice_name == "Get job by id":
                return {"error": "Data from API does not include salary data."}

        # avadataservices | Job Postings
        # /api/v2/Jobs/{slug}
        case ("https://job-postings1.p.rapidapi.com"
              "/api/v2/Jobs/"):
            if nice_name == "/api/v2/Jobs/{slug}":
                result = (
                    extract_value_from_dict(
                        key_name='salary',
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if (i is None or
                            result[i] is None or
                            len(result[i]) == 0):
                        result[i] = {}
                        continue

                    result[i] = result[i].lower()
                    salary_currency = None
                    monthly_salary = False
                    weekly_salary = False
                    daily_salary = False
                    hourly_salary = False

                    # print("key " + str(i) + ": " + result[i], flush=True)

                    if 'year' in result[i].lower():
                        result[i] = (
                            result[i]
                            .replace('per year', '')
                            .replace('Per year', '')
                            .replace('Per Year', '')
                            .replace('PER YEAR', '')
                            .replace('/year', '')
                            .replace('/Year', '')
                            .replace('/YEAR', '')
                            .replace('yearly', '')
                            .replace('Yearly', '')
                            .replace('YEARLY', '')
                            .replace('a year', '')
                            .replace('a Year', '')
                            .replace('A Year', '')
                            .replace('year', '')
                            .replace('Year', '')
                            .replace('YEAR', '')
                            .strip()
                        )

                    elif 'month' in result[i].lower():
                        monthly_salary = True
                        result[i] = (
                            result[i]
                            .replace('per month', '')
                            .replace('Per month', '')
                            .replace('Per Month', '')
                            .replace('PER MONTH', '')
                            .replace('/month', '')
                            .replace('/Month', '')
                            .replace('/MONTH', '')
                            .replace('monthly', '')
                            .replace('Monthly', '')
                            .replace('MONTHLY', '')
                            .replace('month', '')
                            .replace('Month', '')
                            .replace('MONTH', '')
                            .strip()
                        )

                    elif 'week' in result[i].lower():
                        weekly_salary = True
                        result[i] = (
                            result[i]
                            .replace('per week', '')
                            .replace('per Week', '')
                            .replace('Per Week', '')
                            .replace('PER WEEK', '')
                            .replace('/week', '')
                            .replace('/Week', '')
                            .replace('/WEEK', '')
                            .replace('weekly', '')
                            .replace('Weekly', '')
                            .replace('WEEKLY', '')
                            .replace('week', '')
                            .replace('Week', '')
                            .replace('WEEK', '')
                            .strip()
                        )

                    elif ('day' in result[i.lower()] or
                          'daily' in result[i].lower()):
                        daily_salary = True
                        result[i] = (
                            result[i]
                            .replace('per day', '')
                            .replace('Per day', '')
                            .replace('Per Day', '')
                            .replace('PER DAY', '')
                            .replace('/day', '')
                            .replace('/Day', '')
                            .replace('/DAY', '')
                            .replace('day', '')
                            .replace('Day', '')
                            .replace('DAY', '')
                            .replace('/daily', '')
                            .replace('/Daily', '')
                            .replace('/DAILY', '')
                            .replace('daily', '')
                            .replace('Daily', '')
                            .replace('DAILY', '')
                            .strip()
                        )

                    elif 'hour' in result[i].lower():
                        hourly_salary = True
                        result[i] = (
                            result[i]
                            .replace('per hour', '')
                            .replace('Per hour', '')
                            .replace('Per Hour', '')
                            .replace('PER HOUR', '')
                            .replace('/hour', '')
                            .replace('/Hour', '')
                            .replace('/HOUR', '')
                            .replace('hourly', '')
                            .replace('Hourly', '')
                            .replace('HOURLY', '')
                            .replace('hour', '')
                            .replace('Hour', '')
                            .replace('HOUR', '')
                            .strip()
                        )

                    if 'net' in result[i].lower():
                        result[i] = (
                            result[i]
                            .replace('net', '')
                            .replace('Net', '')
                            .replace('NET', '')
                            .strip()
                        )

                    if 'gross' in result[i].lower():
                        result[i] = (
                            result[i]
                            .replace('gross', '')
                            .replace('Gross', '')
                            .replace('GROSS', '')
                            .strip()
                        )

                    if 'starting at' in result[i].lower():
                        result[i] = (
                            result[i]
                            .replace('starting at', '')
                            .replace('Starting at', '')
                            .replace('Starting At', '')
                            .replace('STARTING AT', '')
                            .strip()
                        )

                    if '(zp 3)' in result[i].lower():
                        result[i] = (
                            result[i]
                            .replace('(zp 3)', '')
                            .replace('(Zp 3)', '')
                            .replace('(zP 3)', '')
                            .replace('(ZP 3)', '')
                            .strip()
                        )

                    three_letter_matches = (
                        re.findall(r'\b['r'A-Z]{3}\b', result[i]))

                    for j in range(len(three_letter_matches)):
                        if len(three_letter_matches[j]) != 0:
                            salary_currency = three_letter_matches[j]
                            result[i] = (
                                result[i]
                                .replace(three_letter_matches[j], '')
                                .strip()
                            )

                    if salary_currency is None:
                        if '$' in result[i]:
                            salary_currency = "USD"
                            result[i] = (
                                result[i]
                                .replace("$", '')
                                .strip()
                            )

                    if '-' in result[i]:
                        result[i] = result[i].strip().split('-')
                        for j in range(len(result[i])):
                            result[i][j] = result[i][j].strip()

                            if ' ' in result[i][j]:
                                result[i][j] = (
                                    result[i][j]
                                    .replace(' ', '')
                                    .strip()
                                )

                            if ',' in result[i][j]:
                                result[i][j] = (
                                    result[i][j]
                                    .replace(',', '')
                                    .strip()
                                )
                    # Longer Dash
                    if '—' in result[i]:
                        result[i] = result[i].strip().split('—')
                        for j in range(len(result[i])):
                            result[i][j] = result[i][j].strip()

                            if ' ' in result[i][j]:
                                result[i][j] = (
                                    result[i][j]
                                    .replace(' ', '')
                                    .strip()
                                )

                            if ',' in result[i][j]:
                                result[i][j] = (
                                    result[i][j]
                                    .replace(',', '')
                                    .strip()
                                )

                    if ' to ' in result[i]:
                        result[i] = result[i].strip().split(' to ')

                        for j in range(len(result[i])):
                            result[i][j] = result[i][j].strip()

                            if ' ' in result[i][j]:
                                result[i][j] = (
                                    result[i][j]
                                    .replace(' ', '')
                                    .strip()
                                )

                            if ',' in result[i][j]:
                                result[i][j] = (
                                    result[i][j]
                                    .replace(',', '')
                                    .strip()
                                )

                    if isinstance(result[i], list):
                        for j in range(len(result[i])):
                            result[i][j] = (
                                result[i][j]
                                .replace(',', '')
                                .strip()
                            )

                    elif ',' in result[i]:
                        result[i] = result[i].replace(',', '').strip()

                    if monthly_salary:
                        if isinstance(result[i], list):
                            for j in range(len(result[i])):
                                result[i][j] = convert_str_to_int(
                                    Decimal(
                                        result[i][j]
                                        if isinstance(result[i][j], str)
                                        else result[i][j]
                                    ) * 12)

                        else:
                            result[i] = convert_str_to_int(
                                Decimal(
                                    result[i]
                                    if isinstance(result[i], str)
                                    else result[i]
                                ) * 12)

                    elif weekly_salary:
                        if isinstance(result[i], list):
                            for j in range(len(result[i])):
                                result[i][j] = convert_str_to_int(
                                    Decimal(
                                        result[i][j]
                                        if isinstance(result[i][j], str)
                                        else result[i][j]
                                    ) * 52)

                        else:
                            result[i] = convert_str_to_int(
                                Decimal(
                                    result[i]
                                    if isinstance(result[i], str)
                                    else result[i]
                                ) * 52)

                    elif daily_salary:
                        if isinstance(result[i], list):
                            for j in range(len(result[i])):
                                result[i][j] = convert_str_to_int(
                                    Decimal(
                                        result[i][j].strip()
                                        if isinstance(result[i][j], str)
                                        else result[i][j]
                                    ) * 5 * 52)

                        else:
                            result[i] = convert_str_to_int(
                                Decimal(
                                    result[i]
                                    if isinstance(result[i], str)
                                    else result[i]
                                ) * 5 * 52)

                    elif hourly_salary:
                        if isinstance(result[i], list):
                            for j in range(len(result[i])):
                                result[i][j] = convert_str_to_int(
                                    Decimal(
                                        result[i][j]
                                        if isinstance(result[i][j], str)
                                        else result[i][j]
                                    ) * 2080)

                        else:
                            result[i] = convert_str_to_int(
                                Decimal(
                                    result[i]
                                    if isinstance(result[i], str)
                                    else result[i]
                                ) * 2080)

                    else:
                        if isinstance(result[i], list):
                            for j in range(len(result[i])):
                                if 'K' in result[i][j]:
                                    result[i][j] = (
                                        result[i][j]
                                        .replace("K", "")
                                    )

                                    result[i][j] = convert_str_to_int(
                                        Decimal(
                                            result[i][j]
                                            if isinstance(result[i][j], str)
                                            else result[i][j]
                                        ) * 1000)

                                else:
                                    result[i][j] = convert_str_to_int(
                                        result[i][j].strip()
                                        if isinstance(result[i][j], str)
                                        else result[i][j]
                                    )

                        else:
                            if 'K' in result[i]:
                                result[i] = result[i].replace("K", "")
                                result[i] = convert_str_to_int(
                                    Decimal(
                                        result[i].strip()
                                        if isinstance(result[i], str)
                                        else result[i]
                                    ) * 1000)

                            else:
                                result[i] = convert_str_to_int(
                                    result[i].strip()
                                    if isinstance(result[i], str)
                                    else result[i]
                                )

                    new_dict = {
                        'currency': salary_currency,

                        'min_salary': result[i][0]
                        if (isinstance(result[i], list) and
                            len(result[i]) != 0)
                        else 0,

                        'max_salary': result[i][1]
                        if (isinstance(result[i], list) and
                            len(result[i]) > 1)
                        else result[i][0] if (
                                isinstance(result[i], list) and
                                len(result[i]) == 0
                        ) else 0,
                    }

                    result[i] = new_dict

                return result

        # avadataservices | Job Postings
        # /api/v2/Jobs/Latest
        case ("https://job-postings1.p.rapidapi.com/"):
            if nice_name == "/api/v2/Jobs/Latest":
                return (
                    {
                        "error":
                            "Data from API does not provide JSON data. "
                            "HTML must be interpreted."
                    }
                )

        # avadataservices | Job Postings
        # /api/v2/Jobs/Search
        case ("https://job-postings1.p.rapidapi.com"
              "/api/v2/Jobs/Search"):
            if nice_name == "/api/v2/Jobs/Search":
                return (
                    {
                        "error":
                            "Data from API does not include salary data."
                    }
                )

        # bareq | Remote Jobs API
        # List jobs free
        case ("https://remote-jobs-api1.p.rapidapi.com"
              "/jobs/free"):
            if nice_name == "List jobs free":
                return (
                    {
                        "error":
                            "Data from API does not include salary data."
                    }
                )

        # Bebity | Linkedin Jobs Scraper API
        # Get jobs (JSON)
        case ("https://linkedin-jobs-scraper-api.p.rapidapi.com"
              "/jobs" |
              "https://linkedin-jobs-scraper-api.p.rapidapi.com"
              "/jobs/trial"):
            if (nice_name == "Get jobs (JSON)" or
                    nice_name == "Get jobs trial (JSON)"):
                return (
                    {
                        "error":
                            "Data from API does not include salary data."
                    }
                )

        # Betoalien | USA Jobs for IT
        # All Endpoints
        case ("https://usa-jobs-for-it.p.rapidapi.com"
              "/DataEngineer" |
              "https://usa-jobs-for-it.p.rapidapi.com"
              "/DataAnalyst" |
              "https://usa-jobs-for-it.p.rapidapi.com"
              "/Angular" |
              "https://usa-jobs-for-it.p.rapidapi.com"
              "/Java" |
              "https://usa-jobs-for-it.p.rapidapi.com"
              "/Python" |
              "https://usa-jobs-for-it.p.rapidapi.com"
              "/React" |
              "https://usa-jobs-for-it.p.rapidapi.com"
              "/BusinessIntelligence" |
              "https://usa-jobs-for-it.p.rapidapi.com"
              "/Laravel" |
              "https://usa-jobs-for-it.p.rapidapi.com"
              "/NodeJs" |
              "https://usa-jobs-for-it.p.rapidapi.com"
              "/FullStack" |
              "https://usa-jobs-for-it.p.rapidapi.com"
              "/JavaScript"
              ):
            return (
                {
                    "error":
                        "Data from API does not include salary data."
                }
            )

        # Dodocr7 | Google Jobs
        # OfferInfo
        # SearchOffers
        case ("https://google-jobs.p.rapidapi.com/"):
            if nice_name == "OfferInfo":
                if ((dict_new.get('status', None) is not None and
                        dict_new.get('status') == 404 or
                        dict_new.get('status') == 500) or
                        dict_new.get('error') is not None):
                    return (
                        {
                            'error':
                                'Error with query.'
                        }
                    )
                result = (
                    extract_value_from_dict(
                        key_name='salary',
                        dict_new=dict_new
                    )
                )

                for i in [j for j in result.keys()]:
                    if result[i] == '':
                        result[i] = {}
                        continue

                    hourly_salary = False

                    # Unknown character (Hyphenated fix)
                    for j in range(len(result[i])):
                        if (result[i][j].encode('utf-8') ==
                                b'\xe2\x80\x93'):
                            result[i] = (
                                    result[i][0:j] +
                                    '-' +
                                    result[i][j+1:]
                            )
                        # print("(" + str(result[i][j].encode('utf-8')) + ")",
                        #       flush=True)

                    if "-" in result[i]:
                        result[i] = result[i].split('-')
                        result[i] = [j.strip() for j in result[i]]

                    if (isinstance(result[i], list) and
                            len(result[i]) > 0):
                        if "a year" in result[i][0]:
                            result[i][0] = (
                                result[i][0]
                                .replace("a year", '')
                                .strip()
                            )

                        if 'hour' in result[i][0]:
                            hourly_salary = True
                            result[i][0] = (
                                result[i][0]
                                .replace('per hour', '')
                                .replace('/hour', '')
                                .replace('hourly', '')
                                .replace('an hour', '')
                                .replace('a hour', '')
                                .replace('hour', '')
                                .strip()
                            )

                        if (len(result[i]) > 1 and
                                "a year" in result[i][1]):
                            result[i][1] = (
                                result[i][1]
                                .replace("a year", '')
                                .strip()
                            )

                        if 'hour' in result[i][1]:
                            hourly_salary = True
                            result[i][1] = (
                                result[i][1]
                                .replace('per hour', '')
                                .replace('Per hour', '')
                                .replace('Per Hour', '')
                                .replace('PER HOUR', '')
                                .replace('/hour', '')
                                .replace('/Hour', '')
                                .replace('/HOUR', '')
                                .replace('hourly', '')
                                .replace('Hourly', '')
                                .replace('HOURLY', '')
                                .replace('hour', '')
                                .replace('Hour', '')
                                .replace('HOUR', '')
                                .strip()
                            )

                    current_currency = "?"
                    if isinstance(result[i], list):
                        for j in range(len(result[i])):
                            if "$" in result[i][j]:
                                current_currency = "$"
                                result[i][j] = (
                                    result[i][j]
                                    .replace('$', '')
                                    .replace('USD', '')
                                    .replace('US', '')
                                    .strip()
                                )

                            # Parse K to Integer
                            if "K" in result[i][j]:
                                result[i][j] = (
                                    result[i][j]
                                    .replace("K", "")
                                    .strip()
                                )
                                # Convert to number
                                result[i][j] = convert_str_to_int(
                                    Decimal(
                                        result[i][j]
                                        if isinstance(result[i][j], str)
                                        else result[i][j]
                                    ) * 1000)

                    elif "$" in result[i]:
                        current_currency = "$"
                        result[i] = result[i].replace("$", "")
                        result[i] = result[i].replace("USD", "")
                        result[i] = result[i].replace("US", "")
                        result[i] = result[i].strip()

                        # Parse K to Integer
                        if "K" in result[i]:
                            result[i] = (
                                result[i]
                                .replace("K", "")
                                .strip()
                            )

                            # Convert to number
                            result[i] = convert_str_to_int(
                                Decimal(
                                    result[i].strip()
                                    if isinstance(result[i], str)
                                    else result[i]
                                ) * 1000)

                    result[i] = {
                        'currency': current_currency,

                        'min_salary': convert_str_to_int(
                            result[i].strip()
                            if isinstance(result[i], str) else
                            result[i][0]
                        ) * (1 if not hourly_salary else 2080),

                        'max_salary': convert_str_to_int(
                            (result[i].strip()
                             if isinstance(result[i], str) else
                             result[i])
                            if not isinstance(result[i], list) else

                            ((result[i][1].strip()
                              if isinstance(result[i][1], str) else
                              result[i][1])
                             if len(result[i]) > 1 else

                             (result[i][0].strip()
                              if isinstance(result[i][0], str)
                              else result[i][0]))
                        ) * (1 if not hourly_salary else 2080),
                    }

                return result

            elif nice_name == "SearchOffers":
                # print("Data from API does not include appropriate data. "
                #       "Each job query page must be queried individually.",
                #       flush=True)

                return (
                    {
                        "error":
                            "Data from API does not include "
                            "appropriate data. Each page must "
                            "be queried individually."
                    }
                )

        # Fantastic Jobs | Active Jobs DB
        # Get Jobs
        # Get Jobs - (Text Description)
        case ("https://active-jobs-db.p.rapidapi.com"
              "/active-ats" |
              "https://active-jobs-db.p.rapidapi.com"
              "/rest/v1/active_ats_textdescription_v1"):
            if (nice_name == "Get Jobs" or
                    nice_name == "Get Jobs - (Text Description"):
                return (
                    {
                        "error":
                            "Data from API does not include "
                            "appropriate data. Each page must "
                            "be queried individually."
                    }
                )

        # Flatroy | Jobs from Remoteok
        # Get list
        case ("https://jobs-from-remoteok.p.rapidapi.com/"):
            if nice_name == "Get list":
                result = (
                    extract_values_from_dict(
                        key_names=['salary_min', 'salary_max'],
                        dict_new=dict_new
                    )
                )
                for i in result.keys():
                    for k, j in enumerate(result[i]):
                        if j == '0':
                            del result[i][k]

                    if len(result[i]) > 0:
                        if len(result[i]) == 1:
                            result[i] = {
                                'currency': "USD",
                                'min_salary': convert_str_to_int(
                                    result[i][0].strip()
                                ),
                                'max_salary': convert_str_to_int(
                                    result[i][0].strip()
                                ),
                            }

                        elif len(result[i]) == 2:
                            result[i] = {
                                'currency': "USD",
                                'min_salary': convert_str_to_int(
                                    result[i][0].strip()
                                ),
                                'max_salary': convert_str_to_int(
                                    result[i][1].strip()
                                ),
                            }

                return result

        # Freshdata | Fresh Linkedin Profile Data
        # Freshdata | Linkedin Jobs
        # Get Job Details
        case ("https://linkedin-jobs4.p.rapidapi.com"
              "/get-job-details" |
              "https://fresh-linkedin-profile-data.p.rapidapi.com"
              "/get-job-details"):
            if nice_name == "Get Job Details":
                result = (
                    extract_value_from_dict(
                        key_name='salary_details',
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    currency = result[i].get('currency_code', '?')
                    pay_type = result[i].get('pay_period')

                    new_min_salary = result[i].get('min_salary')

                    new_max_salary = result[i].get('max_salary')

                    if pay_type is not None:
                        if pay_type.lower() == 'hourly':
                            if new_min_salary is not None:
                                # 40 * 52
                                new_min_salary = Decimal(
                                    new_min_salary.strip()
                                ) * 2080

                            if new_max_salary is not None:
                                # 40 * 52
                                new_max_salary = Decimal(
                                    new_max_salary.strip()
                                ) * 2080

                        elif pay_type.lower() == 'yearly':
                            new_min_salary = result[i].get('min_salary')
                            new_max_salary = result[i].get('max_salary')

                    if ("?" in currency and
                            new_min_salary is None and
                            new_max_salary is None):
                        result[i] = {}
                        continue

                    result[i] = {
                        'currency': currency,

                        'min_salary': convert_str_to_int(new_min_salary)
                        if new_min_salary is not None else None,

                        'max_salary': convert_str_to_int(new_max_salary)
                        if new_max_salary is not None else None,
                    }

                return result

        # Freshdata | Fresh Linkedin Profile Data
        # Freshdata | Linkedin Jobs
        # Search Jobs
        case ("https://fresh-linkedin-profile-data.p.rapidapi.com"
              "/search-jobs" |
              "https://linkedin-jobs4.p.rapidapi.com"
              "/search-jobs"):
            if nice_name == "Search Jobs":
                result = (
                    extract_value_from_dict(
                        key_name='salary',
                        dict_new=dict_new
                    )
                )

                # Convert to list
                for i in result.keys():
                    # print(str(i) + " " + str(result[i]), flush=True)
                    if (result[i] is None or
                            len(result[i]) == 0):
                        result[i] = {}
                        continue

                    if ('/yr' not in result[i] and
                            '/hr' not in result[i] and
                            'hour' not in result[i] and
                            'year' not in result[i]):
                        result[i] = {}
                        continue

                    else:
                        if '·' in result[i]:
                            split_string = result[i].split('·')

                            for j in range(len(split_string)):
                                if ('/hr' in split_string[j] or
                                        'hour' in split_string[j] or
                                        '/yr' in split_string[j] or
                                        'year' in split_string[j] or
                                        '$' in split_string[j]):
                                    result[i] = split_string[j]

                            # look for dash
                            if '-' in result[i]:
                                result[i] = result[i].split('-')
                                new_list = []

                                for k in range(len(result[i])):
                                    new_list.append(result[i][k].strip())

                                result[i] = new_list

                            # longer dash
                            elif '—' in result[i]:
                                result[i] = result[i].split('—')
                                new_list = []

                                for k in range(len(result[i])):
                                    new_list.append(result[i][k].strip())

                                result[i] = new_list

                            else:
                                # Convert to list anyway
                                result[i] = [result[i]]

                        elif '-' in result[i]:
                            result[i] = result[i].split('-')
                            new_list = []

                            for k in range(len(result[i])):
                                new_list.append(result[i][k].strip())

                            result[i] = new_list

                        # Longer Dash
                        elif '—' in result[i]:
                            result[i] = result[i].split('—')
                            new_list = []

                            for k in range(len(result[i])):
                                new_list.append(result[i][k].strip())

                            result[i] = new_list

                        else:
                            # Convert to list anyway
                            result[i] = [result[i]]

                # convert to dictionary
                for i in result.keys():
                    # print(str(i) + " " + str(result[i]), flush=True)
                    if (i is None or
                            result[i] is None or
                            len(result[i]) == 0):
                        result[i] = {}
                        continue

                    if not isinstance(result[i], list):
                        raise ValueError("Not a list - " +
                                         str(result[i]) +
                                         " debug key :" + str(i))

                    elif len(result[i]) == 1:
                        current_currency = '?'
                        # Currency parsing
                        if "$" in result[i][0]:
                            result[i][0] = (
                                result[i][0]
                                .replace("$", "")
                                .strip()
                            )
                            current_currency = "USD"

                        wage_multiplier = 1

                        if " + bonus, stock" in result[i][0].lower():
                            result[i][0] = (
                                result[i][0]
                                .replace(" + Bonus, Stock", "")
                                .replace(" + Bonus, stock", "")
                                .replace(" + bonus, Stock", "")
                                .replace(" + bonus, stock", "")
                                .strip()
                            )

                        if " + bonus" in result[i][0].lower():
                            result[i][0] = (
                                result[i][0]
                                .replace(" + Bonus", "")
                                .replace(" + bonus", "")
                                .strip()
                            )

                        if " + profit sharing" in result[i][0].lower():
                            result[i][0] = (
                                result[i][0]
                                .replace(" + Profit Sharing", "")
                                .replace(" + Profit sharing", "")
                                .replace(" + profit Sharing", "")
                                .replace(" + profit sharing", "")
                                .strip()
                            )

                        if ", stock options" in result[i][0].lower():
                            result[i][0] = (
                                result[i][0]
                                .replace(", Stock Options", "")
                                .replace(", Stock options", "")
                                .replace(", stock Options", "")
                                .replace(", stock options", "")
                                .strip()
                            )

                        if ", sign" in result[i][0].lower():
                            result[i][0] = (
                                result[i][0]
                                .replace(", Sign", "")
                                .replace(", sign", "")
                                .strip()
                            )

                        if "+ stock options" in result[i][0].lower():
                            result[i][0] = (
                                result[i][0]
                                .replace("+ Stock Options", "")
                                .replace("+ Stock options", "")
                                .replace("+ stock Options", "")
                                .replace("+ stock options", "")
                                .strip()
                            )

                        if ", profit sharing" in result[i][0].lower():
                            result[i][0] = (
                                result[i][0]
                                .replace(", Profit Sharing", "")
                                .replace(", Profit sharing", "")
                                .replace(", profit Sharing", "")
                                .replace(", profit sharing", "")
                                .strip()
                            )

                        if ", commission" in result[i][0].lower():
                            result[i][0] = (
                                result[i][0]
                                .replace(", Commission", "")
                                .replace(", commission", "")
                                .strip()
                            )

                        # Parse hourly wage
                        if "/hr" in result[i][0]:
                            result[i][0] = (
                                result[i][0]
                                .replace("/hr", "")
                                .strip()
                            )

                            # 40 hours * 52 weeks (US Based)
                            wage_multiplier = 2080

                        elif "/yr" in result[i][0]:
                            result[i][0] = (
                                result[i][0]
                                .replace("/yr", "")
                                .strip()
                            )

                            wage_multiplier = 1

                        maximum_found = False
                        if 'up to' in result[i][0].lower():
                            result[i][0] = (
                                result[i][0][
                                    result[i][0].lower().find('up to') +
                                    len('up to'):]
                            )

                            maximum_found = True

                        if ("from" in result[i][0] or
                                "From" in result[i][0]):
                            result[i][0] = (
                                result[i][0]
                                .replace("from", "")
                                .replace("From", "")
                                .strip()
                            )

                        if ("starting at" in result[i][0] or
                                "Starting at" in result[i][0]):
                            result[i][0] = (
                                result[i][0]
                                .replace("starting at", "")
                                .replace("Starting at", "")
                                .strip()
                            )

                        # Parse K to Integer
                        if "K" in result[i][0]:
                            # print(str(result[i][0]), flush=True)
                            result[i][0] = (
                                result[i][0]
                                .replace("K", "")
                                .strip()
                            )

                            # Convert to number
                            result[i][0] = decimal.Decimal(
                                convert_str_to_int(
                                    result[i][0].strip()
                                    if isinstance(result[i][0], str)
                                    else result[i][0]
                                ) *
                                wage_multiplier *
                                1000
                            )

                        # Parse M to Integer
                        elif "M" in result[i][0]:
                            # print(str(result[i][0]), flush=True)
                            result[i][0] = (
                                result[i][0]
                                .replace("M", "")
                                .strip()
                            )

                            # Convert to number
                            result[i][0] = decimal.Decimal(
                                decimal.Decimal(
                                    result[i][0].strip()
                                    if isinstance(result[i][0], str)
                                    else result[i][0]
                                ) *
                                wage_multiplier *
                                1000000
                            )

                        else:
                            # print("trace: " + result[i][0] +
                            #       " wage: " + str(wage_multiplier))
                            if ',' in result[i][0]:
                                result[i][0] = (result[i][0]
                                                .replace(',', '')
                                                .strip())

                            result[i][0] = decimal.Decimal(
                                decimal.Decimal(
                                    result[i][0].strip()
                                    if isinstance(result[i][0], str)
                                    else result[i][0]
                                ) *
                                wage_multiplier
                            )

                        result[i] = {
                            'currency': current_currency,

                            'min_salary': convert_str_to_int(
                                result[i][0].strip()
                                if isinstance(result[i][0], str)
                                else result[i][0]
                            ) if not maximum_found else 0,

                            'max_salary': convert_str_to_int(
                                result[i][0].strip()
                                if isinstance(result[i][0], str)
                                else result[i][0]
                            ) if maximum_found else convert_str_to_int(
                                result[i][0].strip()
                                if isinstance(result[i][0], str)
                                else result[i][0]
                            ),
                        }

                    elif len(result[i]) == 2:
                        current_currency = '?'

                        # Currency parsing
                        if ("$" in result[i][0] and
                                "$" in result[i][1]):
                            result[i][0] = (
                                result[i][0]
                                .replace("$", "")
                                .strip()
                            )

                            result[i][1] = (
                                result[i][1]
                                .replace("$", "")
                                .strip()
                            )

                            current_currency = "USD"

                        wage_multiplier = 1

                        for j in range(len(result[i])):
                            if " + bonus, stock" in result[i][j].lower():
                                result[i][j] = (
                                    result[i][j]
                                    .replace(" + Bonus, Stock", "")
                                    .replace(" + Bonus, stock", "")
                                    .replace(" + bonus, Stock", "")
                                    .replace(" + bonus, stock", "")
                                    .strip()
                                )

                            if " + bonus" in result[i][j].lower():
                                result[i][j] = (
                                    result[i][j]
                                    .replace(" + Bonus", "")
                                    .replace(" + bonus", "")
                                    .strip()
                                )

                            if " + profit sharing" in result[i][j].lower():
                                result[i][j] = (
                                    result[i][j]
                                    .replace(" + Profit Sharing", "")
                                    .replace(" + Profit sharing", "")
                                    .replace(" + profit Sharing", "")
                                    .replace(" + profit sharing", "")
                                    .strip()
                                )

                            if ", stock options" in result[i][j].lower():
                                result[i][j] = (
                                    result[i][j]
                                    .replace(", Stock Options", "")
                                    .replace(", Stock options", "")
                                    .replace(", stock Options", "")
                                    .replace(", stock options", "")
                                    .strip()
                                )

                            if ", sign" in result[i][j].lower():
                                result[i][j] = (
                                    result[i][j]
                                    .replace(", Sign", "")
                                    .replace(", sign", "")
                                    .strip()
                                )

                            if "+ stock options" in result[i][j].lower():
                                result[i][j] = (
                                    result[i][j]
                                    .replace("+ Stock Options", "")
                                    .replace("+ Stock options", "")
                                    .replace("+ stock Options", "")
                                    .replace("+ stock options", "")
                                    .strip()
                                )

                            if ", profit sharing" in result[i][j].lower():
                                result[i][j] = (
                                    result[i][j]
                                    .replace(", Profit Sharing", "")
                                    .replace(", Profit sharing", "")
                                    .replace(", profit Sharing", "")
                                    .replace(", profit sharing", "")
                                    .strip()
                                )

                            if ", commission" in result[i][j].lower():
                                result[i][j] = (
                                    result[i][j]
                                    .replace(", Commission", "")
                                    .replace(", commission", "")
                                    .strip()
                                )

                        if ("/yr" in result[i][0] and
                                "/yr" in result[i][1]):

                            result[i][0] = (
                                result[i][0]
                                .replace("/yr", "")
                                .strip()
                            )
                            result[i][1] = (
                                result[i][1]
                                .replace("/yr", "")
                                .strip()
                            )
                            wage_multiplier = 1

                        elif ('/hr' in result[i][0] and
                              '/hr' in result[i][1]):
                            result[i][0] = (
                                result[i][0]
                                .replace("/hr", "")
                                .strip()
                            )
                            result[i][1] = (
                                result[i][1]
                                .replace("/hr", "")
                                .strip()
                            )
                            wage_multiplier = 2080

                        # Extra string cleanup
                        if "+" in result[i][0]:
                            result[i][0] = result[i][0][:(
                                result[i][0].find("+"))].strip()

                        if "+" in result[i][1]:
                            result[i][1] = result[i][1][:(
                                result[i][1].find("+"))].strip()

                        if "from" in result[i][0].lower():
                            result[i][0] = (
                                result[i][0]
                                .replace("from", "")
                                .replace("From", "")
                                .strip()
                            )

                        # Parse From to Integer
                        if "to" in result[i][1].lower():
                            result[i][1] = (
                                result[i][1]
                                .replace("to", "")
                                .replace("To", "")
                                .strip()
                            )

                        # Parse K to Integer
                        if "K" in result[i][0]:
                            result[i][0] = (
                                result[i][0]
                                .replace("K", "")
                                .strip()
                            )

                            # Convert to number
                            result[i][0] = convert_str_to_int(
                                Decimal(
                                    result[i][0].strip()
                                    if isinstance(result[i][0], str)
                                    else result[i][0]
                                ) * 1000)

                        # Parse M to Integer
                        elif "M" in result[i][0]:
                            result[i][0] = (
                                result[i][0]
                                .replace("M", "")
                                .strip()
                            )

                            # Convert to number
                            result[i][0] = convert_str_to_int(
                                Decimal(
                                    result[i][0].strip()
                                    if isinstance(result[i][0], str)
                                    else result[i][0]
                                ) * 1000000)

                        else:
                            # Convert to number
                            # print(result[i][0])

                            # Strip comma from number
                            result[i][0] = result[i][0].replace(',', '').strip()

                            result[i][0] = convert_str_to_int(
                                Decimal(
                                    result[i][0].strip()
                                    if isinstance(result[i][0], str)
                                    else result[i][0]
                                )
                            )

                        # Parse K to Integer
                        if "K" in result[i][1]:
                            result[i][1] = (
                                result[i][1]
                                .replace("K", "")
                                .strip()
                            )

                            # Convert to number
                            result[i][1] = convert_str_to_int(
                                Decimal(
                                    result[i][1].strip()
                                    if isinstance(result[i][1], str)
                                    else result[i][1]
                                ) * 1000)

                        # Parse K to Integer
                        elif "M" in result[i][1]:
                            result[i][1] = (
                                result[i][1]
                                .replace("M", "")
                                .strip()
                            )

                            # Convert to number
                            result[i][1] = convert_str_to_int(
                                Decimal(
                                    result[i][1].strip()
                                    if isinstance(result[i][1], str)
                                    else result[i][1]
                                ) * 1000000)

                        else:
                            # Convert to number
                            # Strip comma from number
                            result[i][1] = result[i][1].replace(',', '').strip()
                            result[i][1] = convert_str_to_int(
                                result[i][1].strip()
                                if isinstance(result[i][1], str)
                                else result[i][1]
                            )

                        result[i] = {
                            'currency': current_currency,

                            'min_salary': convert_str_to_int(
                                Decimal(
                                    result[i][0]
                                    if isinstance(result[i][0], str)
                                    else result[i][0]
                                ) * wage_multiplier),

                            'max_salary': convert_str_to_int(
                                Decimal(
                                    result[i][1]
                                    if isinstance(result[i][1], str)
                                    else result[i][1]
                                ) * wage_multiplier)
                            if result[i][1] != 0
                            else convert_str_to_int(
                                Decimal(
                                    result[i][0]
                                    if isinstance(result[i][0], str)
                                    else result[i][0]
                                ) * wage_multiplier)
                            if result[i][0] != 0
                            else 0,
                        }

                return result

        # jaypat87 | Indeed
        # Search
        case ("https://indeed11.p.rapidapi.com"
              "/"):
            if nice_name == "Search":
                return (
                    {
                        "error":
                            "Data from API does not include "
                            "appropriate data. Each page must "
                            "be queried individually."
                    }
                )

        # jaypat87 | Job Search
        # Jobs Search
        # Job Description Full-Text
        case ("https://job-search15.p.rapidapi.com"
              "/"):
            if nice_name == "Jobs Search":
                return (
                    {
                        "error":
                            "Data from API does not include "
                            "appropriate data. Each page must "
                            "be queried individually."
                    }
                )

            elif nice_name == "Job Description Full-Text":
                # This should be derived from the Jobs Search endpoint while
                # retrieving the ID.
                return (
                    {
                        "error":
                            "Data from API does not include "
                            "appropriate data. Each page must "
                            "be queried individually."
                    }
                )

        # jaypat87 | Linkedin Jobs Search
        # Search
        case ("https://linkedin-jobs-search.p.rapidapi.com"
              "/"):
            if nice_name == "Search":
                return (
                    {
                        "error":
                            "Data from API does not include "
                            "appropriate data. Each page must "
                            "be queried individually."
                    }
                )

        # jobicy | Remote Jobs API
        # Remote Jobs API
        case ("https://jobicy.p.rapidapi.com"
              "/api/v2/remote-jobs"):
            if nice_name == "Remote Jobs API":
                if (dict_new.get('success', None) is not None and
                        dict_new.get('success', False) is False):
                    return (
                        {
                            "error":
                                "Query was not processed"
                        }
                    )

                result = (
                    extract_values_from_dict(
                        key_names=[
                            'salaryCurrency',
                            'annualSalaryMin',
                            'annualSalaryMax'
                        ],
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if (i is None or
                            result[i] is None):
                        result[i] = {}
                        continue

                    if (result[i][0] is None and
                            (result[i][1] is None or
                             len(result[i][1]) == 0) and
                            (result[i][2] is None or
                             len(result[i][2]) == 0)):
                        result[i] = {}
                        continue

                    for k, j in enumerate(result[i]):
                        if j == '0':
                            result[i][k] = {}
                            continue

                    result[i] = {
                        'currency': result[i][0],

                        'min_salary':
                            convert_str_to_int(
                                result[i][1].strip()
                                if isinstance(result[i][1], str)
                                else result[i][1]
                            ) if (result[i][1] is not None and
                                  len(result[i][1]) != 0)
                            else 0,

                        'max_salary':
                            convert_str_to_int(
                                result[i][2].strip()
                                if isinstance(result[i][2], str)
                                else result[i][2]
                            ) if (result[i][2] is not None and
                                  len(result[i][2]) != 0)
                            else convert_str_to_int(
                                result[i][1].strip()
                                if isinstance(result[i][1], str)
                                else result[i][1]
                            ) if (result[i][1] is not None and
                                  len(result[i][1]) != 0) else 0,
                    }

                return result

        # jobisite | Job Search
        # Search Jobs
        case ("https://job-search38.p.rapidapi.com"
              "/my/searchJobs"):
            if nice_name == "Search Jobs":
                return (
                    {
                        "error":
                            "Data from API does not include "
                            "appropriate data. Each page must "
                            "be queried individually."
                    }
                )

        # JobsAPI2020 | Zambian Jobs API
        # httpsJobapiCoUkGet
        case ("https://zambian-jobs-api1.p.rapidapi.com"
              "/getdataNew.php"):
            if nice_name == "httpsJobapiCoUkGet":
                return (
                    {
                        "error":
                            "Data from API does not include "
                            "appropriate data. Each page must "
                            "be queried individually."
                    }
                )

        # Jobwiz | Job Search API
        # searchJob
        case ("https://job-search-api1.p.rapidapi.com"
              "/v1/job-description-search"):
            if nice_name == "searchJob":
                result = (
                    extract_value_from_dict(
                        key_name="salary",
                        dict_new=dict_new
                    )
                )

                new_result = {}
                for i in result.keys():
                    if result[i] is not None:
                        result[i] = ast.literal_eval(result[i])
                        new_min_salary = None
                        new_max_salary = None
                        current_currency = '?'

                        if result[i].get('salary_type') is not None:
                            if (result[i].get('salary_type').lower()
                                    == 'hourly'):
                                new_min_salary = result[i].get('min_salary')

                                if new_min_salary is not None:
                                    # 40 * 52
                                    new_min_salary = convert_str_to_int(
                                        Decimal(
                                            new_min_salary.strip()
                                            if isinstance(new_min_salary, str)
                                            else new_min_salary
                                        ) * 2080)

                                new_max_salary = result[i].get('max_salary')

                                if new_max_salary is not None:
                                    # 40 * 52
                                    new_max_salary = convert_str_to_int(
                                        Decimal(
                                            new_max_salary.strip()
                                            if isinstance(new_max_salary, str)
                                            else new_max_salary
                                        ) * 2080)

                            elif (result[i].get('salary_type').lower() ==
                                  'yearly'):
                                new_min_salary = result[i].get('min_salary')
                                new_max_salary = result[i].get('max_salary')

                        if result[i].get('currency') is not None:
                            selected_currency = result[i].get('currency')

                            if ('USD' in selected_currency or
                                    'US' in selected_currency or
                                    '$' in selected_currency):
                                current_currency = '$'

                        new_result[i] = {
                            'currency': current_currency,
                            'min_salary': new_min_salary,
                            'max_salary': new_max_salary,
                        }

                    else:
                        new_result[i] = {
                            'currency': None,
                            'min_salary': None,
                            'max_salary': None,
                        }

                return new_result

        # letscrape | Job Salary Data
        # Job Salary
        case ("https://job-salary-data.p.rapidapi.com"
              "/job-salary"):
            if nice_name == "Job Salary":
                new_result = {}

                for i in dict_new.keys():
                    if dict_new[i] is not None:
                        new_result[i] = [
                            dict_new[i].get('salary_currency', None),
                            dict_new[i].get('min_salary', None),
                            dict_new[i].get('median_salary', None),
                            dict_new[i].get('max_salary', None),
                            dict_new[i].get('salary_period', None),
                        ]

                    else:
                        new_result[i] = ['', '', '', '', '']

                return new_result

        # letscrape | JSearch
        # Search
        case ("https://jsearch.p.rapidapi.com"
              "/search"):
            if nice_name == "Search":
                new_result = {}

                for i in dict_new.keys():
                    # print(dict_new[i], flush=True)
                    if dict_new[i] is not None:
                        if (dict_new[i].get('job_salary_currency') is None and
                                dict_new[i].get('job_min_salary') is None and
                                dict_new[i].get('job_max_salary') is None and
                                dict_new[i].get('job_salary_period') is None):
                            new_result[i] = {}

                        else:
                            salary = dict_new[i].get('job_salary_period')

                            min_salary = dict_new[i].get('job_min_salary', 0)
                            max_salary = dict_new[i].get('job_max_salary', 0)

                            if salary == "HOUR":
                                min_salary = convert_str_to_int(
                                    Decimal(
                                        min_salary.strip()
                                        if isinstance(min_salary, str)
                                        else min_salary) * 2080)

                                max_salary = convert_str_to_int(
                                    Decimal(
                                        max_salary.strip()
                                        if isinstance(max_salary, str)
                                        else max_salary) * 2080)

                            elif salary == "MONTH":
                                min_salary = convert_str_to_int(
                                    Decimal(
                                        min_salary.strip()
                                        if isinstance(min_salary, str)
                                        else min_salary) * 12)

                                max_salary = convert_str_to_int(
                                    Decimal(
                                        max_salary.strip()
                                        if isinstance(max_salary, str)
                                        else max_salary) * 12)

                            # print("Job Salary Period? " + str(salary),
                            #       flush=True)
                            new_result[i] = {
                                'currency':
                                    dict_new[i].get('job_salary_currency', '?'),

                                'min_salary':
                                    convert_str_to_int(
                                        min_salary.strip()
                                        if isinstance(min_salary, str)
                                        else min_salary
                                    ),

                                'max_salary':
                                    convert_str_to_int(
                                        max_salary.strip()
                                        if isinstance(max_salary, str)
                                        else max_salary
                                    )
                            }

                    else:
                        new_result[i] = {}

                return new_result

        # letscrape | JSearch
        # Search Filters
        case ("https://jsearch.p.rapidapi.com"
              "/search-filters"):
            if nice_name == "Search Filters":
                return (
                    {
                        "error":
                            "Data does not include any salaries."
                    }
                )

        # letscrape | JSearch
        # Job Details
        case ("https://jsearch.p.rapidapi.com"
              "/job-details"):
            if nice_name == "Job Details":
                result = (
                    extract_value_from_dict(
                        key_name="estimated_salaries",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    result[i] = ast.literal_eval(result[i])[0]

                    if isinstance(result[i], dict):
                        # print(result[i], flush=True)
                        if result[i] is not None:
                            if (result[i].get('salary_currency') is None and
                                    result[i].get('min_salary') is None and
                                    result[i].get('median_salary') is None and
                                    result[i].get('max_salary') is None):
                                result[i] = {}

                            else:
                                salary = result[i].get('salary_currency')

                                min_salary = result[i].get('min_salary', 0)

                                median_salary = (
                                    result[i].get('median_salary', 0)
                                )

                                max_salary = result[i].get('max_salary', 0)

                                if (min_salary == 0 and
                                        median_salary != 0):
                                    min_salary = median_salary

                                if (max_salary == 0 and
                                        median_salary != 0):
                                    max_salary = median_salary

                                result[i] = {
                                    'currency':
                                        salary,

                                    'min_salary':
                                        int(
                                            min_salary.strip()
                                            if isinstance(min_salary, str)
                                            else min_salary
                                        ),

                                    'max_salary':
                                        int(
                                            max_salary.strip()
                                            if isinstance(max_salary, str)
                                            else max_salary
                                        )
                                }

                    else:
                        result[i] = {}

                return result

        # letscrape | Real-Time Glassdoor Data
        # Company Search
        case ("https://real-time-glassdoor-data.p.rapidapi.com"
              "/company-search"):
            if nice_name == "Company Search":
                return (
                    {
                        "error":
                            "Data does not include any specific salaries."
                    }
                )

        # letscrape | Real-Time Glassdoor Data
        # Company Reviews
        case ("https://real-time-glassdoor-data.p.rapidapi.com"
              "/company-reviews"):
            if nice_name == "Company Reviews":
                return (
                    {
                        "error":
                            "Data does not include any specific salaries."
                    }
                )

        # letscrape | Real-Time Glassdoor Data
        # Company Overview
        case ("https://real-time-glassdoor-data.p.rapidapi.com"
              "/company-overview"):
            if nice_name == "Company Overview":
                return (
                    {
                        "error":
                            "Data does not include any specific salaries."
                    }
                )

        # Lundehund | Twitter X Job API
        # Get Job Detail
        case ("https://twitter-x-api.p.rapidapi.com"
              "/api/job/detail"):
            if nice_name == "Get Job Detail":
                return (
                    {
                        "error":
                            "Data does not include any specific salaries."
                    }
                )

        # Lundehund | Twitter X Job API
        # Search Job
        case ("https://twitter-x-api.p.rapidapi.com"
              "/api/job/search"):
            if nice_name == "Search Job":
                return (
                    {
                        "error":
                            "Data does not include any specific salaries."
                    }
                )

        # Lundehund | Twitter X Job API
        # Search Location
        case ("https://twitter-x-api.p.rapidapi.com"
              "/api/job/search/location"):
            if nice_name == "Search Location":
                return (
                    {
                        "error":
                            "Salaries not in Search location queries."
                    }
                )

        # mantiks | Glassdoor
        # Companies Search
        case ("https://glassdoor.p.rapidapi.com"
              "/companies/search"):
            if nice_name == "Companies Search":
                return (
                    {
                        "error":
                            "Data does not include any specific salaries."
                    }
                )

        # mantiks | Glassdoor
        # Company details
        case ("https://glassdoor.p.rapidapi.com"
              "/company/"):
            if nice_name == "Company Details":
                return (
                    {
                        "error":
                            "Endpoint is disabled."
                    }
                )

        # mantiks | Glassdoor
        # Job details
        case ("https://glassdoor.p.rapidapi.com"
              "/job/"):
            if nice_name == "Job details":
                dict_new = {
                    input_json.get('job_id'):
                        dict_new
                }

                result = {
                    str(input_json.get('job_id')): (
                        dict_new[str(input_json.get('job_id'))].get('salary')
                    )
                }

                if (result[str(input_json.get('job_id'))] is not None and
                        isinstance(
                            result[str(input_json.get('job_id'))],
                            dict)):
                    currency = (
                        result[str(input_json.get('job_id'))].get(
                            'currency', '?')
                    )

                    min_salary = (
                        convert_str_to_int(
                            result[str(input_json.get('job_id'))]
                            .get('min', 0)
                            .strip()
                        )
                    )

                    max_salary = (
                        convert_str_to_int(
                            result[str(input_json.get('job_id'))]
                            .get('max', 0)
                            .strip()
                        )
                    )

                    salary_type = (
                        result[str(input_json.get('job_id'))].get('type')
                    )

                    if salary_type == "ANNUAL":
                        pass

                    else:
                        raise ValueError(
                            "Unhandled salary type: " + str(salary_type))

                    # print("type? " + str(salary_type), flush=True)
                    result[str(input_json.get('job_id'))] = {
                        'currency': currency,
                        'min_salary': min_salary,
                        'max_salary': max_salary
                    }

                else:
                    result[str(input_json.get('job_id'))] = {}

                return result

        # mantiks | Glassdoor
        # Jobs Search
        case ("https://glassdoor.p.rapidapi.com"
              "/jobs/search"):
            if nice_name == "Jobs Search":
                return (
                    {
                        "error":
                            "Data does not include any specific salaries."
                    }
                )

        # mantiks | Glassdoor
        # Locations Search
        case ("https://glassdoor.p.rapidapi.com"
              "/locations/search"):
            if nice_name == "Locations Search":
                return (
                    {
                        "error":
                            "Salaries not listed in Search location "
                            "queries."
                    }
                )

        # mantiks | Indeed
        # Job details
        case ("https://indeed12.p.rapidapi.com"
              "/job/"):
            if nice_name == "Job details":
                return (
                    {
                        "error":
                            "Data does not include any specific salaries."
                    }
                )

        # mantiks | Indeed
        # Jobs Search
        case ("https://indeed12.p.rapidapi.com"
              "/jobs/search"):
            if nice_name == "Jobs Search":
                result = (
                    extract_value_from_dict(
                        key_name='salary',
                        dict_new=dict_new
                    )
                )
                for i in result.keys():
                    result[i] = ast.literal_eval(result[i])

                    if isinstance(result[i], dict):
                        salary_type = result[i].get('type')
                        new_min_salary = result[i].get('min', 0)
                        new_max_salary = result[i].get('max', 0)

                        if (salary_type is not None and
                                "hourly" in salary_type.lower()):
                            new_min_salary = convert_str_to_int(
                                Decimal(new_min_salary) * 2080)
                            new_max_salary = convert_str_to_int(
                                Decimal(new_max_salary) * 2080)

                        result[i] = {
                            'currency': "?",
                            'min_salary': convert_str_to_int(new_min_salary),
                            'max_salary': convert_str_to_int(new_max_salary),
                        }

                    else:
                        result[i] = {}

                return result

        # mantiks | Indeed
        # Company Search
        case ("https://indeed12.p.rapidapi.com"
              "/companies/search"):
            if nice_name == "Company Search":
                return (
                    {
                        "error":
                            "Salaries not listed in data from API."
                    }
                )

        # mantiks | Indeed
        # Company details
        # Company jobs
        case ("https://indeed12.p.rapidapi.com"
              "/company/"):
            if nice_name == "Company details":
                return (
                    {
                        "error":
                            "Salaries not listed in data from API."
                    }
                )

            elif nice_name == "Company jobs":
                return (
                    {
                        "error":
                            "Salaries not listed in data from API."
                    }
                )

        # mgujjargamingm | LinkedIn Data Scraper
        # Company Data
        case ("https://linkedin-data-scraper.p.rapidapi.com"
              "/company" |
              "https://linkedin-bulk-data-scraper.p.rapidapi.com"
              "/company"):
            if nice_name == "Company Data":
                return (
                    {
                        "error":
                            "Salaries not listed in data from API."
                    }
                )

        # mgujjargamingm | LinkedIn Data Scraper
        # Company Data (Premium)
        case ("https://linkedin-data-scraper.p.rapidapi.com"
              "/company_pro" |
              "https://linkedin-bulk-data-scraper.p.rapidapi.com"
              "/company_pro"):
            if nice_name == "Company Data (Premium)":
                return (
                    {
                        "error":
                            "Salaries not listed in data from API."
                    }
                )

        # mgujjargamingm | LinkedIn Data Scraper
        # Company data from web-domain /web-domain
        case ("https://linkedin-data-scraper.p.rapidapi.com"
              "/web-domain" |
              "https://linkedin-bulk-data-scraper.p.rapidapi.com"
              "/web-domain"):
            if nice_name == "Company data from web-domain /web-domain":
                if ((dict_new.get('status', None) is not None and
                        dict_new.get('status') == 404) or
                        (dict_new.get('error', None) is not None and
                         dict_new.get('error') == '404 - Company not found')):
                    return (
                        {
                            'error':
                                'Error with query.'
                        }
                    )

                return (
                    {
                        "error":
                            "Salaries not listed in data from API."
                    }
                )

        # mgujjargamingm | LinkedIn Data Scraper
        # Company Jobs
        case ("https://linkedin-data-scraper.p.rapidapi.com"
              "/company_jobs" |
              "https://linkedin-bulk-data-scraper.p.rapidapi.com"
              "/company_jobs"):
            if nice_name == "Company Jobs":
                return (
                    {
                        "error":
                            "Salaries not listed in data from API."
                    }
                )

        # mgujjargamingm | LinkedIn Data Scraper
        # Search Company
        case ("https://linkedin-data-scraper.p.rapidapi.com"
              "/search_company" |
              "https://linkedin-bulk-data-scraper.p.rapidapi.com"
              "/search_company"):
            if nice_name == "Search Company":
                return (
                    {
                        "error":
                            "Endpoint is broken on API."
                    }
                )

        # mgujjargamingm | LinkedIn Data Scraper
        # Search Jobs
        # Search Jobs ( with filters )
        case ("https://linkedin-data-scraper.p.rapidapi.com"
              "/search_jobs"):
            if (nice_name == "Search Jobs ( with filters )" or
                    nice_name == "Search Jobs"):
                if dict_new.get('error', None) is not None:
                    return (
                        {
                            "error":
                                "Search query failed"
                        }
                    )
                return (
                    {
                        "error":
                            "Salaries not listed in data from API."
                    }
                )

        # mgujjargamingm | LinkedIn Bulk Data Scraper
        # Search Jobs
        # Search Jobs ( with filters )
        case ("https://linkedin-bulk-data-scraper.p.rapidapi.com"
              "/search_jobs"):
            if (nice_name == "Search Jobs ( with filters )" or
                    nice_name == "Search Jobs"):
                if dict_new.get('error', None) is not None:
                    return (
                        {
                            "error":
                                "Search query failed"
                        }
                    )
                # Pulled from RockAPI Behavior
                # Differing values depending on update of API data.
                result = {}
                for i in dict_new.keys():
                    result[i] = dict_new[i].get('tertiaryDescription')

                # Convert to list
                for i in result.keys():
                    if (result[i] is None or
                            len(result[i]) == 0):
                        result[i] = {}
                        continue

                    if ('/yr' not in result[i] and
                            '/hr' not in result[i] and
                            'hour' not in result[i] and
                            'annually' not in result[i] and
                            'year' not in result[i]):
                        result[i] = {}
                        continue

                    else:
                        if '·' in result[i]:
                            split_string = result[i].split('·')

                            for j in range(len(split_string)):
                                if ('/hr' in split_string[j] or
                                        'hour' in split_string[j] or
                                        '/yr' in split_string[j] or
                                        'year' in split_string[j] or
                                        'annually' in split_string[j] or
                                        '$' in split_string[j]):
                                    result[i] = split_string[j]

                            # look for dash
                            if '-' in result[i]:
                                result[i] = result[i].split('-')
                                new_list = []

                                for k in range(len(result[i])):
                                    new_list.append(
                                        result[i][k].strip())

                                result[i] = new_list

                            # longer dash
                            elif '—' in result[i]:
                                result[i] = result[i].split('—')
                                new_list = []

                                for k in range(len(result[i])):
                                    new_list.append(
                                        result[i][k].strip())

                                result[i] = new_list

                            else:
                                # Convert to list anyway
                                result[i] = [result[i]]

                        elif '-' in result[i]:
                            result[i] = result[i].split('-')
                            new_list = []

                            for k in range(len(result[i])):
                                new_list.append(
                                    result[i][k].strip())

                            result[i] = new_list

                        # Longer Dash
                        elif '—' in result[i]:
                            result[i] = result[i].split('—')
                            new_list = []

                            for k in range(len(result[i])):
                                new_list.append(
                                    result[i][k].strip())

                            result[i] = new_list

                        else:
                            # Convert to list anyway
                            result[i] = [result[i]]

                # convert to dictionary
                for i in result.keys():
                    if (i is None or
                            result[i] is None or
                            len(result[i]) == 0):
                        result[i] = {}
                        continue

                    else:
                        # print("Processing: " + str(result[i]), flush=True)
                        if not isinstance(result[i], list):
                            raise ValueError(
                                "Not a list - " +
                                str(result[i]) +
                                " debug key :" + str(i)
                            )

                        elif len(result[i]) == 1:
                            current_currency = '?'
                            # Currency parsing
                            if "$" in result[i][0]:
                                result[i][0] = (
                                    result[i][0]
                                    .replace("$", "")
                                    .strip()
                                )
                                current_currency = "USD"

                            wage_multiplier = 0

                            # Parse hourly wage
                            if "/hr" in result[i][0]:
                                result[i][0] = (
                                    result[i][0].replace("/hr", "")
                                    .strip()
                                )

                                # 40 hours * 52 weeks (US Based)
                                wage_multiplier = 2080

                            elif "/yr" in result[i][0]:
                                result[i][0] = (
                                    result[i][0].replace("/yr", "")
                                    .strip()
                                )
                                wage_multiplier = 1

                            maximum_found = False
                            if 'up to' in result[i][0].lower():
                                result[i][0] = (
                                    result[i][0][
                                        result[i][0].lower().find('up to') +
                                        len('up to'):]
                                    .strip()
                                )
                                maximum_found = True

                            if ("from" in result[i][0] or
                                    "From" in result[i][0]):
                                result[i][0] = (
                                    result[i][0]
                                    .replace("from", "")
                                    .replace("From", "")
                                    .strip()
                                )

                            if ("Starting at " in result[i][0] or
                                    "starting at " in result[i][0]):
                                result[i][0] = (
                                    result[i][0]
                                    .replace("Starting at ", "")
                                    .replace("starting at ", "")
                                    .strip()
                                )

                            if (" + Commission" in result[i][0] or
                                    " + commission" in result[i][0]):
                                result[i][0] = (
                                    result[i][0]
                                    .replace(" + Commission", "")
                                    .replace(" + commission", "")
                                    .strip()
                                )

                            if (" + Bonus" in result[i][0] or
                                    " + bonus" in result[i][0]):
                                result[i][0] = (
                                    result[i][0]
                                    .replace(" + Bonus", "")
                                    .replace(" + bonus", "")
                                    .strip()
                                )

                            if (" + Profit sharing" in result[i][0] or
                                    " + profit sharing" in result[i][0]):
                                result[i][0] = (
                                    result[i][0]
                                    .replace(" + Profit sharing", "")
                                    .replace(" + profit sharing", "")
                                    .strip()
                                )

                            if (", Stock options" in result[i][0] or
                                    ", stock options" in result[i][0]):
                                result[i][0] = (
                                    result[i][0]
                                    .replace(", Stock options", "")
                                    .replace(", stock options", "")
                                    .strip()
                                )

                            if (", Sign" in result[i][0] or
                                    ", sign" in result[i][0]):
                                result[i][0] = (
                                    result[i][0]
                                    .replace(", Sign", "")
                                    .replace(", sign", "")
                                    .strip()
                                )

                            if ("+ Stock options" in result[i][0] or
                                    "+ stock options" in result[i][0]):
                                result[i][0] = (
                                    result[i][0]
                                    .replace("+ Stock options", "")
                                    .replace("+ stock options", "")
                                    .strip()
                                )

                            if (", Profit sharing" in result[i][0] or
                                    ", profit sharing" in result[i][0]):
                                result[i][0] = (
                                    result[i][0]
                                    .replace(", Profit sharing", "")
                                    .replace(", profit sharing", "")
                                    .strip()
                                )

                            if (", Commission" in result[i][0] or
                                    ", commission" in result[i][0]):
                                result[i][0] = (
                                    result[i][0]
                                    .replace(", Commission", "")
                                    .replace(", commission", "")
                                    .strip()
                                )

                            # print("Trace1: " + str(result[i][0]), flush=True)

                            # Parse K to Integer
                            if "K" in result[i][0]:
                                # print(result[i][0], flush=True)
                                result[i][0] = result[i][0].replace("K", "")
                                # Convert to number
                                result[i][0] = convert_str_to_int(
                                    Decimal(
                                        result[i][0].strip()
                                    ) *
                                    wage_multiplier *
                                    1000
                                )

                            # print("Trace2: " + str(result[i][0]), flush=True)

                            result[i] = {
                                'currency': current_currency,

                                'min_salary': convert_str_to_int(
                                    result[i][0].strip()
                                    if isinstance(result[i][0], str)
                                    else result[i][0]
                                ) if not maximum_found else 0,

                                'max_salary': convert_str_to_int(
                                    result[i][0].strip()
                                    if isinstance(result[i][0], str)
                                    else result[i][0]
                                ) if maximum_found else 0,
                            }

                        # Fix for longer lists
                        elif len(result[i]) >= 2:
                            current_currency = '?'
                            # Currency parsing
                            if ("$" in result[i][0] and
                                    "$" in result[i][1]):
                                result[i][0] = (
                                    result[i][0]
                                    .replace("$", "")
                                    .strip()
                                )

                                result[i][1] = (
                                    result[i][1]
                                    .replace("$", "")
                                    .strip()
                                )

                                current_currency = "USD"

                            wage_multiplier = 0
                            if ("/yr" in result[i][0] and
                                    "/yr" in result[i][1]):
                                result[i][0] = (
                                    result[i][0]
                                    .replace("/yr", "")
                                    .strip()
                                )

                                result[i][1] = (
                                    result[i][1]
                                    .replace("/yr", "")
                                    .strip()
                                )

                                wage_multiplier = 1

                            elif ('/hr' in result[i][0] and
                                  '/hr' in result[i][1]):
                                result[i][0] = (
                                    result[i][0]
                                    .replace("/hr", "")
                                    .strip()
                                )

                                result[i][1] = (
                                    result[i][1]
                                    .replace("/hr", "")
                                    .strip()
                                )

                                wage_multiplier = 2080

                            # Extra string cleanup
                            if "+" in result[i][0]:
                                result[i][0] = result[i][0][:(
                                    result[i][0].find("+"))].strip()

                            if "+" in result[i][1]:
                                result[i][1] = result[i][1][:(
                                    result[i][1].find("+"))].strip()

                            if ("from" in result[i][0] or
                                    "From" in result[i][0]):
                                result[i][0] = (
                                    result[i][0]
                                    .replace("from", "")
                                    .replace("From", "")
                                    .strip()
                                )

                            if ("To" in result[i][1] or
                                    "to" in result[i][1]):
                                result[i][1] = (
                                    result[i][1]
                                    .replace("to", "")
                                    .replace("To", "")
                                    .strip()
                                )

                            # Parse K to Integer
                            if "K" in result[i][0]:
                                result[i][0] = (
                                    result[i][0]
                                    .replace("K", "")
                                    .strip()
                                )

                                # Convert to number
                                result[i][0] = convert_str_to_int(
                                    Decimal(
                                        result[i][0].strip()
                                        if isinstance(result[i][0], str)
                                        else result[i][0]
                                    ) * 1000)

                            # Parse K to Integer
                            if "K" in result[i][1]:
                                result[i][1] = (
                                    result[i][1]
                                    .replace("K", "")
                                    .strip()
                                )

                                # Convert to number
                                result[i][1] = convert_str_to_int(
                                    Decimal(
                                        result[i][1].strip()
                                        if isinstance(result[i][1], str)
                                        else result[i][1]
                                    ) * 1000
                                )

                            result[i] = {
                                'currency': current_currency,

                                'min_salary': convert_str_to_int(
                                    Decimal(
                                        result[i][0].strip()
                                        if isinstance(result[i][0], str)
                                        else result[i][0]
                                    ) * wage_multiplier),

                                'max_salary': convert_str_to_int(
                                    Decimal(
                                        result[i][1].strip()
                                        if isinstance(result[i][1], str)
                                        else result[i][1]
                                    ) * wage_multiplier),
                            }
                return result

        # mgujjargamingm | LinkedIn Data Scraper
        # Search GeoUrns
        case ("https://linkedin-data-scraper.p.rapidapi.com"
              "/search_geourns" |
              "https://linkedin-bulk-data-scraper.p.rapidapi.com"
              "/search_geourns"):
            if nice_name == "Search GeoUrns":
                # print("Data from API only gives Geo Urns for DB population.",
                #       flush=True)

                return {"error": "Data from API only gives "
                                 "LinkedIn GeoUrns for DB population."}

        # mgujjargamingm | LinkedIn Data Scraper
        # Suggestion Company Size
        case ("https://linkedin-data-scraper.p.rapidapi.com"
              "/suggestion_company_size" |
              "https://linkedin-bulk-data-scraper.p.rapidapi.com"
              "/suggestion_company_size"):
            if nice_name == "Suggestion Company Size":
                # print("Data from API only gives company sizes for "
                #       "DB population.", flush=True)

                return {"error": "Data from API only gives "
                                 "LinkedIn Company Size codes for "
                                 "DB population."}

        # mgujjargamingm | LinkedIn Data Scraper
        # Search Companies With Filters
        case ("https://linkedin-data-scraper.p.rapidapi.com"
              "/search_company_with_filters" |
              "https://linkedin-bulk-data-scraper.p.rapidapi.com"
              "/search_company_with_filters"):
            if nice_name == "Search Companies With Filters":
                # print("Data from API only gives company summaries.",
                #       flush=True)

                return {"error": "Data from API does not give"
                                 " appropriate data. "}

        # mgujjargamingm | LinkedIn Data Scraper
        # Companies
        case ("https://linkedin-data-scraper.p.rapidapi.com"
              "/bulk_companies" |
              "https://linkedin-bulk-data-scraper.p.rapidapi.com"
              "/bulk_companies"):
            if nice_name == "Companies":
                # print("Endpoint is disabled on API.", flush=True)
                return {"error": "Endpoint has been moved to a different API."}

        # omarmohamed0 | Jobs API
        # All remote (Freelance profiles)
        case ("https://freelancer-api.p.rapidapi.com"
              "/api/find-freelancers" |
              "https://freelancer-api.p.rapidapi.com"
              "/api/find-freelancers/"):
            if (nice_name == "Get all freelancers" or
                    nice_name == "Get all freelancers in specific page"):
                result = (
                    extract_value_from_dict(
                        key_name="hourRating",
                        dict_new=dict_new
                    )
                )

                return result

        # omarmohamed0 | Jobs API
        # All remote (Freelance jobs)
        case ("https://freelancer-api.p.rapidapi.com"
              "/api/find-job" |
              "https://freelancer-api.p.rapidapi.com"
              "/api/find-job/"):
            if (nice_name == "Get All Jobs" or
                    nice_name == "Get all jobs in specific page"):
                result = (
                    extract_value_from_dict(
                        key_name="project-price",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if (i is None or
                            result[i] is None):
                        result[i] = {}
                        continue

                    if result[i] == "No Price":
                        result[i] = {}
                        continue

                    # print(str(result[i]), flush=True)
                    current_currency = '?'

                    # Currency parsing
                    if "$" in result[i]:
                        result[i] = (
                            result[i]
                            .replace("$", "")
                            .strip()
                        )
                        current_currency = "USD"

                    if 'Avg Bid' in result[i]:
                        result[i] = (
                            result[i]
                            .replace("Avg Bid", '')
                            .strip()
                        )

                    if '/ hr' in result[i]:
                        result[i] = (
                            result[i]
                            .replace("/ hr", '')
                            .strip()
                        )

                    if '-' in result[i]:
                        result[i] = result[i].split('-')
                        new_list = []

                        for k in range(len(result[i])):
                            new_list.append(
                                result[i][k].strip())

                        result[i] = {
                            'currency': current_currency,
                            'min_salary': convert_str_to_int(
                                result[i][0].strip()
                                if isinstance(result[i][0], str)
                                else result[i][0]
                            ),

                            'max_salary': convert_str_to_int(
                                result[i][1].strip()
                                if isinstance(result[i][1], str)
                                else result[i][1]
                            ),
                        }
                        continue

                    # Longer dash
                    elif '—' in result[i]:
                        result[i] = result[i].split('—')
                        new_list = []

                        for k in range(len(result[i])):
                            new_list.append(
                                result[i][k].strip())

                        result[i] = {
                            'currency': current_currency,
                            'min_salary': convert_str_to_int(
                                result[i][0].strip()
                                if isinstance(result[i][0], str)
                                else result[i][0]
                            ),

                            'max_salary': convert_str_to_int(
                                result[i][1].strip()
                                if isinstance(result[i][1], str)
                                else result[i][1]
                            ),
                        }
                        continue

                    else:
                        result[i] = {
                            'currency': current_currency,

                            'min_salary': convert_str_to_int(
                                result[i].strip()
                                if isinstance(result[i], str)
                                else result[i]
                            ),

                            'max_salary': convert_str_to_int(
                                result[i].strip()
                                if isinstance(result[i], str)
                                else result[i]
                            ),
                        }

                return result

        # Pat92 | Jobs API
        # List Jobs
        case ("https://jobs-api14.p.rapidapi.com"
              "/list"):
            if nice_name == "List Jobs":
                result = (
                    extract_value_from_dict(
                        key_name="salaryRange",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if (i is None or
                            result[i] is None or
                            result[i] == ''):
                        result[i] = {}
                        continue

                    for j in range(len(result[i])):
                        if (result[i][j].encode('utf-8') ==
                                b'\xe2\x80\x93'):
                            result[i] = (result[i][0:j] + '-' +
                                         result[i][j + 1:])

                    # Manual Parser error fix:
                    # USD to CAD error on API
# Key
# NXRpMDJRRW1TWW5GWEY0VUFBQUFBQSUzRCUzRCUzQkNhc2hpZXIlMjBDYW5hZGElMjAlMjAlM0I="
                    if result[i] == "CA$37,440 an hour":
                        result[i] = "$18 per hour"

                    # Fix for Canadian Dollars
                    if "CA$" in result[i]:
                        result[i] = (
                            result[i]
                            .replace("CA$", "CAD ")
                            .strip()
                        )
                    # print(result[i], flush=True)
                    salary_currency = None
                    monthly_salary = False
                    weekly_salary = False
                    daily_salary = False
                    hourly_salary = False

                    if 'year' in result[i]:
                        result[i] = (
                            result[i]
                            .replace('per year', '')
                            .replace('/year', '')
                            .replace('yearly', '')
                            .replace('a year', '')
                            .replace('year', '')
                            .strip()
                        )

                    elif 'month' in result[i].lower():
                        monthly_salary = True
                        result[i] = (
                            result[i]
                            .replace('per month', '')
                            .replace('/month', '')
                            .replace('monthly', '')
                            .replace('a month', '')
                            .replace('month', '')
                            .strip()
                        )

                    elif 'week' in result[i]:
                        weekly_salary = True
                        result[i] = (
                            result[i]
                            .replace('per week', '')
                            .replace('/week', '')
                            .replace('weekly', '')
                            .replace('a week', '')
                            .replace('week', '')
                            .strip()
                        )

                    elif ('day' in result[i] or
                          'daily' in result[i]):
                        daily_salary = True
                        result[i] = (
                            result[i]
                            .replace('per day', '')
                            .replace('a day', '')
                            .replace('/day', '')
                            .replace('day', '')
                            .replace('/daily', '')
                            .replace('daily', '')
                            .strip()
                        )

                    elif 'hour' in result[i]:
                        hourly_salary = True
                        result[i] = (
                            result[i]
                            .replace('per hour', '')
                            .replace('Per hour', '')
                            .replace('Per Hour', '')
                            .replace('PER HOUR', '')
                            .replace('an hour', '')
                            .replace('An hour', '')
                            .replace('an Hour', '')
                            .replace('An Hour', '')
                            .replace('AN HOUR', '')
                            .replace('/hour', '')
                            .replace('/Hour', '')
                            .replace('/HOUR', '')
                            .replace('hourly', '')
                            .replace('Hourly', '')
                            .replace('HOURLY', '')
                            .replace('hour', '')
                            .replace('Hour', '')
                            .replace('HOUR', '')
                            .strip()
                        )

                    three_letter_matches = (
                        re.findall(r'\b['r'A-Z]{3}\b', result[i]))

                    for j in range(len(three_letter_matches)):
                        if len(three_letter_matches[j]) != 0:
                            salary_currency = three_letter_matches[j]
                            result[i] = (
                                result[i]
                                .replace(three_letter_matches[j], '')
                                .strip()
                            )

                    if salary_currency is None:
                        if '$' in result[i]:
                            salary_currency = "USD"
                            result[i] = (
                                result[i]
                                .replace("$", '')
                                .strip()
                            )

                    if '-' in result[i]:
                        result[i] = (
                            result[i]
                            .strip().
                            split('-')
                        )

                        for j in range(len(result[i])):
                            result[i][j] = result[i][j].strip()

                            if ' ' in result[i][j]:
                                result[i][j] = (
                                    result[i][j]
                                    .replace(' ', '')
                                    .strip()
                                )

                            if ',' in result[i][j]:
                                result[i][j] = (
                                    result[i][j]
                                    .replace(',', '')
                                    .strip()
                                )
                    # Longer Dash
                    elif '—' in result[i]:
                        result[i] = (
                            result[i]
                            .strip().
                            split('—')
                        )

                        for j in range(len(result[i])):
                            result[i][j] = result[i][j].strip()

                            if ' ' in result[i][j]:
                                result[i][j] = (
                                    result[i][j]
                                    .replace(' ', '')
                                    .strip()
                                )

                            if ',' in result[i][j]:
                                result[i][j] = (
                                    result[i][j]
                                    .replace(',', '')
                                    .strip()
                                )

                    if ' to ' in result[i]:
                        result[i] = (
                            result[i]
                            .strip()
                            .split(' to ')
                        )

                        for j in range(len(result[i])):
                            result[i][j] = result[i][j].strip()

                            if ' ' in result[i][j]:
                                result[i][j] = (
                                    result[i][j]
                                    .replace(' ', '')
                                    .strip()
                                )

                            if ',' in result[i][j]:
                                result[i][j] = (
                                    result[i][j]
                                    .replace(',', '')
                                    .strip()
                                )

                    # Remove commas
                    if ',' in result[i]:
                        result[i] = (
                            result[i]
                            .replace(',', '')
                            .strip()
                        )

                    if monthly_salary:
                        if isinstance(result[i], list):
                            for j in range(len(result[i])):
                                # print(result[i][j], flush=True)
                                if 'K' in result[i][j]:
                                    result[i][j] = (
                                        result[i][j]
                                        .replace("K", "")
                                        .strip()
                                    )

                                    result[i][j] = convert_str_to_int(
                                        Decimal(
                                            result[i][j].strip()
                                            if isinstance(result[i][j], str)
                                            else result[i][j]
                                        ) * 1000)

                                else:
                                    result[i][j] = convert_str_to_int(
                                        result[i][j].strip()
                                        if isinstance(result[i][j], str)
                                        else result[i][j]
                                    )

                        else:
                            # print("debug " + result[i], flush=True)

                            if 'K' in result[i]:
                                result[i] = (
                                    result[i]
                                    .replace("K", "")
                                    .strip()
                                )

                                result[i] = convert_str_to_int(
                                    Decimal(
                                        result[i].strip()
                                        if isinstance(result[i], str)
                                        else result[i]
                                    ) * 1000)
                            else:
                                result[i] = convert_str_to_int(
                                    Decimal(
                                        result[i].strip()
                                        if isinstance(result[i], str)
                                        else result[i]
                                    ) * 12)

                    elif weekly_salary:
                        if isinstance(result[i], list):
                            for j in range(len(result[i])):
                                if 'K' in result[i][j]:
                                    result[i][j] = (
                                        result[i][j]
                                        .replace("K", "")
                                        .strip()
                                    )
                                    result[i][j] = convert_str_to_int(
                                        Decimal(
                                            result[i][j].strip()
                                            if isinstance(result[i][j], str)
                                            else result[i][j]
                                        ) * 1000
                                    )

                                result[i][j] = convert_str_to_int(
                                    Decimal(
                                        result[i][j].strip()
                                        if isinstance(result[i][j], str)
                                        else result[i][j]
                                    ) * 52)

                        else:
                            if 'K' in result[i]:
                                result[i] = (
                                    result[i]
                                    .replace("K", "")
                                    .strip()
                                )
                                result[i] = convert_str_to_int(
                                    Decimal(
                                        result[i].strip()
                                        if isinstance(result[i], str)
                                        else result[i]
                                    ) * 1000
                                )
                            result[i] = convert_str_to_int(
                                Decimal(
                                    result[i].strip()
                                    if isinstance(result[i], str)
                                    else result[i]
                                ) * 52)

                    elif daily_salary:
                        if isinstance(result[i], list):
                            for j in range(len(result[i])):
                                result[i][j] = convert_str_to_int(
                                    Decimal(
                                        result[i][j].strip()
                                        if isinstance(result[i][j], str)
                                        else result[i][j]
                                    ) * 5 * 52)

                        else:
                            result[i] = convert_str_to_int(
                                Decimal(
                                    result[i].strip()
                                    if isinstance(result[i], str)
                                    else result[i]
                                ) * 5 * 52)

                    elif hourly_salary:
                        if isinstance(result[i], list):
                            for j in range(len(result[i])):
                                # print("Convert " + result[i][j])
                                result[i][j] = convert_str_to_int(
                                    Decimal(
                                        result[i][j].strip()
                                        if isinstance(result[i][j], str)
                                        else result[i][j]
                                    ) * 2080)

                        else:
                            # print("TESTTEST", flush=True)
                            # print(str(result[i]), flush=True)
                            # print("TESTTEST", flush=True)
                            result[i] = convert_str_to_int(
                                Decimal(
                                    result[i].strip()
                                    if isinstance(result[i], str)
                                    else result[i]
                                ) * 2080)

                    else:
                        if isinstance(result[i], list):
                            for j in range(len(result[i])):
                                if 'K' in result[i][j]:
                                    result[i][j] = (
                                        result[i][j]
                                        .replace("K", "")
                                        .strip()
                                    )

                                    result[i][j] = convert_str_to_int(
                                        Decimal(
                                            result[i][j].strip()
                                            if isinstance(result[i][j], str)
                                            else result[i][j]
                                        ) * 1000)

                                else:
                                    result[i][j] = convert_str_to_int(
                                        result[i][j].strip()
                                        if isinstance(result[i][j], str)
                                        else result[i][j]
                                    )

                        else:
                            if 'K' in result[i]:
                                result[i] = (
                                    result[i]
                                    .replace("K", "")
                                    .strip()
                                )

                                result[i] = convert_str_to_int(
                                    Decimal(
                                        result[i].strip()
                                        if isinstance(result[i], str)
                                        else result[i]
                                    ) * 1000)

                            else:
                                result[i] = convert_str_to_int(
                                    result[i].strip()
                                    if isinstance(result[i], str)
                                    else result[i]
                                )

                    new_dict = {
                        'currency': salary_currency,

                        'min_salary': result[i][0]
                        if (isinstance(result[i], list) and
                            len(result[i]) != 0) else 0,

                        'max_salary': result[i][1]
                        if (isinstance(result[i], list) and
                            len(result[i]) > 1) else
                        result[i][0] if (
                                isinstance(result[i], list) and
                                len(result[i]) == 0
                        ) else 0,
                    }

                    result[i] = new_dict

                return result

        # Pat92 | Jobs API
        # Get salary range
        case ("https://jobs-api14.p.rapidapi.com"
              "/salary/getSalaryRange"):
            if nice_name == "Get salary range":
                return dict_new

        # Pat92 | Jobs API
        # Get job titles
        case ("https://jobs-api14.p.rapidapi.com"
              "/salary/getJobTitles"):
            if nice_name == "Get job titles":
                return {
                    "error": "Data from API does not give appropriate data."
                }

        # qurazor1 | Remoote Job Search
        # list_skills_skills_get
        case ("https://remoote-job-search1.p.rapidapi.com"
              "/remoote/skills"):
            if nice_name == "list_skills_skills_get":
                # print("Data from API does not include job title data.",
                #       flush=True)
                return {"error": "Data from API does not include salary data."}

        # qurazor1 | Remoote Job Search
        # list_jobs_jobs_get
        case ("https://remoote-job-search1.p.rapidapi.com"
              "/remoote/jobs"):
            if nice_name == "list_jobs_jobs_get":
                result = (
                    extract_value_from_dict(
                        key_name='salary_range_raw',
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    if (i is None or
                            result[i] is None):
                        result[i] = {}
                        continue

                    salary_currency = None
                    monthly_salary = False
                    weekly_salary = False
                    daily_salary = False
                    hourly_salary = False

                    # DEBUGGING
                    # print("key " + str(i) + ": " + result[i], flush=True)
                    # Both USD and CAD in salary
                    if ("USD" in result[i] and
                            "CAD" in result[i]):
                        # Attempt to keep USD:
                        if result[i].find("USD") > result[i].find("CAD"):
                            result[i] = result[i][result[i].find("USD"):]
                        else:
                            result[i] = result[i][:result[i].find("CAD")-3]
                        # raise ValueError("Debug")
                        # print("key " + str(i) + ": " + result[i], flush=True)

                    # fix for million
                    if " million" in result[i].lower():
                        result[i] = result[i].replace(" million", "000000")

                    if 'per hour' in result[i].lower():
                        result[i] = result[i][:len('per hour') +
                                              result[i].find('per hour')]

                    if ('year' in result[i].lower() or
                            'per-year-salary' in result[i].lower() or
                            'per annum' in result[i].lower() or
                            'per year' in result[i].lower() or
                            'per yr' in result[i].lower() or
                            'annually' in result[i].lower() or
                            'annual' in result[i].lower() or
                            'annum' in result[i].lower() or
                            'Yr' in result[i].lower() or
                            'yr' in result[i].lower() or
                            '+per' in result[i].lower() or
                            '＋per' in result[i].lower() or
                            '➕per' in result[i].lower() or
                            '+per' in result[i].lower()):
                        result[i] = (
                            result[i]
                            .replace('per-year-salary', '')
                            .replace('Per-year-salary', '')
                            .replace('Per-Year-salary', '')
                            .replace('Per-Year-Salary', '')

                            .replace('per year', '')
                            .replace('per Year', '')
                            .replace('Per Year', '')

                            .replace('per annum', '')
                            .replace('Per annum', '')
                            .replace('Per Annum', '')
                            .replace('PER Annum', '')
                            .replace('PER ANNUM', '')

                            .replace('per yr', '')
                            .replace('Per yr', '')
                            .replace('Per Yr', '')
                            .replace('Per YR', '')
                            .replace('PER YR', '')

                            .replace('annum', '')
                            .replace('Annum', '')

                            .replace('annually', '')
                            .replace('Annually', '')
                            .replace('ANNUALLY', '')

                            .replace('annual', '')
                            .replace('Annual', '')
                            .replace('ANNUAL', '')

                            .replace('yearly', '')
                            .replace('Yearly', '')
                            .replace('YEARLY', '')

                            .replace('/year', '')
                            .replace('/Year', '')
                            .replace('/YEAR', '')

                            .replace('a year', '')
                            .replace('A year', '')
                            .replace('A Year', '')
                            .replace('A YEAR', '')

                            .replace('year', '')
                            .replace('Year', '')
                            .replace('YEAR', '')

                            .replace('+per', '')
                            .replace('+Per', '')
                            .replace('+PER', '')

                            .replace('+per', '')
                            .replace('+Per', '')
                            .replace('+PER', '')

                            .replace('＋per', '')
                            .replace('＋Per', '')
                            .replace('＋PER', '')

                            .replace('➕per', '')
                            .replace('➕Per', '')
                            .replace('➕PER', '')

                            .replace('yr', '')
                            .replace('Yr', '')
                            .replace('YR', '')
                            .strip()
                        )

                    elif 'month' in result[i].lower():
                        monthly_salary = True
                        result[i] = (
                            result[i]
                            .replace('per month', '')
                            .replace('/month', '')
                            .replace('monthly', '')
                            .replace('month', '')
                            .strip()
                        )

                    elif 'week' in result[i].lower():
                        weekly_salary = True
                        result[i] = (
                            result[i]
                            .replace('per week', '')
                            .replace('/week', '')
                            .replace('weekly', '')
                            .replace('week', '')
                            .strip()
                        )

                    elif ('day' in result[i].lower() or
                          'daily' in result[i].lower()):
                        daily_salary = True
                        result[i] = (
                            result[i]
                            .replace('per day', '')
                            .replace('/day', '')
                            .replace('day', '')
                            .replace('/daily', '')
                            .replace('daily', '')
                            .strip()
                        )

                    elif ('hour' in result[i].lower() or
                          'hr' in result[i].lower()):
                        hourly_salary = True
                        result[i] = (
                            result[i]
                            .replace('an hour', '')
                            .replace('An hour', '')
                            .replace('An Hour', '')
                            .replace('per hour', '')
                            .replace('Per hour', '')
                            .replace('Per Hour', '')
                            .replace('per Hour', '')
                            .replace('/hour', '')
                            .replace('/Hour', '')
                            .replace('hourly', '')
                            .replace('Hourly', '')
                            .replace('hour', '')
                            .replace('Hour', '')
                            .replace('hr', '')
                            .replace('Hr', '')
                            .strip()
                        )

                    if '(' in result[i].lower():
                        result[i] = (
                            result[i]
                            .replace('(', '')
                            .strip()
                        )

                    if ')' in result[i].lower():
                        result[i] = (
                            result[i]
                            .replace(')', '')
                            .strip()
                        )

                    # Catch exception on value separated by a comma
                    if ',' in result[i].lower():
                        result[i] = (
                            result[i]
                            .replace(',', '')
                            .strip()
                        )

                    if '/-' in result[i].lower():
                        result[i] = (
                            result[i]
                            .replace('/-', '')
                            .strip()
                        )

                    if 'stock equity' in result[i].lower():
                        result[i] = (
                            result[i]
                            .replace('Stock Equity', '')
                            .replace('stock equity', '')
                            .strip()
                        )

                    if 'between' in result[i].lower():
                        result[i] = (
                            result[i]
                            .replace('Between', '')
                            .replace('between', '')
                            .strip()
                        )

                    if 'per period' in result[i].lower():
                        result[i] = (
                            result[i]
                            .replace('Per Period', '')
                            .replace('Per period', '')
                            .replace('per Period', '')
                            .replace('per period', '')
                            .replace('PER PERIOD', '')
                            .strip()
                        )

                    if 'minimum salary of' in result[i].lower():
                        result[i] = (
                            result[i]
                            .replace('minimum salary of', '')

                            .replace('Minimum salary of', '')
                            .replace('minimum Salary of', '')
                            .replace('minimum salary Of', '')

                            .replace('Minimum Salary of', '')
                            .replace('minimum Salary Of', '')
                            .replace('Minimum salary Of', '')

                            .replace('Minimum Salary Of', '')
                            .replace('MINIMUM SALARY OF', '')
                            .strip()
                        )

                    if 'starting at' in result[i].lower():
                        result[i] = (
                            result[i]
                            .replace('Starting At', '')
                            .replace('Starting at', '')
                            .replace('starting At', '')
                            .replace('starting at', '')
                            .replace('STARTING AT', '')
                            .strip()
                        )

                    if 'from' in result[i].lower():
                        result[i] = (
                            result[i]
                            .replace('from', '')
                            .replace('From', '')
                            .replace('FROM', '')
                            .strip()
                        )

                    if 'up to' in result[i].lower():
                        result[i] = (
                            result[i]
                            .replace('Up to', '')
                            .replace('up to', '')
                            .replace('Up To', '')
                            .strip()
                        )

                    if 'payment' in result[i].lower():
                        result[i] = (
                            result[i]
                            .replace('payment', '')
                            .replace('Payment', '')
                            .replace('PAYMENT', '')
                            .strip()
                        )

                    if 'pay' in result[i].lower():
                        result[i] = (
                            result[i]
                            .replace('pay', '')
                            .replace('Pay', '')
                            .replace('PAY', '')
                            .strip()
                        )

                    if 'maximum' in result[i].lower():
                        result[i] = (
                            result[i]
                            .replace('maximum', '')
                            .replace('Maximum', '')
                            .replace('MAXIMUM', '')
                            .strip()
                        )

                    if 'associate product manager:' in result[i].lower():
                        result[i] = (
                            result[i]
                            .replace('associate product manager:', '')
                            .replace('associate product Manager:', '')
                            .replace('associate Product Manager:', '')
                            .replace('Associate Product Manager:', '')
                            .strip()
                        )

                    if 'associate software engineer:' in result[i].lower():
                        result[i] = (
                            result[i]
                            .replace('associate software engineer:', '')
                            .replace('associate software Engineer:', '')
                            .replace('associate Software Engineer:', '')
                            .replace('Associate Software Engineer:', '')
                            .strip()
                        )

                    if 'associate product designer:' in result[i].lower():
                        result[i] = (
                            result[i]
                            .replace('associate product designer:', '')
                            .replace('associate product Designer:', '')
                            .replace('associate Product Designer:', '')
                            .replace('Associate Product Designer:', '')
                            .strip()
                        )

                    if 'up' in result[i].lower():
                        result[i] = (
                            result[i]
                            .replace('Up', '')
                            .replace('up', '')
                            .strip()
                        )

                    if 'bonus' in result[i].lower():
                        result[i] = (
                            result[i]
                            .replace('Bonus', '')
                            .replace('bonus', '')
                            .strip()
                        )

                    if 'net' in result[i].lower():
                        result[i] = (
                            result[i]
                            .replace('net', '')
                            .replace('Net', '')
                            .strip()
                        )

                    if 'gross' in result[i].lower():
                        result[i] = (
                            result[i]
                            .replace('Gross', '')
                            .replace('gross', '')
                            .strip()
                        )

                    if 'salary' in result[i].lower():
                        result[i] = (
                            result[i]
                            .replace('salary', '')
                            .replace('Salary', '')
                            .strip()
                        )

                    if 'base ＋ equity' in result[i].lower():
                        result[i] = (
                            result[i]
                            .replace('base ＋ equity', '')
                            .replace('Base ＋ Equity', '')
                            .strip()
                        )

                    if ' + equity + benefits' in result[i].lower():
                        result[i] = (
                            result[i]
                            .replace(' + equity + benefits', '')
                            .replace(' + Equity + benefits', '')
                            .replace(' + Equity + Benefits', '')
                            .strip()
                        )

                    if 'base + equity' in result[i].lower():
                        result[i] = (
                            result[i]
                            .replace('base + equity', '')
                            .replace('Base + Equity', '')
                            .strip()
                        )

                    if 'base' in result[i].lower():
                        result[i] = (
                            result[i]
                            .replace('base', '')
                            .replace('Base', '')
                            .replace('BASE', '')
                            .strip()
                        )

                    if ', flexible' in result[i].lower():
                        result[i] = (
                            result[i]
                            .replace(', flexible', '')
                            .replace(', Flexible', '')
                            .replace(', FLEXIBLE', '')
                            .strip()
                        )

                    if '/' in result[i]:
                        result[i] = (
                            result[i]
                            .replace('/', '')
                            .strip()
                        )

                    if ('+' in result[i].lower() or
                            '＋' in result[i].lower() or
                            '➕' in result[i].lower()):
                        result[i] = (
                            result[i]
                            .replace('+', '')
                            .replace('＋', '')
                            .replace('➕', '')
                            .strip()
                        )

                    # Todo: add support for all currency symbols listed in
                    # country database.
                    three_letter_matches = (
                        re.findall(r'\b['r'A-Z]{3}\b', result[i]))

                    for j in range(len(three_letter_matches)):
                        if len(three_letter_matches[j]) != 0:
                            # print("SALARY CURRENCY: " +
                            #       str(three_letter_matches[j]))
                            salary_currency = three_letter_matches[j]
                            result[i] = (
                                result[i]
                                .replace(three_letter_matches[j], '')
                                .replace("$", '')
                                .replace("₱", '')
                                .strip()
                            )
                            # print("Found Currency: " + str(salary_currency),
                            #       flush=True)

                    # Secondary check
                    if salary_currency is None:
                        if '$' in result[i]:
                            salary_currency = "USD"
                            result[i] = result[i].replace("$", '').strip()

                        if 'PHP' in result[i] and '₱' in result[i]:
                            salary_currency = "PHP"
                            result[i] = (result[i]
                                         .replace("₱", '')
                                         .replace("₱", '')
                                         .replace("PHP", '')
                                         .strip())

                    # Dash 1
                    if '-' in result[i]:
                        result[i] = result[i].strip().split('-')

                        for j in range(min(2, len(result[i]))):
                            result[i][j] = result[i][j].strip()

                            if ' ' in result[i][j]:
                                result[i][j] = (
                                    result[i][j].replace(' ', '').strip()
                                )

                            if ',' in result[i][j]:
                                result[i][j] = (
                                    result[i][j].replace(',', '').strip()
                                )
                    # Hyphen
                    if '‐' in result[i]:
                        result[i] = result[i].strip().split('‐')

                        for j in range(min(2, len(result[i]))):
                            result[i][j] = result[i][j].strip()

                            if ' ' in result[i][j]:
                                result[i][j] = (
                                    result[i][j].replace(' ', '').strip()
                                )

                            if ',' in result[i][j]:
                                result[i][j] = (
                                    result[i][j].replace(',', '').strip()
                                )

                    # Non-Breaking Hyphen
                    if '‑' in result[i]:
                        result[i] = result[i].strip().split('‑')

                        for j in range(min(2, len(result[i]))):
                            result[i][j] = result[i][j].strip()

                            if ' ' in result[i][j]:
                                result[i][j] = (
                                    result[i][j].replace(' ', '').strip()
                                )

                            if ',' in result[i][j]:
                                result[i][j] = (
                                    result[i][j].replace(',', '').strip()
                                )

                    # Figure Dash
                    if '‒' in result[i]:
                        result[i] = result[i].strip().split('‒')

                        for j in range(min(2, len(result[i]))):
                            result[i][j] = result[i][j].strip()

                            if ' ' in result[i][j]:
                                result[i][j] = (
                                    result[i][j].replace(' ', '').strip()
                                )

                            if ',' in result[i][j]:
                                result[i][j] = (
                                    result[i][j].replace(',', '').strip()
                                )

                    # En Dash
                    if '–' in result[i]:
                        result[i] = result[i].strip().split('–')

                        for j in range(min(2, len(result[i]))):
                            result[i][j] = result[i][j].strip()

                            if ' ' in result[i][j]:
                                result[i][j] = (
                                    result[i][j].replace(' ', '').strip()
                                )

                            if ',' in result[i][j]:
                                result[i][j] = (
                                    result[i][j].replace(',', '').strip()
                                )

                    # Em Dash
                    if '—' in result[i]:
                        result[i] = result[i].strip().split('—')

                        for j in range(min(2, len(result[i]))):
                            result[i][j] = result[i][j].strip()

                            if ' ' in result[i][j]:
                                result[i][j] = (
                                    result[i][j].replace(' ', '').strip()
                                )

                            if ',' in result[i][j]:
                                result[i][j] = (
                                    result[i][j].replace(',', '').strip()
                                )

                    # Horizontal Bar
                    if '―' in result[i]:
                        result[i] = result[i].strip().split('―')

                        for j in range(min(2, len(result[i]))):
                            result[i][j] = result[i][j].strip()

                            if ' ' in result[i][j]:
                                result[i][j] = (
                                    result[i][j].replace(' ', '').strip()
                                )

                            if ',' in result[i][j]:
                                result[i][j] = (
                                    result[i][j].replace(',', '').strip()
                                )

                    if '~' in result[i]:
                        result[i] = result[i].strip().split('~')

                        for j in range(min(2, len(result[i]))):
                            result[i][j] = result[i][j].strip()

                            if ' ' in result[i][j]:
                                result[i][j] = (
                                    result[i][j].replace(' ', '').strip()
                                )

                            if ',' in result[i][j]:
                                result[i][j] = (
                                    result[i][j].replace(',', '').strip()
                                )

                    if ' to ' in result[i]:
                        result[i] = result[i].strip().split(' to ')

                        for j in range(max(2, len(result[i]))):
                            result[i][j] = result[i][j].strip()

                            if ' ' in result[i][j]:
                                result[i][j] = (
                                    result[i][j].replace(' ', '').strip()
                                )

                            if ',' in result[i][j]:
                                result[i][j] = (
                                    result[i][j].replace(',', '').strip()
                                )

                    if ' and ' in result[i]:
                        result[i] = result[i].strip().split(' and ')

                        for j in range(min(2, len(result[i]))):
                            result[i][j] = result[i][j].strip()

                            if ' ' in result[i][j]:
                                result[i][j] = (
                                    result[i][j].replace(' ', '').strip()
                                )

                            if ',' in result[i][j]:
                                result[i][j] = (
                                    result[i][j].replace(',', '').strip()
                                )

                    # Malformed Salary range
                    # Comma and space in between salary ranges
                    # xxx.00, xxxx
                    if '.00, ' in result[i]:
                        result[i] = [
                            result[i][:result[i].find('.00 ') + 3] +
                            result[i][result[i].find('.00 ') + 4:].strip()
                        ]

                        for j in range(min(2, len(result[i]))):
                            result[i][j] = result[i][j].strip()

                            if ' ' in result[i][j]:
                                result[i][j] = (
                                    result[i][j].replace(' ', '').strip()
                                )

                            if ',' in result[i][j]:
                                result[i][j] = (
                                    result[i][j].replace(',', '').strip()
                                )

                    if monthly_salary:
                        if isinstance(result[i], list):
                            for j in range(min(2, len(result[i]))):
                                result[i][j] = convert_str_to_int(
                                    Decimal(
                                        result[i][j].strip()
                                        if isinstance(result[i][j], str)
                                        else result[i][j]
                                    ) * 12)

                        else:
                            result[i] = convert_str_to_int(
                                Decimal(
                                    result[i].strip()
                                    if isinstance(result[i], str)
                                    else result[i]
                                ) * 12)

                    elif weekly_salary:
                        if isinstance(result[i], list):
                            for j in range(min(2, len(result[i]))):
                                result[i][j] = convert_str_to_int(
                                    Decimal(
                                        result[i][j].strip()
                                        if isinstance(result[i][j], str)
                                        else result[i][j]
                                    ) * 52)

                        else:
                            result[i] = convert_str_to_int(
                                Decimal(
                                    result[i].strip()
                                    if isinstance(result[i], str)
                                    else result[i]
                                ) * 52)

                    elif daily_salary:
                        if isinstance(result[i], list):
                            for j in range(min(2, len(result[i]))):
                                result[i][j] = convert_str_to_int(
                                    Decimal(
                                        result[i][j].strip()
                                        if isinstance(result[i][j], str)
                                        else result[i][j]
                                    ) * 5 * 52
                                )

                        else:
                            result[i] = convert_str_to_int(
                                Decimal(
                                    result[i].strip()
                                    if isinstance(result[i], str)
                                    else result[i]
                                ) * 5 * 52)

                    elif hourly_salary:
                        if isinstance(result[i], list):
                            for j in range(min(2, len(result[i]))):
                                # print("trace " + result[i][j], flush=True)
                                result[i][j] = convert_str_to_int(
                                    Decimal(
                                        result[i][j].strip()
                                        if isinstance(result[i][j], str)
                                        else result[i][j]
                                    ) * 2080)

                        else:
                            # print("trace " + result[i], flush=True)

                            # Locate space
                            while result[i].startswith(" "):
                                result[i] = result[i][1:]

                            while result[i].endswith(" "):
                                result[i] = result[i][:-1]

                            if " " in result[i]:
                                result[i] = result[i].strip().split(' ')
                                for j in range(min(2, len(result[i]))):
                                    result[i][j] = result[i][j].strip()

                                    if ' ' in result[i][j]:
                                        result[i][j] = (
                                            result[i][j].replace(
                                                ' ', '').strip()
                                        )

                                    if ',' in result[i][j]:
                                        result[i][j] = (
                                            result[i][j].replace(
                                                ',', '').strip()
                                        )

                                    result[i][j] = convert_str_to_int(
                                        Decimal(
                                            result[i][j].strip()
                                            if isinstance(result[i][j], str)
                                            else result[i][j]
                                        ) * 2080)
                            else:
                                result[i] = convert_str_to_int(
                                    Decimal(
                                        result[i].strip()
                                        if isinstance(result[i], str)
                                        else result[i]
                                    ) * 2080)

                    else:
                        if isinstance(result[i], list):
                            for j in range(min(2, len(result[i]))):
                                if ('K' in result[i][j] or
                                        'k' in result[i][j]):
                                    result[i][j] = (
                                        result[i][j]
                                        .replace("K", "")
                                        .replace("k", "")
                                        .strip()
                                    )

                                    # print(result[i][j], flush=True)
                                    result[i][j] = convert_str_to_int(
                                        Decimal(
                                            result[i][j].strip()
                                            if isinstance(result[i][j], str)
                                            else result[i][j]
                                        ) * 1000)

                                else:
                                    result[i][j] = convert_str_to_int(
                                        result[i][j].strip()
                                        if isinstance(result[i][j], str)
                                        else result[i][j]
                                    )
                        else:
                            if 'k' in result[i].lower():
                                # print(result[i])
                                result[i] = (result[i]
                                             .replace("K", "")
                                             .replace("k", "")
                                             )

                                try:

                                    result[i] = convert_str_to_int(
                                        Decimal(
                                            result[i].strip()
                                            if isinstance(result[i], str)
                                            else result[i]
                                        ) * 1000)
                                # except Exception:
                                #     raise

                                except InvalidOperation:
                                    # Try splitting using space
                                    if ' ' in result[i]:
                                        result[i] = (result[i]
                                                     .strip()
                                                     .split(' '))

                                        for j in range(min(2, len(result[i]))):
                                            result[i][j] = result[i][j].strip()

                                            if ' ' in result[i][j]:
                                                result[i][j] = (
                                                    result[i][j].replace(
                                                        ' ', '').strip())

                                            if ',' in result[i][j]:
                                                result[i][j] = (
                                                    result[i][j].replace(
                                                        ',', '').strip())

                                            result[i][j] = convert_str_to_int(
                                                Decimal(
                                                    result[i][j].strip()
                                                    if isinstance(
                                                        result[i][j], str)
                                                    else result[i][j]
                                                ) * 1000)

                            else:
                                # Locate space
                                while result[i].startswith(" "):
                                    result[i] = result[i][1:]

                                while result[i].endswith(" "):
                                    result[i] = result[i][:-1]

                                if " " in result[i]:
                                    result[i] = result[i].strip().split(' ')
                                    for j in range(min(2, len(result[i]))):
                                        result[i][j] = result[i][j].strip()

                                        if ' ' in result[i][j]:
                                            result[i][j] = (
                                                result[i][j].replace(
                                                    ' ', '').strip()
                                            )

                                        if ',' in result[i][j]:
                                            result[i][j] = (
                                                result[i][j].replace(
                                                    ',', '').strip()
                                            )
                                    if isinstance(result[i], list):
                                        for j in range(min(2, len(result[i]))):
                                            result[i][j] = convert_str_to_int(
                                                result[i][j].strip()
                                                if isinstance(result[i][j], str)
                                                else result[i][j]
                                            )
                                    else:
                                        result[i] = convert_str_to_int(
                                            result[i].strip()
                                            if isinstance(result[i], str)
                                            else result[i]
                                        )

                                else:
                                    result[i] = convert_str_to_int(
                                        result[i].strip()
                                        if isinstance(result[i], str)
                                        else result[i]
                                    )

                    new_dict = {
                        'currency': salary_currency,

                        'min_salary': (
                            convert_str_to_int(
                                result[i][0]
                                if (isinstance(result[i], list) and
                                    len(result[i]) != 0)
                                else 0
                            )
                        ),

                        'max_salary': (
                            convert_str_to_int(
                                result[i][1]
                                if (isinstance(result[i], list) and
                                    len(result[i]) > 1)
                                else result[i][0]

                                if (isinstance(result[i], list) and
                                    len(result[i]) == 0)
                                else 0
                            )
                        ),
                    }

                    if (new_dict.get('min_salary', None) is not None and
                            isinstance(new_dict.get('min_salary'), int) and
                            new_dict.get('min_salary', 0) > 2147483647):
                        print("Parsing Errors (Min Salary)")
                        new_dict['min_salary'] = 0

                    if (new_dict.get('max_salary', None) is not None and
                            isinstance(new_dict.get('max_salary'), int) and
                            new_dict.get('max_salary', 0) > 2147483647):
                        print("Parsing Errors (Max Salary)")
                        new_dict['max_salary'] = 0

                    result[i] = new_dict
                    # print("Final: " + str(result[i]), flush=True)
                return result

        # qurazor1 | Remoote Job Search
        # get_related_jobs_jobs__int_id___related_post
        case ("https://remoote-job-search1.p.rapidapi.com"
              "/remoote/jobs/"):
            if nice_name == "get_related_jobs_jobs__int_id___related_post":
                result = {}
                for i in dict_new.keys():
                    if (i is None or
                            dict_new[i] is None):
                        result[i] = {}
                        continue

                    currency = dict_new[i].get('currency', '?')

                    min_salary = dict_new[i].get('min_salary', 0)

                    if (isinstance(min_salary, str) and
                            '.0' in min_salary):
                        min_salary = min_salary.replace('.0', '').strip()

                    max_salary = dict_new[i].get('max_salary', 0)

                    if (isinstance(max_salary, str) and
                            '.0' in max_salary):
                        max_salary = min_salary.replace('.0', '').strip()

                    if ((min_salary is None or
                         min_salary == 0) and
                            (max_salary is None or
                             max_salary == 0) and
                            (currency is None or
                             currency == "?")):
                        result[i] = {}

                    else:
                        result[i] = {
                            'currency': currency,

                            'min_salary': int(min_salary)
                            if min_salary is not None else 0,

                            'max_salary': int(max_salary),
                        }
                return result

        # qurazor1 | Remoote Job Search
        # list_countries_countries_get
        case ("https://remoote-job-search1.p.rapidapi.com"
              "/remoote/countries"):
            if nice_name == "list_countries_countries_get":
                # print("Data from API does not include salary data.",
                #       flush=True)

                return (
                    {
                        "error":
                            "Data from API does not "
                            "include salary data."
                    }
                )

        # qurazor1 | Remoote Job Search
        # list_titles_titles_get
        case ("https://remoote-job-search1.p.rapidapi.com"
              "/remoote/titles"):
            if nice_name == "list_titles_titles_get":
                return (
                    {
                        "error":
                            "Data from API does not "
                            "include salary data."
                    }
                )

        # Relu Consultancy | Arbeitsagentur
        # Get Token
        case ("https://arbeitsagentur-employement-agency.p.rapidapi.com"
              "/get-token"):
            if nice_name == "Get Token":
                # print("Data from API is used for token generation only",
                #       flush=True)
                return (
                    {
                        "error":
                            "Data from API is used for token"
                            " generation only"
                    }
                )

        # Relu Consultancy | Arbeitsagentur
        # Search Jobs
        case ("https://arbeitsagentur-employement-agency.p.rapidapi.com"
              "/search"):
            if nice_name == "Search Jobs":
                if (dict_new.get('message', None) is not None and
                        dict_new.get('message') == "No job found"):
                    return (
                        {
                            "error":
                                "Search query failed"
                        }
                    )

                return (
                    {
                        "error":
                            "Data from API does not "
                            "include salary data."
                    }
                )

        # Relu Consultancy | Arbeitsagentur
        # Get Token
        case ("https://indeed-scraper-api-germany.p.rapidapi.com"
              "/get-token"):
            if nice_name == "Get Token":
                # print("Data from API is used for token generation only",
                #       flush=True)

                return (
                    {
                        "error":
                            "Data from API is used for token"
                            " generation only"
                    }
                )

        # Relu Consultancy | Indeed Scraper API - Germany
        # Search Jobs
        case ("https://indeed-scraper-api-germany.p.rapidapi.com"
              "/search"):
            if nice_name == "Search Jobs":
                if (dict_new.get('message', None) is not None and
                        dict_new.get('message') == "No job found"):
                    return (
                        {
                            "error":
                                "Search query failed"
                        }
                    )

                return (
                    {
                        "error":
                            "Data from API does not "
                            "include salary data."
                    }
                )

        # Relu Consultancy | Indeed Scraper API - Germany
        # Job View
        case ("https://indeed-scraper-api-germany.p.rapidapi.com"
              "/jobview"):
            if nice_name == "Job View":
                if (dict_new.get('message', None) is not None and
                        (dict_new.get('message') == "No job found" or
                         dict_new.get('message') ==
                         "Parameters validation error")):
                    return (
                        {
                            "error":
                                "Search query failed"
                        }
                    )

                return (
                    {
                        "error":
                            "Data from API does not "
                            "include salary data."
                    }
                )

        # RockAPIs | Linkedin API
        # Search Employees
        case ("https://linkedin-api8.p.rapidapi.com"
              "/search-employees"):
            # This API Provider doesn't like multiple free accounts
            if nice_name == "Search Employees":
                return (
                    {
                        "error":
                            "Data from API does not "
                            "include salary data."
                    }
                )

        # RockAPIs | Linkedin API
        # Get Company Details
        case ("https://linkedin-api8.p.rapidapi.com"
              "/get-company-details"):
            # This API Provider doesn't like multiple free accounts
            if nice_name == "Get Company Details":
                return (
                    {
                        "error":
                            "Data from API doesn't include salary data."
                    }
                )

        # RockAPIs | Linkedin API
        # Get Company By Domain (BETA)
        case ("https://linkedin-api8.p.rapidapi.com"
              "/get-company-by-domain"):
            if nice_name == "Get Company By Domain (BETA)":
                return (
                    {
                        "error":
                            "Data from API doesn't include salary data."
                    }
                )

        # RockAPIs | Linkedin API
        # Get Company Insights [PREMIUM] (Beta)
        case ("https://linkedin-api8.p.rapidapi.com"
              "/get-company-insights"):
            if nice_name == "Get Company Insights [PREMIUM] (Beta)":
                return (
                    {
                        "error":
                            "API keys unavailable to query API."
                    }
                )

        # RockAPIs | Linkedin API
        # Get Company Employees Count
        case ("https://linkedin-api8.p.rapidapi.com"
              "/get-company-employees-count"):
            if nice_name == "Get Company Employees Count":
                return (
                    {
                        "error":
                            "API keys unavailable to query API."
                    }
                )

        # RockAPIs | Linkedin API
        # Get Company Jobs Count
        case ("https://linkedin-api8.p.rapidapi.com"
              "/get-company-jobs-count"):
            if nice_name == "Get Company Jobs Count":
                return (
                    {
                        "error":
                            "API keys unavailable to query API."
                    }
                )

        # RockAPIs | Linkedin API
        # Get Job Details
        case ("https://linkedin-api8.p.rapidapi.com"
              "/get-job-details"):
            if nice_name == "Get Job Details":
                return (
                    {
                        "error":
                            "API keys unavailable to query API."
                    }
                )

        # RockAPIs | Linkedin API
        # RockAPIs | Rapid LinkedIn Data API
        # RockAPIs | Rapid Linkedin Jobs API
        case ("https://rapid-linkedin-jobs-api.p.rapidapi.com"
              "/search-jobs-v2" |
              "https://rapid-linkedin-jobs-api.p.rapidapi.com"
              "/search-jobs" |

              "https://linkedin-api8.p.rapidapi.com"
              "/search-jobs" |
              "https://linkedin-api8.p.rapidapi.com"
              "/search-jobs-v2" |

              "https://linkedin-data-api.p.rapidapi.com"
              "/search-jobs" |
              "https://linkedin-data-api.p.rapidapi.com"
              "/search-jobs-v2"):
            # This API Provider doesn't like multiple free accounts
            if (nice_name == "Search Jobs V2" or
                    nice_name == "Search Jobs"):
                if (str(dict_new) == '''{'message': 'Blocked User. Please \
contact your API provider.'}'''):
                    return (
                        {
                            "error":
                                "Search query failed"
                        }
                    )

                result = (
                    extract_value_from_dict(
                        key_name='benefits',
                        dict_new=dict_new
                    )
                )

                # Convert to list
                for i in result.keys():
                    if (result[i] is None or
                            len(result[i]) == 0):
                        result[i] = {}
                        continue

                    if ('/yr' not in result[i] and
                            '/hr' not in result[i] and
                            'hour' not in result[i] and
                            'year' not in result[i]):
                        result[i] = {}
                        continue

                    else:
                        if '·' in result[i]:
                            split_string = result[i].split('·')
                            for j in range(len(split_string)):
                                if ('/hr' in split_string[j] or
                                        'hour' in split_string[j] or
                                        '/yr' in split_string[j] or
                                        'year' in split_string[j] or
                                        '$' in split_string[j]):
                                    result[i] = split_string[j]

                            # look for dash
                            if '-' in result[i]:
                                result[i] = result[i].split('-')
                                new_list = []

                                for k in range(len(result[i])):
                                    new_list.append(
                                        result[i][k].strip())

                                result[i] = new_list

                            # Longer Dash
                            elif '—' in result[i]:
                                result[i] = result[i].split('—')
                                new_list = []

                                for k in range(len(result[i])):
                                    new_list.append(
                                        result[i][k].strip())

                                result[i] = new_list

                            else:
                                # Convert to list anyway
                                result[i] = [result[i]]

                        elif '-' in result[i]:
                            result[i] = result[i].split('-')
                            new_list = []

                            for k in range(len(result[i])):
                                new_list.append(result[i][k].strip())

                            result[i] = new_list

                        # longer dash
                        elif '—' in result[i]:
                            result[i] = result[i].split('—')
                            new_list = []

                            for k in range(len(result[i])):
                                new_list.append(result[i][k].strip())

                            result[i] = new_list

                        else:
                            # Convert to list anyway
                            result[i] = [result[i]]

                # convert to dictionary
                for i in result.keys():
                    if (i is None or
                            result[i] is None or
                            len(result[i]) == 0):
                        result[i] = {}
                        continue

                    else:
                        # print("Processing: " + str(result[i]), flush=True)
                        if not isinstance(result[i], list):
                            raise ValueError("Not a list - " +
                                             str(result[i]) +
                                             " debug key :" + str(i))

                        elif len(result[i]) == 1:
                            current_currency = '?'
                            # Currency parsing
                            if "$" in result[i][0]:
                                result[i][0] = (
                                    result[i][0].replace("$", "")
                                )
                                current_currency = "USD"

                            wage_multiplier = 0

                            # Parse hourly wage
                            if "/hr" in result[i][0]:
                                result[i][0] = (
                                    result[i][0].replace("/hr", "")
                                )

                                # 40 hours * 52 weeks (US Based)
                                wage_multiplier = 2080

                            elif "/yr" in result[i][0]:
                                result[i][0] = (
                                    result[i][0].replace("/yr", "")
                                )

                                wage_multiplier = 1

                            maximum_found = False

                            if 'up to' in result[i][0].lower():
                                result[i][0] = (
                                    result[i][0][
                                        result[i][0].lower().find('up to') +
                                        len('up to'):]
                                )
                                maximum_found = True

                            if ("from" in result[i][0] or
                                    "From" in result[i][0]):
                                result[i][0] = (
                                    result[i][0]
                                    .replace("from", "")
                                    .replace("From", "")
                                    .strip()
                                )

                            if ("Starting at " in result[i][0] or
                                    "starting at " in result[i][0]):
                                result[i][0] = (
                                    result[i][0]
                                    .replace("Starting at ", "")
                                    .replace("starting at ", "")
                                    .strip()
                                )

                            # print("Trace1: " + str(result[i][0]), flush=True)

                            # Parse K to Integer
                            if "K" in result[i][0]:
                                result[i][0] = result[i][0].replace("K", "")
                                # Convert to number
                                result[i][0] = decimal.Decimal(
                                    decimal.Decimal(result[i][0]) *
                                    wage_multiplier *
                                    1000
                                )

                            # print("Trace2: " + str(result[i][0]), flush=True)

                            result[i] = {
                                'currency': current_currency,
                                'min_salary': convert_str_to_int(
                                    result[i][0])
                                if not maximum_found else 0,
                                'max_salary': convert_str_to_int(result[i][0])
                                if maximum_found else 0,
                            }

                        elif len(result[i]) == 2:
                            current_currency = '?'
                            # Currency parsing
                            if ("$" in result[i][0] and
                                    "$" in result[i][1]):
                                result[i][0] = result[i][0].replace("$", "")
                                result[i][1] = result[i][1].replace("$", "")
                                current_currency = "USD"

                            wage_multiplier = 0
                            if ("/yr" in result[i][0] and
                                    "/yr" in result[i][1]):
                                result[i][0] = result[i][0].replace("/yr", "")
                                result[i][1] = result[i][1].replace("/yr", "")
                                wage_multiplier = 1

                            elif ('/hr' in result[i][0] and
                                  '/hr' in result[i][1]):
                                result[i][0] = result[i][0].replace("/hr", "")
                                result[i][1] = result[i][1].replace("/hr", "")
                                wage_multiplier = 2080

                            # Extra string cleanup
                            if "+" in result[i][0]:
                                result[i][0] = result[i][0][:(
                                    result[i][0].find("+"))].strip()

                            if "+" in result[i][1]:
                                result[i][1] = result[i][1][:(
                                    result[i][1].find("+"))].strip()

                            if ("from" in result[i][0] or
                                    "From" in result[i][0]):
                                result[i][0] = (
                                    result[i][0]
                                    .replace("from", "")
                                    .replace("From", "")
                                    .strip()
                                )

                            if ("To" in result[i][1] or
                                    "to" in result[i][1]):
                                result[i][1] = (
                                    result[i][1]
                                    .replace("to", "")
                                    .replace("To", "")
                                    .strip()
                                )

                            # Parse K to Integer
                            if "K" in result[i][0]:
                                result[i][0] = (
                                    result[i][0]
                                    .replace("K", "")
                                    .strip()
                                )

                                # Convert to number
                                result[i][0] = convert_str_to_int(
                                    Decimal(result[i][0].strip()) * 1000
                                )

                            # Parse K to Integer
                            if "K" in result[i][1]:
                                result[i][1] = (
                                    result[i][1].replace("K", "")
                                )
                                # Convert to number
                                result[i][1] = convert_str_to_int(
                                    Decimal(result[i][1].strip()) * 1000)

                            result[i] = {
                                'currency': current_currency,

                                'min_salary': convert_str_to_int(
                                    Decimal(result[i][0]) * wage_multiplier),

                                'max_salary': convert_str_to_int(
                                    Decimal(result[i][1]) * wage_multiplier),
                            }
                return result

        # RockAPIs | Linkedin API
        # Get Hiring Team
        case ("https://linkedin-api8.p.rapidapi.com"
              "/get-hiring-team"):
            if nice_name == "Get Hiring Team":
                return (
                    {
                        "error":
                            "API keys unavailable to query API."
                    }
                )

        # RockAPIs | Linkedin API
        # Search Locations
        case ("https://linkedin-api8.p.rapidapi.com"
              "/search-locations"):
            if nice_name == "Search Locations":
                return (
                    {
                        "error":
                            "API keys unavailable to query API."
                    }
                )

        # sohailglt | Linkedin Live Data
        # Company Search
        case ("https://linkedin-live-data.p.rapidapi.com"
              "/company-search"):
            if nice_name == "Company Search":
                return (
                    {
                        "error":
                            "Data does not include job salaries."
                    }
                )

        # sohailglt | Linkedin Live Data
        # People Search
        case ("https://linkedin-live-data.p.rapidapi.com"
              "/people-search"):
            if nice_name == "People Search":
                return (
                    {
                        "error":
                            "Unclear data returned from API"
                    }
                )

        # sohailglt | Linkedin Live Data
        # Get Profile Details
        # Get Company Details
        case ("https://linkedin-live-data.p.rapidapi.com"
              "/profile-details"):
            if nice_name == "Get Company Details":
                return (
                    {
                        "error":
                            "Data does not include salaries."
                    }
                )

            elif nice_name == "Get Profile Details":
                return (
                    {
                        "error":
                            "Unclear data returned from API"
                    }
                )

        # sohailglt | Linkedin Live Data
        # Industries List
        case ("https://linkedin-live-data.p.rapidapi.com"
              "/company-industries"):
            if nice_name == "Industries List":
                # print("Data from API is used for Industries List "
                #       "DB generation only", flush=True)

                return (
                    {
                        "error":
                            "Data from API is used for "
                            "Industries List DB generation "
                            "only"
                    }
                )

        # sohailglt | Linkedin Live Data
        # Industries List
        case ("https://linkedin-live-data.p.rapidapi.com"
              "/company-types"):
            if nice_name == "Company Types":
                # print("Data from API is used for Company Types "
                #       "DB generation only", flush=True)

                return (
                    {
                        "error":
                            "Data from API is used for "
                            "Company Types DB generation "
                            "only"
                    }
                )

        # vuesdata | Indeed Jobs API
        # vuesdata | Indeed Jobs - Sweden
        # vuesdata | Indeed Jobs API - Finland
        # vuesdata | Indeed Jobs API - Denmark
        case ("https://indeed-jobs-api.p.rapidapi.com"
              "/indeed-us/" |
              "https://indeed-jobs-api-finland.p.rapidapi.com"
              "/indeed-fi/" |
              "https://indeed-jobs-api-sweden.p.rapidapi.com"
              "/indeed-se/" |
              "https://indeed-jobs-api-denmark.p.rapidapi.com"
              "/indeed-dk/"):
            if nice_name == "SearchJobs":
                error_keyword = '''\
{'Error': "Jobs API returned no data, You have entered'''

                if error_keyword in str(dict_new)[:len(error_keyword)]:
                    return (
                        {
                            "error":
                                "Search query failed"
                        }
                    )

                result = (
                    extract_value_from_dict(
                        key_name="salary",
                        dict_new=dict_new
                    )
                )

                for i in result.keys():
                    # print(result[i], flush=True)
                    if result[i] == 'No Salary Mentioned':
                        result[i] = {}

                    else:
                        current_currency = "?"
                        yearly_salary = False
                        monthly_salary = False
                        daily_salary = False
                        weekly_salary = False

                        # print(result[i], flush=True)
                        # print("list: " + str(isinstance(result[i], list)),
                        #       flush=True)
                        # print("str: " + str(isinstance(result[i], str)),
                        #       flush=True)

                        if "$" in result[i]:
                            current_currency = "$"
                            result[i] = result[i].replace("$", "").strip()

                        if "a year" in result[i].lower():
                            result[i] = (result[i]
                                         .replace("a year", '')
                                         .replace("a Year", '')
                                         .replace("A Year", '')
                                         .strip())
                            yearly_salary = True

                        if "a month" in result[i].lower():
                            result[i] = (
                                result[i]
                                .replace("a month", '')
                                .replace("a Month", '')
                                .replace("A Month", '')
                                .strip()
                            )
                            monthly_salary = True

                        # API Fix
                        # Per class (Generally per hour)
                        if "per class" in result[i].lower():
                            result[i] = (
                                result[i]
                                .replace("per class", '')
                                .replace("Per class", '')
                                .replace("Per Class", '')
                                .strip()
                            )
                            yearly_salary = False

                        if "an hour" in result[i].lower():
                            result[i] = (result[i]
                                         .replace("an hour", '')
                                         .replace("an Hour", '')
                                         .replace("An Hour", '')
                                         .strip())
                            yearly_salary = False

                        maximum_found = False
                        if "up to" in result[i].lower():
                            result[i] = (
                                result[i]
                                .replace("up to", '')
                                .replace("Up to", '')
                                .replace("Up To", '')
                                .strip()
                            )
                            maximum_found = True

                        if "a day" in result[i].lower():
                            result[i] = (result[i]
                                         .replace("a day", '')
                                         .replace("a Day", '')
                                         .replace("A Day", '')
                                         .strip())
                            yearly_salary = False
                            daily_salary = True

                        if "a week" in result[i].lower():
                            result[i] = (result[i]
                                         .replace("a week", '')
                                         .replace("a Week", '')
                                         .replace("A Week", '')
                                         .strip())
                            yearly_salary = False
                            weekly_salary = True

                        if "-" in result[i]:
                            result[i] = result[i].split('-')
                            result[i] = [j.strip() for j in result[i]]

                        if isinstance(result[i], list):
                            for j in range(len(result[i])):
                                if ',' in result[i][j]:
                                    result[i][j] = (
                                        result[i][j].replace(',', '').strip()
                                    )
                        else:
                            if ',' in result[i]:
                                result[i] = result[i].replace(',', '').strip()

                            if "from" in result[i].lower():
                                result[i] = (
                                    result[i]
                                    .replace("from", "")
                                    .replace("From", "")
                                    .replace("FROM", "")
                                    .strip()
                                )
                        # print(str(result[i]), flush=True)

                        result[i] = {
                            'currency': current_currency,

                            'min_salary': convert_str_to_int(
                                Decimal(result[i].strip())
                                if isinstance(result[i], str) else
                                Decimal(result[i][0].strip())
                            ) * (48 if weekly_salary
                                 else 12 if monthly_salary
                                 else 260 if daily_salary
                                 else 2080 if not yearly_salary
                                 else 1),

                            'max_salary': convert_str_to_int(
                                Decimal(result[i])
                                if not isinstance(result[i], list) else
                                Decimal(result[i][1].strip())
                                if len(result[i]) > 1 else
                                Decimal(result[i][0].strip())
                            ) * (48 if weekly_salary
                                 else 12 if monthly_salary
                                 else 260 if daily_salary
                                 else 2080 if not yearly_salary
                                 else 1),
                        }

                        # Parsing Up to (maximum_found)
                        if (maximum_found and
                                (result[i].get('max_salary') is None or
                                 result[i].get('max_salary') == 0) and
                                (result[i].get('min_salary') is not None or
                                 result[i].get('min_salary') != 0)):
                            result[i]['max_salary'] = (
                                result[i].get('min_salary'))
                            result[i]['min_salary'] = 0

                        # Reset currency symbol if no values found
                        if ((result[i].get('min_salary') == 0 or
                             result[i].get('min_salary') is None) and
                                (result[i].get('max_salary') is None or
                                 result[i].get('max_salary') == 0)):
                            result[i] = {
                                'currency': None,
                                'min_salary': None,
                                'max_salary': None
                            }

                return result

        case _:
            print("Unknown API"
                  "\nDebug Info"
                  "\nAPI URL: " + str(api_url) +
                  "\nName: " + str(nice_name), flush=True)
            raise KeyError("Unknown API: " + api_url + " - " + nice_name)


"""

        # TODO
        case (""
              ""):
            if nice_name == "":
                return None
"""
