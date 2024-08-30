"""
DB Models
MariaDB
Mongo Scrape Storage Table
"""
from sqlalchemy.dialects.mysql import (
    BIGINT,
    VARCHAR,
    SMALLINT,
    LONGTEXT,
    DATETIME,
    BINARY,
    JSON
)
from extensions_sql import db
from sqlalchemy import event, text


class MongoScrapeStorage(db.Model):
    """
    Stores data queried by the server and checks against this data.

    When a request is sent, this table is checked against, and data can be
    pulled from the MongoDB instead of requesting from the API, saving
    requested data against the limits.
    """
    __bind_key__ = "mariadb"

    __tablename__ = "MongoScrapeStorage"

    id = db.Column(
        BIGINT(unsigned=True),
        primary_key=True,
        autoincrement=True,
        nullable=False
    )

    object_id = db.Column(
        BINARY(length=12),
        nullable=True,
        unique=True
    )

    query_time = db.Column(
        DATETIME(fsp=3),
        nullable=True,
    )

    length = db.Column(
        BIGINT(unsigned=True),
        nullable=True
    )

    data_truncated = db.Column(
        LONGTEXT(),
        nullable=True
    )

    code = db.Column(
        SMALLINT(display_width=4,
                 unsigned=True),
        nullable=True
    )

    time = db.Column(
        DATETIME(fsp=3),
        nullable=False,
    )

    proxy = db.Column(
        VARCHAR(length=255),
        nullable=True
    )

    url = db.Column(
        LONGTEXT(),
        nullable=False,
        unique=True,
        # mysql_collate='utf8mb4_bin' # Not supported
    )

    url_ref_key = db.Column(
        LONGTEXT(),
        nullable=False,
        unique=False,
    )

    headers = db.Column(
        JSON(),
        nullable=True,
        default=None
    )

    def __repr__(self):
        """Show info about MongoScrapeStorage"""
        return ("<MongoScrapeStorage "
                f"id={str(self.id)} " +
                
                (f"object_id={str(self.object_id)[:24]} "
                 if self.object_id is not None else '') +
                
                (f"query_time={str(self.query_time)} "
                 if self.query_time is not None else '') +
                
                (f"length={str(self.length)[:24]} "
                 if self.length is not None else '') +

                (f"data_truncated={str(self.data_truncated)[:24]} "
                 if self.data_truncated is not None else '') +
                
                (f"code={str(self.code)[:24]} "
                 if self.code is not None else '') +
                
                f"time={str(self.time)} " +
                
                (f"proxy={str(self.proxy)[:24]} "
                 if self.proxy is not None else '') +
                
                f"url={str(self.url)[:24]} "
                
                f"url_ref_key={str(self.url_ref_key)[:24]} " +
                
                (f"headers={str(self.headers)[:24]} "
                 if self.headers is not None else '') +
                
                ">")

    def to_dict_rest(self):
        """
        Convert a Mongo Scrape Storage row into a dictionary which can be
        received by a client as an object using REST.
        """
        return {
            'id': self.id,
            'object_id': str(self.object_id),
            'query_time': self.query_time,
            'length': self.length,
            'data_truncated': self.data_truncated,
            'code': self.code,
            'time': self.time,
            'proxy': self.proxy,
            'url': self.url,
            'url_ref_key': self.url_ref_key,
            'headers': self.headers,
        }

    def to_dict_jinja(self):
        """
        Convert a Mongo Scrape storage row into a dictionary which can be
        interpreted by a jinja template.
        """
        return {
            'id': self.id,
            'object_id': str(self.object_id),
            'query_time': self.query_time,
            'length': self.length,
            'data_truncated': self.data_truncated,
            'code': self.code,
            'time': self.time,
            'proxy': self.proxy,
            'url': self.url,
            'url_ref_key': self.url_ref_key,
            'headers': self.headers,
        }


# Define the event to alter the column after table creation
@event.listens_for(MongoScrapeStorage.__table__, 'after_create')
def set_url_collation(target, connection, **kwargs):
    sql = text(f"""
        ALTER TABLE {MongoScrapeStorage.__tablename__}
        MODIFY url LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;
    """)
    connection.execute(sql)
