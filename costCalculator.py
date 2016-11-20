

cart = []

options = "Please select an option:\n1. Add Item\n2. Set Tax Rate\n3. Calculate Total Costn4. Exit"

class Item: 
	def __init__(self, q, n, c):
		self.quantity = q
		self.name = n
		self.cost = c 

def addItem():
	numWings = input("Enter the number of Wings you want to order: ")
	cart.append(Item(numWings, "Wings", 0.65))

def calcTotalCosts():
	tcost = 0
	for i in range(cart.length):
		tcost += (cart[i].quantity * cart[i].cost)

#input("Please select an option: 1. Add Item 2. Set Tax Rate")

selection = input(options)
while (selection != 4):
	if (selection == 1):
		addItem()
	elif (selection == 2):
		tax = input("Enter the tax rate in your area: ")
	elif (selection == 3):
		calcTotalCosts();	
				
	selection = input(options)
		
print "Tax = " + str(tax) + "%"
print "Number of Wings ordered: " + str(cart[0].quantity)
cost = cart[0].quantity * cart[0].cost * ((tax / 100.0) + 1)

print "Total cost: $" + str(round(cost, 2))