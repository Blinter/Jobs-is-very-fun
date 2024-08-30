"""
DB Models
Postgres
Country Table
"""
from sqlalchemy import text
from sqlalchemy.orm import load_only

from extensions_sql import db
from sqlalchemy.dialects.postgresql import TSVECTOR
from geoalchemy2 import Geography

from models.postgres.locations.cube import Cube
from models.postgres.locations.subregions import Subregion
from sqlalchemy.orm.attributes import flag_modified


class Country(db.Model):
    """
    Table that holds information about a country.
    """
    __bind_key__ = "postgres"

    __tablename__ = "countries"

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

    iso3 = db.Column(
        db.VARCHAR(length=3),
        nullable=False,
        unique=True
    )

    iso2 = db.Column(
        db.VARCHAR(length=2),
        nullable=False,
        unique=True
    )

    search_vector_name = db.Column(
        TSVECTOR
    )

    search_vector_iso3 = db.Column(
        TSVECTOR
    )

    search_vector_iso2 = db.Column(
        TSVECTOR
    )

    search_vector = db.Column(
        TSVECTOR
    )

    numeric_code = db.Column(
        db.Integer,
        nullable=False,
        unique=True
    )

    phone_code = db.Column(
        db.VARCHAR(length=255),
        nullable=False,
        unique=False
    )

    capital = db.Column(
        db.VARCHAR(length=255),
        nullable=True,
        unique=False
    )

    currency = db.Column(
        db.VARCHAR(length=255),
        nullable=False,
        unique=False
    )

    currency_name = db.Column(
        db.VARCHAR(length=255),
        nullable=False,
        unique=False)

    currency_symbol = db.Column(
        db.VARCHAR(length=255),
        nullable=False,
        unique=False
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
        nullable=True
    )

    region = db.relationship(
        'Region',
        back_populates="countries",
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
        back_populates="countries",
        lazy='select',
        viewonly=True
    )

    states = db.relationship(
        'State',
        back_populates="country",
        cascade="all, delete",
        lazy='select'
    )

    cities = db.relationship(
        'City',
        back_populates="country",
        cascade="all, delete",
        lazy='select'
    )

    country_location = db.relationship(
        'Location',
        back_populates='country',
        cascade="all, delete",
        lazy='select'
    )

    glassdoor_location_ids = db.relationship(
        'GlassdoorLocationID',
        back_populates='country',
        cascade="all, delete",
        lazy='select'
    )

    x_location_ids = db.relationship(
        'XLocationID',
        back_populates='country',
        cascade="all, delete",
        lazy='select'
    )

    linkedin_geourns = db.relationship(
        'LinkedInGeoURNID',
        back_populates='country',
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

        return ("<Country "
                f"id={str(self.id)} "
                f"name={str(self.name)} " +
                # f"iso3={str(self.iso3)} "
                # f"iso2={str(self.iso2)} "
                # f"numeric_code={str(self.numeric_code)} "
                # f"phone_code={str(self.phone_code)} "
                # f"currency_name={str(self.currency_name)} "
                # f"currency_symbol={str(self.currency_symbol)} "
                # f"currency={str(self.currency)} "
                # f"latitude={str(self.latitude)} "
                # f"capital={str(self.capital)} "

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
                f"subregion={str(self.subregion.name)} " +

                # ("[trunc.]" if len(self.states) > 64 else "") +
                # f"states={str(self.states[:64])} " +
                #
                # ("[trunc.]" if len(self.cities) > 64 else "") +
                # f"cities={str(self.cities[:64])} " +
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
                'idx_countries_region_id',
                self.region_id,
                postgresql_using='hash'
            ),
            db.Index(
                'idx_countries_subregion_id',
                self.subregion_id,
                postgresql_using='hash'
            ),
            db.Index(
                'idx_countries_vector_name',
                self.search_vector_name,
                postgresql_using='gin'
            ),
            db.Index(
                'idx_countries_vector_iso3',
                self.search_vector_iso3,
                postgresql_using='gin'
            ),
            db.Index(
                'idx_countries_vector_iso2',
                self.search_vector_iso2,
                postgresql_using='gin'
            ),
            db.Index(
                'idx_countries_vector',
                self.search_vector,
                postgresql_using='gin'
            ),
            db.Index(
                'idx_countries_trgm',
                self.name,
                postgresql_using='gin',
                postgresql_ops={
                    'name': 'gin_trgm_ops'
                }
            ),
            # db.Index(
            #     'idx_countries_geom',
            #     self.geom,
            #     postgresql_using='gist',
            # ),
            db.Index(
                'idx_countries_ll_to_cube',
                self.ll_to_cube,
                postgresql_using='gist',
            ),
        )


@db.event.listens_for(Country, 'before_insert')
@db.event.listens_for(Country, 'before_update')
def update_city_null_columns(_, __, target):
    """
    Fix NULL constraint values based on the seeded Subregion ID.
    Derives Region from Subregion.
    """
    if (target.subregion_id is not None and
            target.region_id is None):
        found_subregion = (
            db.session.query(Subregion).filter(
                Subregion.id == target.subregion_id
            ).options(
                load_only(
                    Subregion.region_id,
                )
            ).first()
        )
        target.region_id = found_subregion.region_id


@db.event.listens_for(Country, 'before_insert')
@db.event.listens_for(Country, 'before_update')
def update_country_search_vector(_, __, target):
    name_changed = db.inspect(target).attrs.name.history.has_changes()
    if name_changed:
        target.name = (
            target.name[0]
            if isinstance(target.name, tuple) else str(target.name)
            if target.name else ''
        )
        target.search_vector_name = db.func.to_tsvector(target.name)
        flag_modified(target, "search_vector_name")

    iso3_changed = db.inspect(target).attrs.iso3.history.has_changes()
    if iso3_changed:
        target.iso3 = (
            target.iso3[0]
            if isinstance(target.iso3, tuple) else target.iso3
        )
        target.iso3 = str(target.iso3) if target.iso3 else ''
        target.search_vector_iso3 = db.func.to_tsvector(target.iso3)
        flag_modified(target, "search_vector_iso3")

    iso2_changed = db.inspect(target).attrs.iso2.history.has_changes()
    if iso2_changed:
        target.iso2 = (
            target.iso2[0]
            if isinstance(target.iso2, tuple) else target.iso2
        )
        target.iso2 = str(target.iso2) if target.iso2 else ''
        target.search_vector_iso2 = db.func.to_tsvector(target.iso2)
        flag_modified(target, "search_vector_iso2")

    if (name_changed or
            iso3_changed or
            iso2_changed):
        target.search_vector = db.func.to_tsvector(
            ' '.join(filter(None, [
                target.name,
                target.iso3,
                target.iso2,
            ]))
        )
        flag_modified(target, "search_vector")


@db.event.listens_for(Country, 'before_insert')
@db.event.listens_for(Country, 'before_update')
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
