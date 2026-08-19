"""
detective.py
Contains the Detective class.
"""

from suspect import Suspect
from clue import Clue


class Detective:

    def __init__(self, name):

        self.name = name
        self.score = 0
        self.inventory = []
        self.interviewed_suspects = []
        self.cases_solved = 0

    # -----------------------------
    # CLUE FUNCTIONS
    # -----------------------------

    def collect_clue(self, clue):

        if clue not in self.inventory:

            clue.collect()

            self.inventory.append(clue)

            self.score += 10

            print(f"\nYou collected: {clue.name}")

        else:

            print("\nYou already collected this clue.")

    def show_inventory(self):

        print("=" * 60)
        print("COLLECTED CLUES")
        print("=" * 60)

        if not self.inventory:

            print("No clues collected.")

            return

        for i, clue in enumerate(self.inventory, start=1):

            print(f"{i}. {clue.name}")

    # -----------------------------
    # SUSPECT FUNCTIONS
    # -----------------------------

    def interview(self, suspect):

        if suspect not in self.interviewed_suspects:

            self.interviewed_suspects.append(suspect)

            self.score += 5

        suspect.interview()

    def show_interviewed(self):

        print("=" * 60)
        print("INTERVIEWED SUSPECTS")
        print("=" * 60)

        if not self.interviewed_suspects:

            print("No suspects interviewed.")

            return

        for suspect in self.interviewed_suspects:

            print("-", suspect.name)

    # -----------------------------
    # CASE FUNCTIONS
    # -----------------------------

    def solve_case(self, suspect):

        if suspect.is_guilty():

            self.score += 50

            self.cases_solved += 1

            print("\nCongratulations Detective!")

            print("You solved the case!")

        else:

            print("\nWrong suspect!")

            print("The criminal escaped!")

    # -----------------------------
    # PLAYER INFO
    # -----------------------------

    def show_stats(self):

        print("=" * 60)

        print("DETECTIVE PROFILE")

        print("=" * 60)

        print(f"Name          : {self.name}")
        print(f"Score         : {self.score}")
        print(f"Cases Solved  : {self.cases_solved}")
        print(f"Clues         : {len(self.inventory)}")
        print(f"Interviews    : {len(self.interviewed_suspects)}")

    def __str__(self):

        return self.name