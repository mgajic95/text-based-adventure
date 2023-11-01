import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def display_status(self):
        print(f"\n{self.name}'s Status:")
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
    print("\nA wild monster appears!")
    time.sleep(1)

    choices = ["Fight", "Run"]
    player_choice = make_choice(choices)

    if player_choice == 1:  # Fight
        print("You engage in a fierce battle!")
        # Add battle logic here based on player's stats
        print("You defeated the monster!")

    elif player_choice == 2:  # Run
        print("You attempt to run away.")
        # Add run logic here based on player's stats
        print("You successfully escaped from the monster.")

def explore():
    print("\nYou enter a dark cave.")
    time.sleep(1)

    choices = ["Enter deeper into the cave", "Go back"]
    player_choice = make_choice(choices)

    if player_choice == 1:  # Enter deeper into the cave
        print("You discover a hidden treasure!")
        # Add treasure logic here based on player's stats
        print("You add the treasure to your inventory.")

    elif player_choice == 2:  # Go back
        print("You decide not to risk it and return to the outside.")

def main():
    introduction()

    player_name = input("Enter your name: ")
    player = Player(player_name)

    while True:
        player.display_status()

        battle()
        if player.health <= 0:
            print("You have been defeated! Game Over.")
            break

        explore()
        if player.health <= 0:
            print("You have been defeated! Game Over.")
            break

if __name__ == "__main__":
    main()
