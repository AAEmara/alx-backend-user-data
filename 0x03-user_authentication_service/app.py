#!/usr/bin/env python3
"""A module that defines a flask app."""

from auth import Auth
from flask import Flask, jsonify, request


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
