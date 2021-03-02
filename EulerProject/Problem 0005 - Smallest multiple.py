"""
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def evenly_divisible_checker(number, range_start, range_stop):
    result = True
    for i in range (range_start, range_stop+1, 1):
        if number % i != 0:
            result = False
            break
    return result

#print(evenly_divisible_checker(2520, 1, 10))

a = 1
while True:
    if evenly_divisible_checker(a, 1, 20):
        print(a)
        break
    a += 1

# Answer is: 232792560
# OK!
### The solution is not optimized from resourse/time perspective!
# Problem insight: https://projecteuler.net/overview=005
