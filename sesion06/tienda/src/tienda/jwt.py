from joserfc import jwt, jwk
from os import getenv
import time

JWT_SECRET=getenv('JWT_SECRET')
key = jwk.import_key(JWT_SECRET, "oct")

def encode(data) -> str:
    payload = {
        "data": data,
        "exp": int(time.time()) + 3600,
    }
    return jwt.encode(
        {"alg": "HS256"},
        payload,
        key
    )
