"""
DB Models
Postgres
Subregions Table
"""
from sqlalchemy import text

from extensions_sql import db
from sqlalchemy.dialects.postgresql import TSVECTOR
from geoalchemy2 import Geography

from models.postgres.locations.cube import Cube
from sqlalchemy.orm.attributes import flag_modified


class Subregion(db.Model):
    """
    Table that holds information about a subregion.
    """
    __bind_key__ = "postgres"

    __tablename__ = "subregions"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    name = db.Column(
        db.VARCHAR(),
        nullable=False,
        unique=True
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
        back_populates="subregions",
        lazy='select',
        viewonly=True
    )

    countries = db.relationship(
        'Country',
        back_populates="subregion",
        cascade="all, delete",
        lazy='select'
    )

    states = db.relationship(
        'State',
        back_populates="subregion",
        cascade="all, delete",
        lazy='select'
    )

    cities = db.relationship(
        'City',
        back_populates="subregion",
        cascade="all, delete",
        lazy='select'
    )

    subregion_location = db.relationship(
        'Location',
        back_populates='subregion',
        cascade="all, delete",
        lazy='select'
    )

    glassdoor_location_ids = db.relationship(
        'GlassdoorLocationID',
        back_populates='subregion',
        cascade="all, delete",
        lazy='select'
    )

    x_location_ids = db.relationship(
        'XLocationID',
        back_populates='subregion',
        cascade="all, delete",
        lazy='select'
    )

    linkedin_geourns = db.relationship(
        'LinkedInGeoURNID',
        back_populates='subregion',
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
        """Show info about Subregion"""

        return ("<Subregion "
                f"id={str(self.id)} "
                f"name={str(self.name)} "
                f"region={str(self.region.name)} " +

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

                # ("[trunc.]" if len(self.countries) > 64 else "") +
                # f"countries={str(self.countries)} " +
                #
                # ("[trunc.]" if len(self.states) > 64 else "") +
                # f"states={str(self.states)} " +
                #
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
                'idx_subregions_region_id',
                self.region_id,
                postgresql_using='hash'
            ),
            db.Index(
                'idx_subregions_vector',
                self.search_vector,
                postgresql_using='gin'
            ),
            db.Index(
                'idx_subregions_trgm',
                self.name,
                postgresql_using='gin',
                postgresql_ops={
                    'name': 'gin_trgm_ops'
                }
            ),

            # Maintained by database
            # db.Index(
            #     'idx_subregions_geom',
            #     self.geom,
            #     postgresql_using='gist',
            # ),

            db.Index(
                'idx_subregions_ll_to_cube',
                self.ll_to_cube,
                postgresql_using='gist',
            ),
        )


@db.event.listens_for(Subregion, 'before_insert')
@db.event.listens_for(Subregion, 'before_update')
def update_subregion_search_vector(_, __, target):
    if db.inspect(target).attrs.name.history.has_changes():
        target.name = (
            target.name[0]
            if isinstance(target.name, tuple) else str(target.name)
            if target.name else '')
        target.search_vector = db.func.to_tsvector(target.name)
        flag_modified(target, "search_vector")


@db.event.listens_for(Subregion, 'before_insert')
@db.event.listens_for(Subregion, 'before_update')
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
