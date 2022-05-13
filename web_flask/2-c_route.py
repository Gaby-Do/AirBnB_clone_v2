#!/usr/bin/python3
"""
script that starts a Flask web application:
Routes:
/: display "Hello HBNB"
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """displays "Hello HBNB!""""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """displays "HBNB""""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """displays "C " plus value of text variable"""
    return "C "+text.replace('_', ' ')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
