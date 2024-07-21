#!/usr/bin/env python3
"""A module that defines authentication functions."""

from bcrypt import gensalt, hashpw
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Hashes a password and salt.
    Args:
        password: the password to be salted and hashed.
    Returns:
        Salted hash in bytes form.
    """
    # Encoding the password in utf-8.
    password_bytes = password.encode('utf-8')
    # Generating salt.
    salt = gensalt()
    # Hashing the password and salt.
    password_hash = hashpw(password_bytes, salt)
    return (password_hash)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Takes the user credentials and registers a User instance.
        Args:
            email: The user's given email.
            password: The user's given password.
        Returns:
            The registered User object.
        """
        # Retrieving the User instance if it exists.
        try:
            # Searching for the user in the database.
            user = self._db.find_user_by(email=email)
            # if the user exists, we will raise a ValueError.
            if user:
                raise(ValueError(f"User {email} already exists"))
        except AttributeError:
            # if the user doesn't exist, we will hash a password and
            # create the user.
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
        return (new_user)
