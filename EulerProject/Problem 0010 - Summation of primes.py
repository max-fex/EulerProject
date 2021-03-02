"""
Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

def prime_number_checker_from_3(n):
    result = True
    for y in range(3, n):
        if n % y == 0:
            result = False
            break
        y += 2
    #print(result)
    return result

def sum_of_prime_factors_below_n(n):
    sum_of_primes = 2
    x = 3
    while x <= n:
        print("X: ", x)
        if prime_number_checker_from_3(x):
            prime_factor = x
            sum_of_primes += prime_factor
            print("Current sum: ", sum_of_primes)
        x += 2
    print(sum_of_primes)

#sum_of_prime_factors_below_n(2000000)

def primes_sieve1(limit):
    primes = dict()
    for i in range(2, limit + 1):
        primes[i] = True
    for i in primes:
        factors = range(i,limit + 1, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]

print(primes_sieve1(1000000))
