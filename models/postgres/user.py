"""
DB Models
Postgres
User Table
"""

import logging
from flask_bcrypt import Bcrypt
from extensions_sql import db

bcrypt = Bcrypt()


class User(db.Model):
    """
    User Object which holds the data required to use the website.
    Password should always be encrypted and the defined class allows for
    authentication.
    """
    __bind_key__ = "postgres"

    __tablename__ = "users"

    id = db.Column(
        db.BigInteger,
        primary_key=True,
        autoincrement=True
    )

    username = db.Column(
        db.VARCHAR(length=20),
        nullable=True,
        unique=True
    )

    email = db.Column(
        db.VARCHAR(length=128),
        nullable=True
    )

    encrypted_password = db.Column(
        db.Text(),
        nullable=True
    )

    image_url = db.Column(
        db.Text(),
        nullable=True
    )

    image_enabled = db.Column(
        db.Boolean(),
        nullable=True
    )

    github_sso = db.Column(
        db.Boolean(),
        nullable=True
    )

    github_sso_id = db.Column(
        db.String(128),
        nullable=True,
        unique=True
    )

    github_sso_email = db.Column(
        db.String(255),
        nullable=True,
        unique=True
    )

    github_sso_name = db.Column(
        db.String(128),
        nullable=True,
        unique=True
    )

    github_sso_image = db.Column(
        db.String(255),
        nullable=True
    )

    google_sso = db.Column(
        db.Boolean(),
        nullable=True
    )

    google_sso_id = db.Column(
        db.String(128),
        nullable=True,
        unique=True
    )

    google_sso_email = db.Column(
        db.String(255),
        nullable=True,
        unique=True
    )

    google_sso_image = db.Column(
        db.String(255),
        nullable=True
    )

    notes = db.Column(
        db.Text(),
        nullable=True
    )

    profiles = db.relationship(
        'Profile',
        back_populates='user',
        cascade="all, delete",
        lazy='select'
    )

    def encrypt_password(self):
        """Encrypt password using bcrypt"""
        self.encrypted_password = bcrypt.generate_password_hash(
            self.encrypted_password).decode(
            "utf8")
        return self

    def authenticate(self, password):
        """Validate that password is correct.
        Return True if valid; else return False.
        Logs to console if the authentication failed.
        """
        if bcrypt.check_password_hash(self.encrypted_password, password):
            return True
        else:
            logging.warning(f"Authentication failed for user {self.username}.")
            return False

    def authenticate_no_log(self, password):
        """Validate that password is correct.
        This is used for reset password.
        User has already verified their email and this should not be logged.
        Return True if valid; else return False.
        """
        return bcrypt.check_password_hash(self.encrypted_password, password)

    def __repr__(self):
        """Show info about user."""

        return ("<User "
                f"id={str(self.id)} " +

                (f"username={str(self.username)} "
                 if (self.username is not None and
                 len(str(self.username)) > 0) else '') +

                (f"google_sso={str(self.google_sso)} "
                 if self.google_sso is not None else '') +

                (f"github_sso={str(self.github_sso)} "
                 if self.github_sso is not None else '') +

                (f"email={str(self.email)} "
                 if (self.email is not None and
                 len(str(self.email)) > 0) else '') +

                ">")
