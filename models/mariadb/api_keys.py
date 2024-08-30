"""
DB Models
MariaDB
API Keys Table
"""
from sqlalchemy import text, FetchedValue
from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, BIT, INTEGER, DATETIME
from extensions_sql import db


class APIKey(db.Model):
    """
    This is part of the Admin Dashboard.
    Admins can add keys if the API requires an API key to access it.

    Since scraping the data may be difficult, the original API from
    API List URLs may be removed and the keys will be saved here to be
    deleted later.

    Next Request is calculated by the server and then updated when the API is
    queried again.
    """
    __bind_key__ = "mariadb"

    __tablename__ = "APIKeys"

    id = db.Column(
        BIGINT(unsigned=True),
        primary_key=True,
        autoincrement=True,
        nullable=False
    )

    url = db.Column(
        VARCHAR(length=255),
        nullable=False,
        unique=False
    )

    key = db.Column(
        VARCHAR(length=255),
        nullable=False,
        unique=False
    )

    special_limits = db.Column(
        BIT(length=1),
        nullable=False,
        default=False
    )

    custom_month_limit = db.Column(
        INTEGER(unsigned=True),
        nullable=True
    )

    custom_daily_limit = db.Column(
        INTEGER(unsigned=True),
        nullable=True
    )

    custom_hour_limit = db.Column(
        INTEGER(unsigned=True),
        nullable=True
    )

    custom_minute_limit = db.Column(
        INTEGER(unsigned=True),
        nullable=True
    )

    custom_second_limit_per = db.Column(
        INTEGER(unsigned=True),
        nullable=True
    )

    last_access = db.Column(
        DATETIME(fsp=3),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
        server_onupdate=FetchedValue()
    )

    next_access = db.Column(
        DATETIME(fsp=3),
        nullable=True
    )

    preferred_proxy = db.Column(
        VARCHAR(length=255),
        nullable=False,
        unique=False,
        default=''
    )

    disabled = db.Column(
        BIT(length=1),
        nullable=False,
        default=False
    )

    def __repr__(self):
        """Show info about API Key"""
        return ("<APIKey "
                f"id={str(self.id)} "
                
                "url= " + ((str(self.url)
                            .replace(str('www.'), '')
                            .replace('https://', '')
                            .replace('http://', ''))[:24]) + " "
                                                             
                f"key={str(self.key)} " +

                f"special_limits={str(self.self.special_limits)} " +

                (((f"custom_month_limit={str(self.custom_month_limit)} "
                   if self.custom_month_limit is not None else '') +

                  (f"custom_daily_limit={str(self.custom_daily_limit)} "
                   if self.custom_daily_limit is not None else '') +

                  (f"custom_hour_limit={str(self.custom_hour_limit)} "
                   if self.custom_hour_limit is not None else '') +

                  (f"custom_minute_limit={str(self.custom_minute_limit)} "
                   if self.custom_minute_limit is not None else '') +

                  ("custom_second_limit_per="
                   f"{str(self.custom_second_limit_per)} "
                   if self.custom_second_limit_per is not None else ''))

                 if self.special_limits else "") +

                f"last_access={str(self.last_access)} " +
                
                (f"next_access={str(self.next_access)} "
                 if self.next_access is not None else '') +
                
                f"preferred_proxy={str(self.preferred_proxy)} "
                
                f"disabled={str(self.disabled)} "
                
                ">")

    def to_dict_rest(self):
        """
        Convert an API Key into a dictionary which can be received by a client
        as an object using REST.
        """
        return {
            'id': self.id,
            'url': str(self.url)
            .replace("www.", "")
            .replace("https://", "")
            .replace("http://", ""),
            'key': self.key,
            'last_access': str(self.last_access)[5:-7],
            'next_access': str(self.next_access)[5:-7],
            'special_limits': self.special_limits,
            'custom_month_limit': self.custom_month_limit,
            'custom_daily_limit': self.custom_daily_limit,
            'custom_hour_limit': self.custom_hour_limit,
            'custom_minute_limit': self.custom_minute_limit,
            'second_limit_per': self.second_limit_per,
            'preferred_proxy': str(self.preferred_proxy),
            'disabled': str(self.disabled)
        }

    def to_dict_get_api_key_id_key(self):
        """
        Convert an API Key from a Selective Load for the
        admin_query_get_api_key_id_key REST endpoint.
        """
        return {
            'id': self.id,
            'key': self.key
        }

    def to_dict_get_api_keys_last_access_only(self):
        """
        Convert an API Key from a Selective Load for the
        admin_query_get_api_key_last_access REST endpoint.
        """
        return {
            'last_access': str(self.last_access)[5:-7],
        }

    def to_dict_jinja(self):
        """
        Convert a API Key into a dictionary which can be interpreted by a
        jinja template.
        """
        return {
            'id': self.id,
            'nice_name': str(self.nice_name),
            'url': str(self.url)
            .replace("www.", "")
            .replace("https://", "")
            .replace("http://", ""),
            'key': str(self.key),
            'special_limits': self.special_limits,
            'custom_month_limit': self.custom_month_limit,
            'custom_daily_limit': self.custom_daily_limit,
            'custom_hour_limit': self.custom_hour_limit,
            'custom_minute_limit': self.custom_minute_limit,
            'last_access': str(self.last_access)[5:-7],
            'next_access': str(self.next_access)[5:-7],
            'preferred_proxy': str(self.preferred_proxy),
            'disabled': str(self.disabled)
        }
