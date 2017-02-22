# Calculates Combination (nCr), where 0 <= r <= n

n = 6
r = 4

numerator = 1
for i in range(r+1, n+1):
	numerator *= i

diff = n - r

denominator = 1
for i in range(1, diff+1):
	denominator *= i
	
nCr = numerator / denominator

print nCr