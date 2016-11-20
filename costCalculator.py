

cart = []

modeOptions = "Please select your mode:\n1. Quick Cost Calculator\n2. Shopping Cart\n"
options = "Please select an option:\n1. Add Item\n2. Set Tax Rate\n3. Calculate Total Cost\n4. Exit"

class Item: 
	def __init__(self, q, n, c):
		self.quantity = q
		self.name = n
		self.cost = c 

def addItem():
	numItems = input("Enter the number of Items you want to order: ")
	cart.append(Item(numItems, "Wings", 0.65))

def calcTotalCosts():
	tcost = 0
	for i in range(cart.length):
		tcost += (cart[i].quantity * cart[i].cost)

mode = input(modeOptions)
if (mode == 1):
	numItems = input("Enter quantity: ")
	salesPrice = input("Enter sales price of each item: ")
	taxRate = input("Enter tax rate, or 0 if you not applicable")
	
	if (taxRate == 0):
		cost = numItems * salesPrice
	else:
		cost = numItems * salesPrice * ((taxRate / 100.0) + 1)
	
	print "Total Cost: $" + str(round(cost, 2))	

elif (mode == 2):
	print "This is mode 2"

else:
	print "Please select a valid mode."
	mode = input(modeOptions)

# selection = input(options)
# while (selection != 4):
# 	if (selection == 1):
# 		addItem()
# 	elif (selection == 2):
# 		tax = input("Enter the tax rate in your area: ")
# 	elif (selection == 3):
# 		calcTotalCosts();	
# 				
# 	selection = input(options)
# 		
# print "Tax = " + str(tax) + "%"
# print "Number of Wings ordered: " + str(cart[0].quantity)
# cost = cart[0].quantity * cart[0].cost * ((tax / 100.0) + 1)
# 
# print "Total cost: $" + str(round(cost, 2))
