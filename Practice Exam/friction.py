# Continuation of physics.py until I can find a better organization method of these files
# This file primarily focuses on friction problems

import math #needed for trigonometry functions

# Gravitational Acceleration in meters per second squared
g = 9.8

# Momentum & Friction Relationship
# If a Car/Object of X mass is moving at Y velocity/speed, w/ Z coefficient of friction 
# How long does it take for the driver to stop after applying the brakes?
# How Far does the car travel?
# Note that Force = Momentum / Time, or rather Force is the rate at which Momentum Changes
# Momentum = Mass * Velocity
# Force of Friction = Normal Force * Coefficient of Friction = g * mass * coefficient
# Therefore, Force = Momentum / Time; Time = Momentum / Force
# 		--> Time = Mass * Velocity / (g * Mass * coefficient) = Velocity / (g * coefficient)
# Notice that Mass is actually irrelevant to this problem 

# mass = input("Mass of Car/Object: ")
velocity = input("Velocity at which Car/Object is traveling: ")
kineticCo = input("Coefficient of Kinetic Friction: ")

time = velocity / (g * kineticCo)
print "Time taken to stop = " + str(time) + " seconds"

# Since the car stops (ending velocity = 0), the average is simply half the initial velocity
distance = velocity / 2 * time
print "Distance Traveled after applying brakes = " + str(distance) + " meters"

# Inclined Planes
# Acceleration from angle of slope and coefficient of sliding friction

angle = input("Angle of the Inclined Plane: ")
kineticCO = input("Coefficient of Kinetic Friction: ")

a = g * (math.sin(math.radians(angle)) - kineticCO * math.cos(math.radians(angle)))
print "Acceleration = " + str(a) + " meters per second squared"

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

