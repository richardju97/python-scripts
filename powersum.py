# powersum.py
# script for computing powersums based on Class 1 of Mathematics B at Tohoku University (special JYPE course)

# The kth power sum is defined as
# 1^k + 2^k + ... + n^k

from math import factorial
from math import pow

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
        return 1/(n + 1) * sum

def calcb(n):
    if (n == 1):
        return 1
    elif (n == 2):
        return 0.5
    else:
        return bernoullinum(n-1)

def powersum(k, n):
    sum = 0
    for i in range(0, k+1):
        sum += ncr(k+1, i) * calcb(i + 1) * (pow(n, k+1-i))

    return 1/(k+1) * sum

print(powersum(4, 2))
