from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hashed(password: str):
    """Hashing the user password"""

    return pwd_context.hash(password)


def verify(plain_password: str, hashed_password: str):
    """Verify that the user password is correct"""

    return pwd_context.verify(plain_password, hashed_password)
