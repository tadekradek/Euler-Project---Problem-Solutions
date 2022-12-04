"""
Special Pythagorean triplet
 
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

# a and b needs to satisfy the condition 1000 = a + b - (a*b)/500
# or unsimplied version = 1000000 = 2000a + 2000b - 2a*b

values = []

for a in range (1,1000):
    for b in range (a,1000):
        if (2000*a + 2000*b - 2*a*b == 1000**2):
            values.append(a)
            values.append(b)

c = 1000 - values[0] - values[1]
c

result = values[0]*values[1]*c
result

# full contact method, also works but much slower
# values = []
# for a in range (1,1000):
#     for b in range(a,1000):
#         for c in range(b,1000):
#             if(a+b+c==1000) and (a**2+b**2==c**2):
#                 values.append(a)
#                 values.append(b)
#                 values.append(c)
                
