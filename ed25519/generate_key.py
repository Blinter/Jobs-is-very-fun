from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization

"""Save EdDSA"""
private_key = Ed25519PrivateKey.generate()

public_key = private_key.public_key()
private_bytes = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

public_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

"""Save Private EdDSA Key"""
with open("EdDSA_private.pem", "wb") as f:
    f.write(private_bytes)

"""Save Public EdDSA Key"""
with open("EdDSA_public.pem", "wb") as f:
    f.write(public_bytes)
