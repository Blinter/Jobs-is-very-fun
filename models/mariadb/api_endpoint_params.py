"""
DB Models
MariaDB
API Endpoint Params Table
"""
from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, BIT, TEXT
from extensions_sql import db


class APIEndpointParam(db.Model):
    """
    An API Endpoint can one or more additional parameters.

    These parameters can be added in manually from the dashboard.
    """
    __bind_key__ = "mariadb"

    __tablename__ = "APIEndpointParams"

    id = db.Column(
        BIGINT(unsigned=True),
        primary_key=True,
        autoincrement=True,
        nullable=False
    )

    api_endpoint_id = db.Column(
        BIGINT(unsigned=True),
        db.ForeignKey('APIEndpoints.id'),
        nullable=False
    )

    api_endpoint = db.relationship(
        'APIEndpoint',
        back_populates='endpoint_params',
        lazy='select',
        viewonly=True
    )

    param = db.Column(
        VARCHAR(length=255),
        nullable=False,
        unique=False
    )

    description = db.Column(
        TEXT(),
        nullable=False,
        unique=False
    )

    hint_type = db.Column(
        VARCHAR(length=255),
        nullable=False,
        unique=False
    )

    # Could include a URL
    default_value = db.Column(
        VARCHAR(length=2048),
        nullable=True,
        unique=False
    )

    # a param usually includes only one path param.
    path_param = db.Column(
        BIT(length=1),
        nullable=False,
        default=False
    )

    required = db.Column(
        BIT(length=1),
        nullable=False,
        default=False
    )

    disabled = db.Column(
        BIT(length=1),
        nullable=False,
        default=False
    )

    def __repr__(self):
        """Show info about API Endpoint Param"""
        return ("<APIEndpointParam "
                f"id={str(self.id)} "
                
                f"api_endpoint_id={str(self.api_endpoint_id)} "
                
                f"api_endpoint={str(self.api_endpoint)[:24]} "
                
                f"param={str(self.param)} "
                
                f"description={str(self.description)[:24]} " +

                f"hint_type={self.hint_type} " +

                (f"default_value={self.default_value} "
                 if (self.default_value and
                     len(str(self.default_value)) > 0) else '') +

                (f"path_param "
                 if self.path_param == 1 else '') +

                (f"required "
                 if self.required == 1 else '') +

                (f"disabled "
                 if self.disabled == 1 else '') +

                ">")

    def to_dict(self):
        """
        Convert an API Endpoint into a dictionary which can be received by a
        client as an object using REST or Jinja Template.
        """
        return {
            'id': self.id,
            'api_endpoint_id': self.api_endpoint_id,
            'param': self.param,
            'description': self.description if self.description
            else None,
            'hint_type': self.hint_type if self.hint_type
            else None,
            'default_value': self.default_value if self.default_value
            else None,
            'path_param': self.path_param if self.path_param
            else None,
            'required': self.required,
            'disabled': self.disabled
        }
