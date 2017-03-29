#!/usr/bin/python3
"""
Super simple Flask app.
"""
from flask import Flask


app = Flask(__name__)


@app.route("/")
def main():
    """
    Default route.
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """
    hbnb directory
    """
    return "HBNB!"


@app.route("/c/<text>")
def c_dir(text):
    """
    Returns C and the text sent in.
    """
    return ("C {}".format(text.replace('_', ' ')))


@app.route("/python/")
@app.route("/python/<text>")
def python_dir(text="is cool"):
    """
    Returns python and the text.
    """
    return ("Python {}".format(text.replace('_', ' ')))


if __name__ == "__main__":
    app.run()
