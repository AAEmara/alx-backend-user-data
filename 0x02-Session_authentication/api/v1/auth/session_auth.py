#!/usr/bin/env python3
"""A module that defines Session Authentication."""

from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """A class that defines the session authentication mechanism.
    """
    user_id_by_session_id = dict()

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for the given `user_id`.
        Args:
            user_id: The ID of the user that the session will be created for.
        Returns:
            None: if the `user_id` is None or not a string.
            session_id: if the `user_id` is valid.
        """
        if user_id is None or not isinstance(user_id, str):
            return (None)
        session_id: str = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return (session_id)

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Retrieves the User Id based on the given Session Id.
        Args:
            session_id: The session's ID.
        Returns:
            None: if the `session_id` is None or not a string.
            user_id: if the `session_id` is valid and available.
        """
        if session_id is None or not isinstance(session_id, str):
            return (None)
        user_id = self.user_id_by_session_id.get(session_id)
        return (user_id)
