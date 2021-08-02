# doskvolDemonGenerator.py
# Uses the tables at the end of Blades in the Dark to generate a description
# for a random demon.

from src.util import rc, json_retreiver

def print_demon():
    """This will print text describing a new demon"""
    demon = new_demon()
    print(
        f"""
    Tremble at the sight of {demon['name']}!
    Behold, {demon['features'][0]} and {demon['features'][1]}.
    This {demon['affinity']} demon has a {demon['aspect']} aspect.
    This demon desires {demon['desire']} above all else!
    """
    )

def new_demon():
    return {
        'name': rc(demon_name),
        'features': [rc(demon_features), rc(demon_features)],
        'affinity': rc(demonic_affinity),
        'aspect': rc(demonic_aspect),
        'desire': rc(demon_desire)
    }

demon_name = json_retreiver("src/Demons/demon_names.json")
demon_features = json_retreiver("src/Demons/demon_features.json")
demonic_aspect = json_retreiver("src/Demons/demonic_aspect.json")
demonic_affinity = json_retreiver("src/Demons/demonic_affinity.json")
demon_desire = json_retreiver("src/Demons/demon_desire.json")

if __name__ == "__main__":
    print_demon()
