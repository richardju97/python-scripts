# card.py
# Everything that has to do with the deck of cards

# enum for suits?

class Card:
	def __init__(self, num):
		self.number = num
		self.suit = 0

	def getSuit(self):
		return self.suit

	def getNumber(self):
		return self.number

class Deck:
	def __init__(self, shuffle, jokers):
		self.deck = []
		
