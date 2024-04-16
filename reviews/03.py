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
# 1. Does the code run without error?
# Errors occur if user intentionally inputs non-numerical values into initial input prompt for velocity,
# otherwise no python errors occur
# 2. How understandable is the output?
# Output lacks units to aid in understanding the actual values being computed
#
# 3. How readable is the code itself?
# Code is readable
#
# 4. How clearly do the code comments describe the problem it is trying to solve?
# No comments, very hard to establish the purpose of the code as a result
#
# 5. How clearly do the variable names relate to the concepts they concretize?
# Variable names directly relate to values
#
# 6. How well does the range of variables capture the problem described?
# Without knowing what specifically the 'problem' is in relation to the broader scope of project
# (which is something involving newton's cradle) hard to know how variables capture the problem
# 7. To what degree does the script follow a functional programming paradigm, packaging components etc.
# Only PEP-8 errors are not double returning after function definition, but that seems like a minor issue
#
# 8. How clearly do the visualizations show the solutions to the problem?
# Visualizations display some graph of some sort, but graph is generated independent of initial input and thus
# it is hard to quantify how "related" the graph is to the parameters of the problem, which is itself hard to know about
# 9.
#
########################################################################


