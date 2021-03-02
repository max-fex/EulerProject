"""
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

import time
from cmath import sqrt
from math import floor


def time_decorator(func):
    def time_wrapper(n):
        count_start = time.time()
        func(n)
        count_stop = time.time()
        execution_time = count_stop - count_start
        print ("Function execution time is " +
               str(execution_time) + " seconds.\n")
    return time_wrapper

def prime_number_checker(n):
    result = True
    for y in range(2, n):
        if n % y == 0:
            result = False
            break
        else:
            pass
            y += 1
    return result

def prime_number_checker_for_odds(n):
    result = True
    for y in range(3, n):
        if n % y == 0:
            result = False
            break
        y += 2
    return result

def prime_number_checker_for_odds_1(n):
    result = True
    for y in range(3, n, 2):
        #print("PRIME CHECKER. y = ", y)
        if n % y == 0:
            #print("PRIME CHECKER. y = ", y)
            result = False
            break
    return result



@time_decorator
def max_prime_factor_function_1(n):
    max_prime_factor = 0
    for x in range(1, n+1):
        #if investigated_number % x == 0 and prime_number_checker(x):
        if n % x == 0 and prime_number_checker(x):
            max_prime_factor = x
            #print("prime factor: ", str(max_prime_factor))
            x += 1
        else:
            x +=1
            pass
    print("[Option 1] MAX prime factor of  %d  is:  %d." % (n, max_prime_factor))

@time_decorator
def max_prime_factor_function_2(n):
    x = n
    while True:
        x = x - 1
        if n % x == 0 and prime_number_checker(x):
            max_prime_factor = x
            print("MAX prime factor 2: ", str(max_prime_factor))
            break
        else:
            x = x - 1

@time_decorator
def max_prime_factor_function_3(n):
    x = n
    while True:
        x -= 1
        if n % x == 0 and prime_number_checker(x):
            max_prime_factor = x
            print("MAX prime factor 3: ", str(max_prime_factor))
            break
        else:
            x -= 1

@time_decorator
def max_prime_factor_function_4(n):
    if n % 2 == 0:
        x = n - 1
    while True:
        if n % x == 0 and prime_number_checker(x):
            max_prime_factor = x
            print("MAX prime factor 4: ", str(max_prime_factor))
            break
        x -= 2

@time_decorator
def max_prime_factor_function_5(n):
    if n % 2 == 0:
        x = n - 1
    x = n
    while True:
        if n % x == 0 and prime_number_checker_for_odds(x):
            max_prime_factor = x
            print("MAX prime factor 5: ", str(max_prime_factor))
            break
        x -= 2

@time_decorator
def max_prime_factor_function_6(n):
    if n % 2 == 0:
        x = n - 1
    else:
        x = n
    while True:
        if n % x == 0:
            #print("Factor: ", x)
            if prime_number_checker_for_odds_1(x):
                max_prime_factor = x
                print("[Option 6] MAX prime factor of  %d  is:  %d." % (n, max_prime_factor))
                break
            else:
                #print("int else pass")
                pass
        x -= 2
        #print("new x: ", x)

@time_decorator
def max_prime_factor_function_7(n):
    root_floored = int(floor(sqrt(n).real))
    #print("Root floored: ", root_floored)
    if root_floored % 2 == 0:
        x = root_floored - 1
    else:
        x = root_floored
    while True:
        if n % x == 0:
            #print("Factor: ", x)
            if prime_number_checker_for_odds_1(x):
                max_prime_factor = x
                print("[Option 7] MAX prime factor of  %d  is:  %d." % (n, max_prime_factor))
                break
            else:
                #print("int else pass")
                pass
        x -= 2
        #print("new x: ", x)



#max_prime_factor_function_1(85319500)
#max_prime_factor_function_2(25319500)
#max_prime_factor_function_3(775147)
#max_prime_factor_function_4(775147)
#max_prime_factor_function_5(775146)
#max_prime_factor_function_6(85319500)
max_prime_factor_function_7(600851475143)
#print(sqrt(600851475143))
#print(floor(sqrt(600851475143).real))


#print(prime_number_checker(600851475143))
#print(prime_number_checker_for_odds_1(600851475143))


# Answer is: MAX prime factor of  600851475143  is:  6857.
# Solution 7 is the fastest - 0.086 seconds to run (other options could not find an answer in more than hour)
# OK!
# Problem insight: https://projecteuler.net/overview=003