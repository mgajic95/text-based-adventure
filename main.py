import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def display_status(self):
        print(f"\n{name}'s Status:")
        print(f"Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))

def introduction():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a mysterious land. Your goal is to survive and explore.")
    print("Choose your actions wisely!")

def make_choice(choices):
    print("\nChoose an action:")
    for index, choice in enumerate(choices, start=1):
        print(f"{index}. {choice}")
