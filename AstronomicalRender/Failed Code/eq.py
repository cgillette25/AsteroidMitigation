import math
import numpy as np
# Get user input for asteroid
print("Please enter the following information about the asteroids. \nWe will assume all values are with respect to SI units.")
print("Enter only numerical values;")
mass = int(input("What is mass of the asteroid? "))
acceleration = int(input("What is the acceleration of the asteroid? "))
speed = int(input("what is the velocity of the asteroid? "))
time= int(input("You want to know the position of the asteroid after ___ amount of days. "))
position1 = [0,0,0]
position2=[0,0,0]
# Size of array = 3
p1=int(input("Enter x-coordinate of the current position of the asteroid: "))
p2=int(input("Enter y-coordinate of the current position of the asteroid: "))
p3=int(input("Enter z-coordinate of the current position of the asteroid: "))

position1[0]=p1
position1[1]=p2
position1[2]=p3

print("So your asteroid is currently at: ", position1, ". With the centre of the Earth at origin.")

xtime=int(input("How many days back was the initial point noted? "))

P1=int(input("Enter x-coordinate of the initial position of the asteroid: "))
P2=int(input("Enter y-coordinate of the initial position of the asteroid: "))
P3=int(input("Enter z-coordinate of the initial position of the asteroid: "))

position2[0]=P1
position2[1]=P2
position2[2]=P3

print("So your asteroid was initially at: ", position2, ". With the centre of the Earth at origin.")
print("It is moving at ", speed, " km/h and has a mass of ", mass, " kilograms.")


#d1=math.sqrt((P1**2)+(p1**2))
#d2=math.sqrt((P2**2)+(p2**2))
#d3=math.sqrt((P3**2)+(p3**2))
unit_mag=math.sqrt(((p1-P1)**2) + ((p2-P2)**2) + ((p3-P3)**2))

unit_vector=[0,0,0]
unit_vector[0]=(p1-P1)/unit_mag
unit_vector[1]=(p2-P2)/unit_mag
unit_vector[2]=(p3-P3)/unit_mag

# Calculate the distance, they gave us time, the velocity, and the acceleration
d=(speed*time) #+ (0.5*acceleration*(time**2))
#d=d/1000 #converting from meters to kilometers

print("After ", time, " days, the asteroid will move ", d, "kilometers")

Final_position=[p1 - d*unit_vector[0], p2 - d*unit_vector[1], p3 - d*unit_vector[2]]

print("After ", time, " days, your asteroid will be at: ", Final_position)

'''
We will gather more data to determine legitimate formulas for the effect of
the Sun's gravitational pull on asteroids as well as its trajectory, for now we just have a basic code
not taking into account other effects due to the environment
'''

#sun_gravity = int(input("What is the gravitaitonal effect of the sun on the asteroid?"))
#cout << what is the diameter of the asteroid?
#cout << how far away is the asteroid?
#cout << what is the speed of the asteroid?
# Program trajectory
# calcualte trajectory, and output trajectory
# K r/|r|^3 = M<x''(t),y''(t),z''(t)>
#Determine threat level/casuality count
# Depending on speed, and size of asteroid
#Given launch date determine force of impact
# cout << all info for both groups

