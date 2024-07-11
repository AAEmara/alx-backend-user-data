#!/usr/bin/env python3
"""A module that includes the api authentication."""

from flask import request
from typing import List, TypeVar


class Auth:
    """An API Authentication Class.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Authenticates certain paths for the given user.
        Args:
            path: The authenticated path for the user.
            excluded_paths: paths that are not authenticated for the user.
        Returns:
            False
        """
        return (False)

    def authorization_header(self, request=None) -> str:
        """The Authorization HEADER.
        Args:
            request: The request sent by the user.
        Returns:
            None
        """
        return (None)

    def current_user(self, request=None) -> TypeVar('User'):
        """The current user in the authentication process.
        Args:
            request: the request sent by the user.
        Returns:
            None
        """
        return (None)
