"""
DB Models
MariaDB
Database Routines Table
"""
from sqlalchemy import (
    text,
    FetchedValue,
    Interval
)
from sqlalchemy.dialects.mysql import (
    BIGINT,
    BIT,
    TINYINT,
    DATETIME,
    JSON,
    LONGTEXT,
    VARCHAR,
)
from extensions_sql import db


class DatabaseRoutines(db.Model):
    """
    Database Routines
    Specify API requests or call database routines by file on a regular schedule

    """
    __bind_key__ = "mariadb"

    __tablename__ = "Database Routines"

    id = db.Column(
        BIGINT(unsigned=True),
        primary_key=True,
        autoincrement=True,
        nullable=False
    )

    type__ = db.Column(
        TINYINT(length=1),
        nullable=False,
        default=False
    )

    disabled = db.Column(
        BIT(length=1),
        nullable=False,
        default=False
    )

    processing = db.Column(
        BIT(length=1),
        nullable=False,
        default=False
    )

    last_run = db.Column(
        DATETIME(),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
        server_onupdate=FetchedValue()
    )

    frequency = db.Column(
        Interval(),
        nullable=True,
        unique=False,
    )

    input_json = db.Column(
        JSON(),
        nullable=True,
        default=''
    )

    url = db.Column(
        LONGTEXT(),
        nullable=True
    )

    endpoint_nice_name = db.Column(
        VARCHAR(length=255),
        nullable=True
    )

    api_key_auto = db.Column(
        BIT(length=1),
        nullable=True,
        default=True
    )

    proxy = db.Column(
        VARCHAR(length=255),
        nullable=True
    )

    api = db.Column(
        VARCHAR(length=255),
        nullable=True
    )

    api_key = db.Column(
        VARCHAR(length=255),
        nullable=True
    )

    current_counter = db.Column(
        BIGINT(unsigned=True),
        primary_key=True,
        autoincrement=True,
        nullable=True
    )

    def __repr__(self):
        """Show info about Database Routines"""
        return (
            "<DatabaseRoutines "
            f"id={str(self.id)} "
            
            f"type={str(self.keyword_id)} "

            f"count={str(self.type__)} "
            f"disabled={str(self.disabled)} "
            f"processing={str(self.processing)} "
            f"last_run={str(self.last_run)} "
            f"frequency={str(self.frequency)} "
            f"input_json={str(self.input_json)} "
            f"url={str(self.url)} "
            f"endpoint_nice_name={str(self.endpoint_nice_name)} "
            f"api_key_auto={str(self.api_key_auto)} "
            f"proxy={str(self.proxy)} "
            f"api={str(self.api)} "
            f"api_key={str(self.api_key)} "
            
            f"current_counter={str(self.current_counter)} "

            ">")
