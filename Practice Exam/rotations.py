# rotations.py

import math

class ConstantRotatingObject:
	def __init__(self):
		self.radius = None
		self.rotationalSpeed = None
		self.translationalSpeed = None
		
	def setRadius(self, r):
		self.radius = r
		
	def setRotationalSpeed(self, o):
		self.rotationalSpeed = o
		
	def setTranslationalSpeed(self, v):
		self.translationalSpeed = v
		
	def calcRotationalSpeed(self, t):
		return 2.0 * PI / t
		
	def calcTranslationalSpeed(self, t):
		return 2.0 * PI * self.radius / t