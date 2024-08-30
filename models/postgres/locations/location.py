"""
DB Models
Postgres
Location Table
"""
from sqlalchemy import text

from extensions_sql import db
from geoalchemy2 import Geography

from models.postgres.locations.cube import Cube


class Location(db.Model):
    """
    Main table that holds all the possible locations of a Listed Job or by
    Surveys taken by the user.
    """
    __bind_key__ = "postgres"

    __tablename__ = "locations"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    region_id = db.Column(
        db.Integer,
        db.ForeignKey('regions.id'),
        nullable=True
    )

    region = db.relationship(
        'Region',
        back_populates="region_location",
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
        back_populates="subregion_location",
        lazy='select',
        viewonly=True
    )

    country_id = db.Column(
        db.Integer,
        db.ForeignKey('countries.id'),
        nullable=True
    )

    country = db.relationship(
        'Country',
        back_populates="country_location",
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
        back_populates="state_location",
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
        back_populates="city_location",
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

    survey_locations = db.relationship(
        'SurveyLocation',
        back_populates="location",
        cascade="all, delete",
        lazy='select'
    )

    listed_job_locations = db.relationship(
        'ListedJobLocation',
        back_populates="listed_job_location",
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
        """Show info about Location."""

        return ("<Location "
                f"id={str(self.id)} " +

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

                (f"city={str(self.city.name)} "
                 if self.city_id is not None and
                    self.city is not None else '') +

                (f"state={str(self.state.name)} "
                 if self.state_id is not None and
                    self.state is not None else '') +

                (f"country={str(self.country.name)} "
                 if self.country_id is not None and
                    self.country is not None else '') +

                (f"subregion={str(self.subregion.name)} "
                 if self.subregion_id is not None and
                    self.subregion is not None else '') +

                (f"region={str(self.region.name)} "
                 if self.region_id is not None and
                    self.region is not None else '') +

                (f"remote={str(self.remote)} "
                 if self.remote is not None else '') +

                # ("[trunc.]" if len(self.survey_locations) > 32 else "") +
                # f"survey_locations={self.survey_locations[:32]}" +
                #
                # ("[trunc.]" if len(self.listed_job_locations) > 32 else "") +
                # f"listed_job_locations={self.listed_job_locations[:32]}" +
                ">")

    @db.orm.declared_attr
    def __table_args__(self):
        return (
            db.Index(
                'idx_locations_remote',
                self.remote,
                postgresql_using='hash'
            ),
            db.Index(
                'idx_locations_region_id',
                self.region_id,
                postgresql_using='hash'
            ),
            db.Index(
                'idx_locations_subregion_id',
                self.subregion_id,
                postgresql_using='hash'
            ),
            db.Index(
                'idx_locations_country_id',
                self.country_id,
                postgresql_using='hash'
            ),
            db.Index(
                'idx_locations_state_id',
                self.state_id,
                postgresql_using='hash'
            ),
            db.Index(
                'idx_locations_city_id',
                self.city_id,
                postgresql_using='hash'
            ),
            # db.Index(
            #     'idx_locations_geom',
            #     self.geom,
            #     postgresql_using='gist',
            # ),
            db.Index(
                'idx_locations_ll_to_cube',
                self.ll_to_cube,
                postgresql_using='gist',
            ),
        )

    def to_jobs_rest(self):
        """
        Returns a string for use in jobs dashboard.
        """

        nice_location = ""

        if (self.remote is not None and
                self.remote is True):
            nice_location += 'Remote ('

        if self.city_id is not None and self.city is not None:
            nice_location += self.city.name

        if self.state_id is not None and self.state is not None:
            if self.city_id is not None and self.city is not None:
                nice_location += ", "
            nice_location += self.state.name

        if self.country_id is not None and self.country is not None:
            if ((self.city_id is not None and
                 self.city is not None and
                 self.state_id is None and
                 self.state is None) or
                    (self.state_id is not None and
                     self.state is not None)):
                nice_location += ", "
            nice_location += self.country.name

        if (self.remote is not None and
                self.remote is True):
            nice_location += ')'

        return nice_location


@db.event.listens_for(Location, 'before_insert')
@db.event.listens_for(Location, 'before_update')
def update_location_null_columns(_, __, target):
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


@db.event.listens_for(Location, 'before_insert')
@db.event.listens_for(Location, 'before_update')
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
