"""
DB Models
MariaDB
Cache CDN Table
"""
import pytz
from sqlalchemy.dialects.mysql import (DATETIME, BIGINT)
from extensions_sql import db


class DatabaseTimegraph(db.Model):
    """DatabaseTimegraph Object"""
    __bind_key__ = "mariadb"

    __tablename__ = "DatabaseJobTimegraph"

    time = db.Column(
        DATETIME(fsp=0),
        primary_key=True,
        nullable=False
    )

    total = db.Column(
        BIGINT(unsigned=True),
        nullable=False,
    )

    active = db.Column(
        BIGINT(unsigned=True),
        nullable=False,
    )

    expired = db.Column(
        BIGINT(unsigned=True),
        nullable=False,
    )

    def __repr__(self):
        """Show info about Cache CDN"""
        return ("<DatabaseTimegraph "
                
                f"time={str(self.time)} "
                
                f"total={str(self.total)} "
                
                f"active={str(self.active)} "
                
                f"expired={str(self.expired)} "
                
                ">")

    def to_dict_rest(self):
        """
        Convert a DatabaseTimegraph into a dictionary
        which is then sent to the client.
        """
        return {
            'time': self.time,
            'total': self.total,
            'active': self.active,
            'expired': self.expired,
        }
