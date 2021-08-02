# doskvolGhostGenerator.py
# Uses the tables at the end of Blades in the Dark to generate a description
# for a random ghost.

import random
import json


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


def print_ghost():
    """This will print text that describes a new ghost"""
    print(
        f"""
    This is the ghost of {rc(first_name)} '{rc(aliases)}' {rc(family_name)}.
    There is/are (a/an) {rc(ghostly_effect)} when this {rc(ghost_trait)} spirit appears!
    """
    )

def new_ghost():
    return {
        'name': rc(first_name),
        'aliases': rc(aliases),
        'family_name': rc(family_name),
        'effect': rc(ghostly_effect),
        'trait': rc(ghost_trait)
    }


first_name = json_retreiver("src/Ghosts/first_names.json")
family_name = json_retreiver("src/Ghosts/family_names.json")
aliases = json_retreiver("src/Ghosts/aliases.json")
ghost_trait = json_retreiver("src/Ghosts/ghost_traits.json")
ghostly_effect = json_retreiver("src/Ghosts/ghostly_effect.json")

if __name__ == "__main__":
    print_ghost()
