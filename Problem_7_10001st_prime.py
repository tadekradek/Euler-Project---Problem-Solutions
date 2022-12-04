"""
10001st prime

Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""
import math

def is_prime(n):
    if any(n%i == 0 for i in range(2, math.ceil((n / 2) + 1))):
        return False
    else:
        return True


prime_generator = (i for i in range(2,1000000000000000) if is_prime(i))

prime_numbers = []
for i in range (1,10002):
    prime_numbers.append(next(prime_generator))

prime_numbers[-1]
