"""
DB Models
MariaDB
Proxies Table
"""
from sqlalchemy import text, FetchedValue
from sqlalchemy.dialects.mysql import (MEDIUMINT, TINYINT, VARCHAR, BIGINT,
                                       BIT, DATETIME)
from extensions_sql import db
from enums.proxies import ProxyType


class Proxy(db.Model):
    """
    Proxies are used to prevent the server from reaching IP-based limits when
    scraping or calling an API from different registered accounts.

    This is implemented to mitigate per-user restrictions when crawling an API.
    """
    __bind_key__ = "mariadb"

    __tablename__ = "Proxies"

    id = db.Column(
        MEDIUMINT(unsigned=True),
        primary_key=True,
        autoincrement=True,
        nullable=False
    )

    proxy_type = db.Column(
        TINYINT(unsigned=True),
        nullable=False
    )

    proxy_address = db.Column(
        VARCHAR(length=255),
        nullable=False
    )

    proxy_username = db.Column(
        VARCHAR(length=255),
        nullable=True
    )

    proxy_password = db.Column(
        VARCHAR(length=255),
        nullable=True
    )

    requests = db.Column(
        BIGINT(unsigned=True),
        nullable=True
    )

    failed_requests = db.Column(
        BIGINT(unsigned=True),
        nullable=True
    )

    disabled = db.Column(
        BIT(length=1),
        nullable=False,
        default=False
    )

    auth_required = db.Column(
        BIT(length=1),
        nullable=False,
        default=False
    )

    testing = db.Column(
        BIT(length=1),
        nullable=False,
        default=False
    )

    last_access = db.Column(
        DATETIME(fsp=3),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
        server_onupdate=FetchedValue()
    )

    @staticmethod
    def get_proxy_type(str_proxy):
        for i in ProxyType:
            if str_proxy == i.name:
                return i.value
        return False

    def set_proxy_type(self, str_proxy):
        for i in ProxyType:
            if str_proxy == i.name:
                self.proxy_type = i.value
        return False

    def verify_proxy_type(self):
        for i in ProxyType:
            if self.proxy_type == i.name:
                return True
        return False

    def __repr__(self):
        """Show info about Proxy"""
        return ("<Proxy "                
                f"id={str(self.id)} " +

                (f"proxy_type={str(self.proxy_type)} "
                 if self.verify_proxy_type() else '') +

                (f"proxy_address={str(self.proxy_address)} "
                 if self.proxy_address is not None else '') +

                (f"proxy_username={str(self.proxy_username)} "
                 if self.proxy_username is not None else '') +

                (f"proxy_password={str(self.proxy_password)} "
                 if self.proxy_password is not None else '') +

                (f"requests={str(self.requests)} "
                 if self.requests is not None else '') +

                (f"failed_requests={str(self.failed_requests)} "
                 if self.failed_requests is not None else '') +

                (f"disabled " if self.disabled == 1 else '') +

                (f"auth_required " if self.auth_required == 1 else '') +

                (f"testing " if self.testing == 1 else None) +

                f"last_access={str(self.last_access)} " +

                ">")

    def to_dict_rest(self):
        """
        Convert a profile into a dictionary which can be received by a client
        as an object using REST.
        """
        return {
            'id': self.id,

            'proxy_type': self.proxy_type,

            'proxy_address': self.proxy_address,

            'proxy_username': self.proxy_username
            if self.proxy_username else None,

            'proxy_password': self.proxy_password
            if self.proxy_password else None,

            'requests': int(self.requests)
            if self.requests else None,

            'failed_requests': self.failed_requests
            if self.failed_requests else None,

            'disabled': self.disabled
            if self.disabled else False,

            'auth_required': self.auth_required
            if self.auth_required else False,

            'testing': self.testing
            if self.testing else False,

            'last_access': str(self.last_access)[5:-3]
        }

    def to_dict_jinja(self):
        """
        Convert a proxy into a dictionary which can be interpreted by a
        jinja template.
        """
        return {
            'id': self.id,

            'proxy_type': self.proxy_type,

            'proxy_address': self.proxy_address,

            'proxy_username': self.proxy_username
            if self.proxy_username else None,

            'proxy_password': self.proxy_password
            if self.proxy_password else None,

            'requests': int(self.requests) if self.requests else None,

            'failed_requests': self.failed_requests
            if self.failed_requests else None,

            'disabled': self.disabled if self.disabled else False,

            'auth_required': self.auth_required
            if self.auth_required else False,

            'testing': self.testing if self.testing else False,

            'last_access': str(self.last_access)[5:-7]
        }
