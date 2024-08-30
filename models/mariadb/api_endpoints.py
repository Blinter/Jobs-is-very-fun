"""
DB Models
MariaDB
API Endpoints Table
"""
from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, BIT, TEXT, TINYINT

from enums.api_endpoint_types import api_endpoint_type_to_description
from extensions_sql import db


class APIEndpoint(db.Model):
    """
    An API can have one or more endpoints which are queryable.

    These endpoints can be added in manually from the dashboard.

    Endpoints can have additional parameters which are stored in the
    API Endpoint Params Table.

    Endpoints can have additional Headers which are stored in the
    API Endpoint Headers Table.

    Endpoints can have additional Bodies which are stored in the
    API Endpoint Bodies Table.
    """
    __bind_key__ = "mariadb"

    __tablename__ = "APIEndpoints"

    id = db.Column(
        BIGINT(unsigned=True),
        primary_key=True,
        autoincrement=True,
        nullable=False
    )

    api_id = db.Column(
        BIGINT(unsigned=True),
        db.ForeignKey('APIListURL.id'),
        nullable=False
    )

    api = db.relationship(
        'APIListURL',
        back_populates="endpoints",
        lazy='select',
        viewonly=True
    )

    nice_name = db.Column(
        VARCHAR(length=255),
        nullable=False,
        unique=False
    )

    nice_category = db.Column(
        VARCHAR(length=255),
        nullable=True,
        unique=False
    )

    nice_description = db.Column(
        TEXT(),
        nullable=True,
        unique=False
    )

    http_method = db.Column(
        VARCHAR(length=7),
        nullable=False,
        unique=False
    )

    http_path = db.Column(
        VARCHAR(2048),
        nullable=False,
        unique=False
    )

    http_path_suffix = db.Column(
        VARCHAR(255),
        nullable=True,
        unique=False
    )

    disabled = db.Column(
        BIT(length=1),
        nullable=False,
        default=False
    )

    type__ = db.Column(
        TINYINT(unsigned=True),
        nullable=False,
        default=db.cast(0, TINYINT())
    )

    endpoint_params = db.relationship(
        'APIEndpointParam',
        back_populates="api_endpoint",
        cascade="all, delete",
        lazy='select',
    )

    endpoint_headers = db.relationship(
        'APIEndpointHeader',
        back_populates="api_endpoint",
        cascade="all, delete",
        lazy='select',
    )

    endpoint_bodies = db.relationship(
        'APIEndpointBody',
        back_populates="api_endpoint",
        cascade="all, delete",
        lazy='select',
    )

    endpoint_extras = db.relationship(
        'APIEndpointExtra',
        back_populates="api_endpoint",
        cascade="all, delete",
        lazy='select',
    )

    def __repr__(self):
        """Show info about API Endpoint"""
        return (
            "<APIEndpoint "
            f"id={str(self.id)} "
            
            f"api_id={str(self.api_id)} "
            
            f"api={str(self.api)[:24]} "
            
            f"nice_name={str(self.nice_name)} " +

            (f"nice_category={str(self.nice_category)} "
             if self.nice_category is not None else '') +
            
            (f"nice_description={str(self.nice_description)[:24]} "
             if (self.nice_description is not None and
             len(self.nice_description) != 0) else '') +
            
            f"http_method={str(self.http_method)} "
            
            f"http_path={str(self.http_path)} " +
            
            (f"http_path_suffix={str(self.http_path_suffix)} "
             if self.http_path_suffix is not None else '') +
            
            f"disabled={str(self.disabled)} " +
            
            f"type={str(self.type__)} " +
            
            (f"api_endpoint_params={str(self.endpoint_params)[:24]} "
             if self.endpoint_params is not None else '') +
            
            (f"api_endpoint_headers={str(self.endpoint_headers)[:24]} "
             if self.endpoint_headers is not None else '') +
            
            (f"api_endpoint_bodies={str(self.endpoint_bodies)[:24]} "
             if self.endpoint_bodies is not None else '') +
            
            (f"api_endpoint_extras={str(self.endpoint_extras)[:24]}"
             if self.endpoint_extras is not None else '') +
            
            ">")

    def to_dict(self):
        """
        Convert an API Endpoint into a dictionary which can be received by a
        client as an object using REST or Jinja template.
        """
        return {
            'id': self.id,
            'api_id': str(self.api_id),
            'nice_name': str(self.nice_name),
            'nice_description': self.nice_description,
            'http_method': str(self.http_method),
            'http_path': str(self.http_path),
            'http_path_suffix': str(self.http_path_suffix),
            'disabled': str(self.disabled),
            'type': str(self.type__),
            'api_endpoint_params': str(self.endpoint_params),
            'api_endpoint_headers': str(self.endpoint_headers),
            'api_endpoint_bodies': str(self.endpoint_bodies),
            'api_endpoint_extras': str(self.endpoint_extras),
        }

    def to_dict_get_api_endpoint_name_id(self):
        """
        Convert an API Key from a Selective Load for the
        admin_query_get_api_endpoint_name_id REST endpoint.
        Loads ID and Nice Name only.
        """
        return {
            'id': self.id,
            'nice_name': self.nice_name
        }

    def to_dict_get_api_endpoint_description_only(self):
        """
        Convert an API Key from a Selective Load for the
        admin_query_get_api_endpoint_description REST endpoint.
        Loads nice_description only.
        """
        return {
            'nice_description': self.nice_description,
        }

    def to_dict_dashboard_template(self):
        """
        Convert an API Endpoint into a dictionary which can be received by a
        client as an object using REST or Jinja template.
        Loads data required for the dashboard template only.

        id
        nice_name
        get_nice_type()
        nice_description
        api.host
        api.nice_name

        """
        return {
            'id': self.id,
            'api_id': str(self.api_id),
            'nice_name': self.nice_name,
            'nice_description': self.nice_description[0:80]
            if self.nice_description is not None else '',
            'disabled': str(self.disabled),
            'type': api_endpoint_type_to_description(self.type__)
            if self.type__ is not None else '',
            'api_nice_name': str(self.api.nice_name),
            'api_host': str(self.api.host),
        }

    def get_nice_type(self):
        """
        Converts the type of the Endpoint to a human-readable text string based
        on the IntEnum value.
        """
        return api_endpoint_type_to_description(self.type__)
