
from math import sin, cos, pi
import math

import matplotlib.pyplot as plt



def max_height_time(v ,g):
    return ( 0 -v ) /(-g)

def height_of_cannon_ball(h0, v, t):
    return h0 + (v / 2) * t

def max_distance(v ,t):
    return v * 2 * t

def vertical_velocity(v ,x):
    return v * math.sin(x)

def horizonal_velocity(v ,x):
    return v * math.cos(x)

angles = pi /6

v = 100
g = [3.7 ,8.87 ,9.81 ,1.6 ,3.711 ,23.1 ,9.0 ,8.7 ,11.0]
bodies = ["mercury", "venus   ", "earth   ", "moon   ", "mars   ", "jupiter ", "saturn  ", "uranus  ", "neptune "]


print('Body     ', 'Time in Air', 'Max Hight', "max Distance")
for index, element in enumerate(bodies):
    max_height_time_val = max_height_time(vertical_velocity(v, angles), g[index])
    time_in_air_val = max_height_time_val * 2
    height_val = height_of_cannon_ball(0, vertical_velocity(v, angles), max_height_time_val)
    max_distance_val = max_distance(horizonal_velocity(v, angles), max_height_time_val)
    print(element, f'{time_in_air_val:.2f}', f'{height_val:.2f}' ,f'{max_distance_val:.2f}')
plt.plot(height_val ,max_distance_val)

plt.show()

# print(f'The mass of a liter of platinum is {platinum * .001:.2f} KG')

# Time = t
# time_seconds = s
# Height = h
# starting hight = h0
# velocity = v
# acceleration = g
# mercury_g = 3.7 m/s**2
# venus_g = 8.87 m/s**2
# earth_g = 9.81 m/s**2
# earth_moon_g = 1.6 m/s**2
# mars_g = 3.711 m/s**2
# jupiter_g = 23.1 m/s**2
# saturn_g = 9.0 m/s**2
# uranus_g = 8.7 m/s**2
# neptune_g = 11.0 m/s**2
# pluo_g = 0.7 m/s**2
# mass_of_cannon_ball = 5.4 kg
# angle = x
# x = 30 degrees
# x = 45 degrees
# x = 60 degrees
# x = 75 degrees
# x = 90 degrees
# velocity v =v0+100 m/s
# if v <= 1500 m/s:
# if h <= 100m
########################################################################
# Reviewer Comments
########################################################################
#
# 1.Runs fine
#
#
# 2.Graph doesn't seem to have anything on it, perhaps you haven't gotten to it yet.
#
#
# 3.Velocity appears to be doing calculations with x as the radian input for the trig functions a little unclear why
# you would use x as the variable. The bigger problem I have with this is the fact that I am relatively sure that the
# default for trig function inputs are in radians not degrees, as your notes seem to suggest.
#
#
# 4.Text output is inconsistent in capitalization, mispelled height, and lacks units.
#
#
# 5.Variable names make sense, except for x being used for radians.
#
#
# 6.This is fine if for planets with little no atmosphere, but useless in any other context. I am suspicious of the
# method you used to find the time max height is reached(should really be using the vertical component of velocity
# alone for that, plus your relation ship is simply not true. Use acceleration_g * t = velocity_vertical to find when
# acceleration due to gravity would cancel your vertical motion and by proxy the time you will have reached max
# height.) , and I take issue with the assertion that the time for max distance would simply be twice the time for
# max height.
#
#
# 7.It is certainly compact, but I feel you simplified too much almost to the point of complete incoherence.
#
#
# 8.What little you have done in your graphing process doesn't indicate your graphs are going to be readable,
# axes seem unlabeled and even if it does plot everything your implementation won't be easy to disern what values
# correspond to what plant.
#
#
# 9.Honestly I think this program would greatly benefit from setting up kinematic framework, like handling 2D motion 
# in time, meaning you should calculate the x and y components of acceleration, then use to get your velocity values,
# and then use that to get your position values. From there you will have all the data, you would merely need to 
# filter it in your outputs so only the critical points your interested in are included 
# #######################################################################

