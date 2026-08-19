"""
utils.py
Contains helper functions used throughout the game.
"""

import os
import time


def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def pause(message="\nPress Enter to continue..."):
    """Pause the game until the player presses Enter."""
    input(message)


def divider(length=60):
    """Print a horizontal divider."""
    print("=" * length)


def title(text):
    """Display a formatted title."""
    clear_screen()
    divider()
    print(text.center(60))
    divider()


def slow_print(text, delay=0.03):
    """
    Print text one character at a time.
    Creates a simple typewriter effect.
    """
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def choice_input(prompt, valid_choices):
    """
    Keep asking until the user enters a valid choice.
    Returns the selected choice.
    """
    while True:
        choice = input(prompt).strip()

        if choice in valid_choices:
            return choice

        print("Invalid choice. Please try again.")