# Continuation of physics.py until I can find a better organization method of these files
# This file primarily focuses on friction problems

import math #needed for trigonometry functions

# Gravitational Acceleration in meters per second squared
g = 9.8

# Kinetic Friction Pulley System
# Given weights of both blocks in a pulley system, finds Kinetic Friction Coefficient
# Assumes that both blocks are moving at a constant velocity

sittingBlock = input("Mass of the Sitting Block: ")
fallingBlock = input("Mass of the Falling Block: ")

# sittingWeight = sittingBlock * g
# fallingWeight = fallingBlock * g
# kineticCo = fallingWeight / sittingWeight

kineticCO = fallingBlock / sittingBlock

print "Kinetic Coefficient of Friction = " + str(kineticCo)

# Static Friction (Force needed to start motion)
staticCO = input("Static Coffeffcient of Friction: ")
mass = input("Mass of resting Object (kilograms): ")

Fweight = mass * g
forceNeeded = Fweight * staticCO
print "Force needed to move object = " + str(forceNeeded) + " N"

