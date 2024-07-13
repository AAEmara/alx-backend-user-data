#!/usr/bin/env python3
"""A method that defines Basic Authentication."""

from api.v1.auth.auth import Auth
from base64 import standard_b64decode
import binascii


class BasicAuth(Auth):
    """A class that represents the Basic Authentication.
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Creates a base64 header for Basic Authentication.
        Args:
            authorization_header: Authorization header in the
            Basic Authentication.
        Returns:
            Base64 part of the Authorization Header from the
            Basic Authentication.
        """
        if authorization_header is None:
            return (None)
        elif not isinstance(authorization_header, str):
            return (None)
        elif "Basic " not in authorization_header:
            return (None)

        return authorization_header[len("Basic "):]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """
        """
        if base64_authorization_header is None:
            return (None)
        elif not isinstance(base64_authorization_header, str):
            return (None)
        try:
            value = standard_b64decode(base64_authorization_header)
            return (value.decode("utf-8"))
        except binascii.Error:
            # The input is not a valid Base64.
            return (None)
