# My Python project is Newton's Cradle.
import math
import numpy as np
import matplotlib.pyplot as plt

mass = 1
def conservation_of_momentum(velocity, initial_velocity=0, mass=1):
  return sum(velocity)
  
def positon_of_ball(angle, length=10):
  return length * math.sin(angle)
  
def angular_momentum(angular_velocity, length, mass):
  return mass * length * angular_velocity
  
def angular_velocity(time, initial_angle=math.pi /6, initial_angular_velocity=0.5):
  return initial_angular_velocity * math.cos(initial_angle) * math.cos(time)

velocity = [float(x) for x in input("Enter the velocity (comma-separated): ").split(",")]
print("Conservation of Momentum:", conservation_of_momentum(velocity))
print("Position of Ball:", positon_of_ball(math.pi /6, 10))
print("Angular Momentum:", angular_momentum(0.5, 10, 1))
print("Angular Velocity:", angular_velocity(1, math.pi /6, 0.5))

time_points = np.linspace(0, 10, 100)

angular_velocities = [angular_velocity(t) for t in time_points]

plt.plot(time_points, angular_velocities)
plt.xlabel('Time (s)')
plt.ylabel('Angular Velocity (rad/s)')
plt.title('Angular Velocity vs Time')
plt.grid(True)
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

