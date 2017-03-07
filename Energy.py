# Energy.py
# Extension of physics.py

from math import pow

g = 9.81 #Gravitational Acceleration, in meters per second squared

class MovableObject:
	def __init__(self, mass):
		self.mass = mass
		
	def ke(Vinstant):
		return 0.5 * self.mass * pow(Vinstant, 2)
		
	def gpe(height):
		return height * g * self.mass
		
# 	def totalenergy():
# 	Need 1 total energy function for GPE+KE and another for height+velocity	
		