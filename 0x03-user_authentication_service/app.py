#!/usr/bin/env python3
"""A module that defines a flask app."""

from auth import Auth
from flask import Flask, jsonify, request, abort, make_response, redirect


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


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout():
    """Logs out of the current session.
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return (redirect("/", code=302))
    abort(403)


@app.route("/profile", methods=["GET"], strict_slashes=False)
def profile():
    """Returning the User that was searched for.
    """
    session_id = request.cookies.get("session_id")
    try:
        user = AUTH._db.find_user_by(session_id=session_id)
        if user:
            email = user.email
            message = {"email": email}
            return (jsonify(message), 200)
        abort(403)
    except Exception:
        abort(403)


@app.route("/reset_password", methods=["POST"], strict_slashes=False)
def get_reset_password_token():
    """Generates a reset password token for the requesting user.
    """
    email = request.form.get("email")
    try:
        reset_token = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403)
    message = {"email": email, "reset_token": reset_token}
    return (jsonify(message), 200)


@app.route("/reset_password", methods=["PUT"], strict_slashes=False)
def update_password():
    """Updates the user's password.
    """
    from sqlalchemy.orm.exc import NoResultFound
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")
    try:
        reset_token = AUTH.get_reset_password_token(email)
        user = AUTH._db.find_user_by(email=email)
    except (ValueError, NoResultFound):
        abort(403)
    AUTH.update_password(reset_token, new_password)
    message = {"email": email, "message": "Password updated"}
    return (jsonify(message), 200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
