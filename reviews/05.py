# Goal: Simulate the motion of a rocket escaping from a gravity well
# Matrices and Vectors: Force vectors, thrust vs time, mass vs time, height vs time, Net force vs time
# Read in: Gravity well mass and radius
# Visualize: Graphs of distance vs time, net force vs time, mass vs time
import numpy as np
import matplotlib.pyplot as plt
# Defining Variables
Planetlist = [['Mercury', 2440000, (3.285 * 10**23)], ['Venus', 6051800, (4.867 * 10**24)], ['Earth', 6378000, (5.792 * 10**24)], ['Moon', 1740000, (7.348 * 10**22)], ['Mars', 3390000, (6.390 * 10**23)], ['Pluto', 1188000, (1.309 * 10**22)]]
Time = 0
Planetname = input('Planet?')
# Planetname, Distance, Planetmass = Planetlist[np.where((Planetlist == (Planetname)))]
# Row = np.where((Planetlist == (Planetname)))
# print(Row)
# Distance = Planetlist[Row, 1]
# Planetmass = Planetlist[Row, 2]
# print(Planetname)
# print(Distance)
# print(Planetmass)
Distance = 6378000  # m
GravityConstant = 6.6743 * (10**(-11))
Planetmass = 5.9722 * (10**24)  # kg
Rocketmass = float(input("Rocket engine mass?"))  # kg
Fuelmass = float(input("Fuel mass?"))  # kg
Gravityacceleration = ((Planetmass * GravityConstant)/(Distance**2))
Gravityforce = Gravityacceleration * (Rocketmass + Fuelmass)
# For checking accuracy of calculation-it returns 9.79N as the force of gravity which is close enough
print(Gravityforce)
Escapevelocity = ((Gravityacceleration * Distance * 2) ** 0.5)
# Critical for later points of the calculation, printed to verify
print(Escapevelocity, ' M/s')
Burnrate = 10  # kg/s
Fuelburntime = Fuelmass/Burnrate  # s
Rocketacceleration = ((Escapevelocity/Rocketmass)*(Fuelmass/Fuelburntime) - Gravityacceleration)
Time = 0
Timelist = []
Distancelist = []
while Time < 10:
    Distance += 0.5 * Rocketacceleration * (Time ** 2)
    Timelist.append(float(Time))
    Distancelist.append(float(Distance))
    Time += 1


plt.plot(Timelist, Distancelist)
plt.xlabel(Time)
plt.ylabel(Distance)
plt.show()

plt.show()

########################################################################
# Reviewer Comments
########################################################################
#
# 1.
#
#
# 2.
#
#
# 3.
#
#
# 4.
#
#
# 5.
#
#
# 6.
#
#
# 7.
#
#
# 8.
#
#
# 9.
#
########################################################################

