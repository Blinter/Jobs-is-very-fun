"""
DB Models
MariaDB
API Endpoint Extras Table
"""
from sqlalchemy.dialects.mysql import BIGINT, LONGTEXT
from extensions_sql import db


class APIEndpointExtra(db.Model):
    """
    An API Endpoint can one or more additional extra docs.

    These extras can be modified from the dashboard.
    """
    __bind_key__ = "mariadb"

    __tablename__ = "APIEndpointExtras"

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
        back_populates='endpoint_extras',
        lazy='select',
        viewonly=True
    )

    extra_documentation = db.Column(
        LONGTEXT(),
        nullable=True,
        unique=False
    )

    def __repr__(self):
        """Show info about API Endpoint Extra"""
        return ("<APIEndpointBody "
                f"id={str(self.id)} "
                
                f"api_endpoint_id={str(self.api_endpoint_id)} "
                
                f"api_endpoint={str(self.api_endpoint)[:24]} " +

                (f"extra_documentation={str(self.extra_documentation)} "
                 if (self.extra_documentation is not None and
                 len(str(self.extra_documentation)) != 0) else '') +

                ">")

    def to_dict(self):
        """
        Convert an API Endpoint Extra into a dictionary which can be received
        by a client as an object using REST or Jinja Template.
        """
        return {
            'id': self.id,
            'api_endpoint_id': self.api_endpoint_id,
            'extra_documentation': str(self.extra_documentation)
        }

    def to_dict_id_only(self):
        """
        Convert an API Key from a Selective Load for the
        admin_query_get_api_endpoint_extra_doc_list REST endpoint.
        """
        return {
            'id': self.id
        }

    def to_dict_extra_doc_only(self):
        """
        Convert an API Key from a Selective Load for the
        admin_query_get_api_endpoint_extra_doc_list REST endpoint.
        """
        return self.extra_documentation
