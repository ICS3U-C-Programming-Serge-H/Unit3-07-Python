#!/usr/bin/env python3
# Created by: Serge Hamouche
# Created on: Mar 30, 2025
# This program tells the user if you can date the grandmothers grandchild.


def main():
    try:
        # Get user's age
        user_age = int(input("Enter your age: "))

        # Check if the age is valid
        if user_age < 0 or user_age > 120:
            print("Invalid age. Please enter an age between 0 and 120.")
        elif user_age > 25 and user_age < 40:
            print("You can date my grandchild.")
        else:
            print("Sorry, you cannot date my grandchild.")

    except ValueError:
        print("invalid input, please enter an age.")

    finally:
        print("Thanks for playing.")


main()
