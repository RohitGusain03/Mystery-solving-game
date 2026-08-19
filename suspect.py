"""
suspect.py
Contains the Suspect class.
"""

from clue import Clue


class Suspect:

    def __init__(self, name, age, occupation, alibi, dialogue):

        self.name = name
        self.age = age
        self.occupation = occupation
        self.alibi = alibi
        self.dialogue = dialogue

        self.guilty = False
        self.interviewed = False
        self.clues = []

    def interview(self):

        self.interviewed = True

        print("=" * 60)
        print(f"Interviewing {self.name}")
        print("=" * 60)

        print(f"Age        : {self.age}")
        print(f"Occupation : {self.occupation}")
        print(f"Alibi      : {self.alibi}")

        print("\nStatement")
        print(f'"{self.dialogue}"')

    def add_clue(self, clue):

        if isinstance(clue, Clue):
            self.clues.append(clue)

    def show_clues(self):

        if not self.clues:
            print("No clues linked to this suspect.")
            return

        print(f"\nEvidence against {self.name}\n")

        for clue in self.clues:
            print(f"- {clue.name}")

    def set_guilty(self):

        self.guilty = True

    def is_guilty(self):

        return self.guilty

    def __str__(self):

        return self.name