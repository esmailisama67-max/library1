from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "mysecretkey"

ALGORITHM = "HS256"


def create_access_token(data: dict):

    payload = data.copy()

    payload["exp"] = (
        datetime.utcnow()
        + timedelta(minutes=15)
    )

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

def create_refresh_token(data):

    payload = data.copy()

    payload["exp"] = (
        datetime.utcnow() +
        timedelta(days=30)
    )


    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    
def verify_token(token: str):

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload

    except JWTError:
        return None