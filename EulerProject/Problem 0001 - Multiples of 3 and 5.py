"""
Multiples of 3 and 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
max_limit = 1000
sum = 0
for i in range (0, max_limit):
    if i%3==0 or i%5==0:
        sum=sum+i
    else:
        pass
print(sum)

# OK!
# Problem insight: https://projecteuler.net/overview=001
