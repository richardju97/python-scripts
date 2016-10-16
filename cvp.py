
# Basic Break Even Point Calculator based the CVP Formula
# Requires user input for the Selling Price per Unit, Unit Variable Cost, and Total Fixed Cost

cvpoption_string = "Please select which of the following you want to calculate.\n"
cvpoption_string += "1. Break Even Point (in terms of units).\n"
cvpoption_string += "2. Units needed to reach target net income.\n"

option = input(cvpoption_string)

sellingPrice = input("Enter Unit Selling Price: ")
var = input("Enter Unit Variable Cost: ")
fixed = input("Enter Total Fixed Cost: ")

if (option == 1):
	units = fixed / (sellingPrice - var)
	print "You need to sell " + str(units) + " units in order to break even."

elif (option == 2):
	targetNI = input("Enter Target Net Income: ")
	units = (targetNI + fixed) / (sellingPrice - var)
	print "You need to sell " + str(units) + " units in order to earn a net income of " + str(targetNI) + "."

# Note that this is currently truncating instead of rounding up
