# Continuation of physics.py until I can find a better organization method of these files
# This file primarily focuses on tension problems

import math #needed for trigonometry functions

# Gravitational Acceleration in meters per second squared
g = 9.8

# Pulling a sled
# Assume no friction

mass = input("Mass of sled (kilograms): ")
angle = input("Angle above the horizontal (degrees): ")
pullForce = input("Force Exerted through pulling (Newtons): ")

# Acceleration of the sled
pullX = pullForce * math.cos(math.radians(angle))
a = pullX / mass
print "Acceleration = " + str(a) + " meters per second squared"

# Normal Force exerted on sled
Fweight = mass * g
pullY = pullForce * math.sin(math.radians(angle)) 
normal = Fweight - pullY
print "Normal Force exerted on the sled = " + str(normal) + " N"


# Suspended by two cables problem
# Simple Problem - Assumes cables of the same length are suspended at the same angle

mass = input("Mass of the suspended object (kilograms): ")
height = input("Distance between ceiling and the suspended object (meters): ")
length = input("Length of each cable (meters): ")

angle = math.degrees(math.asin(height / length))
print "Angle between cables and the ceiling = " + str(angle) + " degrees"

Fweight = mass * g
tension = Fweight / 2 / (height / length)
print "Tension in each cable = " + str(tension) + " N"