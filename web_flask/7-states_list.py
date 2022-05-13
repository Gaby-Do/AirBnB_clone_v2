#!/usr/bin/python3
"""starts a Flask web application"""


from flask import Flask, render_template 
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)





@app.teardown_appcontext
