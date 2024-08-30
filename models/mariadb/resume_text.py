"""
DB Models
MariaDB
ResumeText Table
"""
from sqlalchemy.dialects.mysql import MEDIUMTEXT, BIGINT
from extensions_sql import db


class ResumeText(db.Model):
    """
    ResumeText

    A row will be removed when the Profile of a User is deleted.

    This stores the complete resume text provided by a user when a resume is
    uploaded. It will be stored in the Resume table on the Postgres Database.
    """
    __bind_key__ = "mariadb"

    __tablename__ = "ResumeText"

    id = db.Column(
        BIGINT(unsigned=True),
        primary_key=True,
        autoincrement=True,
        nullable=False
    )

    text = db.Column(
        MEDIUMTEXT(),
        nullable=False
    )

    def __repr__(self):
        """Show info about Resume Text."""

        return ("<ResumeText "
                f"id={str(self.id)} " +

                ((("[trunc.] " if len(str(self.text)) > 128 else "") +
                  f"{str(self.text)[:128]} "
                  if len(str(self.text)) > 0 else '')
                 if self.text is not None else '') +
                ">")
