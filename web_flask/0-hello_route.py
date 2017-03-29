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

if __name__ == "__main__":
    app.run()
