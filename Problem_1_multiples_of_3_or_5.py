"""
Multiples of 5

Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

def multiples_of_3_or_5(x):
    sum_of_all = 0
    for i in range(0,x+1):
        if i%3 == 0 or i%5 ==0:
            sum_of_all += i
    return sum_of_all

multiples_of_3_or_5(999)


