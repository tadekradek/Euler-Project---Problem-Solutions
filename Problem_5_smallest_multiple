"""
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import numpy as np
import math

def is_prime(n):
    if any(n%i == 0 for i in range(2, math.ceil((n / 2) + 1))):
        return False
    else:
        return True

def factors(n):
    factors = np.array([])
    for i in range(2, math.ceil((n / 2) + 1)):
        if n%i ==0:
            factors = np.append(factors,i)
    return factors

def prime_factors(n):
    factors = np.array([])
    for i in range(2, math.ceil((n / 2) + 1)):
        if n%i ==0 and is_prime(i):
            factors = np.append(factors,i)
    return factors

factors(125)
prime_factors(125)

def smallest_evenly_divisible_in_range(a,b):

    # the smallest number that could meet the condition has to be non less than multiplication of all prime factors of this number,
    # so in first step I divide the range from 1 to 20 (or in general cases from 1 to n) into prime and non prime numbers
    

    prime_numbers = np.array([])
    non_prime_numbers_in_range = np.array([])
    for i in range(a,b+1):
        if is_prime(i):
            prime_numbers = np.append(prime_numbers,i)
        else:
            non_prime_numbers_in_range = np.append(non_prime_numbers_in_range,i)
    
    to_multiply = prime_numbers

    #once we have list of prime numbers in this range, we are multiplying them
    #now, for every non-prime numbers we are checking if the result of multiplication is divisible by this non-prime number
    #if no, then we are checking prime factors of non-prime number

    for i in non_prime_numbers_in_range:
        if np.prod(to_multiply)%i !=0:
            print(i)
            for j in range (0, len(prime_factors(i))):
                if (np.prod(to_multiply)*np.prod(prime_factors(i)[j]))%i==0:
                    print(prime_factors(i)[j])
                    print(to_multiply)
                    to_multiply = np.append(to_multiply,prime_factors(i)[j])
                    print(to_multiply)
                    break

    return np.prod(to_multiply)


result = smallest_evenly_divisible_in_range(1,20)
result


