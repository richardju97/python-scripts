# Boolean Algebra
# Various Calculations related to Boolean Algebra
# Based on CS 25000 "Computer Architecture" Course at Purdue University

numInputs = 2
numCol = numInputs + 1

rowDivider = "-"
for i in range((numCol*6)):
	rowDivider += "-"
	
row = "|"
input = "A"
for j in range(numInputs):
	row += "  " + chr(ord(input)+j) + "  |"

row += "  Q  |"
	
print rowDivider
print row
print rowDivider
print "|  0  |  0  |  0  |"
print "|  0  |  1  |  0  |"
print "|  1  |  0  |  0  |"
print "|  1  |  1  |  1  |"
print rowDivider