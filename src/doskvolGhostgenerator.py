# doskvolGhostGenerator.py
# Uses the tables at the end of Blades in the Dark to generate a description
# for a random ghost.

from src.util import rc, json_retreiver

def print_ghost():
    """This will print text that describes a new ghost"""
    ghost = new_ghost()
    print(
        f"""
    This is the ghost of {ghost['name']} '{ghost['aliases']}' {ghost['family_name']}.
    There is/are (a/an) {ghost['effect']} when this {ghost['trait']} spirit appears!
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
