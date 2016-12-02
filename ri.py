#Residual Income Calculator

options_string = "1. Set Income\n2. Set Average Invested Capital\n3. Set Imputed Interest Rate\n4. Calculate Residual Income\n0. Exit Program\n"

option = input(options_string)

income = 0
avgInvestedCapital = 0
imputedInterestRate = 0

while (option != 0):
	
	if (option == 1):
		income = input("Set Income: ")
	
	elif (option == 2):
		avgInvestedCapital = input("Set Average Invested Capital: ")
	
	elif (option == 3):
		imputedInterestRate = input("Set Imputed Interest Rate: ")
	
	elif (option == 4):
		residualIncome = income - (avgInvestedCapital * imputedInterestRate)
		print "Income = " + str(income) + "\n"
		print "Average Invested Capital = " + str(avgInvestedCapital) + "\n"
		print "Imputed Interest Rate = " + str(imputedInterestRate) + "\n"
		print "Residual Income = " + str(residualIncome) + "\n"
	
	option = input(options_string)
