# Fibonacci Sequence Functions
#0, 1, 1, 2, 3, 5, 8,...

def fibo_sequence(number):

    """
    Generates Fibonacci sequence till nth number in sequence
    :parameter: (positive) int
    :return: list
    """

    while True:  # Loop checks if input is valid
        if not str(number).isnumeric():  # Checks if input is a number, negative and strings numbers are invalid
            print("Not a valid number")
            number = input("Enter positive number: ")
        else:
            break

    number = int(number)  # Converts string number back to integer

    # Variables
    a = 0
    b = 1
    c = 0

    # Empty List
    sequence_fibo = []

    # Algorithm
    for _ in range(number - 1):
        c = b                      # Memoriezes initial value of b
        b = b + a
        sequence_fibo.append(a)
        a = c

    sequence_fibo.append(a)
    return sequence_fibo


def fibo_sequence_desired(number):

    """
    Generates sequence till desired number in sequence or until the sequence passes it.
    :parameter: (positive) int
    :return: list
    """

    while True:  # Loop checks if input is valid
        if not str(number).isnumeric():  # Checks if input is a number, negative and strings numbers are invalid
            print("Not a valid number")
            number = input("Enter positive number: ")
        else:
            break

    number = int(number)  # Converts string number back to integer

    # Variables
    a = 0
    b = 1
    c = 0

    # Empty List
    sequence_fibo = []

    # Algorithm
    while a != number and a < number:
        c = b
        b = b + a
        sequence_fibo.append(a)
        a = c

    sequence_fibo.append(a)
    return sequence_fibo
