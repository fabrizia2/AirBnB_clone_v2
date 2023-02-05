#!/usr/bin/python3

"""
starts a flask web application
"""

"""import lib"""
from flask import Flask

"""create an application object"""
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb_display():
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_is(text):
    return "C " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
