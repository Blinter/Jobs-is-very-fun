"""
DB Models
Postgres
Admin Table
"""
import logging
from flask_bcrypt import Bcrypt
from extensions_sql import db

bcrypt = Bcrypt()


class Admin(db.Model):
    """
    Admin
    """
    __bind_key__ = "postgres"

    __tablename__ = "admins"

    id = db.Column(
        db.BigInteger,
        primary_key=True,
        autoincrement=True
    )

    username = db.Column(
        db.VARCHAR(length=20),
        unique=True,
        nullable=False
    )

    email = db.Column(
        db.VARCHAR(length=128),
        nullable=False
    )

    encrypted_password = db.Column(
        db.Text(),
        nullable=False
    )

    notes = db.Column(
        db.Text(),
        nullable=True
    )

    def encrypt_password(self):
        """Encrypt password using bcrypt"""
        self.encrypted_password = bcrypt.generate_password_hash(
            self.email_password).decode(
            "utf8")
        return self

    def authenticate(self, email_password):
        """Validate that password is correct.
        Return True if valid; else return False.
        Logs to console if the authentication failed.
        """
        if bcrypt.check_password_hash(
                self.email_password,
                email_password):
            return True

        else:
            logging.warning(f"Authentication failed for user {self.username}.")
            return False

    def __repr__(self):
        """Show info about Admin."""

        return ("<Admin "                
                f"id={str(self.id)} " +

                (f"email={str(self.email)} "
                 if (self.email is not None and
                     len(self.email) > 0) else "") +

                ">")
