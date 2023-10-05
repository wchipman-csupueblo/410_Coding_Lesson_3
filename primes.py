#!/usr/bin/env python3


def display_title():
    print("Prime Number Checker")
    print()


def get_valid_int():
    # Loop till we get a valid number
    while True:
        # Get input
        num = int(input("Please enter an integer between 1 and 5000: "))
        # Check input is between 1 and 5000
        if num <= 1 or num >= 5000:
            print("Invalid integer. Try again.")
        else:
            return num


def get_factor_count(num):
    # Set a counter variable
    factor_count = 0
    # Loop through and decide if each number is a factor using modulus
    for i in range(1, num+1):
        remainder = num % i
        if remainder == 0:
            factor_count += 1
    return factor_count


def main():
    # display the  title
    # loop through
    # get a number
    # get the factor count
    # print the message based on the results
    # Run again
    display_title()

    again = "y"
    while again.lower() == "y":
        num = get_valid_int()
        factor_count = get_factor_count(num)
        if factor_count == 2:
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
            print(f"It has {factor_count} factors.")
        print()

        again = input("try again? (y/n): ")
        print()

    print("Bye!")

    pass


if __name__ == "__main__":
    main()
