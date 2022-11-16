# Next Prime Number
# Function that prints the next prime number in order of positive integers

# Planned:
# Twin Primes

"""This file contains simple functions for checking primes"""

import math

def prime_checker(number):
    """
    Checks if a number is prime
    :param int
    :return: boolean
    """

    while True:  # Checks if input is a positive number
        if not str(number).isnumeric():
            print("Invalid input")
            number = input("Enter positive number: ")
        else:
            break

    number = int(number)

    # Simple for-loop that divides number with divisor and checks for remainder

    # Checks all factors lower than ceil(sqrt(number))
    for divisor_num in range(2, math.ceil(math.sqrt(number + 1))):
        if number % divisor_num == 0:
            return False

    return True

def next_prime():
    """
    Prints the next prime in order of positive integers when user asks for it
    :parameter: None
    :return: None
    """

    is_prime_number = 1
    answer_input = 0

    while answer_input != 'n':
        if prime_checker(is_prime_number):
            print(is_prime_number)
            is_prime_number +=1
            answer_input = input("Generate next prime? Enter anything but 'n' to continue: ")
        else:
            is_prime_number += 1


