"""
DB Models
MariaDB
API Endpoint Headers Table
"""
from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, BIT
from extensions_sql import db


class APIEndpointHeader(db.Model):
    """
    An API Endpoint can one or more additional headers.

    These headers can be modified from the dashboard.
    """
    __bind_key__ = "mariadb"

    __tablename__ = "APIEndpointHeaders"

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
        back_populates='endpoint_headers',
        lazy='select',
        viewonly=True
    )

    header = db.Column(
        VARCHAR(length=255),
        nullable=False,
        unique=False
    )

    value = db.Column(
        VARCHAR(length=255),
        nullable=True,
        unique=False
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
        """Show info about API Endpoint Header"""
        return ("<APIEndpointHeader "
                f"id={str(self.id)} "
                
                f"api_endpoint_id={str(self.api_endpoint_id)} "
                
                f"api_endpoint={str(self.api_endpoint)[:24]} "
                
                f"header={str(self.header)} " +

                (f"value={str(self.value)} "
                 if (self.value is not None and
                 len(str(self.value)) > 0) else '') +

                (f"required " if self.required == 1 else '') +

                (f"disabled " if self.disabled == 1 else '') +

                ">")

    def to_dict(self):
        """
        Convert an API Endpoint Header into a dictionary which can be received
        by a client as an object using REST or Jinja Template.
        """
        return {
            'id': self.id,
            'api_endpoint_id': self.api_endpoint_id,
            'header': self.header,
            'value': self.value,
            'required': self.required,
            'disabled': str(self.disabled)
        }
