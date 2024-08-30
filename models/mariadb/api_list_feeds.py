"""
DB Models
MariaDB
API List Feed Table
"""

from sqlalchemy.dialects.mysql import BIGINT, VARCHAR
from extensions_sql import db


class APIListFeed(db.Model):
    """
    This is part of the Admin Dashboard.
    Admins can add additional feeds that can be scraped or visited.

    Since scraping the data may be difficult, the list of websites to check
    may be stored here for later.
    """
    __bind_key__ = "mariadb"

    __tablename__ = "APIListFeeds"

    id = db.Column(
        BIGINT(unsigned=True),
        primary_key=True,
        autoincrement=True,
        nullable=False
    )

    url = db.Column(
        VARCHAR(length=255),
        nullable=False,
        unique=True
    )

    def __repr__(self):
        """Show info about API List Feed"""
        return ("<APIListFeed "
                f"id={str(self.id)} "
                
                f"url={str(self.url)[:24]} "
                
                ">")
