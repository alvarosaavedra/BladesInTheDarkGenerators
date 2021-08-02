# doskvolPeopleGenerator.py
# Uses the tables at the end of Blades in the Dark to generate a description
# for a random person. Use an argument of "rare" or "common" in the terminal
import sys
import random

from src.util import rc, json_retreiver

def print_person(quality):
    """This prints a random description of a person, the "quality" argument
    needs to be "rare" or "common"""
    if (quality != "rare" and quality != "common"):
        print("Please enter 'rare' or 'common' as an argument")
        return None
    person = new_people(quality)
    
    print(
        f"""
    {person['first_name']} '{person['aliases']}' {person['family_name']}:
    A/An {person['appearance']} {person['gender']} {person['heritage']} wearing/using a/an {person['style']}.
    They work as a {person['profession']} and use {person['methods']} to try and gain/cause {person['goals']}.
    Overall, they seem {person['traits']} but are also {person['quirks']} They are interested in {person['interests']}.
    """
    )
    
def new_people(quality):
    return {
        'first_name': rc(first_name),
        'aliases': rc(aliases),
        'family_name': rc(family_name),
        'appearance': rc(appearance),
        'gender': rc(gender),
        'heritage': random.choices(heritage, weights=[50, 10, 5, 5, 5, 5])[0],
        'style': rc(style),
        'profession': rc(rare_profession) if quality == "rare" else rc(common_profession),
        'methods': rc(methods),
        'goals': rc(goals),
        'traits': rc(traits),
        'quirks': rc(quirks),
        'interests': rc(interests)}


heritage = json_retreiver("src/People/heritage.json")
gender = json_retreiver("src/People/gender.json")
appearance = json_retreiver("src/People/appearance.json")
goals = json_retreiver("src/People/goals.json")
methods = json_retreiver("src/People/methods.json")
common_profession = json_retreiver("src/People/common_profession.json")
rare_profession = json_retreiver("src/People/rare_profession.json")
style = json_retreiver("src/People/style.json")
traits = json_retreiver("src/People/traits.json")
interests = json_retreiver("src/People/interests.json")
quirks = json_retreiver("src/People/quirks.json")

first_name = json_retreiver("src/People/first_names.json")
family_name = json_retreiver("src/People/family_names.json")
aliases = json_retreiver("src/People/aliases.json")


if __name__ == "__main__":
    chosen_person = sys.argv[1]
    print_person(chosen_person)
