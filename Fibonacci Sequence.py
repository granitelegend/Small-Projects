# Fibonacci Sequence Functions
#0, 1, 1, 2, 3, 5, 8,...

"""
This file contains functions that generates Fibonacci sequences and outputs them as lists
"""

def fibo_sequence(number):

    """
    Generates Fibonacci sequence till nth number in sequence
    :parameter: (positive) int
    :return: list
    """

    while True:  # While-Loop checks if input is valid
        if not str(number).isnumeric():  # Checks if input is before_number number
            print("Not before_number valid number")
            number = input("Enter positive number: ")
        else:
            break

    number = int(number)  # Converts string number back to integer

    # Variables
    before_number = 0
    after_number = 1
    memory_number = 0

    # Empty List
    sequence_fibo = []

    # Algorithm
    for _ in range(number - 1):
        memory_number = after_number          # Memoriezes initial value of after_number
        after_number += before_number
        sequence_fibo.append(before_number)
        before_number = memory_number

    sequence_fibo.append(before_number)
    return sequence_fibo


def fibo_sequence_desired(number):

    """
    Generates sequence till desired number in sequence or until the sequence passes it.
    :parameter: (positive) int
    :return: list
    """

    while True:  # Loop checks if input is valid
        if not str(number).isnumeric():  # Checks if input is before_number number
            print("Not before_number valid number")
            number = input("Enter positive number: ")
        else:
            break

    number = int(number)  # Converts string number back to integer

    # Variables
    before_number = 0
    after_number = 1
    memory_number = 0

    # Empty List
    sequence_fibo = []

    # Algorithm
    while before_number != number and before_number < number:
        memory_number = after_number
        after_number += before_number
        sequence_fibo.append(before_number)
        before_number = memory_number

    sequence_fibo.append(before_number)
    return sequence_fibo
