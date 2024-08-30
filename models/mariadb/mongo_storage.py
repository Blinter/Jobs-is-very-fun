"""
DB Models
MariaDB
Mongo Storage Table
"""
from sqlalchemy.dialects.mysql import (
    BIGINT,
    VARCHAR,
    SMALLINT,
    LONGTEXT,
    DATETIME,
    BINARY,
    JSON,
    BIT
)
from extensions_sql import db


class MongoStorage(db.Model):
    """
    Stores data queried by the server and checks against this data.

    When a request is sent, this table is checked against, and data can be
    pulled from the MongoDB instead of requesting from the API, saving
    requested data against the limits.
    """
    __bind_key__ = "mariadb"

    __tablename__ = "MongoStorage"

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

    api = db.Column(
        VARCHAR(length=255),
        nullable=False
    )

    api_key = db.Column(
        VARCHAR(length=255),
        nullable=True
    )

    # instead of filling out API Key and Proxy, use the next available API
    # Key and preferred proxy.
    api_key_auto = db.Column(
        BIT(length=1),
        nullable=True,
        default=True
    )

    url = db.Column(
        LONGTEXT(),
        nullable=False
    )

    endpoint_nice_name = db.Column(
        VARCHAR(length=255),
        nullable=False
    )

    input_json = db.Column(
        JSON(),
        nullable=False,
        default=''
    )

    def __repr__(self):
        """Show info about Mongo_Storage"""
        return ("<MongoStorage "
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

                (f"api={str(self.api)[:24]} "
                 if self.api is not None else '') +
                
                (f"api_key={str(self.api_key)[:24]} "
                 if self.api_key is not None else '') +

                (f"api_key_auto={str(self.api_key_auto)} "
                 if self.api_key_auto is not None else '') +
                
                f"url={str(self.url)[:24]} "
                
                f"endpoint_nice_name={str(self.endpoint_nice_name)[:24]} "
                
                f"input_json={str(self.input_json)[:24]} "
                
                ">")

    def to_dict_rest(self):
        """
        Convert a Mongo Storage row into a dictionary which can be received by a
        client as an object using REST.
        """
        return {
            'id': self.id,
            'object_id': str(self.object_id),
            'query_time': self.query_time,
            'length': self.length
            if (self.length is not None and
                isinstance(self.length, int) and
                self.length != 0)
            else None,
            'data_truncated': self.data_truncated
            if (self.data_truncated is not None and
                isinstance(self.data_truncated, str) and
                len(self.data_truncated) != 0 and self.data_truncated != ' ')
            else None,
            'code': self.code,
            'time': self.time,
            'proxy': self.proxy
            if (self.proxy is not None and
                isinstance(self.proxy, str) and
                len(self.proxy) != 0 and
                self.proxy != ' ')
            else None,
            'api': self.api,
            'api_key': self.api_key
            if (self.api_key is not None and
                isinstance(self.api_key, str) and
                len(self.api_key) != 0 and
                self.api_key != ' ')
            else None,
            'url': self.url,
            'endpoint_nice_name': self.endpoint_nice_name,
            'input_json': self.input_json
        }

    def to_dict_jinja(self):
        """
        Convert a Mongo Storage row into a dictionary which can be interpreted
        by a jinja template.
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
            'api': self.api,
            'api_key': self.api_key,
            'url': self.url,
            'endpoint_nice_name': self.endpoint_nice_name,
            'input_json': self.input_json
        }
