# doskvolMasterGenerator.py
# A menu interface capable of calling the individual Doskvol generators

import doskvolBuildingGenerator as building
import doskvolDemonGenerator as demon
import doskvolGhostgenerator as ghost
import doskvolPeopleGenerator as npc
import doskvolStreetsGenerator as street


def main():
    while True:
        generator = input(
            """
Select generator:
[1] Create common NPC
[2] Create rare NPC
[3] Create street description
[4] Create common building desciption
[5] Create rare building description
[6] Create a demon
[7] Create a ghost
[8] Quit

"""
        )
        if generator == "1":
            npc.print_person("common")

        elif generator == "2":
            npc.print_person("rare")

        elif generator == "3":
            street.print_street()

        elif generator == "4":
            building.print_building("common")

        elif generator == "5":
            building.print_building("rare")

        elif generator == "6":
            demon.print_demon()

        elif generator == "7":
            ghost.print_ghost()

        elif generator == "8":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
