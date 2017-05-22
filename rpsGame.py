#python file for simulating a rock-paper-scossors chain game

import sys
from random import randint

n = int(sys.argv[1])
matches = 0

lineA = []
lineB = []

for i in range(0, n):
	lineA.append("personA" + str(i))
	lineB.append("personB" + str(i))

#0 = Tie, 1 = A wins, 2 = B wins
def compete(idxA, idxB):
	global matches 
	matches += 1
	return randint(0, 299) % 3	

aSize = len(lineA)
bSize = len(lineB)
while (aSize != 0 and bSize != 0):
	i = 0
	j = 0
	temp = compete(i, j)
	while (temp == 0):
		print "Tie!!"
		if (i < aSize-1):
			i += 1
		if (j < bSize-1):
			j += 1
		temp = compete(i, j)
		
	if (temp == 1):
		print "Person A won!"
		if (j == 0):
			lineA.append(lineB[0])
			del lineB[0]
		else:
			lineA.extend(lineB[0:j])
			del lineB[0:j]
		print "Line A: " + str(lineA)
		print "Line B: " + str(lineB)
	elif (temp == 2):
		print "Person B won!"
		if (i == 0):
			lineB.append(lineA[0])
			del lineA[0]
		else:
			lineB.extend(lineA[0:i])		
			del lineA[0:i]
		print "Line A: " + str(lineA)
		print "Line B: " + str(lineB)
	aSize = len(lineA)
	bSize = len(lineB)	

print "--------------------"
print "Game Finished!"
print "The Game took " + str(matches) + " matches!"
