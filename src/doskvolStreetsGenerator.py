# doskvolStreetsGenerator.py
# Uses the tables at the end of Blades in the Dark to generate a description
# for a random city street.
from src.util import rc, json_retreiver


def print_street():
    """This will print text describing a random street"""
    street = new_street()
    print(
        f"""
    This {street['moods']} {street['infastructure_type']} is primarily used for {street['use']}.
    (A/An) {street['sights']} catch(es) your eye. You hear {street['sounds']} 
    and smell {street['smells']} on the air. You can't help but notice 
    {street['details']} and {street['details']}."""
    )


def new_street():
    return {
        'moods':rc(moods),
        'infastructure_type': rc(infastructure_type),
        'use':rc(use),
        'sights':rc(sights).capitalize(),
        'sounds': rc(sounds),
        'smells': rc(smells),
        'details': [rc(details), rc(details)]
    }

# Establish lists from json dumps
moods = json_retreiver("src/Streets/moods.json")
sights = json_retreiver("src/Streets/sights.json")
sounds = json_retreiver("src/Streets/sounds.json")
smells = json_retreiver("src/Streets/smells.json")
use = json_retreiver("src/Streets/use.json")
infastructure_type = json_retreiver("src/Streets/infastructure_type.json")
details = json_retreiver("src/Streets/details.json")

if __name__ == "__main__":
    print_street()
