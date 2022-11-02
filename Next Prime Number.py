# Next Prime Number
# Function that prints the next prime number in order of positive integers

# Planned:
# Twin Primes

import math

def prime_checker(number):
    """
    Checks if a number is prime
    :param number: (positive integer)
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

    for divisorNum in range(2, math.ceil(math.sqrt(number + 1))):  # Checks all factors lower than ceil(sqrt(number))
        if number % divisorNum == 0:
            return False
            break
        else:
            continue

    return True

def next_prime():
    """
    Prints the next prime in order of positive integers when user asks for it
    :return: None
    """

    a = 1
    answer_input = 0

    while answer_input != 'n':
        if prime_checker(a):
            print(a)
            a +=1
            answer_input = input("Generate next prime? Enter anything but 'n' to continue: ")
        else:
            a += 1
            continue

next_prime()


