# Collection of Various Calculations for Physics
# Based on the PHYS 22000 Course ("") at Purdue University

#Needed for Trigonometry functions
import math

#Gravitational Acceleration on Earth, in meters per second
g = 9.8

# Given initial horizontal velocity and 0 vertical velocity
# Calculate how far the object will drop after traveling a certain distance

Vx = input("Horizontal Velocity: ")
distance = input("Distance: ")

time = distance / Vx
print "Time taken to reach given distance = " + str(time) + " seconds"

fallDistance = time*time * g / 2
print "Distance fallen = " + str(fallDistance) + " meters"

# Vector Components
# Given a Vector's magnitude and angle with the X-axis, find their X and Y components
# vectorMag = input("Vector Magnitude: ")
# print "Note that this program assumes the angle provided is the smaller of the two (between the X-axis and Negative X-Axis)"
# vectorAngle = input("Angle between Vector and the X/Negative-X Axis in degrees: ")

def calcVectorComponents(vectorMag, vectorAngle):
	Vx = vectorMag * math.cos(math.radians(vectorAngle))
	Vy = vectorMag * math.sin(math.radians(vectorAngle))

# 	print "X component of the vector = " + str(Vx)
# 	print "Y component of the Vector = " + str(Vy)

	return Vx, Vy

# Vector Addition
# Given two vectors acting on the same point and their angles, find the resulting Vector

vectorMag1 = input("Vector1 Magnitude: ")
vectorAngle1 = input("Angle between Vector1 and the X/Negative-X Axis in degrees: ")

vectorMag2 = input("Vector2 Magnitude: ")
vectorAngle2 = input("Angle between Vector2 and the X/Negative-X Axis in degrees: ")

(Vx1, Vy1) = calcVectorComponents(vectorMag1, vectorAngle1)
(Vx2, Vy2) = calcVectorComponents(vectorMag2, vectorAngle2)

Vx = Vx1 + Vx2
Vy = Vy1 + Vy2

print "Vx = " + str(Vx)
print "Vy = " + str(Vy)

vectorResultMag = math.sqrt(Vx*Vx + Vy*Vy)
print "Resulting Vector Magnitude = " + str(vectorResultMag)

vectorResultAngle = math.degrees(math.atan(Vy/Vx))
print "Resulting Vector Angle w/ the X-Axis = " + str(vectorResultAngle)

# Mechanics (Falling/Dropped Object)
# Given starting height of object, calculate time traveled
initialHeight = 400
timeTaken = (initialHeight * 2)**(0.5) / g
print "Time Taken = " + str(timeTaken) + " seconds"

finalVelocity = g * timeTaken
print "Final Velocity = " + str(finalVelocity) + " meters per second"

averageVelocity = finalVelocity / 2
print "Average Velocity = " + str(averageVelocity) + " meters per second"

# Given time taken to fall, calculate the height at which the object was dropped
timeTaken = 4
initialHeight = ((timeTaken * g)**2) / 2
print "Initial Height = " + str(initialHeight) + " meters"