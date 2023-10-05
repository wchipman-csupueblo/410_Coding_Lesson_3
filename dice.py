#!/usr/bin/env python3

import random


def roll():
    # generate a random number between 1 and 6
    value = random.randint(1, 6)
    # return that number
    return value


def display_title():
    print("Dice Roller")
    print()


def roll_dice():
    # Roll 2 dice and store values separatly
    die1 = roll()
    die2 = roll()
    # Get the total of the dice rolls
    total = die1 + die2
    # Print out all values
    print("Die 1:", die1)
    print(f"Die 2: {die2}")
    print("Total:", total)
    # If 2 ones or 2 sixes are rolled, print special message
    if total == 2:
        print("Snake Eyes!")
    elif die1 == 6 and die2 == 6:
        print("Boxcars!")
    elif (die1 == 5 and die2 == 3) or (die1 == 3 and die2 == 5):
        print("You got a special Eight!")


def main():
    # Display title
    display_title()
    # Ask if they want to roll the dice
    choice = input("Roll the dice? (y/n): ")
    print()
    # if yes then create a loop
    while choice.lower() == "y":
        #  Loop: roll both dice
        roll_dice()
        #        ask if they want to roll again
        choice = input("Roll again? (y/n): ")
        print()
    # Exit
    # empty comment


if __name__ == "__main__":
    main()
