#!/usr/bin/python3
"""
script that starts a Flask web application:
Routes:
/: display "Hello HBNB"
"""


from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """displays 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """displays 'C' followed by the value of the text variable"""
    return "C "+text.replace('_', ' ')


@app.route('/python/', defaults={'text': "is cool"})
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """displays 'Python' plus the value of the text variable or default"""
    return "Python "+text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """displays 'n is a number' if n is int"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """displays HTML page if n is int"""
    return render_template('5-number.html', num=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
