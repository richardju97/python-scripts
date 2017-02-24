# Collection of various Calculations
# Based on the MA/STAT 41600 "Probability" Course at Purdue University

from combination import C
from math import pow, sqrt

# Thought - this might work better with lots of classes and object oriented programming rather than just functions

# Bernoulli Random Variable
# X~Bernoulli(p), p = probability of success
def bernoulli():
	return 0
	
# Expected Value
# E(x) = p
def ex_bernoulli():
	return 0
	
# Variance
# Var(x) = pq
def var_bernoulli():
	return 0

# Binomial Random Variable
# X~Bin(n, p), n = total number of trials, p = probability of success
class binomial:
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
	def expected():
		return self.n * self.p
	
# 	Var(x) = npq
	def variance():
		return self.n * self.p * self.q
	
# Geometric Random Variable (success)
def geo_success():
	return 0

# Geometric Random Variable (failure)
def geo_failure():
	return 0

# E(x) = 1/p	
def ex_geo():
	return 0
	
# Var(x) = q/(p^2)
def var_geo():
	return 0

# Negative Binomial Random Variable
def NB():
	return 0

# E(x) = r/p
def ex_NB():
	return 0
	
# Var(x) = rq/(p^2)
def var_NB():
	return 0

# Poisson Random Variable
# X~Poisson(lambda), lambda = number of occurrences in a given time frame
def poisson():
	return 0
	
# E(x) = lambda
def ex_possion():
	return 0
	
# Var(x) = lambda
def var_poission():
	return 0

