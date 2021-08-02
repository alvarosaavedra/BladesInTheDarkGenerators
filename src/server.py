from flask import Flask, render_template
import json
import random

from doskvolDemonGenerator import new_demon
from doskvolGhostgenerator import new_ghost
from doskvolStreetsGenerator import new_street
from doskvolBuildingGenerator import new_building
from doskvolPeopleGenerator import new_people


app = Flask(__name__)

def json_retreiver(json_filename):
    """Call this from a variable with a filename string to populate
    with json content"""
    filename = json_filename
    with open(filename) as f:
        return json.load(f)

def rc(variable):
    """rc = random choice. Picks a random item from the list and returns
    it. This is mostly to shorten up the variables in the print command"""
    return random.choice(variable)

@app.route("/")
def hello_world(name=None):
    return render_template('hello.html', name=name)

@app.route("/building/<quality>")
@app.route("/building")
def building(quality=None):
    return render_template('building.html', **new_building(quality))

@app.route("/people/<quality>")
@app.route("/people")
def people(quality=None):
    return render_template('people.html', **new_people(quality))

@app.route("/demon")
def demon():
    return render_template('demon.html', **new_demon())

@app.route("/ghost")
def ghost():
    return render_template('ghost.html', **new_ghost())

@app.route("/street")
def street():
    return render_template('streets.html', **new_street())
