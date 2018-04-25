# powersum.py
# script for computing powersums based on Class 1 of Mathematics B at Tohoku University (special JYPE course)

# The kth power sum is defined as
# 1^k + 2^k + ... + n^k

from math import factorial

# Combination
# Function for computing Combinations nCr

def ncr(n, r):
    combination = factorial(n) / (factorial(n - r) * factorial(r))
    return combination

# Bernoulli Number
# Function for computing Bernoulli Numbers

def bernoullinum(n):
    if (n == 0):
        return 1
    else:
        sum = 0
        for i in range (0, n):
            sum -= ncr(n+1, i) * bernoullinum(i)
#            print(i)
        return 1/(n + 1) * sum

print(bernoullinum(2))
