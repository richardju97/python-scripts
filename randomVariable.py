# Collection of various Calculations
# Based on the MA/STAT 41600 "Probability" Course at Purdue University

from combination import C
from math import pow, sqrt

# Discrete Random Variables

# Binomial Random Variable
# X~Bin(n, p), n = total number of trials, p = probability of success
class Binomial:
	def __init__(self, n, p):
		self.n = n
		self.p = p
		self.q = 1 - p

# 	Probability Mass Function, Px(x) or P(X = x)
	def pmf(self, x):
		coefficient = C(self.n, x)
		success = pow(self.p, x)
		failure = pow(self.q, self.n-x)
		probability = coefficient * success * failure
		return probability

# 	Expected Value, E(x) = np
	def expected(self):
		return self.n * self.p
	
# 	Variance, Var(x) = npq
	def variance(self):
		return self.n * self.p * self.q
		
# Bernoulli Random Variable
# X~Bernoulli(p), p = probability of success
class Bernoulli:
	def __init__(self, p):
		self.p = p
		self.q = 1 - p
	
# 	Probability Mass Function, Px(x) or P(X = x)
	def pmf(self):
		return self.p
	
# 	Expected Value, E(x) = p
	def expected(self):
		return self.p
	
# 	Variance, Var(x) = pq
	def variance(self):
		return self.p * self.q
		
# 	Summation of n Bernoulli random variables, or a Binomial Random Variable
	def summation(n):
		sumOfBernoulli = Binomial(n, self.p)
		return sumOfBernoulli
	
# Negative Binomial Random Variable
# X~NB(r, p), rth success of multiple independent trials with p = probability of success
class NegativeBinomial:
	def __init__(self, r, p):
		self.r = r
		self.p = p
		self.q = 1 - p

# 	Probability Mass Function, Px(x) or P(X = x)
	def pmf(x):
		coefficient = C(x-1, self.r-1)
		success = pow(self.p, self.r)
		failure = pow(self.q, x-self.r)
		return coefficient * success * failure

# 	Expected Value, E(x) = r/p
	def expected(self):
		return r / p
	
# 	Variance, Var(x) = rq/(p^2)
	def variance(self):
		return (r * q / pow(p, 2))	
	
# Geometric Random Variable
# X~Geometric(p), p = probability of success
class Geometric():
	def __init__(self, p):
		self.p = p
		self.q = 1 - p
	
# 	Geometric Random Variable (success)
	def pmf_success(x):
		return (pow(self.q, x-1), self.p)

# 	Geometric Random Variable (failure)
	def pmf_failure(x):
		return (pow(self.q, x) * self.p)

# 	Expected Value, E(x) = 1/p	
	def expected():
		return (1/self.p)
	
# 	Variance, Var(x) = q/(p^2)
	def variance():
		return (self.q / pow(self.p, 2))

# Returns the summation of r geometric random variables, or a Negative Binomial Random Variable with r=r and probability p
	def summation(r):
		sumOfGeometric = NegativeBinomial(r, self.p)
		return sumOfGeometric

# Poisson Random Variable
# X~Poisson(lambda), lambda = number of occurrences in a given time frame
# Note that we use l in place of lambda as lambda is a reserved word in python
class Poisson:
	def __init__(self, l):
		self.l = l

# 	Probability Mass Function, Px(x) or P(X = x)
	def pmf(x):
# 		e**-l * l**x / x!, need to figure out factorial
		return (exp(-l) * pow(l, x) / factorial(x))
	
# 	Expected Value, E(x) = lambda
	def expected(self):
		return self.l
	
# 	Variance, Var(x) = lambda
	def variance(self):
		return self.l

# Continous Random Variables
class Uniform:
	def __init__(self, a, b):
		self.a = a
		self.b = b
		
	def pdf(x):
		return ( (x - self.a) / (self.b - self.a) )
	
	def expected(self):
		return ( (self.a + self.b) / 2)
	
# 	def variance(self):
# 		return 

class Exponential:
	def __init__(self, l):
		self.l = l
		
	def expected(self):
		return 1 / self.l
		
	def variance(self):
		return 1 / pow(self.l, 2)
		
class Gamma:
	def __init__(self, alpha, beta):
		self.alpha = alpha
		self.beta = beta

# Need to look into functions that require a table (e.g. Normal RV)