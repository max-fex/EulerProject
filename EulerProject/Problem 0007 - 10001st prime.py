"""
10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""
# Setting global variable to reflect current program location
from os import path
__path__ = [path.dirname(path.abspath(__file__))]
from .Helpers import time_decorator_w_start as tds


def prime_number_checker_universal(n):
    result = True
    if n == 1:
        result = False
    elif n == 2:
        result = True
    else:
        for y in range(3, n):
            if n % y == 0:
                result = False
                break
            y += 2
    #print(result)
    return result

#prime_number_checker_universal(1)
#prime_number_checker_universal(2)
#prime_number_checker_universal(3)
#prime_number_checker_universal(641)
#prime_number_checker_universal(600851475143600851475143600851475143600851475143)

@tds
def prime_searcher(n):
    i = 2
    prime_num = 3
    n_investigated = 3
    while i <= n:
        if prime_number_checker_universal(n_investigated):
            prime_num = n_investigated
            print("%d-st prime num  -  %d" % (i, prime_num))
            i += 1
        n_investigated += 2
    print("The  %d-st  prime number is  %d." % (i-1, prime_num))

prime_searcher(10001)

# Answer: The  10001-st  prime number is  104743.
# OK!
# Program is not optimized! ==>>
# ==>> Function execution time is 90.25813150405884 seconds.
# Problem insight: https://projecteuler.net/overview=007

