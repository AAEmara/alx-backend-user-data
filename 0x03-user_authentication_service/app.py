#!/usr/bin/env python3
"""A module that defines a flask app."""

from auth import Auth
from flask import Flask, jsonify, request, abort, make_response


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def welcome():
    """A basic welcome endpoint.
    """
    payload = {"message": "Bienvenue"}
    return (jsonify(payload))


@app.route("/users", methods=["POST"], strict_slashes=False)
def users():
    """Registering a User through the given credentials.
    """
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        user_data = AUTH.register_user(email, password)
        if user_data:
            payload = {"email": email, "message": "user created"}
            return (jsonify(payload))
    except ValueError as err:
        payload = {"message": "email already registered"}
        return (jsonify(payload), 400)


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login():
    """Allows the user to send his credentials in order to login.
    """
    email = request.form.get("email")
    password = request.form.get("password")
    is_valid = AUTH.valid_login(email, password)
    if not is_valid:
        abort(401)
    session_id = AUTH.create_session(email)
    user = AUTH._db.find_user_by(email=email)
    payload = {"email": email, "message": "logged in"}
    response = jsonify(payload)
    response.set_cookie("session_id", session_id)
    return (response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
