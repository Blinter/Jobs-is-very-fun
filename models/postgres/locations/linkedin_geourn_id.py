"""
DB Models
Postgres
LinkedIn GeoURN ID Table
"""
from sqlalchemy import text

from extensions_sql import db
from geoalchemy2 import Geography
from sqlalchemy.dialects.postgresql import TSVECTOR

from models.postgres.locations.cube import Cube
from sqlalchemy.orm.attributes import flag_modified


class LinkedInGeoURNID(db.Model):
    """
    Table that holds information about LinkedIn GeoURN ID.
    """
    __bind_key__ = "postgres"

    __tablename__ = "linkedin_geourns"

    id = db.Column(
        db.BIGINT,
        primary_key=True,
        nullable=False
    )

    name = db.Column(
        db.VARCHAR(),
        nullable=False,
    )

    search_vector = db.Column(
        TSVECTOR
    )

    region_id = db.Column(
        db.Integer,
        db.ForeignKey('regions.id'),
        nullable=True
    )

    region = db.relationship(
        'Region',
        back_populates="linkedin_geourns",
        lazy='select',
        viewonly=True
    )

    subregion_id = db.Column(
        db.Integer,
        db.ForeignKey('subregions.id'),
        nullable=True
    )

    subregion = db.relationship(
        'Subregion',
        back_populates="linkedin_geourns",
        lazy='select',
        viewonly=True,
    )

    country_id = db.Column(
        db.Integer,
        db.ForeignKey('countries.id'),
        nullable=True
    )

    country = db.relationship(
        'Country',
        back_populates="linkedin_geourns",
        lazy='select',
        viewonly=True
    )

    state_id = db.Column(
        db.Integer,
        db.ForeignKey('states.id'),
        nullable=True
    )

    state = db.relationship(
        'State',
        back_populates="linkedin_geourns",
        lazy='select',
        viewonly=True
    )

    city_id = db.Column(
        db.Integer,
        db.ForeignKey('cities.id'),
        nullable=True
    )

    city = db.relationship(
        'City',
        back_populates="linkedin_geourns",
        lazy='select',
        viewonly=True
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

    remote = db.Column(
        db.Boolean,
        nullable=False,
        unique=False,
        default=False,
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
        """Show info about X Location ID"""

        return ("<LinkedInGeoURNID " +
                f"id={str(self.id)} " +
                f"name={str(self.name)} " +

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

                # (f"city={str(self.city.name)[:64]} "
                #  if self.city_id is not None else '') +
                #
                # (f"state={str(self.state.name)[:64]} "
                #  if self.state_id is not None else '') +
                #
                # (f"country={str(self.country.name)[:64]} "
                #  if self.country_id is not None else '') +
                #
                # (f"subregion={str(self.subregion.name)[:64]} "
                #  if self.subregion_id is not None else '') +
                #
                # (f"region={str(self.region.name)[:64]} "
                #  if self.region_id is not None else '') +

                ">")

    @db.orm.declared_attr
    def __table_args__(self):
        return (
            db.Index(
                'idx_linkedin_geourns_region_id',
                self.region_id,
                postgresql_using='hash'
            ),
            db.Index(
                'idx_linkedin_geourns_subregion_id',
                self.subregion_id,
                postgresql_using='hash'
            ),
            db.Index(
                'idx_linkedin_geourns_country_id',
                self.country_id,
                postgresql_using='hash'
            ),
            db.Index(
                'idx_linkedin_geourns_state_id',
                self.state_id,
                postgresql_using='hash'
            ),
            db.Index(
                'idx_linkedin_geourns_city_id',
                self.city_id,
                postgresql_using='hash'
            ),
            db.Index(
                'idx_linkedin_geourns_vector',
                self.search_vector,
                postgresql_using='gin'
            ),
            db.Index(
                'idx_linkedin_geourns_trgm',
                self.name,
                postgresql_using='gin',
                postgresql_ops={
                    'name': 'gin_trgm_ops'
                }
            ),
            # db.Index(
            #     'idx_linkedin_geourns_geom',
            #     self.geom,
            #     postgresql_using='gist',
            # ),
            db.Index(
                'idx_linkedin_geourns_ll_to_cube',
                self.ll_to_cube,
                postgresql_using='gist',
            ),
        )


@db.event.listens_for(LinkedInGeoURNID, 'before_insert')
@db.event.listens_for(LinkedInGeoURNID, 'before_update')
def update_linkedin_geourn_search_vector(_, __, target):
    if db.inspect(target).attrs.name.history.has_changes():
        target.name = (
            target.name[0]
            if isinstance(target.name, tuple) else str(target.name)
            if target.name else '')
        target.search_vector = db.func.to_tsvector(target.name)
        flag_modified(target, "search_vector")


@db.event.listens_for(LinkedInGeoURNID, 'before_insert')
@db.event.listens_for(LinkedInGeoURNID, 'before_update')
def update_linkedin_geo_urn_id_null_columns(_, __, target):
    """
    Derive locations before insert to keep the database organized.
    """

    # Derive from subregion if region is None
    if (target.subregion_id is not None and
            target.region_id is None):
        from routines.parsing.find_location import get_subregion_by_id
        found_subregion = get_subregion_by_id(target.subregion_id)
        target.region_id = found_subregion.region_id

    # Derive from country if subregion/region is None
    elif (target.country_id is not None and
            (target.region_id is None or
             target.subregion_id is None)):
        from routines.parsing.find_location import get_country_by_id
        found_country = get_country_by_id(target.country_id)
        target.subregion_id = found_country.subregion_id
        target.region_id = found_country.region_id

    # Derive from state if country/subregion/region is None
    elif (target.state_id is not None and
            (target.region_id is None or
             target.subregion_id is None or
             target.country_id is None)):
        from routines.parsing.find_location import get_state_by_id
        found_state = get_state_by_id(target.state_id)
        target.country_id = found_state.country_id
        target.subregion_id = found_state.subregion_id
        target.region_id = found_state.region_id

    # Derive from city if state/country/subregion/region is None
    elif (target.city_id is not None and
            (target.region_id is None or
             target.subregion_id is None or
             target.country_id is None or
             target.state_id is None)):
        from routines.parsing.find_location import get_city_by_id
        found_city = get_city_by_id(target.city_id)
        target.state_id = found_city.state_id
        target.country_id = found_city.country_id
        target.subregion_id = found_city.subregion_id
        target.region_id = found_city.region_id


@db.event.listens_for(LinkedInGeoURNID, 'before_insert')
@db.event.listens_for(LinkedInGeoURNID, 'before_update')
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
