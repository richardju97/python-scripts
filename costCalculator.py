

cart = []

class Item: 
	def __init__(self, q, n, c):
		self.quantity = q
		self.name = n
		self.cost = c 

def addItem():
	numWings = input("Enter the number of Wings you want to order: ")
	cart.append(Item(numWings, "Wings", 0.65))

#input("Please select an option: 1. Add Item 2. Set Tax Rate")

tax = input("Enter the tax rate in your area: ")

addItem()

print "Tax = " + str(tax) + "%"
print "Number of Wings ordered: " + str(cart[0].quantity)
cost = cart[0].quantity * cart[0].cost * ((tax / 100.0) + 1)

print "Total cost: $" + str(round(cost, 2))