"""
Parsing
Locate Region, Subregion, Country, State, City from string

Trigram Extensions:
CREATE EXTENSION IF NOT EXISTS pg_trgm;

Latitude and Longitude search:
Requires postgresql-16-postgis-3 installed on database system.

CREATE EXTENSION postgis;
CREATE EXTENSION cube;
CREATE EXTENSION earthdistance;
"""
import re

import requests
from sqlalchemy import text

from extensions_sql import db
from sqlalchemy.orm import load_only, selectinload

from models.postgres.locations.cube import Cube
from models.postgres.locations.linkedin_geourn_id import LinkedInGeoURNID
from models.postgres.locations.location import Location
from models.postgres.locations.x_location_id import XLocationID
from models.postgres.locations.glassdoor_location_id import GlassdoorLocationID
from models.postgres.locations.regions import Region
from models.postgres.locations.subregions import Subregion
from models.postgres.locations.countries import Country
from models.postgres.locations.states import State
from models.postgres.locations.cities import City
from secrets_jobs.credentials import pelias_parser_query_url


def find_glassdoor_location_id(glassdoor_location_id: int):
    """
    Find Glassdoor Location by Location_ID searched from API.
    """
    if (glassdoor_location_id is None or
            not isinstance(glassdoor_location_id, int) or
            glassdoor_location_id < 0):
        return None

    found_row: GlassdoorLocationID = db.session.query(
        db.session.query(GlassdoorLocationID.id)
        .filter(GlassdoorLocationID.id == int(glassdoor_location_id)).exists()
    ).scalar()
    return (
        db.session.query(GlassdoorLocationID)
        .filter(GlassdoorLocationID.id == int(glassdoor_location_id))
        .first()
    ) if found_row else None


def find_linkedin_geourn_id(linkedin_id: int):
    """
    Find LinkedIn Location by Location_ID searched from API.
    """
    if (linkedin_id is None or
            not isinstance(linkedin_id, int) or
            linkedin_id < 0):
        return None

    found_row: LinkedInGeoURNID = db.session.query(
        db.session.query(LinkedInGeoURNID.id)
        .filter(LinkedInGeoURNID.id == int(linkedin_id)).exists()
    ).scalar()
    return (
        db.session.query(LinkedInGeoURNID)
        .filter(LinkedInGeoURNID.id == int(linkedin_id))
        .first()
    ) if found_row is not None else None


def find_x_location_id(location_id: int):
    """
    Find X Location by Location_ID searched from API.
    """
    if (location_id is None or
            not isinstance(location_id, int) or
            location_id < 0):
        return None

    found_row: XLocationID = db.session.query(
        db.session.query(XLocationID.id)
        .filter(XLocationID.id == int(location_id)).exists()
    ).scalar()

    return (
        db.session.query(XLocationID)
        .filter(XLocationID.id == int(location_id))
        .first()
    ) if found_row is not None else None


def find_country(country_string: str):
    """
    Search for country three separate ways
    """

    if (country_string is None or
            len(country_string) == 0):
        return None

    # Load best matching State using iLIKE or ISO3/ISO2 search.
    found_country = (
        db.session.query(Country)
        .filter(
            db.or_(
                Country.name.ilike(country_string),
                Country.iso3 == country_string,
                Country.iso2 == country_string
            )
        )
        .options(
            load_only(
                Country.name,
                Country.id,
                Country.iso3,
                Country.iso2,
                Country.latitude,
                Country.longitude,
            ),

            selectinload(Country.subregion)
            .load_only(
                Subregion.id,
                Subregion.name
            ),

            selectinload(Country.region)
            .load_only(
                Region.id,
                Region.name
            )
        ).first()
    )

    if found_country is not None:
        return found_country

    # Load best matching State using text search.
    search_query = db.func.plainto_tsquery('english', country_string)
    found_country = (
        db.session.query(Country)
        .filter(Country.search_vector.op('@@')(search_query))
        .order_by(db.func.ts_rank_cd(
            Country.search_vector,
            search_query).desc())
        .options(
            load_only(
                Country.name,
                Country.id,
                Country.iso3,
                Country.iso2,
                Country.latitude,
                Country.longitude,
            ),

            selectinload(Country.subregion)
            .load_only(
                Subregion.id,
                Subregion.name
            ),

            selectinload(Country.region)
            .load_only(
                Region.id,
                Region.name
            )
        )
        .first()
    )

    if found_country is not None:
        return found_country

    # Load best matching State using trigram search.
    found_country = (
        db.session.query(Country)
        .filter(db.func.similarity(Country.name, country_string) > 0.3)
        .order_by(db.func.similarity(Country.name, country_string).desc())
        .options(
            load_only(
                Country.id,
                Country.name,
                Country.iso3,
                Country.iso2,
                Country.latitude,
                Country.longitude,
            ),

            selectinload(Country.subregion)
            .load_only(
                Subregion.id,
                Subregion.name
            ),

            selectinload(Country.region)
            .load_only(
                Region.id,
                Region.name
            )
        )
        .first()
    )
    if found_country is not None:
        return found_country

    return None


def find_state(
        country_id: int,
        state_string: str,
        regex_letter_code: list,
        delimited_string: list):
    """
    Load best matching State using three different searches.
    """
    if (state_string is None or
            len(state_string) == 0):
        return None

    found_state = (
        db.session.query(State)
        .filter(
            db.or_(
                db.and_(
                    State.name.ilike(state_string),
                    (State.country_id == int(country_id)
                     if (country_id is not None and
                         isinstance(country_id, int) and
                         country_id != -1) else True),
                ),
                db.and_(
                    State.state_code.in_(regex_letter_code)
                    if (regex_letter_code is not None and
                        isinstance(regex_letter_code, list) and
                        len(regex_letter_code) != 0) else False,
                    (State.country_id == int(country_id)
                     if (country_id is not None and
                         isinstance(country_id, int) and
                         country_id != -1) else True),
                ),
                db.and_(
                    db.func.lower(State.name).in_(delimited_string)
                    if (delimited_string is not None and
                        isinstance(delimited_string, list) and
                        len(delimited_string) != 0) else False,
                    (State.country_id == int(country_id)
                     if (country_id is not None and
                         isinstance(country_id, int) and
                         country_id != -1) else True),
                ),
            )
        )
        .options(
            load_only(
                State.id,
                State.name,
                State.latitude,
                State.longitude,
            ),

            selectinload(State.country)
            .load_only(
                Country.id,
                Country.name,
                Country.iso3,
                Country.iso2,
            ),

            selectinload(State.subregion)
            .load_only(
                Subregion.id,
                Subregion.name
            ),

            selectinload(State.region)
            .load_only(
                Region.id,
                Region.name
            )
        )
        .first()
    )
    if found_state is not None:
        return found_state

    # Load best matching State using text search.
    search_query = db.func.plainto_tsquery('english', state_string)
    found_state = (
        db.session.query(State)
        .filter(
            db.and_(
                State.search_vector.op('@@')(search_query),
                (State.country_id == int(country_id)
                 if (country_id is not None and
                     isinstance(country_id, int) and
                     country_id != -1) else True)
            )
        )
        .order_by(db.func.ts_rank_cd(State.search_vector, search_query).desc())
        .options(
            load_only(
                State.id,
                State.name,
                State.latitude,
                State.longitude,
            ),

            selectinload(State.country)
            .load_only(
                Country.id,
                Country.name,
                Country.iso3,
                Country.iso2,
            ),

            selectinload(State.subregion)
            .load_only(
                Subregion.id,
                Subregion.name
            ),

            selectinload(State.region)
            .load_only(
                Region.id,
                Region.name
            )
        )
        .first()
    )

    if found_state is not None:
        return found_state

    found_state = (
        db.session.query(State)
        .filter(
            db.and_(
                db.func.similarity(State.name, state_string) > 0.7,
                (State.country_id == int(country_id)
                 if (country_id is not None and
                     isinstance(country_id, int) and
                     country_id != -1) else True)
            )
        )
        .order_by(
            db.func.similarity(
                State.name,
                state_string
            ).desc()
        )
        .options(
            load_only(
                State.id,
                State.name,
                State.latitude,
                State.longitude,
            ),

            selectinload(State.country)
            .load_only(
                Country.id,
                Country.name,
                Country.iso3,
                Country.iso2,
            ),

            selectinload(State.subregion)
            .load_only(
                Subregion.id,
                Subregion.name
            ),

            selectinload(State.region)
            .load_only(
                Region.id,
                Region.name
            )
        )
        .first()
    )

    if found_state is not None:
        return found_state

    else:
        return None


def find_state_contains(
        country_id: int,
        state_string: str,
        delimited_string: list):
    """
    Load best matching City using contains method
    """
    if (state_string is None or
            len(state_string) == 0):
        return None

    found_state = (
        db.session.query(State)
        .filter(
            db.or_(
                db.and_(
                    db.func.lower(State.name).contains(state_string.lower()),
                    (City.country_id == int(country_id)
                     if (country_id is not None and
                         isinstance(country_id, int) and
                         country_id != -1) else True),
                ),
                db.and_(
                    db.or_(*[db.func.lower(State.name).contains(i.lower())
                             for i in delimited_string]),
                    (City.country_id == int(country_id)
                     if (country_id is not None and
                         isinstance(country_id, int) and
                         country_id != -1) else True),
                ),
            ),
        )
        .options(
            load_only(
                State.id,
                State.name,
                State.state_code,
                State.latitude,
                State.longitude,
            ),

            selectinload(State.country)
            .load_only(
                Country.id,
                Country.name,
                Country.iso3,
                Country.iso2,
            ),

            selectinload(State.subregion)
            .load_only(
                Subregion.id,
                Subregion.name
            ),

            selectinload(State.region)
            .load_only(
                Region.id,
                Region.name
            )
        ).first()
    )

    if found_state is not None:
        return found_state

    else:
        return None


def find_city(
        country_id: int,
        state_id: int,
        city_string: str,
        delimited_string: list):
    """
    Load best matching City using three different searches.
    """
    if (city_string is None or
            len(city_string) == 0):
        return None

    found_city = (
        db.session.query(City)
        .filter(
            db.or_(
                db.and_(
                    City.name.ilike(city_string),
                    (City.country_id == int(country_id)
                     if (country_id is not None and
                         isinstance(country_id, int) and
                         country_id != -1) else True),
                    (City.state_id == int(state_id)
                     if (state_id is not None and
                         isinstance(state_id, int) and
                         state_id != -1) else True)
                ),
                db.and_(
                    db.func.lower(City.name).in_(delimited_string)
                    if (delimited_string is not None and
                        isinstance(delimited_string, list) and
                        len(delimited_string) > 0) else False,
                    (City.country_id == int(country_id)
                     if (country_id is not None and
                         isinstance(country_id, int) and
                         country_id != -1) else True),
                    (City.state_id == int(state_id)
                     if (state_id is not None and
                         isinstance(state_id, int) and
                         state_id != -1) else True)
                ),
            )
        )
        .options(
            load_only(
                City.id,
                City.name,
                City.latitude,
                City.longitude,
            ),

            selectinload(City.state)
            .load_only(
                State.id,
                State.name,
                State.state_code,
            ),

            selectinload(City.country)
            .load_only(
                Country.id,
                Country.name,
                Country.iso3,
                Country.iso2,
            ),

            selectinload(City.subregion)
            .load_only(
                Subregion.id,
                Subregion.name
            ),

            selectinload(City.region)
            .load_only(
                Region.id,
                Region.name
            )
        ).first()
    )

    if found_city is not None:
        return found_city

    # Load best matching State using text search.
    search_query = db.func.plainto_tsquery('english', city_string)

    found_city = (
        db.session.query(City)
        .filter(
            db.and_(
                City.search_vector.op('@@')(search_query),
                (City.country_id == int(country_id)
                 if (country_id is not None and
                     isinstance(country_id, int) and
                     country_id != -1) else True),
                (City.state_id == int(state_id)
                 if (state_id is not None and
                     isinstance(state_id, int) and
                     state_id != -1) else True)
            )
        )
        .order_by(
            db.func.ts_rank_cd(
                City.search_vector,
                search_query
            ).desc()
        )
        .options(
            load_only(
                City.id,
                City.name,
                City.latitude,
                City.longitude,
            ),

            selectinload(City.state)
            .load_only(
                State.id,
                State.name,
                State.state_code,
            ),

            selectinload(City.country)
            .load_only(
                Country.id,
                Country.name,
                Country.iso3,
                Country.iso2,
            ),

            selectinload(City.subregion)
            .load_only(
                Subregion.id,
                Subregion.name
            ),

            selectinload(City.region)
            .load_only(
                Region.id,
                Region.name
            )
        ).first()
    )

    if found_city is not None:
        return found_city

    found_city = (
        db.session.query(City)
        .filter(
            db.and_(
                db.func.similarity(
                    db.func.lower(City.name),
                    db.func.lower(city_string)
                ) > 0.8,
                (City.country_id == int(country_id)
                 if (country_id is not None and
                     isinstance(country_id, int) and
                     country_id != -1) else True),
                (City.state_id == int(state_id)
                 if (state_id is not None and
                     isinstance(state_id, int) and
                     state_id != -1) else True)
            )
        )
        .order_by(
            db.func.similarity(
                City.name,
                city_string
            ).desc()
        )
        .options(
            load_only(
                City.id,
                City.name,
                City.latitude,
                City.longitude,
            ),

            selectinload(City.state)
            .load_only(
                State.id,
                State.name,
                State.state_code,
            ),

            selectinload(City.country)
            .load_only(
                Country.id,
                Country.name,
                Country.iso3,
                Country.iso2,
            ),

            selectinload(City.subregion)
            .load_only(
                Subregion.id,
                Subregion.name
            ),

            selectinload(City.region)
            .load_only(
                Region.id,
                Region.name
            )
        ).first()
    )

    if found_city is not None:
        return found_city

    else:
        return None


def find_city_contains(
        country_id: int,
        state_id: int,
        city_string: str,
        delimited_string: list):
    """
    Load best matching City using contains method
    """
    if (city_string is None or
            len(city_string) == 0):
        return None

    found_city = (
        db.session.query(City)
        .filter(
            db.or_(
                db.and_(
                    db.func.lower(City.name).contains(city_string.lower()),
                    (City.country_id == int(country_id)
                     if (country_id is not None and
                         isinstance(country_id, int) and
                         country_id != -1) else True),
                    (City.state_id == int(state_id)
                     if (state_id is not None and
                         isinstance(state_id, int) and
                         state_id != -1) else True)
                ),
                db.and_(
                    db.or_(*[db.func.lower(City.name).contains(i.lower())
                             for i in delimited_string]),
                    (City.country_id == int(country_id)
                     if (country_id is not None and
                         isinstance(country_id, int) and
                         country_id != -1) else True),
                    (City.state_id == int(state_id)
                     if (state_id is not None and
                         isinstance(state_id, int) and
                         state_id != -1) else True)
                ),
            ),
        )
        .options(
            load_only(
                City.id,
                City.name,
                City.latitude,
                City.longitude,
            ),

            selectinload(City.state)
            .load_only(
                State.id,
                State.name,
                State.state_code,
            ),

            selectinload(City.country)
            .load_only(
                Country.id,
                Country.name,
                Country.iso3,
                Country.iso2,
            ),

            selectinload(City.subregion)
            .load_only(
                Subregion.id,
                Subregion.name
            ),

            selectinload(City.region)
            .load_only(
                Region.id,
                Region.name
            )
        ).first()
    )

    if found_city is not None:
        return found_city

    else:
        return None


def find_city_and_state(
        city_string: str,
        delimited_city_string: list,
        state_string: str,
        regex_letters_state: list,
        delimited_state_string: list):
    """
    Load best matching City State Combo

    Checks:
        1) City
        City.name.ilike(city_string),

        2) City
        db.func.lower(City.name).in_(delimited_city_string)
        if delimited_city_string is not None else False,

        3) State
        City.state.name.ilike(state_string)

        4) State
        City.state_code.in_(regex_letters_state)
        if regex_letters_state is not None else False,

        5) State
        db.func.lower(City.state.name).in_(delimited_state_string)
        if delimited_state_string is not None else False,

        1+3
        1+4
        1+5

        2+3
        2+4
        2+5

    """
    if ((city_string is None or
         city_string == '') and
            (state_string is None or
             state_string == '')):
        return None

    if (city_string is None or
            city_string == ''):
        return None

    # print("Debug city string: " + city_string, flush=True)
    # print("Debug state string: " + state_string, flush=True)

    found_city = (
        db.session.query(City)
        .filter(
            db.or_(
                db.and_(
                    City.name.ilike(city_string),
                    City.state.has(State.name.ilike(state_string))
                ),
                db.and_(
                    City.name.ilike(city_string),
                    City.state.has(State.state_code.in_(regex_letters_state))
                    if (regex_letters_state is not None and
                        isinstance(regex_letters_state, list) and
                        len(regex_letters_state) != 0) else False,
                ),
                db.and_(
                    City.name.ilike(city_string),
                    City.state.has(
                        db.func.lower(State.name).in_(delimited_state_string))
                    if (delimited_state_string is not None and
                        isinstance(delimited_state_string, list) and
                        len(delimited_state_string) != 0) else False,
                ),
                db.and_(
                    db.func.lower(City.name).in_(delimited_city_string)
                    if (delimited_city_string is not None and
                        isinstance(delimited_city_string, list) and
                        len(delimited_city_string) != 0) else False,
                    City.state.has(State.name.ilike(state_string))
                ),
                db.and_(
                    db.func.lower(City.name).in_(delimited_city_string)
                    if (delimited_city_string is not None and
                        isinstance(delimited_city_string, list) and
                        len(delimited_city_string) != 0) else False,
                    City.state.has(State.state_code.in_(regex_letters_state))
                    if (regex_letters_state is not None and
                        isinstance(regex_letters_state, list) and
                        len(regex_letters_state) != 0) else False,
                ),
                db.and_(
                    db.func.lower(City.name).in_(delimited_city_string)
                    if (delimited_city_string is not None and
                        isinstance(delimited_city_string, list) and
                        len(delimited_city_string) != 0) else False,
                    City.state.has(
                        db.func.lower(State.name).in_(delimited_state_string))
                    if (delimited_state_string is not None and
                        isinstance(delimited_state_string, list) and
                        len(delimited_state_string) != 0) else False,
                ),
            )
        )
        .options(
            load_only(
                City.id,
                City.name,
                City.latitude,
                City.longitude,
            ),

            selectinload(City.state)
            .load_only(
                State.id,
                State.name,
                State.state_code,
            ),

            selectinload(City.country)
            .load_only(
                Country.id,
                Country.name,
                Country.iso3,
                Country.iso2,
            ),

            selectinload(City.subregion)
            .load_only(
                Subregion.id,
                Subregion.name
            ),

            selectinload(City.region)
            .load_only(
                Region.id,
                Region.name
            )
        )
        .first()
    )

    if found_city is not None:
        return found_city

    """
    # Load best matching State using text search.
    search_query = db.func.plainto_tsquery(
        'english',
        state_string
    )
    State Search Vector
    
        1) City
        City.name.ilike(city_string),

        2) City
        db.func.lower(City.name).in_(delimited_city_string)
        if delimited_city_string is not None else False,
        
        Fix later
    """
    """
    found_city = (
        db.session.query(City)
        .filter(
            db.or_(
                db.and_(
                    City.name.ilike(city_string),
                    City.state.has(State.search_vector.op('@@')(search_query))
                ),
                db.and_(
                    db.func.lower(City.name).in_(delimited_city_string)
                    if delimited_city_string is not None else False,
                    City.state.has(State.search_vector.op('@@')(search_query))
                ),
            )
        )
        .order_by(
            db.func.ts_rank_cd(
                City.state.search_vector, # error
                search_query
            ).desc()
        )
        .options(
            load_only(
                City.id,
                City.name,
                City.latitude,
                City.longitude,
            ),

            selectinload(City.state)
            .load_only(
                State.id,
                State.name,
                State.state_code,
                State.search_vector
            ),

            selectinload(City.country)
            .load_only(
                Country.id,
                Country.name,
                Country.iso3,
                Country.iso2,
            ),

            selectinload(City.subregion)
            .load_only(
                Subregion.id,
                Subregion.name
            ),

            selectinload(City.region)
            .load_only(
                Region.id,
                Region.name
            )
        )
        .first()
    )
    if found_city is not None:
        return found_city
    """
    """
    State Search Trigram

        1) City
        City.name.ilike(city_string),

        2) City
        db.func.lower(City.name).in_(delimited_city_string)
        if delimited_city_string is not None else False,

    """
    """
    found_city = (
        db.session.query(City)
        .filter(
            db.or_(
                db.and_(
                    City.name.ilike(city_string),
                    City.state.has(
                        db.func.similarity(State.name, state_string) > 0.7),
                ),
                db.and_(
                    db.func.lower(City.name).in_(delimited_city_string)
                    if delimited_city_string is not None else False,
                    City.state.has(
                        db.func.similarity(State.name, state_string) > 0.7),
                ),
            )
        )
        .order_by(
            db.func.similarity(
                City.state.name, # Error
                state_string
            ).desc()
        )
        .options(
            load_only(
                City.id,
                City.name,
                City.latitude,
                City.longitude,
            ),

            selectinload(City.state)
            .load_only(
                State.id,
                State.name,
                State.state_code,
            ),

            selectinload(City.country)
            .load_only(
                Country.id,
                Country.name,
                Country.iso3,
                Country.iso2,
            ),

            selectinload(City.subregion)
            .load_only(
                Subregion.id,
                Subregion.name
            ),

            selectinload(City.region)
            .load_only(
                Region.id,
                Region.name
            )
        )
        .first()
    )
    if found_city is not None:
        return found_city
    """
    """
    City Search Vector

        1) State
        City.state.name.ilike(state_string)

        2) State
        City.state_code.in_(regex_letters_state)
        if regex_letters_state is not None else False,

        3) State
        db.func.lower(City.state.name).in_(delimited_state_string)
        if delimited_state_string is not None else False,

    """
    """
    found_city = (
        db.session.query(City)
        .filter(
            db.or_(
                db.and_(
                    City.search_vector.op('@@')(search_query),
                    City.state.has(State.name.ilike(state_string)),
                ),
                db.and_(
                    City.search_vector.op('@@')(search_query),
                    City.state.has(
                        State.state_code.in_(regex_letters_state))
                    if regex_letters_state is not None else False,
                ),
                db.and_(
                    City.search_vector.op('@@')(search_query),
                    City.state.has(
                        db.func.lower(State.name).in_(delimited_state_string))
                    if delimited_state_string is not None else False,
                ),
            )
        )
        .order_by(db.func.ts_rank_cd(
            State.search_vector, # Error
            search_query).desc()) 
        .options(
            load_only(
                City.id,
                City.name,
                City.latitude,
                City.longitude,
            ),

            selectinload(City.state)
            .load_only(
                State.id,
                State.name,
                State.state_code,
            ),

            selectinload(City.country)
            .load_only(
                Country.id,
                Country.name,
                Country.iso3,
                Country.iso2,
            ),

            selectinload(City.subregion)
            .load_only(
                Subregion.id,
                Subregion.name
            ),

            selectinload(City.region)
            .load_only(
                Region.id,
                Region.name
            )
        )
        .first()
    )
    if found_city is not None:
        return found_city
    """
    """
    City Search Trigram

        1) State
        City.state.name.ilike(state_string)

        2) State
        City.state_code.in_(regex_letters_state)
        if regex_letters_state is not None else False,

        3) State
        db.func.lower(City.state.name).in_(delimited_state_string)
        if delimited_state_string is not None else False,

    """
    """
    found_city = (
        db.session.query(City)
        .filter(
            db.or_(
                db.and_(
                    db.func.similarity(City.name, city_string) > 0.7,
                    City.state.has(State.name.ilike(state_string))
                ),
                db.and_(
                    db.func.similarity(City.name, city_string) > 0.7,
                    City.state.has(State.state_code.in_(regex_letters_state))
                    if regex_letters_state is not None else False,
                ),
                db.and_(
                    db.func.similarity(City.name, city_string) > 0.7,
                    City.state.has(
                        db.func.lower(State.name).in_(delimited_state_string))
                    if delimited_state_string is not None else False,
                ),
            )
        )
        .order_by(
            db.func.similarity(
                State.name, # Error
                state_string
            ).desc()
        )
        .options(
            load_only(
                City.id,
                City.name,
                City.latitude,
                City.longitude,
            ),

            selectinload(City.state)
            .load_only(
                State.id,
                State.name,
                State.state_code,
            ),

            selectinload(City.country)
            .load_only(
                Country.id,
                Country.name,
                Country.iso3,
                Country.iso2,
            ),

            selectinload(City.subregion)
            .load_only(
                Subregion.id,
                Subregion.name
            ),

            selectinload(City.region)
            .load_only(
                Region.id,
                Region.name
            )
        )
        .first()
    )
    """

    if found_city is not None:
        return found_city

    else:
        return None


def find_all_locations_for_region(region_id: int = None) -> list:
    """
    Used in location searches: Provides all Locations which contain a
    region for a broad location search.
    """
    if region_id is None or region_id < 0:
        return []

    return (
        db.session.query(Location)
        .filter(Location.region_id == region_id)
        .options(load_only(Location.id))
        .all()
    )


def find_all_locations_for_subregion(subregion_id: int = None) -> list:
    """
    Used in location searches: Provides all Locations which contain a
    subregion for a broad location search.
    """
    if subregion_id is None or subregion_id < 0:
        return []

    return (
        db.session.query(Location)
        .filter(Location.subregion_id == subregion_id)
        .options(load_only(Location.id))
        .all()
    )


def find_all_locations_for_country(country_id: int = None) -> list:
    """
    Used in location searches: Provides all Locations which contain a
    country for a broad location search.
    """
    if country_id is None or country_id < 0:
        return []

    return (
        db.session.query(Location)
        .filter(Location.country_id == country_id)
        .options(load_only(Location.id))
        .all()
    )


def find_all_locations_for_state(state_id: int = None) -> list:
    """
    Used in location searches: Provides all Locations which contain a
    state for a broad location search.
    """
    if state_id is None or state_id < 0:
        return []

    return (
        db.session.query(Location)
        .filter(Location.state_id == state_id)
        .options(load_only(Location.id))
        .all()
    )


def find_all_locations_for_city(city_id: int = None) -> list:
    """
    Used in location searches: Provides all Locations which contain a
    city for a broad location search.
    """
    if city_id is None or city_id < 0:
        return []

    return (
        db.session.query(Location)
        .filter(Location.city_id == city_id)
        .options(load_only(Location.id))
        .all()
    )


def find_locations_within_distance_miles(
        find_latitude: float = None,
        find_longitude: float = None,
        distance_miles: int = 30,
        remote_flag: bool = False):
    """
    Uses earth_distance to find locations within distance by miles
    for a specific latitude and longitude, with a remote flag.
    """
    if (find_latitude is None or
            find_longitude is None or
            distance_miles is None or
            distance_miles <= 0):
        return None

    distance_meters = distance_miles * 1609.34
    query = text("""SELECT 
    id, 
    (earth_distance(
        ll_to_earth(
            latitude, 
            longitude
        ), 
        ll_to_earth(
            :lat, 
            :lon
        )
    ) / 1609.34) AS distance 
FROM 
    locations 
WHERE 
    earth_box(
        ll_to_earth(
            :lat, 
            :lon
        ), 
        :distance
    ) @> 
    ll_to_earth(
        latitude, 
        longitude
    ) 
AND 
    earth_distance(
        ll_to_earth(
            latitude, 
            longitude
        ), 
        ll_to_earth(
            :lat, 
            :lon
        )
    ) <= :distance 
AND
    remote IS :remote
ORDER BY distance ASC""")

    return (
            db.session.execute(
                query, {
                    'lat': find_latitude,
                    'lon': find_longitude,
                    'distance': distance_meters,
                    'remote': remote_flag
                }
            ).fetchall()
    )


def find_locations_within_distance_miles_all_remote(
        find_latitude: float = None,
        find_longitude: float = None,
        distance_miles: int = 30):
    """
    Uses earth_distance to find locations within distance by miles
    for a specific latitude and longitude, and is remote.
    """
    if (find_latitude is None or
            find_longitude is None or
            distance_miles is None or
            distance_miles <= 0):
        print("No location to order distance", flush=True)
        return find_locations_remote_only()
    # print(str(find_latitude), flush=True)
    # print(str(find_longitude), flush=True)

    distance_meters = distance_miles * 1609.34
    query = text("""SELECT 
    id, 
    (earth_distance(
        ll_to_earth(
            latitude, 
            longitude
        ), 
        ll_to_earth(
            :lat, 
            :lon
        )
    ) / 1609.34) AS distance 
FROM 
    locations 
WHERE 
    (earth_box(
        ll_to_earth(
            :lat, 
            :lon
        ), 
        :distance
    ) @> 
    ll_to_earth(
        latitude, 
        longitude
    ) 
AND 
    earth_distance(
        ll_to_earth(
            latitude, 
            longitude
        ), 
        ll_to_earth(
            :lat, 
            :lon
        )
    ) <= :distance 
AND
    remote IS TRUE)
OR 
    remote IS TRUE
ORDER BY distance ASC""")

    return (
            db.session.execute(
                query, {
                    'lat': find_latitude,
                    'lon': find_longitude,
                    'distance': distance_meters
                }
            ).fetchall()
    )


def find_locations_remote_only():
    """
    Finds all locations that have a remote flag set as true.
    """
    return (
        db.session.query(Location).filter(Location.remote).all()
    )


def find_locations_within_distance_km(
        find_latitude: float = None,
        find_longitude: float = None,
        distance_km: int = 30,
        remote_flag: bool = False):
    """
    Uses earth_distance to find all locations within a certain distance
    in kilometers for a specific latitude and longitude.
    """
    if (find_latitude is None or
            find_longitude is None or
            distance_km is None or
            distance_km <= 0):
        return None

    # Convert kilometers to meters
    distance_kilometers = distance_km * 1000
    query = text("""SELECT 
    id, 
    (earth_distance(
        ll_to_earth(
            latitude, 
            longitude
        ), 
        ll_to_earth(
            :lat, 
            :lon
        )
    ) / 1000) AS distance 
FROM 
    locations 
WHERE 
    earth_box(
        ll_to_earth(
            :lat, 
            :lon
        ), 
        :distance
    ) @> 
    ll_to_earth(
        latitude, 
        longitude
    ) 
AND 
    earth_distance(
        ll_to_earth(
            latitude, 
            longitude
        ), 
        ll_to_earth(
            :lat, 
            :lon
        )
    ) <= :distance 
AND
    remote IS :remote
ORDER BY distance ASC""")

    return (
            db.session.execute(
                query, {
                    'lat': find_latitude,
                    'lon': find_longitude,
                    'distance': distance_kilometers,
                    'remote': remote_flag
                }
            ).fetchall()
    )


def convert_raw_locations_id_to_locations(
        location_list: list) -> list:
    """
    Used for debugging. location_list is a list of location ID's.
    Provides a list of locations in a map, in the same order as provided.
    """
    # print(str(location_list), flush=True)
    # Fetch all the required locations in a single query
    locations = db.session.query(Location).filter(
        Location.id.in_(location_list)).all()
    for i in locations:
        print(i, flush=True)
    # Create a mapping from IDs to Location objects
    location_map = {str(location.id): location for location in locations}
    # print(str(location_map), flush=True)
    # Replace IDs in location_list with the corresponding Location objects
    return [location_map.get(i) for i in location_list]


def order_listed_jobs_location(
        listed_job_locations: list,
        location_list: list,
        ascending: bool = True) -> list:
    """
    Reorders a ListedJobLocation list and extracts the location ID,
    returning a list without duplicates.
    """
    # print(str(location_list), flush=True)
    # print(str(listed_job_locations), flush=True)
    if (listed_job_locations is None or
            len(listed_job_locations) == 0 or
            location_list is None or
            len(location_list) == 0):
        return []

    result = []
    for i in (range(len(location_list))
              if ascending else
              reversed(location_list)):
        for j in range(len(listed_job_locations)):
            if listed_job_locations[j].location_id == location_list[i]:
                result.append(listed_job_locations[j])

    return result


def order_listed_jobs_location_job_id_only(
        listed_job_locations: list,
        location_list: list,
        ascending: bool = True) -> list:
    """
    Reorders a ListedJobLocation list and extracts the ListedJob ID,
    returning a list in the same order as given.
    """
    # print(str(location_list), flush=True)
    # print(str(listed_job_locations), flush=True)
    if (listed_job_locations is None or
            len(listed_job_locations) == 0 or
            location_list is None or
            len(location_list) == 0):
        return []

    result = []
    for i in (range(len(location_list))
              if ascending else
              reversed(location_list)):
        for j in range(len(listed_job_locations)):
            if listed_job_locations[j].location_id == location_list[i]:
                result.append(listed_job_locations[j].listed_job_id)

    return result


def order_listed_jobs_by_location(
        listed_jobs: list,
        location_list: list,
        ascending: bool = True) -> list:
    """
    Orders a ListedJob list by the order given in a Location List.
    """
    # print(str(location_list), flush=True)
    # print(str(listed_jobs), flush=True)
    if not listed_jobs or not location_list:
        return []

    result = []

    # for i in (range(len(listed_jobs))
    #           if ascending else
    #           range(len(listed_jobs)-1, 0, -1)):
    #     if (listed_jobs[i].listed_job_location is not None and
    #             len(listed_jobs[i].listed_job_location) != 0):
    #         for j in range(len(listed_jobs[i].listed_job_location)):
    #             if (listed_jobs[i].listed_job_location[j].location_id
    #                     in location_list):
    #                 result.append(listed_jobs[i])

    # Non-Comprehension (for readability)
    for i in (range(len(location_list))
              if ascending else
              reversed(location_list)):

        if (location_list[i] is None or
                not isinstance(location_list[i], int)):
            continue
        for j in range(len(listed_jobs)):
            for k in range(len(listed_jobs[j].listed_job_location)):
                if (listed_jobs[j].listed_job_location[k].location_id
                        == location_list[i]):
                    result.append(listed_jobs[j])

    # Comprehension for speed
    # return [
    #     job for loc in
    #     (location_list if ascending else reversed(location_list))
    #     if isinstance(loc, int)
    #     for job in listed_jobs
    #     if any(loc == location.location_id for location in
    #            job.listed_job_location)
    # ]

    return result


def find_city_by_coordinates(
        find_latitude: float,
        find_longitude: float):
    """
    Get best matching City/State/Country using latitude and latitude
    coordinates.
    Loads ID, name, state_id, country_id


    Requires postgresql-16-postgis-3

    CREATE EXTENSION postgis;
    CREATE EXTENSION cube;
    CREATE EXTENSION earthdistance;
    """
    if (find_latitude is None or
            find_longitude is None):
        return None

    query = text("""SELECT 
    cities.id 
FROM 
    cities 
ORDER BY 
    earth_distance(
        ll_to_earth(
            latitude, 
            longitude
        ), 
        ll_to_earth(
            :target_lat, 
            :target_lon
        )
    ) 
    ASC LIMIT 1;""")
    found_city = (
        db.session.execute(query, {
            "target_lat": find_latitude,
            "target_lon": find_longitude
        }).fetchone()
    )
    # Executed raw SQL for this query, so reset the city
    if found_city is not None:
        found_city: City = get_city_by_id(int(found_city.id))

    # print(str(found_city.name), flush=True)
    return found_city if found_city else None


def find_city_by_coordinates_fast(
        find_latitude: float,
        find_longitude: float):
    """
    Get best matching City/State/Country using latitude and latitude
    coordinates.
    Loads ID, name, state_id, country_id


    Requires postgresql-16-postgis-3

    CREATE EXTENSION postgis;
    CREATE EXTENSION cube;
    CREATE EXTENSION earthdistance;
    """
    if (find_latitude is None or
            find_longitude is None):
        return None
    if (find_latitude is None or
            find_longitude is None):
        return None

    ll_to_cube_value = db.session.execute(
        text("SELECT ll_to_earth(:lat, :lon)"),
        {"lat": find_latitude, "lon": find_longitude}
    ).scalar()

    query = text("""
        SELECT 
            cities.id 
        FROM 
            cities 
        WHERE 
            earth_distance(cities.ll_to_cube, :ll_to_cube_value) < 
            :distance_threshold
        ORDER BY 
            earth_distance(cities.ll_to_cube, :ll_to_cube_value)
        LIMIT 1;
        """)

    found_city = db.session.execute(
        query, {
            "ll_to_cube_value": ll_to_cube_value,
            "distance_threshold": 80467  # 50 miles in meters
        }).fetchone()

    # Executed raw SQL for this query, so reset the city
    if found_city is not None:
        found_city: City = get_city_by_id(int(found_city.id))

    # print(str(found_city.name), flush=True)
    return found_city if found_city else None


def get_city_by_id(city_id: int):
    """
    Get City by ID
    Loads the id, name, latitude, longitude state_id,
     and country_id for the City
    """
    if (city_id is None or
            city_id <= 0):
        return None
    return (
        db.session.query(City)
        .filter(City.id == int(city_id))
        .options(
            load_only(
                City.id,
                City.name,
                City.latitude,
                City.longitude,
            ),

            selectinload(City.state)
            .load_only(
                State.id,
                State.name,
                State.state_code,
            ),

            selectinload(City.country)
            .load_only(
                Country.id,
                Country.name,
                Country.iso3,
                Country.iso2,
            ),

            selectinload(City.subregion)
            .load_only(
                Subregion.id,
                Subregion.name
            ),

            selectinload(City.region)
            .load_only(
                Region.id,
                Region.name
            )
        )
        .first()
    )


def get_city_by_id_full(city_id: int):
    """
    Get City by ID
    Loads the id, name, latitude, longitude
     and related values for the City
    """
    if (city_id is None or
            city_id <= 0):
        return None
    return (
        db.session.query(City)
        .filter(City.id == int(city_id))
        .options(
            load_only(
                City.id,
                City.name,
                City.latitude,
                City.longitude,
            ),

            selectinload(City.state)
            .load_only(
                State.id,
                State.name,
                State.state_code,
            ),

            selectinload(City.country)
            .load_only(
                Country.id,
                Country.name,
                Country.iso3,
                Country.iso2,
            ),

            selectinload(City.subregion)
            .load_only(
                Subregion.id,
                Subregion.name
            ),

            selectinload(City.region)
            .load_only(
                Region.id,
                Region.name
            )

        ).first()
    )


def get_state_by_id(state_id: int):
    """
    Get State by ID
    Loads the name, state_code, longitude, latitude and country_id for the State
    """
    if (state_id is None or
            state_id <= 0):
        return None
    return (
        db.session.query(State)
        .filter(State.id == int(state_id))
        .options(
            load_only(
                State.id,
                State.name,
                State.state_code,
                State.latitude,
                State.longitude,
            ),

            selectinload(State.country)
            .load_only(
                Country.id,
                Country.name,
                Country.iso3,
                Country.iso2,
            ),

            selectinload(State.subregion)
            .load_only(
                Subregion.id,
                Subregion.name
            ),

            selectinload(State.region)
            .load_only(
                Region.id,
                Region.name
            )
        )
        .first()
    )


def get_state_by_id_full(state_id: int):
    """
    Get State by ID
    Loads the name, state_code, longitude, latitude
    Country ID/name/iso3/iso2
    Subregion ID/name
    Region ID/name
    """
    if (state_id is None or
            state_id <= 0):
        return None
    return (
        db.session.query(State)
        .filter(State.id == int(state_id))
        .options(
            load_only(
                State.id,
                State.name,
                State.state_code,
                State.latitude,
                State.longitude,
            ),

            selectinload(State.country)
            .load_only(
                Country.id,
                Country.name,
                Country.iso3,
                Country.iso2,
            ),

            selectinload(State.subregion)
            .load_only(
                Subregion.id,
                Subregion.name
            ),

            selectinload(State.region)
            .load_only(
                Region.id,
                Region.name
            )

        ).first()
    )


def get_country_by_id_full(country_id: int):
    """
    Get Country by ID
    Loads the full Country Row
    """
    if (country_id is None or
            country_id <= 0):
        return None
    return (
        db.session.query(Country)
        .filter(Country.id == int(country_id))
        .first()
    )


def get_country_by_id(country_id: int):
    """
    Get Country by ID
    Loads the id, name, iso3, iso2, longitude, latitude
    subregion/region id + name
     for the Country
    """
    if (country_id is None or
            country_id <= 0):
        return None
    return (
        db.session.query(Country)
        .filter(Country.id == int(country_id))
        .options(
            load_only(
                Country.id,
                Country.name,
                Country.iso3,
                Country.iso2,
                Country.latitude,
                Country.longitude,
            ),

            selectinload(Country.subregion)
            .load_only(
                Subregion.id,
                Subregion.name
            ),

            selectinload(Country.region)
            .load_only(
                Region.id,
                Region.name
            )
        )
        .first()
    )


def get_subregion_by_id(subregion_id: int):
    """
    Get Subregion by ID
    Loads the id, name, latitude, and longitude for the Subregion
    """
    if (subregion_id is None or
            subregion_id <= 0):
        return None
    return (
        db.session.query(Subregion)
        .filter(Subregion.id == int(subregion_id))
        .options(
            load_only(
                Subregion.id,
                Subregion.name,
                Subregion.latitude,
                Subregion.longitude
            ),

            selectinload(Subregion.region)
            .load_only(
                Region.id,
                Region.name
            )
        )
        .first()
    )


def get_subregion_by_id_full(subregion_id: int):
    """
    Get Subregion by ID
    Loads the full Subregion row
    """
    if (subregion_id is None or
            subregion_id <= 0):
        return None
    return (
        db.session.query(Subregion)
        .filter(Subregion.id == int(subregion_id))
        .first()
    )


def get_region_by_id(region_id: int):
    """
    Get Region by ID
    Loads the id, name, latitude, longitude for the Subregion
    """
    if (region_id is None or
            region_id <= 0):
        return None

    return (
        db.session.query(Region)
        .filter(Region.id == int(region_id))
        .options(
            load_only(
                Region.id,
                Region.name,
                Region.latitude,
                Region.longitude
            )
        )
        .first()
    )


def get_region_by_id_full(region_id: int):
    """
    Get Region by ID
    Loads the full Region row
    """
    if (region_id is None or
            region_id <= 0):
        return None

    return (
        db.session.query(Region)
        .filter(Region.id == int(region_id))
        .first()
    )


def parse_location_to_detailed_list(
        location_str: str,
        score: float = 0.9) -> list:
    """
    Uses pelias-parser

    Converts an input string to a parsed region list.
    0 - City
    1 - State
    2 - Country
    """
    if (location_str is None or
            len(location_str) == 0):
        return []

    response = requests.get(
        url=pelias_parser_query_url,
        headers={
            'Charset': 'utf8',
            'Content-Type': 'application/json; charset=utf-8',
        },
        params={'text': location_str}
    )

    # print(str(response.json()), flush=True)

    detailed_location_list: list = ['', '', '']

    if isinstance(response.json().get('solutions', False), dict):
        return detailed_location_list

    best_scored_solution = response.json().get('solutions', False)

    if (not isinstance(best_scored_solution, list) or
            len(best_scored_solution) == 0):
        return detailed_location_list

    best_scored_solution = best_scored_solution[0]

    if not isinstance(best_scored_solution, dict):
        return detailed_location_list

    if best_scored_solution.get('score', 0) <= score:
        # print("Insufficient Score", flush=True)
        return detailed_location_list

    best_scored_solution = (
        best_scored_solution.get('classifications', False)
    )

    if not best_scored_solution:
        return detailed_location_list

    if not isinstance(best_scored_solution, list):
        return detailed_location_list

    # print("ID: " + str(i), flush=True)

    for j in best_scored_solution:

        if not isinstance(j, dict):
            continue

        loaded_label = j.get('label', '')
        loaded_value = j.get('value', '')

        # print(str(loaded_label) + ": " +
        #       str(loaded_value), flush=True)

        if loaded_label == "country":
            detailed_location_list[2] = loaded_value

        if loaded_label == "region":
            detailed_location_list[1] = loaded_value

        if loaded_label == "locality":
            detailed_location_list[0] = loaded_value

        # Output
        # locality: City, # region: State
        # locality: City, # region Country

    # print(str(detailed_location_list), flush=True)
    return detailed_location_list


def get_glassdoor_location_from_id(location_id: int):
    """
    Gets Glassdoor Location ID Row from database, if the ID is in the database.
    """
    if (location_id is None or
            not isinstance(location_id, int) or
            location_id == -1):
        return None

    return (
        db.session.query(GlassdoorLocationID)
        .filter(GlassdoorLocationID.id == int(location_id))
        .first()
    )


def derive_locations(
        parsed_location_list: dict,
        found_region=None,
        found_subregion=None,
        found_country=None,
        found_state=None,
        found_city=None):

    remote_job = parsed_location_list.get('remote__jobs', None)

    if (found_region is None and
            found_subregion is None and
            found_country is None and
            found_state is None and
            found_city is None and
            remote_job is None):
        return parsed_location_list

    if (remote_job is not None and
            remote_job is True):
        parsed_location_list['remote'] = True

    # Derive locations - continue to process
    if (found_city is not None or
            parsed_location_list.get('city_id', None) is not None):
        # Fix found_city
        if (found_city is None and
                parsed_location_list.get('city_id', None) is not None):
            found_city: City = get_city_by_id(
                city_id=parsed_location_list['city_id']
            )

        parsed_location_list['latitude'] = found_city.latitude
        parsed_location_list['longitude'] = found_city.longitude

        # Fix latitude_longitude for null.
        if (found_city.state is not None and
                (found_city.state.latitude is not None or
                 found_city.state.longitude is not None) and
                (parsed_location_list.get('latitude', None) is None or
                 parsed_location_list.get('longitude', None) is None)):
            # Derive from State
            parsed_location_list['latitude'] = found_city.state.latitude
            parsed_location_list['longitude'] = found_city.state.longitude

        if (found_city.country is not None and
                (found_city.country.latitude is not None or
                 found_city.country.longitude is not None) and
                (parsed_location_list.get('latitude', None) is None or
                 parsed_location_list.get('longitude', None) is None)):
            # Derive from Country
            parsed_location_list['latitude'] = found_city.country.latitude
            parsed_location_list['longitude'] = found_city.country.longitude

        if (found_city.subregion is not None and
                (found_city.subregion.latitude is not None or
                 found_city.subregion.longitude is not None) and
                (parsed_location_list.get('latitude', None) is None or
                 parsed_location_list.get('longitude', None) is None)):
            # Derive from Subregion
            parsed_location_list['latitude'] = found_city.subregion.latitude
            parsed_location_list['longitude'] = found_city.subregion.longitude

        if (found_city.region is not None and
                (found_city.region.latitude is not None or
                 found_city.region.longitude is not None) and
                (parsed_location_list.get('latitude', None) is None or
                 parsed_location_list.get('longitude', None) is None)):
            # Derive from Region
            parsed_location_list['latitude'] = found_city.region.latitude
            parsed_location_list['longitude'] = found_city.region.longitude

        if (parsed_location_list.get('latitude', None) is None or
                parsed_location_list.get('longitude', None) is None):
            raise ValueError("Cannot find lat/longitude for location.")

        parsed_location_list['city_id'] = found_city.id
        parsed_location_list['city'] = found_city.name

        parsed_location_list['state_id'] = found_city.state.id
        parsed_location_list['state'] = found_city.state.name
        parsed_location_list['state_code'] = (
            found_city.state.state_code)

        parsed_location_list['country_id'] = (
            found_city.country.id)
        parsed_location_list['country'] = (
            found_city.country.name)
        parsed_location_list['country_iso3'] = (
            found_city.country.iso3)
        parsed_location_list['country_iso2'] = (
            found_city.country.iso2)

        parsed_location_list['subregion_id'] = (
            found_city.subregion_id)
        parsed_location_list['subregion'] = (
            found_city.subregion.name)

        parsed_location_list['region_id'] = (
            found_city.region.id)
        parsed_location_list['region'] = (
            found_city.region.name)

    elif (found_state is not None or
          parsed_location_list.get('state_id', None) is not None):
        # Fix found_state
        if (found_state is None and
                parsed_location_list.get('state_id', None) is not None):
            found_state: State = get_state_by_id(
                state_id=parsed_location_list['state_id']
            )

        parsed_location_list['latitude'] = found_state.latitude
        parsed_location_list['longitude'] = found_state.longitude

        # Fix latitude_longitude for null.
        if (parsed_location_list.get('latitude', None) is None or
                parsed_location_list.get('longitude', None) is None):
            # Derive from Country
            parsed_location_list['latitude'] = found_state.country.latitude
            parsed_location_list['longitude'] = found_state.country.longitude

        if (parsed_location_list.get('latitude', None) is None or
                parsed_location_list.get('longitude', None) is None):
            # Derive from Subregion
            parsed_location_list['latitude'] = found_state.subregion.latitude
            parsed_location_list['longitude'] = found_state.subregion.longitude

        if (parsed_location_list.get('latitude', None) is None or
                parsed_location_list.get('longitude', None) is None):
            # Derive from Region
            parsed_location_list['latitude'] = found_state.region.latitude
            parsed_location_list['longitude'] = found_state.region.longitude

        if (parsed_location_list.get('latitude', None) is None or
                parsed_location_list.get('longitude', None) is None):
            raise ValueError("Cannot find lat/longitude for location.")

        parsed_location_list['state_id'] = found_state.id
        parsed_location_list['state'] = found_state.name
        parsed_location_list['state_code'] = found_state.state_code

        parsed_location_list[
            'country_id'] = found_state.country.id
        parsed_location_list[
            'country'] = found_state.country.name
        parsed_location_list[
            'country_iso3'] = found_state.country.iso3
        parsed_location_list[
            'country_iso2'] = found_state.country.iso2

        parsed_location_list['subregion_id'] = (
            found_state.subregion_id)
        parsed_location_list['subregion'] = (
            found_state.subregion.name)

        parsed_location_list['region_id'] = (
            found_state.region.id)
        parsed_location_list['region'] = (
            found_state.region.name)
    elif (found_country is not None or
          parsed_location_list.get('country_id', None) is not None):
        # Fix found_country
        if (found_country is None and
                parsed_location_list.get('country_id', None) is not None):
            found_country: Country = get_country_by_id(
                country_id=parsed_location_list['country_id']
            )
        if (found_country.latitude is not None or
                found_country.longitude is not None):
            parsed_location_list['latitude'] = found_country.latitude
            parsed_location_list['longitude'] = found_country.longitude

        # Fix latitude_longitude for null.
        if (found_country.subregion is not None and
            (found_country.subregion.latitude is not None or
             found_country.subregion.longitude is not None) and
                (parsed_location_list.get('latitude', None) is None or
                 parsed_location_list.get('longitude', None) is None)):
            # Derive from Subregion
            parsed_location_list['latitude'] = found_country.subregion.latitude
            parsed_location_list['longitude'] = (
                found_country.subregion.longitude)

        if (found_country.region is not None and
            (found_country.region.latitude is not None or
             found_country.region.longitude is not None) and
                (parsed_location_list.get('latitude', None) is None or
                 parsed_location_list.get('longitude', None) is None)):
            # Derive from Region
            parsed_location_list['latitude'] = found_country.region.latitude
            parsed_location_list['longitude'] = found_country.region.longitude

        if (parsed_location_list.get('latitude', None) is None or
                parsed_location_list.get('longitude', None) is None):
            raise ValueError("Cannot find lat/longitude for location.")

        parsed_location_list['country_id'] = found_country.id
        parsed_location_list['country'] = found_country.name
        parsed_location_list['country_iso3'] = found_country.iso3
        parsed_location_list['country_iso2'] = found_country.iso2

        # Fix for Antarctica
        if found_country.subregion_id is not None:
            parsed_location_list['subregion_id'] = (
                found_country.subregion_id)

        if (found_country.subregion is not None and
                found_country.subregion.name is not None):
            parsed_location_list['subregion'] = (
                found_country.subregion.name)

        if found_country.region_id is not None:
            parsed_location_list[
                'region_id'] = found_country.region_id

        if found_country.region is not None:
            parsed_location_list[
                'region'] = found_country.region.name

    elif (found_subregion is not None or
          parsed_location_list.get('subregion_id', None) is not None):
        # Fix found_subregion
        if (found_subregion is None and
                parsed_location_list.get('subregion_id', None) is not None):
            found_subregion: Subregion = get_subregion_by_id(
                subregion_id=parsed_location_list['subregion_id']
            )

        if found_subregion.latitude is not None:
            parsed_location_list['latitude'] = found_subregion.latitude

        if found_subregion.longitude is not None:
            parsed_location_list['longitude'] = found_subregion.longitude

        # Fix latitude_longitude for null.
        if (found_subregion.region is not None and
                (found_subregion.region.latitude is not None or
                 found_subregion.region.longitude is not None) and
                (parsed_location_list.get('latitude', None) is None or
                 parsed_location_list.get('longitude', None) is None)):
            # Derive from Region
            parsed_location_list['latitude'] = found_subregion.region.latitude
            parsed_location_list['longitude'] = found_subregion.region.longitude

        if (parsed_location_list.get('latitude', None) is None or
                parsed_location_list.get('longitude', None) is None):
            raise ValueError("Cannot find lat/longitude for location.")

        parsed_location_list['subregion_id'] = found_subregion.id
        parsed_location_list['subregion'] = found_subregion.name
        parsed_location_list[
            'region_id'] = found_subregion.region.id
        parsed_location_list[
            'region'] = found_subregion.region.name

    elif (found_region is not None or
          parsed_location_list.get('region_id', None) is not None):
        # Fix found_region
        if (found_region is None and
                parsed_location_list.get('region_id', None) is not None):
            found_region: Region = get_region_by_id(
                region_id=parsed_location_list['region_id']
            )

        parsed_location_list['latitude'] = found_region.latitude
        parsed_location_list['longitude'] = found_region.longitude

        # Fix latitude_longitude for null.
        if (parsed_location_list.get('latitude', None) is None or
                parsed_location_list.get('longitude', None) is None):
            raise ValueError("Cannot find lat/longitude for location.")

        parsed_location_list['region_id'] = found_region.id
        parsed_location_list['region'] = found_region.name

    else:
        # Invalid location
        return {}

    return parsed_location_list


def cleanup_locations(parsed_location_list: dict):
    """
    Cleans up location dictionary by pulling only ID's from dict.
    """
    if (parsed_location_list is None or
            len(parsed_location_list) == 0):
        return {}

    return {
        'region_id': parsed_location_list.pop('region_id', None),
        'subregion_id': parsed_location_list.pop('subregion_id', None),
        'country_id': parsed_location_list.pop('country_id', None),
        'state_id': parsed_location_list.pop('state_id', None),
        'city_id': parsed_location_list.pop('city_id', None),

        'latitude': parsed_location_list.pop('latitude', None),
        'longitude': parsed_location_list.pop('longitude', None),

        'remote': parsed_location_list.pop('remote', False)
    }


def fix_city_name(
        input_city: str,
        input_state: str,
        input_country=''):
    """
    Fixes a city name with provided data to clean up city matching.
    """
    if (input_city is None or
            not isinstance(input_city, str) or
            len(input_city) == 0):
        return None

    match input_city:
        case "New York":
            if ((isinstance(input_state, str) and
                 input_state == '' or
                 input_state.upper() == "NY" or
                 input_state.upper() == "NEW YORK") or
                    (isinstance(input_country, str) and
                     (input_country == '' or
                      input_country.upper() == "UNITED STATES" or
                      input_country.upper() == "UNITED STATES OF AMERICA" or
                      input_country.upper() == "US" or
                      input_country.upper() == "USA"))):
                return "New York City"
        case _:
            return input_city


def delimit_string(
        input_string: str,
        length_combo=1):
    """
    Use Regex to convert a string into a list used for database matches.
    """
    if (input_string is None or
            len(input_string) == 0):
        return []

    # print("debug delimited input string: [" + input_string + "]")

    if length_combo < 1:
        length_combo: int = 1

    pattern = r' - |,'

    delimited_string: list = re.split(pattern, input_string.lower())

    for i in str(input_string).lower().split(' '):
        if i not in delimited_string:
            delimited_string.append(i)

    delimited_string: list = [
        i.strip().replace('-', '')
        for i in delimited_string
    ]

    delimited_string: list = [
        i for i in delimited_string
        if (i != "" and
            i is not None)
    ]

    if (delimited_string is None or
            len(delimited_string) == 0):
        # print("Skip from regex coming up as empty.")
        return []

    # Add substrings when matching from the longest combination to
    # shortest
    temp_delimited_string: list = []

    for j in range(1, len(delimited_string) + 1):
        for i in range(1, j):
            string_to_append = ' '.join(delimited_string[i:j])
            if string_to_append not in delimited_string:
                temp_delimited_string.append(string_to_append)

    new_delimited_string = []

    # Insert uniques
    while len(temp_delimited_string) != 0:
        new_delimited_string.append(
            temp_delimited_string.pop(
                temp_delimited_string.index(max(temp_delimited_string, key=len))
            )
        )

    # Keep original and insert it in the beginning later.
    first_delimited_string: str = delimited_string.pop(0)

    # Add back the original city to the beginning, with the
    # longest combinations following it.
    new_delimited_string.insert(0, first_delimited_string)

    new_delimited_string: list = [
        i for i in new_delimited_string
        if (i != "" and
            i != '[]' and
            i != '()' and
            i is not None)
    ]

    new_delimited_string.extend(delimited_string)

    # count spaces in string and only add string combo's
    new_delimited_string: list = [
        i for i in new_delimited_string
        if i.count(' ') >= length_combo - 1
    ]

    # print(str(new_delimited_string), flush=True)

    return new_delimited_string


def delimit_two_letter_matches_string(input_string: str):
    """
    Filter settings are currently based for US
    State codes include only 2 upper-case letters.

    Clean and look for two upper case letters in string
    separated by end of string or by comma.
    """
    if (input_string is None or
            len(input_string) == 0):
        return []

    two_letter_matches = re.findall(r'\b['r'A-Z]{2}\b', input_string)

    # Debug any regex matches
    # print(str(two_letter_state_matches), flush=True)

    # Clean and try to get a list of strings that are
    # possible matches.
    pattern = r' - |,'

    delimited_string: list = (
        re.split(pattern, str(two_letter_matches).lower())
    )

    for j in str(input_string).lower().split(' '):
        if (isinstance(j, list) and
                j != '[]' and
                j != "" and
                j != '()' and
                j is not None and
                j.lower() not in delimited_string):
            delimited_string.append(j)

    delimited_string: list = [
        i.strip(" ").replace('-', '')
        for i in delimited_string
        if (i != '[]' and
            i != "" and
            i != '()' and
            i is not None)
    ]

    delimited_string: list = [
        i.lower() for i in delimited_string
        if (i != '[]' and
            i != "" and
            i != '()' and
            i is not None)
    ]

    return delimited_string


def delimit_three_letter_matches_string(input_string: str):
    """
    Filter settings are currently based for US
    State codes include only 3 upper-case letters.

    Clean and look for three upper case letters in string
    separated by end of string or by comma.
    """
    if (input_string is None or
            len(input_string) == 0):
        return []

    three_letter_matches = re.findall(r'\b['r'A-Z]{3}\b', input_string)

    # Debug any regex matches
    # print(str(three_letter_state_matches), flush=True)

    # Clean and try to get a list of strings that are
    # possible matches.
    pattern = r' - |,'

    delimited_string: list = (
        re.split(pattern, str(three_letter_matches).lower())
    )

    for j in str(input_string).lower().split(' '):
        if (isinstance(j, list) and
                j != '[]' and
                j != "" and
                j != '()' and
                j is not None and
                j.lower() not in delimited_string):
            delimited_string.append(j)

    delimited_string: list = [
        i.strip(" ").replace('-', '')
        for i in delimited_string
        if (i != '[]' and
            i != "" and
            i != '()' and
            i is not None)
    ]

    delimited_string: list = [
        i.lower() for i in delimited_string
        if (i != '[]' and
            i != "" and
            i != '()' and
            i is not None)
    ]

    return delimited_string


def two_letter_matches_string(input_string: str):
    """
    Converts a string into two letter capital matches for matching states.
    """
    if (input_string is None or
            len(input_string) == 0):
        return []

    two_letter_matches: list = re.findall(r'\b['r'A-Z]{2}\b', input_string)
    return two_letter_matches


def three_letter_matches_string(input_string: str):
    """
    Converts a string into three letter capital matches for matching states.
    """
    if (input_string is None or
            len(input_string) == 0):
        return []

    three_letter_matches: list = re.findall(r'\b['r'A-Z]{3}\b', input_string)
    return three_letter_matches
