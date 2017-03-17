# Extension of physics.py, with a focus on air resistance

import math

# Given maximum pulling force, the dimensions of an object's cross section (e.g. Car), coEfficient of Drag

# Assumes air density is 1.0 kg/m^3 (standard for 20 degrees Celsius)
rho = 1.2

#Coefficient of Drag
CD = input("Coefficient of Drag: ")
Ax = input("Horizontal dimension of Corresponding Cross Section: ")
Ay = input("Vertical dimension of Corresponding Cross Section: ")

#Cross Sectional Area
A = Ax * Ay

Fpull = input("Maximum Pull Force: ")

Vmax = math.sqrt(Fpull * 2 / (rho * A * CD))
print "Maximum possible Velocity = " + str(Vmax)