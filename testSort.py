# Test Case File for Various Sorting Algorithms

import sys
from random import randint

# Generates an Array of size n with random Integers
def generateRandomArray(n):
	myArray = []
	for i in range (0, n):
# 		r = randint(0, 100)
		myArray.append(randint(0, 100))
	return myArray
		
print generateRandomArray(10)
