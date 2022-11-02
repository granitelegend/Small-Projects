# Prime Factorization

import math

def brute_prime_factorization(number):

    """
    Brute-force algorithm that performs prime factorization for a given number
    :param number: (positive integer)
    :return: list
    """

    while True:  # Checks if input is a positive number
        if not str(number).isnumeric():
            print("Invalid input")
            number = input("Enter positive number: ")
        else:
            break

    number = int(number)

    factor_list = [1]

    # Simple for-loop that divides number with divisor and checks for remainder

    for divisorNum in range(2, number + 1):
        if number % divisorNum == 0:
            factor_list.append(divisorNum)
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
            print("Invalid input")
            number = input("Enter positive number: ")
        else:
            break

    number = int(number)

    # Simple for-loop that divides number with divisor and checks for remainder

    for divisorNum in range(2,math.ceil(math.sqrt(number + 1))):  # Checks all factors lower than ceil(sqrt(number))
        if number % divisorNum == 0:
            return False
            break
        else:
            continue

    return True

def fermat_factorization(number):

    """
    Uses Fermats method of factorization, stops when first two factors has been found
    :param number: (positive odd integer)
    :return: list
    """

    while True:  # Checks if input is a positive odd number
        if not str(number).isnumeric() or int(number) % 2 == 0:
            print("Invalid input")
            number = input("Enter positive odd number: ")
        else:
            break

    number = int(number)

    a = math.ceil(math.sqrt(number))
    b = 0

    fermat_factor_list = []
    flag_fermat = True

    while flag_fermat != False and a < number:
        b = (a**2 - number)  # is b^2
        if not float(math.sqrt(b)).is_integer():
            a += 1
            continue
        else:
            fermat_factor_list.append(int(a-math.sqrt(b)))
            fermat_factor_list.append(int(a+math.sqrt(b)))
            flag_fermat = False

    return fermat_factor_list


def brutefermat_prime_factorization(number):  # Combines all previous functions into one, might even be slower

    """
    A combination of brute-force divison and Fermat's method of factorization.
    If integer is odd, uses Fermat method first and then filters and performs brute-force method.
    If even uses brute-force method.
    Checks if number is prime before using any prime factorizon function, using prime_checker().
    :param number: (positive integer)
    :return: list or string
    """


    if prime_checker(number):
        return [1, number]
    else:
        pass

    factor_list = [1]

    add_factors_list = list(fermat_factorization(number))  # Puts factors using Fermat method into list
    enumerate_list = sorted(list(set(range(2, number + 1)).difference(set(add_factors_list))))

    if number % 2 != 0:
        for divisorNum in enumerate_list:
            print(divisorNum)
            if number % divisorNum == 0:
                factor_list.append(divisorNum)
            else:
                continue

        factor_list  = sorted(factor_list + add_factors_list)
        return factor_list

    else:
       brute_prime_factorization(number)


