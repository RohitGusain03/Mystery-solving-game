"""
clue.py
Defines the Clue class used in the Detective Mystery game.
"""


class Clue:
    """
    Represents a single clue found during the investigation.
    """

    def __init__(self, name, description, suspect, is_real=True):
        self.name = name
        self.description = description
        self.suspect = suspect
        self.is_real = is_real
        self.collected = False

    def collect(self):
        """Mark the clue as collected."""
        self.collected = True

    def display(self):
        """Display clue information."""
        print("-" * 50)
        print(f"Clue Name : {self.name}")
        print(f"Description : {self.description}")

        if self.collected:
            print("Status : Collected")
        else:
            print("Status : Not Collected")

    def __str__(self):
        return self.name