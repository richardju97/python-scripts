# Boolean Algebra
# Various Calculations related to Boolean Algebra
# Based on CS 25000 "Computer Architecture" Course at Purdue University

numInputs = input("Number of Inputs desired: ")
numCol = numInputs + 1
numRows = 2**numInputs

rowDivider = "-"
for i in range((numCol*6)):
	rowDivider += "-"
	
rowHeader = "|"
input = "A"
binaryArray = []
for j in range(numInputs):
	rowHeader += "  " + chr(ord(input)+j) + "  |"
	binaryArray.append(0)

rowHeader += "  Q  |"
binaryArray.append('x')

print rowDivider
print rowHeader
print rowDivider

for k in range(numRows):
	row = "|"
	for l in range(numCol):
		row += "  " + str(binaryArray[l]) + "  |"
	print row

	for m in range(numCol-2, -1, -1):
		if (binaryArray[m] == 0):
			binaryArray[m] = 1
			break
		elif (binaryArray[m] == 1 and m != 0):
			binaryArray[m] = 0
			
print rowDivider