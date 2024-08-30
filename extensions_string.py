import re


def clean_search_string(user_input):
    """
    Remove all non-alphanumeric characters except spaces
    using a regular expression
    """
    if (user_input is None or
            not isinstance(user_input, str) or
            len(user_input) == 0 or
            user_input == ' '):
        return None

    cleaned_string = re.sub(r'[^a-zA-Z0-9-. ]', '', user_input)
    # Strip any leading or trailing whitespace
    cleaned_string = cleaned_string.strip()
    # Replace multiple spaces with a single space
    cleaned_string = re.sub(r'\s+', ' ', cleaned_string)
    return cleaned_string


def clean_location_string(user_input):
    """
    Remove all non-alphanumeric characters except
    spaces, hyphens, periods, commas, apostrophes, slashes, ampersands,
    parentheses, colons, semicolons, plus signs, pound signs,
    and underscores using a regular expression
    """
    if (user_input is None or
            not isinstance(user_input, str) or
            len(user_input) == 0 or
            user_input == ' '):
        return None

    # print("Unclean: " + user_input, flush=True)
    cleaned_string = re.sub(r'[^a-zA-Z0-9-.,\'/&():;+#_ ]', '', user_input)
    # print("Cleaned: " + cleaned_string, flush=True)
    # Strip any leading or trailing whitespace
    cleaned_string = cleaned_string.strip()

    # Replace multiple spaces with a single space
    cleaned_string = re.sub(r'\s+', ' ', cleaned_string)

    return cleaned_string


def clean_unknown_characters(user_input: str):
    """
    Remove replacement characters, null characters, and control characters
    """
    if (user_input is None or
            not isinstance(user_input, str) or
            len(user_input) == 0 or
            user_input == ' '):
        return None

    return re.sub(r'[\uFFFD\u0000-\u001F\u007F]', '', user_input).strip()
