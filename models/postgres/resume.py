"""
DB Models
Postgres
Resume Table
"""

from extensions_sql import db


class Resume(db.Model):
    """
    Stores ID of a resume stored in MariaDB.
    When a profile is deleted, the MariaDB data is also deleted.
    """
    __bind_key__ = "postgres"

    __tablename__ = "resumes"

    id = db.Column(
        db.BigInteger,
        primary_key=True,
        autoincrement=True
    )

    mariadb_text_id = db.Column(
        db.BigInteger,
        nullable=True
    )

    profile_id = db.Column(
        db.BigInteger,
        db.ForeignKey('profiles.id'),
        nullable=False
    )

    profile = db.relationship(
        "Profile",
        back_populates="resumes",
        lazy='select',
        viewonly=True
    )

    def __repr__(self):
        """Show info about Resume."""

        return ("<Resume "
                f"id={str(self.id)} " +
                
                (f"mariadb_text_id={str(self.mariadb_text_id)} "
                 if self.mariadb_text_id is not None else '') +
                
                (f"profile={str(self.profile)} "
                 if self.profile_id is not None else '') +

                ">")
