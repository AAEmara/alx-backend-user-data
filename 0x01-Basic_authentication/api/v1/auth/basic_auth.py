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
        """Decoding the info. in the Authorization Header.
        Args:
            base64_authorization_header: The information encoded in Base64.
        Returns:
            None: if the info. is not a valid Base64 input or not a string.
            Decoded Info.: if the input is a valid Base64 info.
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

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """Extracting the user's credentials.
        Args:
            decoded_base64_authorization_header: The decoded user credentials.
        Returns:
            (None, None): if the info. is not a valid Base64 input,
            or not a string, or not separated by a colon ":".
            (Email, Password): if the info. is a valid Base64 value,
            separated by a colon ":".
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        elif not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        elif ":" not in decoded_base64_authorization_header:
            return (None, None)
        values_list = decoded_base64_authorization_header.split(":")
        return (values_list[0], values_list[1])

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """Retrieves the User instance based on user's credentials.
        Args:
            user_email: User's Email.
            user_pwd: User's Password.
        Returns:
            User Instance.
        """
        if ((user_email is None) or (not isinstance(user_email, str))):
            return (None)
        elif ((user_pwd is None) or (not isinstance(user_pwd, str))):
            return (None)

        with app.app_context():
            response = view_all_users()
            users: str = response.get_json()
            if users:
                for user_data in users:
                    user = User(**user_data)
                    user.password = user_pwd
                    if (
                        (user_email == user.email) and
                        (user.is_valid_password(user_pwd))
                       ):
                        try:
                            uuid.UUID(user_pwd)
                            return (user)
                        except ValueError:
                            return (None)
        return (None)
