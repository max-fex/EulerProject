"""
Sum square difference
Problem 6
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers
and the square of the sum.
"""

def sum_of_squares(n):
    sum_sq = 0
    i = 1
    while i <= n:
        sum_sq += i*i
        i += 1
    return sum_sq

def square_of_sums(n):
    not_sq_sum = 0
    j = 1
    while j <= n:
        not_sq_sum += j
        j += 1
    sq_sum = not_sq_sum * not_sq_sum
    return sq_sum

def difference (n):
    df = square_of_sums(n) - sum_of_squares(n)
    print("The difference between the sum of the squares "
          "of the first  %d  natural numbers "
          "and the square of the sum is:  %d."
          % (n, df))


difference(100)

# Answer: The difference between the sum of the squares of the first  100  natural numbers and the square of the sum is:  25164150.
# OK!
# Problem insight: https://projecteuler.net/overview=006
