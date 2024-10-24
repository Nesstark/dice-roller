# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

import random

def roll_dice(sides=6):
    return random.randint(1, sides)

def main():
    print("Welcome to the Dice Roller!")
    while True:
        sides = input("Enter the number of sides for the dice (default is 6), or type 'exit' to quit: ")
        if sides.lower() == 'exit':
            print("Thanks for playing! Goodbye.")
            break
        if sides.isdigit():
            sides = int(sides)
        else:
            sides = 6
        result = roll_dice(sides)
        print(f"You rolled a {result} on a {sides}-sided dice.\n")

if __name__ == "__main__":
    main()
