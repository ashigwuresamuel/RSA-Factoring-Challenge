#!/usr/bin/python3

import sys
import time
import math


def factorize_number(num_1):
    factors = []
    divisor = 2

    while num_1 > 1:
        if num_1 % divisor == 0:
            factors.append(str(divisor))
            num_1 //= divisor

        else:
            divisor += 1

    return '*'.join(factors)


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 factors.py <filename>")
        return

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            for line in file:
                number = int(line.strip())
                factorization = factorize_number(number)
                print(f"{number}={factorization}")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except ValueError:
        print("Invalid format. file must contains only natural numbers.")
    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    main()
