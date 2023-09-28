#!/usr/bin/env python3

import conversion as c


def display_welcome():
    print("Feet and Meters Converter")
    print()


def display_menu():
    print("Conversions Menu:")
    print("a. Feet to Meters")
    print("b. Meters to Feet")


def main():
    display_welcome()

    again = "y"
    while again.lower() == "y":
        display_menu()
        choice = input("Select a conversion (a/b): ")
        print()

        if choice == "a":
            pass
        elif choice == "b":
            pass
        else:
            print("you did not enter a valid selection.")
        print()

        again = input("Would you like to perform another conversion? (y/n): ")
        print()

    print("Thanks, bye!")
