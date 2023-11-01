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

    while True:
            try:
                choice = int(input("Enter the number of your choice: "))
                if 1 <= choice <= len(choices):
                    return choice
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")


def battle():
    print("\nA wild monster appears! ")
    time.sleep(1)

    choices = ["Fight", "Run"]
    player_choice = make_choice(choices)

    if player_choice == 1:
        print("You engage in fierce battle!")

        print("You defeated the monster!!")

    elif player_choice == 2: #run
        print("You run away from the danger...")

        print("You successfully escaped from the monster.")

        