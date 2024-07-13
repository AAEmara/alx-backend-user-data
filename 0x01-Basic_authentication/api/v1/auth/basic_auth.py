#!/usr/bin/env python3
"""A method that defines Basic Authentication."""

from api.v1.auth.auth import Auth


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
