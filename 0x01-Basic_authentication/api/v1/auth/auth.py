#!/usr/bin/env python3
"""A module that includes the api authentication."""

from flask import request
from typing import List, TypeVar


class Auth:
    """An API Authentication Class.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks paths for authentication.
        Args:
            path: The path to be checked for authentication.
            excluded_paths: paths that doesn't require authentication.
        Returns:
            True: if the path is None, or not in excluded_path,
            or if the excluded_paths are not None and it's path doesn't end
            with a slash.
            False: if the path ends with a slash or otherwise the previous
            conditions.
        """
        if (path is None):
            return (True)
        elif (excluded_paths is None):
            return (True)
        elif (len(excluded_paths) == 0):
            return (True)
        elif path in excluded_paths or path + '/' in excluded_paths:
            return (False)
        return (True)

    def authorization_header(self, request=None) -> str:
        """Fetching the Authorization HEADER.
        Args:
            request: The request sent by the user.
        Returns:
            None: if the request is empty of if the `Authorization` header
            is not included in the request.
            Authorization Header Content: if the `Authorization` header
            is available in the request.
        """
        if request is None:
            return (None)
        elif "Authorization" not in request.headers:
            return (None)
        else:
            return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """The current user in the authentication process.
        Args:
            request: the request sent by the user.
        Returns:
            None
        """
        return (None)
