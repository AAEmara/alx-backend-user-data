#!/usr/bin/env python3
"""A module that handles all routes for the Session Authentication."""

from api.v1.views import app_views
from flask import request, jsonify, session
from models.user import User
from os import getenv


@app_views.route("/auth_session/login", methods=["POST"], strict_slashes=False)
def login():
    """Performs the user login process.
    """
    user_email = request.form.get("email")
    if not user_email:
        error_message = {"error": "email missing"}
        return (jsonify(error_message), 400)
    user_password = request.form.get("password")
    if not user_password:
        error_message = {"error": "password missing"}
        return (jsonify(error_message), 400)

    # Retrieving the User instance based on the email.
    user = User.search({"email": user_email})
    if not len(user):
        error_message = {"error": "no user found for this email"}
        return (jsonify(error_message), 404)
    user = user[0]
    # Checking on the password of the retrieved user.
    if not user.is_valid_password(user_password):
        error_message = {"error": "wrong password"}
        return (jsonify(error_message), 401)

    # Creating a Session ID for the User instance retrieved.
    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())
    session_name = getenv("SESSION_NAME")
    response.set_cookie(session_name, session_id)
    return (response)


@app_views.route("/auth_session/logout",
                 methods=["DELETE"],
                 strict_slashes=True)
def logout():
    """Performs the user logout process.
    """
    from api.v1.app import auth
    is_destroyed = auth.destroy_session(request)
    if not is_destroyed:
        abort(404)
    return (jsonify(dict()), 200)
