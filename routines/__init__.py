"""
Utility Functions
extract_value_from_dict
"""
import ast
from datetime import datetime

import pytz


def convert_str_to_datetime_y_m_d_h_m_s_z(datetime_str: str):
    # print(str(datetime_str), flush=True)
    try:
        # Try parsing without fractional seconds
        return datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%SZ').replace(
            tzinfo=pytz.UTC)
    except ValueError:
        # Try parsing with fractional seconds
        return datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S.%fZ').replace(
            tzinfo=pytz.UTC)


def convert_str_to_datetime_y_m_d_h_m_s_f(datetime_str: str):
    return (datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S.%f')
            .replace(tzinfo=pytz.UTC))


def convert_str_to_datetime_gmt_default(datetime_str: str):
    return (datetime.strptime(datetime_str, '%a, %d %b %Y %H:%M:%S GMT')
            .replace(tzinfo=pytz.UTC))


def convert_str_to_datetime_date(datetime_str: str):
    return (datetime.strptime(datetime_str, '%Y-%m-%d')
            .replace(tzinfo=pytz.UTC))


def convert_str_to_datetime_utc_default(datetime_str: str):
    return (datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S %z %Z')
            .replace(tzinfo=pytz.UTC))


# RockAPIs | Linkedin API
# RockAPIs | Rapid LinkedIn Data API
# RockAPIs | Rapid Linkedin Jobs API
def convert_str_to_datetime_utc_extra(datetime_str: str):
    if (datetime_str is None or
            len(datetime_str) == 0):
        return None
    return (datetime.strptime(datetime_str[:-11], '%Y-%m-%d %H:%M:%S')
            .replace(tzinfo=pytz.UTC))


def convert_str_to_datetime_non_us(datetime_str: str):
    if (datetime_str is None or
            len(datetime_str) == 0):
        return None
    return (datetime.strptime(datetime_str, '%d-%m-%y')
            .replace(tzinfo=pytz.UTC))


def convert_str_to_datetime_date_time_only(datetime_str: str):
    if (datetime_str is None or
            len(datetime_str) == 0):
        return None
    return (datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
            .replace(tzinfo=pytz.UTC))


def convert_str_to_datetime_date_time2(datetime_str: str):
    if (datetime_str is None or
            len(datetime_str) == 0):
        return None
    return (datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S')
            .replace(tzinfo=pytz.UTC))


def convert_str_to_datetime_from_iso(datetime_str: str):
    if (datetime_str is None or
            len(datetime_str) == 0):
        return None
    return (datetime.fromisoformat(datetime_str)
            .replace(tzinfo=pytz.UTC))


def extract_value_from_dict(key_name: str, dict_new: dict):
    """
    Returns a dictionary with just the provided key.
    """
    if (dict_new is None or
            not isinstance(dict_new, dict)):
        print("dict_new provided is empty or not a dictionary.", flush=True)
        # print(str(dict_new), flush=True)
        if isinstance(dict_new, str):
            print('dict_new is a string.', flush=True)
        if isinstance(dict_new, list):
            print('dict_new is a list.', flush=True)
        return None
    try:
        if ('error' in dict_new.keys() and
                dict_new.get('error') is not None):
            return {}
        if ('code' in dict_new.keys() and
                len(dict_new.keys()) == 1):
            return {}
        # "{'error': " <-
        # if "{'error': " == str(dict_new).lower()[:len("{'error': ")]:
        #     return {}

        new_dict = {}
        for i in dict_new.keys():
            if (not isinstance(dict_new[i], dict) or
                    key_name not in dict_new[i].keys()):
                continue
            # print(str(i) + " " + str(dict_new[i]), flush=True)
            new_dict[str(i)] = dict_new[i].get(key_name, None)
        return new_dict
    except Exception as e:
        print(str(e), flush=True)
        raise e


def extract_values_from_dict(key_names: list, dict_new: dict):
    """
    Returns a dictionary with just the provided key.
    """
    if (dict_new is None or
            not isinstance(dict_new, dict)):
        print("dict_new provided is empty or not a dictionary.", flush=True)
        # print(str(dict_new))
        if isinstance(dict_new, str):
            print('dict_new is a string.', flush=True)
        if isinstance(dict_new, list):
            print('dict_new is a list.', flush=True)
        return None
    try:
        if ('error' in dict_new.keys() and
                dict_new.get('error') is not None):
            return {}

        new_dict = {}
        for i in dict_new.keys():
            # print(str(i), flush=True)
            new_dict[str(i)] = []
            for j in range(len(key_names)):
                new_list_value = dict_new[i].get(key_names[j], None)
                new_dict[str(i)].append(new_list_value)
        return new_dict
    except Exception as e:
        print(str(e), flush=True)
        raise e


def extract_value_from_list_dict(key_name: str, list_new: list):
    """
    Returns a dictionary with just the provided key.
    The input is a list (K:V pair) but values are a dict.
    """
    try:
        new_dict = {}
        for i in range(len(list_new)):
            # print(str(i), flush=True)
            # print(list_new, flush=True)
            new_dict[str(i)] = list_new[i].get(key_name, None)
        return new_dict
    except Exception as e:
        print(str(e), flush=True)
        raise e


def extract_from_list_dict(key_name: str, list_new: list):
    """
    Returns a list with just the provided key.
    The input is a list of dicts (K:V pair).
    """
    try:
        new_list = []
        for i in range(len(list_new)):
            # print(str(i), flush=True)
            # print(list_new, flush=True)
            new_list.append(list_new[i].get(key_name, None))
        return new_list
    except Exception as e:
        print(str(e), flush=True)
        raise e


def extract_value_from_dict_list(key_name: str, list_new_dict: dict):
    """
    Returns a dictionary with just the provided key_name extracted from a
    list of dictionaries.
    The input is a list of dictionary (K:V pair) but value is a list.
    """
    if (list_new_dict is None or
            not isinstance(list_new_dict, dict)):
        print("list_new provided is empty or not a dict.", flush=True)
        if isinstance(list_new_dict, str):
            print('dict_new is a string.', flush=True)
        if isinstance(list_new_dict, list):
            print('list_new is a list.', flush=True)
        return None
    try:
        if ('error' in list_new_dict.keys() and
                list_new_dict.get('error') is not None):
            return {}

        new_dict = {}
        for i in list_new_dict.keys():
            new_dict[i] = {}
            if (not isinstance(list_new_dict[i], dict) and
                    isinstance(list_new_dict[i], str)):
                list_new_dict[i] = ast.literal_eval(list_new_dict[i])
            # print(str(i), flush=True)
            # print(list_new_dict, flush=True)
            # print(str(list_new_dict[i]), flush=True)
            new_dict[i] = list_new_dict[i][0].get(key_name, None)
        return new_dict
    except Exception as e:
        print(str(e), flush=True)
        raise e


def extract_values_from_dict_list(key_name: str, list_new_dict: list):
    """
    Returns a dictionary with just the provided key.
    The input is a dictionary (K:V pair) within a list but values are a list.
    """
    if (list_new_dict is None or
            not isinstance(list_new_dict, dict)):
        print("list_new provided is empty or not a dict.", flush=True)
        if isinstance(list_new_dict, str):
            print('dict_new is a string.', flush=True)
        if isinstance(list_new_dict, list):
            print('list_new is a list.', flush=True)
        return None
    try:
        if ('error' in list_new_dict.keys() and
                list_new_dict.get('error') is not None):
            return {}

        new_dict = {}
        for i in list_new_dict.keys():
            new_dict[i] = {}
            if (not isinstance(list_new_dict[i], dict) and
                    isinstance(list_new_dict[i], str)):
                list_new_dict[i] = ast.literal_eval(list_new_dict[i])
            for j in range(len(list_new_dict[i])):
                # print(str(i), flush=True)
                # print(list_new_dict, flush=True)
                # print(str(list_new_dict[i]), flush=True)
                new_dict[i][str(j)] = list_new_dict[i][j].get(key_name, None)
        return new_dict
    except Exception as e:
        print(str(e), flush=True)
        raise e


def extract_value_from_dict_nested(
        key_name: str,
        key_name_nested: str,
        dict_new: dict):
    """
    Returns a dictionary with just the provided key.
    """
    # print(str(dict_new), flush=True)
    if (dict_new is None or
            not isinstance(dict_new, dict) or
            len(dict_new) == 0):
        print("dict_new provided is empty or not a dictionary.", flush=True)
        # print(str(dict_new), flush=True)
        if isinstance(dict_new, str):
            print('dict_new is a string.', flush=True)
        elif isinstance(dict_new, list):
            print('dict_new is a list.', flush=True)
        return None
    try:
        if ('error' in dict_new.keys() and
                dict_new.get('error') is not None):
            return {}

        new_dict = {}
        for i in dict_new.keys():
            # print(str(i), flush=True)
            # print('Key Name: ' + key_name, flush=True)
            # print('Dict: ' + str(isinstance(dict_new[i], dict)), flush=True)
            new_dict[str(i)] = dict_new[i].get(key_name, None)
            # print("Key Name: " + key_name + " " + str(new_dict[str(i)]),
            #       flush=True)
            if dict_new[i].get(key_name, None) is not None:
                try:
                    if (new_dict[str(i)] is None or
                            not isinstance(new_dict[str(i)], dict) or
                            len(new_dict[str(i)]) == 0):
                        new_dict[str(i)] = ast.literal_eval(new_dict[str(i)])
                    # print(str(new_dict[str(i)]), flush=True)
                    new_dict[str(i)] = (
                        new_dict[str(i)].get(key_name_nested, None))
                    # print(str(new_dict[str(i)]), flush=True)
                except Exception as e:
                    new_dict[str(i)] = None
                    print(str(e), flush=True)

        return new_dict
    except Exception as e:
        print(str(e), flush=True)
        raise e
