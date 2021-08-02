# doskvolBuildingGenerator.py
# Uses the tables at the end of Blades in the Dark to generate a description
# for a random building. Use an argument of "rare" or "common" in the terminal
import sys

from util import rc, json_retreiver


def print_building(quality):
    """This prints a random description of a building, the "quality" argument
    needs to be "rare" or "common"""
    if (quality != "rare" and quality != "common"):
        print("Please enter 'rare' or 'common' as an argument")
        return None
    building = new_building(quality)
    print(
        f"""
    This {building['exterior_details']} {building['material']} {building['use']} is notable
    for it's {building['interior_details'][0]} and {building['interior_details'][1]}""")

def new_building(quality):
    return {
        'exterior_details': rc(exterior_details),
        'material': rc(material),
        'use': rc(rare_use) if quality == "rare" else rc(common_use),
        'interior_details': [rc(interior_details),rc(interior_details)]
    }


common_use = json_retreiver("src/Buildings/common_use.json")
rare_use = json_retreiver("src/Buildings/rare_use.json")
material = json_retreiver("src/Buildings/material.json")
exterior_details = json_retreiver("src/Buildings/exterior_details.json")
interior_details = json_retreiver("src/Buildings/interior_details.json")


if __name__ == "__main__":
    chosen_building = sys.argv[1]
    print_building(chosen_building)
