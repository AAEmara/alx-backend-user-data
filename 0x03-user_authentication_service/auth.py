#!/usr/bin/env python3
"""A module that defines authentication functions."""

from bcrypt import gensalt, hashpw


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
