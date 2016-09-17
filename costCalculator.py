

import sys

tax = input("Enter the tax rate in your area: ")
numWings = input("Enter the number of Wings you want to order: ")

print "Tax = " + str(tax) + "%"
print "Number of Wings ordered: " + str(numWings)
cost = numWings * 0.65 * ((tax / 100.0) + 1)

print "Total cost: $" + str(round(cost, 2))