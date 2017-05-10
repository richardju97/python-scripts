
# Offers various options for calculating the number of units required to achieve a certain target net income
# Requires user input for the Selling Price per Unit, Unit Variable Cost, and Total Fixed Cost

cvpoption_string = "Please select which of the following you want to calculate.\n"
cvpoption_string += "1. Break Even Point (in terms of units).\n"
cvpoption_string += "2. Units needed to reach target net income before taxes.\n"
cvpoption_string += "3. Units needed to reach target net income after taxes.\n"

option = input(cvpoption_string)

sellingPrice = input("Enter Unit Selling Price: ")
var = input("Enter Unit Variable Cost: ")
fixed = input("Enter Total Fixed Cost: ")

if (option == 1):
	units = fixed / (sellingPrice - var)
	print "You need to sell " + str(units) + " units in order to break even."

elif (option == 2):
	targetNI = input("Enter Target Net Income before taxes: ")
	units = (targetNI + fixed) / (sellingPrice - var)
	print "You need to sell " + str(units) + " units in order to earn a net income of " + str(targetNI) + " before taxes."

elif (option == 3):
	targetNI = input("Enter Target Net Income after taxes: ")
	taxRate = input("Enter Income Tax Rate in decimal form (e.g. 40% would be entered as 0.4): ")
	targetNIAT = targetNI / (1 - taxRate)
	units = (targetNIAT + fixed) / (sellingPrice - var)
	print "You need to sell " +str(units) + " units in order to earn a net income of " + str(targetNI) + " after taxes."
		
else:
	print "Error: Invalid Input"
		
# Note that this is currently appears to be truncating instead of rounding up
