"""
Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is 1**2 +2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is (1+2..+10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 285 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


"""
import numpy as np
vector = np.array([range(1,101)])
vector

sum_of_squares = (vector**2).sum()
sum_of_squares

square_of_sum = (vector).sum()**2
square_of_sum

result = square_of_sum-sum_of_squares
result
