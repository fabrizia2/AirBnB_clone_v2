#!/usr/bin/python3

"""
starts a flask web application
"""

from flask import Flask

"""create an application object"""
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """returns Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_display():
    """Displays HBNB"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
