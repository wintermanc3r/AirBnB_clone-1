#!/usr/bin/python3
"""
Super simple Flask app.
"""
from flask import Flask
from flask import abort, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.route("/hbnb_filters")
def all_state():
    amenities = [x for x in storage.all('Amenity').values()]
    states = [x for x in storage.all('State').values()]
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)

if __name__ == "__main__":
    app.run()
