# Calculates Combination (nCr), where 0 <= r <= n
# NOTE: may be a more efficient method of calculating factorials
# http://cs.stackexchange.com/questions/14456/factorial-algorithm-more-efficient-than-naive-multiplication

# n = 6
# r = 4

def C(n, r):
# For efficiency, we factor out r! from n! to minimize the amount of computation time needed (especially for larger combinations)
	numerator = 1
	for i in range(r+1, n+1):
		numerator *= i

	diff = n - r

	denominator = 1
	for i in range(1, diff+1):
		denominator *= i
	
	nCr = numerator / denominator

	return nCr;

# numerator = 1
# for i in range(r+1, n+1):
# 	numerator *= i
# 
# diff = n - r
# 
# denominator = 1
# for i in range(1, diff+1):
# 	denominator *= i
# 	
# nCr = numerator / denominator
# 
# print nCr

# print C(6, 4)