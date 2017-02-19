# Given two parent binary strings, computes an offspring binary string based on the selected genetic algorithm

# Single Point Cross Over

def singleXOver(parent1, parent2, n):
	if (len(parent1) > n):
		return parent1[:n] + parent2[n:]
		

# Double Point Cross Over
def doubleXOver(parent1, parent2, n, m):
	if (len(parent1) > n and len(parent1) > m):
		return parent1[:n] + parent2[n:m] + parent1[m:]
# Uniform Cross Over


# Arithmetic Cross Over

# Mutation

# Test Cases
parent1 = '11001011'
parent2 = '11011111'
# print singleXOver(parent1, parent2, 5)
# print doubleXOver(parent1, parent2, 2, 7)