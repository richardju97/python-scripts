# powersum.py
# script for computing powersums based on Class 1 of Mathematics B at Tohoku University (special JYPE course)

# The kth power sum is defined as
# 1^k + 2^k + ... + n^k

from math import factorial

# Combination
# Function for computing Combinations nCr

def ncr(n, r):
    combination = factorial(n) / (factorial(n - r) * factorial(r))
    print(combination)

ncr(4, 2)
