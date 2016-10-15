
# Basic Break Even Point Calculator based the CVP Formula
# Requires user input for the Selling Price per Unit, Unit Variable Cost, and Total Fixed Cost

sellingPrice = input("Enter Unit Selling Price: ")
var = input("Enter Unit Variable Cost: ")
fixed = input("Enter Total Fixed Cost: ")

units = fixed / (sellingPrice - var)

print "You need to sell " + str(units) + " units in order to break even"
# Note that this is currently truncating instead of rounding up