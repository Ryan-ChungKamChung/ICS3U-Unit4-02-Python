#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in December 2020
# Program does factorials


def main():
    # Function does factorials

    print("I will do the factorial of the number you give me")

    # Input
    number_string = input("Enter number: ")

    # Process
    try:
        number = int(number_string)
        assert number > 0

        loop_counter = 0
        number_factorial = 1

        while loop_counter < number:
            loop_counter = loop_counter + 1
            number_factorial = number_factorial * loop_counter

        # Output
        print("The factorial of {0} is {1}".format(number, number_factorial))
    except AssertionError:
        # Output
        if number == 0:
            print("The factorial of 0 is 1")
        else:
            print("This isn't a valid number")
    except Exception:
        # Output
        print("This isn't a valid number")


if __name__ == "__main__":
    main()
