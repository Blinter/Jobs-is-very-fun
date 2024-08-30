"""
States Seed #2+ Template

Seed file can be run
cd <base_dir>
PYTHONPATH=<base_dir> python3 <base_dir>/<file_name>.py
"""

'''

from models.postgres.locations.regions import Region
from models.postgres.locations.subregions import Subregion
from models.postgres.locations.countries import Country
from models.postgres.locations.states import State
from models.postgres.locations.cities import City
from app import create_app, db

app = create_app()

with app.app_context():
    try:
        country_list = db.session.query(Country).all()
        list_of_states = []

        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        list_of_states.append(State(
            name="",
            state_code="",
            latitude=__,
            longitude=__,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "")][0]),
        ))
        db.session.add_all(list_of_states)
        db.session.commit()
        print("Database seeded successfully!")
    except Exception as e:
        print(f"Error committing data: {e}")

'''
