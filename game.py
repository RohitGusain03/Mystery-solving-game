"""
game.py
Main game engine.
"""

import random

from detective import Detective
from suspect import Suspect
from clue import Clue
from utils import title, pause, choice_input


class Game:

    def __init__(self):
        self.detective = None
        self.suspects = []
        self.clues = []
        self.guilty_suspect = None

    # -----------------------------
    # SETUP
    # -----------------------------

    def create_detective(self):
        title("DETECTIVE MYSTERY")
        name = input("Enter your detective name: ")
        self.detective = Detective(name)

    def create_suspects(self):
        self.suspects = [
            Suspect("Alice",34,"Curator",
                    "I was restoring paintings.",
                    "I never touched the diamond."),
            Suspect("Bob",41,"Security Guard",
                    "I watched the cameras.",
                    "Everything looked normal."),
            Suspect("Charlie",29,"Visitor",
                    "I was taking photos.",
                    "I don't know anything.")
        ]

    def create_clues(self):
        self.clues = [
            Clue("Fingerprint","Found on the museum safe.","Bob"),
            Clue("Broken Glass","Near the entrance.","Charlie"),
            Clue("Security Card","Dropped outside the vault.","Alice"),
            Clue("Shoe Print","Large muddy footprints.","Bob"),
            Clue("Museum Map","Has vault markings.","Charlie")
        ]

    def assign_clues(self):
        for clue in self.clues:
            for suspect in self.suspects:
                if suspect.name == clue.suspect:
                    suspect.add_clue(clue)

    def choose_criminal(self):
        self.guilty_suspect = random.choice(self.suspects)
        self.guilty_suspect.set_guilty()

    def setup(self):
        self.create_detective()
        self.create_suspects()
        self.create_clues()
        self.assign_clues()
        self.choose_criminal()

    # -----------------------------
    # MENUS
    # -----------------------------

    def main_menu(self):
        while True:
            title("DETECTIVE MYSTERY")

            print(f"Detective : {self.detective.name}")
            print(f"Score     : {self.detective.score}")
            print(f"Clues     : {len(self.detective.inventory)}")
            print()

            print("1. Visit Crime Scene")
            print("2. Interview Suspects")
            print("3. View Inventory")
            print("4. Detective Profile")
            print("5. Solve Case")
            print("6. Exit")

            choice = choice_input(
                "\nChoose: ",
                ["1","2","3","4","5","6"]
            )

            if choice == "1":
                self.visit_crime_scene()
            elif choice == "2":
                self.interview_menu()
            elif choice == "3":
                self.detective.show_inventory()
                pause()
            elif choice == "4":
                self.detective.show_stats()
                pause()
            elif choice == "5":
                self.solve_case()
            else:
                break

    # -----------------------------
    # CRIME SCENE
    # -----------------------------

    def visit_crime_scene(self):
        while True:
            title("CRIME SCENE")

            remaining = [
                clue for clue in self.clues
                if clue not in self.detective.inventory
            ]

            if not remaining:
                print("You have collected every clue.")
                pause()
                return

            for i, clue in enumerate(remaining, start=1):
                print(f"{i}. {clue.name}")

            print("0. Back")

            choice = input("\nSelect clue: ")

            if choice == "0":
                return

            if not choice.isdigit():
                continue

            choice = int(choice)

            if 1 <= choice <= len(remaining):
                self.detective.collect_clue(
                    remaining[choice - 1]
                )
                pause()

    # -----------------------------
    # INTERVIEW
    # -----------------------------

    def interview_menu(self):
        while True:
            title("INTERVIEW ROOM")

            for i, suspect in enumerate(self.suspects, start=1):
                print(f"{i}. {suspect.name}")

            print("0. Back")

            choice = input("\nChoose suspect: ")

            if choice == "0":
                return

            if not choice.isdigit():
                continue

            choice = int(choice)

            if 1 <= choice <= len(self.suspects):
                suspect = self.suspects[choice - 1]
                self.detective.interview(suspect)
                suspect.show_clues()
                pause()

    # -----------------------------
    # SOLVE CASE
    # -----------------------------

    def solve_case(self):
        title("SOLVE CASE")

        if len(self.detective.inventory) < len(self.clues):
            print("Collect all clues before accusing someone.")
            pause()
            return

        for i, suspect in enumerate(self.suspects, start=1):
            print(f"{i}. {suspect.name}")

        choice = input("\nWho is guilty? ")

        if not choice.isdigit():
            return

        choice = int(choice)

        if 1 <= choice <= len(self.suspects):
            suspect = self.suspects[choice - 1]
            self.detective.solve_case(suspect)
            pause()