"""
DB Models
Postgres
State Table
"""
from sqlalchemy import text
from sqlalchemy.orm import load_only

from extensions_sql import db
from sqlalchemy.dialects.postgresql import TSVECTOR
from geoalchemy2 import Geography

from models.postgres.locations.countries import Country
from models.postgres.locations.cube import Cube
from sqlalchemy.orm.attributes import flag_modified


class State(db.Model):
    """
    Table that holds information about a state.
    """
    __bind_key__ = "postgres"

    __tablename__ = "states"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    name = db.Column(
        db.VARCHAR(),
        nullable=False,
        unique=False
    )

    state_code = db.Column(
        db.VARCHAR(),
        nullable=False,
        unique=False
    )

    search_vector_name = db.Column(
        TSVECTOR
    )

    search_vector_state_code = db.Column(
        TSVECTOR
    )

    search_vector = db.Column(
        TSVECTOR
    )

    latitude = db.Column(
        db.Float(),
        nullable=True,
        unique=False
    )

    longitude = db.Column(
        db.Float(),
        nullable=True,
        unique=False
    )

    geom = db.Column(
        Geography(
            geometry_type='POINT',
            srid=4326,
        ),
        nullable=True,
    )

    ll_to_cube = db.Column(
        Cube,
        nullable=True,
    )

    region_id = db.Column(
        db.Integer,
        db.ForeignKey('regions.id'),
        nullable=False
    )

    region = db.relationship(
        'Region',
        back_populates="states",
        lazy='select',
        viewonly=True
    )

    subregion_id = db.Column(
        db.Integer,
        db.ForeignKey('subregions.id'),
        nullable=False
    )

    subregion = db.relationship(
        'Subregion',
        back_populates="states",
        lazy='select',
        viewonly=True
    )

    country_id = db.Column(
        db.Integer,
        db.ForeignKey('countries.id'),
        nullable=False
    )

    country = db.relationship(
        'Country',
        back_populates="states",
        lazy='select',
        viewonly=True
    )

    cities = db.relationship(
        'City',
        back_populates="state",
        cascade="all, delete",
        lazy='select'
    )

    state_location = db.relationship(
        'Location',
        back_populates='state',
        cascade="all, delete",
        lazy='select'
    )

    glassdoor_location_ids = db.relationship(
        'GlassdoorLocationID',
        back_populates='state',
        cascade="all, delete",
        lazy='select'
    )

    x_location_ids = db.relationship(
        'XLocationID',
        back_populates='state',
        cascade="all, delete",
        lazy='select'
    )

    linkedin_geourns = db.relationship(
        'LinkedInGeoURNID',
        back_populates='state',
        cascade="all, delete",
        lazy='select'
    )

    @staticmethod
    def ll_to_earth(latitude, longitude):
        # This should be a function to convert lat/lon to the earth cube
        return text(
            str(latitude[0]
                if isinstance(latitude, tuple) else latitude) + ', ' +
            str(longitude[0]
                if isinstance(longitude, tuple) else longitude))

    def __repr__(self):
        """Show info about Country"""

        return ("<State "
                f"id={str(self.id)} "
                f"name={str(self.name)} " +
                # f"state_code={str(self.state_code)} "

                (("latitude=" + str(
                    self.latitude[0]
                    if isinstance(self.latitude, tuple)
                    else self.latitude) + " ")
                 if self.latitude is not None else '') +

                (("longitude=" + str(
                    self.longitude[0]
                    if isinstance(self.longitude, tuple)
                    else self.longitude) + " ")
                 if self.longitude is not None else '') +

                f"region={str(self.region.name)} "
                f"subregion={str(self.subregion.name)} "
                f"country={str(self.country.name)} " +

                # ("[trunc.]" if len(self.cities) > 64 else "") +
                # f"cities={str(self.cities[:64])} "
                #
                # "glassdoor_location_ids="
                # f"{str(self.glassdoor_location_ids)[:24]}"
                #
                # "x_location_ids="
                # f"{str(self.x_location_ids)[:24]}"
                #
                # "linkedin_geourns="
                # f"{str(self.linkedin_geourns)[:24]}"
                ">")

    @db.orm.declared_attr
    def __table_args__(self):
        return (
            db.Index(
                'idx_states_region_id',
                self.region_id,
                postgresql_using='hash'
            ),
            db.Index(
                'idx_states_subregion_id',
                self.subregion_id,
                postgresql_using='hash'
            ),
            db.Index(
                'idx_states_country_id',
                self.country_id,
                postgresql_using='hash'
            ),
            db.Index(
                'idx_states_vector_name',
                self.search_vector_name,
                postgresql_using='gin'
            ),
            db.Index(
                'idx_states_vector_state_code',
                self.search_vector_state_code,
                postgresql_using='gin'
            ),
            db.Index(
                'idx_states_vector',
                self.search_vector,
                postgresql_using='gin'
            ),
            db.Index(
                'idx_states_trgm',
                self.name,
                postgresql_using='gin',
                postgresql_ops={
                    'name': 'gin_trgm_ops'
                }
            ),
            # db.Index(
            #     'idx_states_geom',
            #     self.geom,
            #     postgresql_using='gist',
            # ),
            db.Index(
                'idx_states_ll_to_cube',
                self.ll_to_cube,
                postgresql_using='gist',
            ),
        )


@db.event.listens_for(State, 'before_insert')
@db.event.listens_for(State, 'before_update')
def update_city_null_columns(_, __, target):
    """
    Fix NULL constraint values based on the seeded city ID.
    Derives Subregion/Region from Country.
    """
    if (target.country_id is not None and
            (target.subregion_id is None or
             target.region_id is None)):
        found_country = (
            db.session.query(Country).filter(
                Country.id == target.country_id
            ).options(
                load_only(
                    Country.subregion_id,
                    Country.region_id,
                )
            ).first()
        )
        target.subregion_id = found_country.subregion_id
        target.region_id = found_country.region_id


@db.event.listens_for(State, 'before_insert')
@db.event.listens_for(State, 'before_update')
def update_state_search_vector(_, __, target):
    name_changed = db.inspect(target).attrs.name.history.has_changes()
    if name_changed:
        target.name = (
            target.name[0]
            if isinstance(target.name, tuple) else str(target.name)
            if target.name else '')
        target.name = str(target.name) if target.name else ''
        target.search_vector_name = db.func.to_tsvector(target.name)
        flag_modified(target, "search_vector_name")

    state_code_changed = (
        db.inspect(target).attrs.state_code.history.has_changes())
    if state_code_changed:
        target.state_code = (
            target.state_code[0]
            if isinstance(target.state_code, tuple) else target.state_code)
        target.state_code = str(target.state_code) if target.state_code else ''
        target.search_vector_state_code = db.func.to_tsvector(target.state_code)
        flag_modified(target, "search_vector_name")

    if (name_changed or
            state_code_changed):
        target.search_vector = db.func.to_tsvector(
            ' '.join(filter(None, [
                target.name,
                target.state_code
            ]))
        )
        flag_modified(target, "search_vector")


@db.event.listens_for(State, 'before_insert')
@db.event.listens_for(State, 'before_update')
def update_longitude_latitude_columns(_, connection, target):
    if target.latitude is not None:
        target.latitude = (
            target.latitude[0]
            if isinstance(target.latitude, tuple) else target.latitude),

    if target.longitude is not None:
        target.longitude = (
            target.longitude[0]
            if isinstance(target.longitude, tuple) else target.longitude),

    if (target.latitude is not None and
            target.longitude is not None):
        target.geom = (
            'SRID=4326;POINT(' +
            str(target.latitude[0]
                if isinstance(target.latitude, tuple) else target.latitude) +
            ' ' +
            str(target.longitude[0]
                if isinstance(target.longitude, tuple) else target.longitude) +
            ')')

        # Use a raw SQL query to set ll_to_cube
        target.ll_to_cube = (
            connection.execute(text(
                "SELECT ll_to_earth(" +
                str(target.latitude[0]
                    if isinstance(target.latitude, tuple)
                    else target.latitude) +
                ", " + str(target.longitude[0]
                           if isinstance(target.longitude, tuple)
                           else target.longitude) +
                ")"
            ))
        ).scalar()
