# Prime Factorization
# Planned:
# Wheel Factorization

"""
This file contains functions that factorizes a number and returns a list of factors.
It also has a simple function that checks if a number is prime.
"""

import math

INVALID_INPUT_WARNING = "Invalid input"

def brute_prime_factorization(number):
    """
    Brute-force algorithm that performs prime factorization for a given number
    :param number: (positive integer)
    :return: list
    """

    while True:  # Checks if input is a positive number
        if not str(number).isnumeric():
            print(INVALID_INPUT_WARNING)
            number = input("Enter positive number: ")
        else:
            break

    number = int(number)

    factor_list = [1]

    # Simple for-loop that divides number with divisor and checks for remainder

    for divisor_num in range(2, number + 1):  # Main algorithm
        if number % divisor_num == 0:
            factor_list.append(divisor_num)
        else:
            continue

    return factor_list


def prime_checker(number):
    """
    Checks if a number is prime
    :param number: (positive integer)
    :return: boolean
    """

    while True:  # Checks if input is a positive number
        if not str(number).isnumeric():
            print(INVALID_INPUT_WARNING)
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


def fermat_factorization(integer_be_factorized):
    """
    Uses Fermats method of factorization, stops when first two factors has been found
    :param integer_be_factorized: (positive odd integer)
    :return: list
    """

    while True:  # Checks if input is first_integer positive odd number
        if not str(integer_be_factorized).isnumeric() or int(integer_be_factorized) % 2 == 0:
            print(INVALID_INPUT_WARNING)
            integer_be_factorized = input("Enter positive odd number: ")
        else:
            break

    integer_be_factorized = int(integer_be_factorized)

    first_integer = math.ceil(math.sqrt(integer_be_factorized))
    second_integer = 0

    fermat_factor_list = []
    flag_fermat = True

    while flag_fermat is not False and first_integer < integer_be_factorized:  # Main Algorithm
        second_integer = (first_integer ** 2 - integer_be_factorized)  # is second_integer^2
        if not float(math.sqrt(second_integer)).is_integer():
            first_integer += 1
        else:
            fermat_factor_list.append(int(first_integer - math.sqrt(second_integer)))
            fermat_factor_list.append(int(first_integer + math.sqrt(second_integer)))
            flag_fermat = False

    return fermat_factor_list

# Combines all previous functions into one, might even be slower

def brutefermat_prime_factorization(integer_be_factorized):

    """
    A combination of brute-force divison and Fermat's method of factorization.
    If integer is odd, uses Fermat method first and then filters and performs brute-force method.
    If even uses brute-force method.
    Checks if number is prime before using any prime factorizon function, using prime_checker().
    :param integer_be_factorized: (positive integer)
    :return: list or string
    """

    if prime_checker(integer_be_factorized):  # Return list if number is prime
        return [1, integer_be_factorized]

    factor_list = [1]  # Technically 1 is a factor and is added initially

    # Puts factors using Fermat method into a list
    add_factors_list = list(fermat_factorization(integer_be_factorized))
    # Filters out factors, in order to perform less calculations when doing brute-force method
    factorset_diff = set(range(2, integer_be_factorized + 1)).difference(set(add_factors_list))
    enumerate_list = sorted(list(factorset_diff))

    if integer_be_factorized % 2 != 0:  # Main Algorithm, check if number odd
        for divisor_num in enumerate_list:
            print(divisor_num)
            if integer_be_factorized % divisor_num == 0:
                factor_list.append(divisor_num)

        # Combines list from both factorization methods
        factor_list = sorted(factor_list + add_factors_list)
        return factor_list
    return brute_prime_factorization(integer_be_factorized)
