#!/usr/bin/python3
"""
Super simple Flask app.
"""
from flask import Flask
from flask import abort, render_template

app = Flask(__name__)
from models import storage

@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.route("/")
def main():
    """
    Default route.
    """
    return "Hello HBNB"


@app.route("/hbnb")
def hbnb():
    """
    hbnb directory
    """
    return "HBNB"


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


@app.route("/number/<n>")
def number(n):
    """
    Returns n, if it's an integer
    """
    try:
        return ("{} is a number".format(int(n)))
    except:
        abort(404)


@app.route("/number_template/<n>")
def number_template(n):
    """
    Returns n, if it's an integer
    """
    try:
        n = int(n)
        return render_template('5-number.html', n=n)
    except:
        abort(404)


@app.route("/number_odd_or_even/<n>")
def number_odd_or_even_template(n):
    """
    Returns n, if it's an integer
    """
    try:
        n = int(n)
        if n % 2 == 0:
            s = "even"
        else:
            s = "odd"
        return render_template('6-number_odd_or_even.html', n=n, s=s)
    except:
        abort(404)



@app.route("/states_list")
def states_list():
    return render_template('7-states_list.html', states=storage.all('State'))


@app.route("/cities_by_states")
def cities_by_states():
    if storage.storage_type == "file":
        print("File")
    else:
        print("DB")
    return render_template('7-states_list.html', states=storage.all('State'))



if __name__ == "__main__":
    app.run()
