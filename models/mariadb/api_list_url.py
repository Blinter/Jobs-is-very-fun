"""
DB Models
MariaDB
API LIST URL Table
"""
from sqlalchemy import text, FetchedValue
from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, BIT, INTEGER, DATETIME
from extensions_sql import db


class APIListURL(db.Model):
    """
    This is part of the Admin Dashboard.
    Admins can add additional feeds that can be scraped or visited.

    Since scraping the data may be difficult, the list of APIs to check
    may be stored here for later.

    Limit columns are added so that the scraper does not receive errors when
    sending requests.
    """
    __bind_key__ = "mariadb"

    __tablename__ = "APIListURL"

    id = db.Column(
        BIGINT(unsigned=True),
        primary_key=True,
        autoincrement=True,
        nullable=False
    )

    nice_name = db.Column(
        VARCHAR(length=255),
        nullable=False,
        unique=False
    )

    host = db.Column(
        VARCHAR(length=255),
        nullable=False,
        unique=False
    )

    url = db.Column(
        VARCHAR(length=255),
        nullable=False,
        unique=True
    )

    per_ip_restriction = db.Column(
        BIT(length=1),
        nullable=False,
        default=True
    )

    requests_count = db.Column(
        BIGINT(unsigned=True),
        nullable=False,
        default=0
    )

    failed_count = db.Column(
        BIGINT(unsigned=True),
        nullable=False,
        default=0
    )

    sub_required = db.Column(
        BIT(length=1),
        nullable=False,
        default=False
    )

    special_restrictions = db.Column(
        BIT(length=1),
        nullable=False,
        default=False
    )

    unrestricted = db.Column(
        BIT(length=1),
        nullable=False,
        default=False
    )

    month_limit = db.Column(
        INTEGER(unsigned=True),
        nullable=True
    )

    daily_limit = db.Column(
        INTEGER(unsigned=True),
        nullable=True
    )

    hour_limit = db.Column(
        INTEGER(unsigned=True),
        nullable=True
    )

    minute_limit = db.Column(
        INTEGER(unsigned=True),
        nullable=True
    )

    second_limit_per = db.Column(
        INTEGER(unsigned=True),
        nullable=True
    )

    disabled = db.Column(
        BIT(length=1),
        nullable=False,
        default=False
    )

    last_access = db.Column(
        DATETIME(fsp=3),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
        server_onupdate=FetchedValue()
    )

    endpoints = db.relationship(
        'APIEndpoint',
        back_populates="api",
        cascade="all, delete",
        lazy='select',
    )

    headers = db.relationship(
        'APIHeader',
        back_populates="api",
        cascade="all, delete",
        lazy='select',
    )

    def __repr__(self):
        """Show info about API LIST URL"""
        return ("<API_List_URL "
                f"id={str(self.id)} "
                
                f"nice_name={str(self.nice_name)[:24]} "
                
                f"host={str(self.host)[:24]} " +
                
                f"url={str(self.url)[:24]} " +
                
                f"per_ip_restriction={str(self.per_ip_restriction)} " +

                (f"requests_count={str(self.requests_count)} "
                 if self.requests_count is not None else '') +
                
                (f"failed_count={str(self.failed_count)} "
                 if self.failed_count is not None else '') +
                
                f"sub_required={str(self.sub_required)} "
                
                f"special_restrictions={str(self.special_restrictions)} "
                
                f"unrestricted={str(self.unrestricted)} " +
                
                (f"month_limit={str(self.month_limit)} "
                 if self.month_limit is not None else '') +

                (f"daily_limit={str(self.daily_limit)} "
                 if self.daily_limit is not None else '') +

                (f"hour_limit={str(self.hour_limit)} "
                 if self.hour_limit is not None else '') +

                (f"minute_limit={str(self.minute_limit)} "
                 if self.minute_limit is not None else '') +

                (f"second_limit_per={str(self.second_limit_per)} "
                 if self.second_limit_per is not None else '') +
                
                f"disabled={str(self.disabled)} "
                
                f"last_access={str(self.last_access)} " +

                (f"endpoints={str(self.endpoints)[:24]} "
                 if self.endpoints is not None else '') +

                (f"headers={str(self.headers)[:24]} "
                 if self.headers is not None else '') +
                
                ">")

    def to_dict_rest(self):
        """
        Convert a API URL into a dictionary which can be received by a client
        as an object using REST.
        """
        return {
            'id': self.id,
            'nice_name': self.nice_name,
            'host': self.host,
            'url': self.url,
            'per_ip_restriction': self.per_ip_restriction,
            'requests_count': self.requests_count,
            'failed_count': self.failed_count,
            'sub_required': self.sub_required,
            'special_restrictions': self.special_restrictions,
            'unrestricted': self.unrestricted,
            'month_limit': self.month_limit,
            'daily_limit': self.daily_limit,
            'hour_limit': self.hour_limit,
            'minute_limit': self.minute_limit,
            'second_limit_per': self.second_limit_per,
            'disabled': str(self.disabled),
            'endpoints': str(self.endpoints),
            'headers': str(self.headers),
            'last_access': str(self.last_access)[5:-3],
        }

    def to_dict_jinja(self):
        """
        Convert a API URL into a dictionary which can be interpreted by a
        jinja template.
        """
        return {
            'id': self.id,

            'nice_name': str(self.nice_name),

            'host': str(self.host),

            'url': str(self.url)
            .replace("https://", "")
            .replace("http://", ""),

            'per_ip_restriction': self.per_ip_restriction,

            'requests_count': self.requests_count,

            'failed_count': self.failed_count,

            'sub_required': self.sub_required,

            'special_restrictions': self.special_restrictions,

            'unrestricted': self.unrestricted,

            'month_limit': self.month_limit,
            'daily_limit': self.daily_limit,
            'hour_limit': self.hour_limit,
            'minute_limit': self.minute_limit,
            'second_limit_per': self.second_limit_per,

            'disabled': str(self.disabled),
            'endpoints': str(self.endpoints),
            'headers': str(self.headers),
            'last_access': str(self.last_access)[5:-7]
        }

    def to_dict_jinja_api_list(self):
        """
        Convert a API URL into a dictionary specifically for the Admin API
        list administrator page.
        """
        return {
            'id': self.id,

            'nice_name': str(self.nice_name),

            'url': str(self.url)
            .replace("https://", "")
            .replace("http://", ""),

            'requests_count': str(self.requests_count),

            'failed_count': str(self.failed_count),

            'disabled': self.disabled,

            'last_access': str(self.last_access)[5:-7]
        }
