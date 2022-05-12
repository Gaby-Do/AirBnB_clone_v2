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
	return "Hello HBNB!"
