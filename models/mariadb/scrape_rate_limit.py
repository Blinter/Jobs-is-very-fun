"""
DB Models
MariaDB
Scrape Rate Limit Table
"""
from sqlalchemy import text, FetchedValue
from sqlalchemy.dialects.mysql import VARCHAR, BIT, INTEGER, DATETIME
from extensions_sql import db


class ScrapeRateLimits(db.Model):
    """
    Part of the scraping routine process,
    whenever a domain is queried, it will be checked against a soft-limit.
    It can be fine-tuned after a domain has been added.
    The routine will automatically add new domains to the table.
    New proxies will also automatically be added once used.
    The proxy will automatically disable based on scraping settings.
    """
    __bind_key__ = "mariadb"

    __tablename__ = "ScrapeRateLimit"

    id = db.Column(
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
        nullable=False
    )

    domain = db.Column(
        VARCHAR(length=255),
        nullable=False,
        unique=False
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
        nullable=False,
        default=12
    )

    minute_limit = db.Column(
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

    proxy = db.Column(
        VARCHAR(length=255),
        nullable=False,
        unique=False,

    )

    disabled = db.Column(
        BIT(length=1),
        nullable=False,
        default=False
    )

    def __repr__(self):
        """Show info about Scrape Rate Limit"""
        return ("<ScrapeRateLimit "
                f"id={str(self.id)} "
                "domain= " + str(self.domain)[:24] + " "
                f"proxy={str(self.proxy)} " +

                (f"month_limit={str(self.month_limit)} "
                 if self.month_limit is not None else '') +

                (f"daily_limit={str(self.daily_limit)} "
                 if self.daily_limit is not None else '') +

                (f"hour_limit={str(self.hour_limit)} "
                 if self.hour_limit is not None else '') +

                (f"minute_limit={str(self.minute_limit)} "
                 if self.minute_limit is not None else '') +

                f"last_access={str(self.last_access)} " +

                (f"next_access={str(self.next_access)} "
                 if self.next_access is not None else '') +

                f"disabled={str(self.disabled)} "
                ">")

    def to_dict_rest(self):
        """
        Convert a Scrape Rate Limit into a dictionary which can be received by
        a client as an object using REST.
        """
        return {
            'id': self.id,
            'domain': str(self.domain),
            'proxy': str(self.proxy),

            'month_limit': self.month_limit,
            'daily_limit': self.daily_limit,
            'hour_limit': self.hour_limit,
            'minute_limit': self.minute_limit,

            'last_access': str(self.last_access)[5:-7],
            'next_access': str(self.next_access)[5:-7],
            'disabled': str(self.disabled)
        }

    def to_dict_get_last_access_only(self):
        """
        Convert a Scrape Rate Limit from a Selective Load
        """
        return {
            'last_access': str(self.last_access)[5:-7],
        }

    def to_dict_jinja(self):
        """
        Convert a Scrape Rate Limit into a dictionary which can be interpreted
        by a jinja template.
        """
        return {
            'id': self.id,
            'domain': str(self.domain),
            'proxy': str(self.proxy),
            'month_limit': self.month_limit,
            'daily_limit': self.daily_limit,
            'hour_limit': self.hour_limit,
            'minute_limit': self.minute_limit,
            'last_access': str(self.last_access)[5:-7],
            'next_access': str(self.next_access)[5:-7],
            'disabled': str(self.disabled)
        }
