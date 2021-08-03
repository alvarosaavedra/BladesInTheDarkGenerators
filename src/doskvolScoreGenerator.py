# doskvolScoresGenerator.py
# Uses the tables at the end of Blades in the Dark to generate a description
# for a random city street.
from src.util import rc, json_retreiver


def print_score():
    """This will print text describing a random street"""
    score = new_score()
    print(
        f"""
    The crew heard of a job from {score['contact']}.  
    {score['client']} wants to hire someone to {score['work']} {score['target']}.  
    {score['positive_faction']} would like to see this work done 
    but {score['negative_faction']} would definitely not.  
    The crew might not know that {score['twist']}."""
    )


def new_score():
    return {
        'client':rc(connections).capitalize(),
        'target': rc(connections),
        'contact':rc(contacts),
        'work': rc(works),
        'twist': rc(twists),
        'positive_faction': rc(factions),
        'negative_faction': rc(factions),
    }

# Establish lists from json dumps
connections = json_retreiver("src/Scores/connections.json")
contacts = json_retreiver("src/Scores/contacts.json")
works = json_retreiver("src/Scores/works.json")
factions = json_retreiver("src/Scores/factions.json")
twists = json_retreiver("src/Scores/twits.json")


if __name__ == "__main__":
    print_score()