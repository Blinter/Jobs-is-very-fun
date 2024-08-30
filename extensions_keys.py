from secrets_jobs.credentials import (
    jwt_path_to_private_key,
    jwt_path_to_public_key,
    mail_server_mail_from
)
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import jwt


class JWTKeys:
    def __init__(self):
        with open(jwt_path_to_private_key, "rb") as f:
            self._private_key = serialization.load_pem_private_key(
                f.read(),
                password=None,
                backend=default_backend()
            )

        with open(jwt_path_to_public_key, "rb") as f:
            self._public_key = serialization.load_pem_public_key(
                f.read()
            )

    def key_private(self):
        return self._private_key

    def key_public(self):
        return self._private_key

    def sign_payload(
            self,
            payload,
            algorithm=None):
        return jwt.encode(
            payload=payload,
            key=self._private_key,
            algorithm="EdDSA"
            if algorithm is None else algorithm
        )

    def get_payload(
            self,
            payload,
            algorithms=None):
        return jwt.decode(
            jwt=payload,
            key=self._private_key,
            algorithms=["EdDSA"]
            if algorithms is None else algorithms,
            audience=mail_server_mail_from
        )


jwt_keys = JWTKeys()
