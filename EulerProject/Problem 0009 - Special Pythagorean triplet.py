"""
Special Pythagorean triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
from math import sqrt

def pyth_triplet_checker(a, b, c):
    result = False
    left = a*a + b*b
    right = c*c
    if  left == right:
        print("%d^2 + %d^2 = %d^2  : " % (a, b, c),
              "%d + %d = %d" % (a*a, b*b, c*c),
              "  :  %d = %d" % (left, right))
        result = True
    #print(result)
    return result

#print(pyth_triplet_checker(1, 2, 3))
#print(pyth_triplet_checker(3, 4, 5))
#print(pyth_triplet_checker(256, 243, 501))
#print(pyth_triplet_checker(1, 498, 501))
#print(pyth_triplet_checker(4, 495, 501))
#print(pyth_triplet_checker(16, 483, 501))


def pyth_triplet_searcher(sum_of_abc):
    stop = False
    for a in range (1, sum_of_abc):
        if not stop:
            b = 1
            while a + b + 1 <= sum_of_abc:
                c = sum_of_abc - a - b
                #print(a, b, c)
                if pyth_triplet_checker(a, b, c):
                    print("Product of abc: ", a * b * c)
                    stop = True
                    break
                else:
                    b += 1

pyth_triplet_searcher(1000)

# Answer: Product of abc:  31875000
# 200^2 + 375^2 = 425^2  :  40000 + 140625 = 180625   :  180625 = 180625
# OK!
# Problem insight: https://projecteuler.net/overview=009
