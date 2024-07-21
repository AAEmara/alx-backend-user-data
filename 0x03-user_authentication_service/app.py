#!/usr/bin/env python3
"""A module that defines a flask app."""

from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def welcome():
    """A basic welcome endpoint.
    """
    payload = {"message": "Bienvenue"}
    return (jsonify(payload))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
