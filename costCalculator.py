

cart = []

modeOptions = "Please select your mode:\n1. Quick Cost Calculator\n2. Shopping Cart\n"
options = "Please select an option:\n1. Add Item\n2. Set Tax Rate\n3. Calculate Total Cost\n0. Exit\n"

taxRate = 0

class Item: 
	def __init__(self, q, n, c):
		self.quantity = q
		self.name = n
		self.cost = c 

def addItem():
	itemName = raw_input("Enter the name of the item: ")
	numItems = input("Enter the number of " + itemName + " you want to purchase: ")
	salesPrice = input("Enter sales price for each individual item: ")
	cart.append(Item(numItems, itemName, salesPrice))
	print "\n"

def calcTotalCosts():
	tcost = 0
	for i in cart:
		print "---------------------"
		print str(i.quantity) + " x " + i.name + " @ " + str(i.cost) + " = " + str(round(i.quantity * i.cost, 2)) 
		tcost += (i.quantity * i.cost)
	
	print "---------------------\n"
	
	if (taxRate != 0):
		taxCost = tcost * ((taxRate/100.0))
		print "Tax: $" + str(round(taxCost, 2))
		tcost += taxCost
		
	print "Total Cost: $" + str(round(tcost, 2)) + "\n"

mode = input(modeOptions)
if (mode == 1):
	numItems = input("Enter quantity: ")
	salesPrice = input("Enter sales price of each item: ")
	taxRate = input("Enter tax rate, or 0 if not applicable: ")
	
	if (taxRate == 0):
		cost = numItems * salesPrice
	else:
		cost = numItems * salesPrice * ((taxRate / 100.0) + 1)
	
	print "Total Cost: $" + str(round(cost, 2))	

elif (mode == 2):
	selection = input(options)
	while (selection != 0):
		if (selection == 1):
			addItem()
		elif (selection == 2):
			taxRate = input("Enter the tax rate in your area: ")
		elif (selection == 3):
			calcTotalCosts();	
		else:	
			print "Please enter a valid input: "
		selection = input(options)

else:
	print "Please select a valid mode."
	mode = input(modeOptions)
