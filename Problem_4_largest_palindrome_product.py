"""
Largest palindrome product

Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

#in order to make the solution universal, the function displays largest palindrom lower than provided number

from numpy import floor

def largest_palindrom_lower_than(n): #redudant after all
    palindrom = ""
    for i in range (n-1, 1, -1):
        palindrom = str(i)
        if all(palindrom[j] == palindrom[-(j+1)] for j in range(0, int(floor((len(str(i))/2))+1))):
            break
        else:
            continue
    return int(palindrom)


def is_palindrom(n):
    palindrom = str(n)
    if all(palindrom[j] == palindrom[-(j+1)] for j in range(0, int(floor((len(str(n))/2))+1))):
        return True
    else:
        return False


def largest_palindrom_of_3_digits_product():
    palindroms = []
    palindroms_product_of = []
    for i in range(100,999):
        for j in range(100,999):
            if is_palindrom(i*j) == True and i*j not in palindroms:
                palindroms.append(i*j)
                palindroms_product_of.append([[i],[j]])
                
    print(palindroms)           
    return ("Largest palindrom being product of two 3-digits number is {}, result of {} and {} multiplication".format(max(palindroms), str(palindroms_product_of[palindroms.index(max(palindroms))][0]), str(palindroms_product_of[palindroms.index(max(palindroms))][1])))

largest_palindrom_of_3_digits_product()