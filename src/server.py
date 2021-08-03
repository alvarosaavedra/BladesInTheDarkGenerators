from flask import Flask, render_template
import json
import random

from src.doskvolDemonGenerator import new_demon
from src.doskvolGhostgenerator import new_ghost
from src.doskvolStreetsGenerator import new_street
from src.doskvolBuildingGenerator import new_building
from src.doskvolPeopleGenerator import new_people
from src.doskvolScoreGenerator import new_score


app = Flask(__name__)

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

@app.route("/score")
def score():
    return render_template('score.html', **new_score())
