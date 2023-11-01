import time
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.score = 0

    def display_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))
        print(f"Score: {self.score}")

def introduction():
    print("Welcome to the Advanced Adventure Game!")
    print("You find yourself in a dangerous land. Your goal is to survive, explore, and earn points.")
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

def battle(player, enemy_difficulty):  # Correct the function signature
    print(f"\nA wild monster appears with difficulty level {enemy_difficulty}!")
    time.sleep(1)

    choices = ["Fight", "Run"]
    player_choice = make_choice(choices)

    if player_choice == 1:  # Fight
        player_damage = random.randint(10, 20)
        enemy_damage = random.randint(5, 15 + enemy_difficulty)

        print("You engage in a fierce battle!")
        print(f"You dealt {player_damage} damage to the monster.")
        print(f"The monster dealt {enemy_damage} damage to you.")

        if player_damage > enemy_damage:
            print("You defeated the monster!")
            return True
        else:
            print("You were defeated by the monster!")
            return False

    elif player_choice == 2:  # Run
        print("You attempt to run away.")

        run_success_probability = min(0.5, 0.2 + 0.1 * enemy_difficulty)
        if random.random() < run_success_probability:
            print("You successfully escaped from the monster.")
            return True
        else:
            print("You failed to escape. Prepare for battle!")
            return False

def explore(player):
    print("\nYou enter a mysterious area.")
    time.sleep(1)

    choices = ["Search for treasure", "Rest and regain health", "Continue exploring"]
    player_choice = make_choice(choices)

    if player_choice == 1:  # Search for treasure
        treasure_found_probability = min(0.8, 0.1 + 0.1 * player.score)
        if random.random() < treasure_found_probability:
            print("You discover a hidden treasure!")
            player.inventory.append("Treasure")
            player.score += 10
        else:
            print("You search but find nothing.")

    elif player_choice == 2:  # Rest and regain health
        health_gain = random.randint(10, 30)
        print(f"You rest and regain {health_gain} health.")
        player.health = min(100, player.health + health_gain)

    elif player_choice == 3:  # Continue exploring
        print("You continue exploring.")

def main():
    introduction()

    player_name = input("Enter your name: ")
    player = Player(player_name)

    enemy_difficulty = 1

    while player.health > 0:
        player.display_status()

        if not battle(player, enemy_difficulty):
            print("Game Over. You can try again.")
            break

        explore(player)  # Pass the 'player' object to the explore function

        enemy_difficulty += 1

        if player.health <= 0:
            print("You have been defeated! Game Over.")

def main():
    while True:  # Add a loop for replaying the game
        introduction()

        player_name = input("Enter your name: ")
        player = Player(player_name)

        enemy_difficulty = 1

        while player.health > 0:
            player.display_status()

            if not battle(player, enemy_difficulty):
                print("Game Over. You can try again.")
                break

            explore(player)

            enemy_difficulty += 1

            if player.health <= 0:
                print("You have been defeated! Game Over.")
                break

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
