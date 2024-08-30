import math
from decimal import Decimal

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError

from extensions_sql import db
from models.postgres.locations.countries import Country


def convert_salary_currency_to_symbol(salary_currency: str):
    if (salary_currency is None or
            not isinstance(salary_currency, str) or
            len(salary_currency) == 0 or
            salary_currency == '' or
            salary_currency == ' '):
        return None

    # Database methods are enclosed in a try-except block.
    try:
        # Access currency_symbol Table
        return (
            db.session.scalars(
                select(Country.currency_symbol)
                .filter(Country.currency.ilike(salary_currency.lower()))
            ).first()
        )

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.close()
        print(f"IntegrityError: {e}", flush=True)
        return None

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.close()
        print(f"OperationalError: {e}", flush=True)
        return None

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.close()
        print(f"SQLAlchemyError: {e}", flush=True)
        return None

    # Other Errors
    except Exception as e:
        db.session.close()
        print(f"Error: {e}", flush=True)
        return None


def format_with_commas(value):
    """Returns a string with removed .0 if it ends with .0"""
    if not value:
        return ''

    formatted_value = "{:,}".format(value)

    if formatted_value.endswith('.0'):
        formatted_value = formatted_value[:-2]

    return formatted_value


def convert_str_to_int(value):
    """
    Removes decimal places and floors salaries
    Returns an integer and accepts a string.
    """
    # print("Converting " + str(value), flush=True)

    if not value:
        return ''

    if not isinstance(value, str):
        value = str(value)

    if "." in value:
        value: str = value[:value.find('.')]

    if value == '0':
        return 0
    # print(str(value), flush=True)
    value: Decimal = Decimal(value)

    return int(math.floor(value))
