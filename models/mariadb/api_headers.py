"""
DB Models
MariaDB
API Headers Table
"""
from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, BIT
from extensions_sql import db


class APIHeader(db.Model):
    """
    An API can one or more additional default headers.

    These headers can be modified from the dashboard.
    """
    __bind_key__ = "mariadb"

    __tablename__ = "APIHeaders"

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
        back_populates="headers",
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

    api_key_header = db.Column(
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
        """Show info about API Header"""
        return ("<APIHeader "
                f"id={str(self.id)} "
                
                f"api_id={str(self.api_id)} "
                
                f"api={str(self.api)[:24]} "
                
                f"header={str(self.header)} " +

                (f"value={str(self.value)} "
                 if self.value is not None else '') +

                f"required={str(self.required)} "
                
                f"api_key_header={str(self.api_key_header)} "
                
                f"disabled={str(self.disabled)} "
                
                ">")

    def to_dict(self):
        """
        Convert an API Header into a dictionary which can be received
        by a client as an object using REST or Jinja Template.
        """
        return {
            'id': self.id,
            'api_id': self.api_id,
            'header': self.header,
            'value': self.value,
            'required': self.required,
            'api_key_header': str(self.api_key_header),
            'disabled': str(self.disabled)
        }
