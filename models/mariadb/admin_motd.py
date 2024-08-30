"""
DB Models
MariaDB
Admin MOTD Table
"""

from sqlalchemy.dialects.mysql import LONGTEXT, BIGINT
from extensions_sql import db


class AdminMOTD(db.Model):
    """
    This is displayed on the Admin Dashboard. It can be modified and
    additional changes will append to the table, allowing a version history.
    """
    __bind_key__ = "mariadb"

    __tablename__ = "AdminMOTD"

    id = db.Column(
        BIGINT(unsigned=True),
        primary_key=True,
        autoincrement=True,
        nullable=False
    )

    motd = db.Column(
        LONGTEXT(),
        nullable=True
    )

    def __repr__(self):
        """Show info about AdminMOTD"""
        return ("<AdminMOTD " +

                (f"Message={str(self.motd)[:256]} "
                 if (self.motd is not None and
                 len(self.motd) != 0) else '') +

                ">")
