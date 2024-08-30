"""
DB Models
MariaDB
API Endpoint Body Table
"""
from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, BIT, TEXT
from extensions_sql import db


class APIEndpointBody(db.Model):
    """
    An API Endpoint can one or more additional bodies.

    These bodies can be modified from the dashboard.
    """
    __bind_key__ = "mariadb"

    __tablename__ = "APIEndpointBodies"

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
        back_populates='endpoint_bodies',
        lazy='select',
        viewonly=True
    )

    key = db.Column(
        VARCHAR(length=255),
        nullable=False,
        unique=False
    )

    key_description = db.Column(
        TEXT(),
        nullable=True,
        unique=False
    )

    value = db.Column(
        VARCHAR(length=255),
        nullable=True,
        unique=False
    )

    value_hint_type = db.Column(
        VARCHAR(length=255),
        nullable=True,
        unique=False
    )

    value_default = db.Column(
        TEXT(),
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
        """Show info about API Endpoint Body"""
        return ("<APIEndpointBody "
                f"id={str(self.id)} "
                
                f"api_endpoint_id={str(self.api_endpoint_id)} "
                
                f"api_endpoint={str(self.api_endpoint)[:24]} "
                
                f"key={str(self.key)} " +

                (f"key_description={str(self.key_description)[:24]} "
                 if (self.key_description is not None and
                 len(self.key_description) != 0) else '') +

                (f"value={str(self.value)} "
                 if (self.value is not None and
                 len(str(self.value)) != 0) else '') +

                (f"value_hint_type={str(self.value_hint_type)} "
                 if (self.value_hint_type is not None and
                 len(str(self.value_hint_type)) != 0) else '') +

                (f"value_default={str(self.value_default)} "
                 if (self.value_default is not None and
                 len(str(self.value_default)) != 0) else '') +

                ("required " if self.required == 1 else '') +
                ("disabled " if self.disabled == 1 else '') +
                ">")

    def to_dict(self):
        """
        Convert an API Endpoint Body into a dictionary which can be received
        by a client as an object using REST or Jinja Template.
        """
        return {
            'id': self.id,
            'api_endpoint_id': self.api_endpoint_id,
            'key': self.key,

            'key_description': self.key_description
            if self.key_description else None,

            'value': self.value
            if self.value else None,

            'value_hint_type': self.value_hint_type
            if self.value_hint_type else None,

            'value_default': self.value_default
            if self.value_default else None,

            'required': self.required
        }
