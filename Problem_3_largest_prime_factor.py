"""Largest prime factor
 
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

"""
this is problably correct solution, but its clearly bruteforce method

def max_prime_factor(n):
    all_factors = []
    for x in range (1, n+1):
        if n%x == 0:
            all_factors.append(x)
            print(x)
    print(all_factors)

    prime_factors = []
    for i in all_factors[1:]:
        if not any(i%x == 0 for x in range(2,i)):
            prime_factors.append(i)

    return "All factors of number {} are {}, while only {} are prime and {} is the largest one".format(n, all_factors, prime_factors, max(prime_factors))

            
max_prime_factor(600851475143)
"""

def is_prime(n):
    if any(n%i == 0 for i in range(2,n)):
        return False
    else:
        return True

def max_prime_factor(n):   
    max_value = []     
    for x in range(2,n):
        if n%x == 0:
            if is_prime(int(n/x)) == True:
                max_value.append(int(n/x))
                print(len(max_value))
                print(max_value)
                break
            else:
                continue
    
    if len(max_value) == 1:
        return "The biggest prime factor of {} is {}".format(n, max_value[0])
    else:
        return "{}, the number you provided is prime, thus it has no other prime factors that 1 and itself".format(n)


max_prime_factor(600851475143)
