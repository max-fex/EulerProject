"""
Largest palindrome product
Problem 4
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


from math import floor

def palindrome_checker(n):
    s = str(n)
    l = len(s)
    result = True
    for i in range (0, floor(l/2), 1):
        if s[i] != s[l-1-i]:
            result = False
            break
    return result

"""
# palindrome_checker tests:
print(palindrome_checker(123))
print(palindrome_checker(1234))
print(palindrome_checker(123456654321))
print(palindrome_checker(1234567654321))
print(palindrome_checker(12345665432))
print(palindrome_checker(1234567654321))
print(palindrome_checker(1235567654321))
"""


a = 999
b = 999

def larges_palindrome():
    max_palindrome = k = j = 0
    for k in range(a, 500-1, -1):
        for j in range(b, 100-1, -1):
            mult = k * j
            if palindrome_checker(mult):
                if mult > max_palindrome:
                    max_palindrome = mult
                    max_k = k
                    max_j = j
    print("The largest palindrome "
          "made from the product of two 3-digit numbers "
          "is %d = %d × %d." % (max_palindrome, max_k, max_j))

larges_palindrome()

# Answer: The largest palindrome made from the product of two 3-digit numbers is 906609 = 993 × 913.
# OK
# Problem insight: https://projecteuler.net/overview=004

