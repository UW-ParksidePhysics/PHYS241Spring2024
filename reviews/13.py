# Define parameters (maximum time, gravitational acceleration, mass of balls, length of string)
# Calculate variables (write functions for angle, angular velocity, and kinetic and potential energy)
# Create plots (angle vs time, energy vs time, angular velocity vs time)
# I plan to refine the three graphs by adding more marks on each axis to make it more accurate. I will also get rid of the extra space between the beginning of the graph to the first mark and from the last mark to the end of the graph. If needed, I will also change the color of the lines on the graph.

import numpy as np
import matplotlib.pyplot as plt


# Define parameters
maximum_time = 3  # Maximum time for simulation (s)
gravitational_acceleration = 9.81  # m/s^2
ball_mass = 0.2  # kg
string_length = 0.1  # m


# Function to calculate the angle of the pendulum at time t
def calculate_angle(t):
  angular_frequency = np.sqrt(gravitational_acceleration / string_length)
  angle = (np.pi / 4) * np.cos(angular_frequency * t)
  return angle


# Function to calculate the angular velocity of the pendulum at time t
def calculate_angular_velocity(t):
  angular_frequency = np.sqrt(gravitational_acceleration / string_length)
  angular_velocity = (-np.pi / 4) * np.sin(angular_frequency * t) * angular_frequency
  return angular_velocity


# Function to calculate kinetic energy at time t
def calculate_kinetic_energy(t):
  angular_velocity = calculate_angular_velocity(t)
  kinetic_energy = 0.5 * ball_mass * (string_length ** 2) * (angular_velocity ** 2)
  return kinetic_energy


# Function to calculate potential energy at time t
def calculate_potential_energy(t):
  angle = calculate_angle(t)
  potential_energy = ball_mass * gravitational_acceleration * string_length * (1 - np.cos(angle))
  return potential_energy


# Create a time array
time = np.linspace(0, maximum_time, 1000)


# Create a matrix to store pendulum values (angle and angular velocity) over time
pendulum_values = np.zeros((len(time), 2))


# Calculate and store angle and angular velocity over time
for i, t in enumerate(time):
  # Calculate angle and angular velocity
  angular_frequency = np.sqrt(gravitational_acceleration / string_length)
  angle = (np.pi / 4) * np.cos(angular_frequency * t)
  angular_velocity = (-np.pi / 4) * np.sin(angular_frequency * t) * angular_frequency
  # Store angle and angular velocity in the matrix
  pendulum_values[i, 0] = angle
  pendulum_values[i, 1] = angular_velocity


# Extract angle and angular velocity from the matrix
angle_values = pendulum_values[:, 0]
angular_velocity_values = pendulum_values[:, 1]


# Calculate kinetic and potential energy over time
kinetic_energy_values = np.array([calculate_kinetic_energy(t) for t in time])
potential_energy_values = np.array([calculate_potential_energy(t) for t in time])


# Create plots
plt.figure()

# Plot of Angle vs Time
plt.subplot(3, 1, 1)
plt.plot(time, angle_values)
plt.title('Angle vs Time')
plt.xlabel('t (s)')
plt.ylabel('θ (rad)')

# Plot of Angular Velocity vs Time
plt.subplot(3, 1, 2)
plt.plot(time, angular_velocity_values)
plt.title('Angular Velocity vs Time')
plt.xlabel('t (s)')
plt.ylabel('ω (rad/s)')

# Plot of Kinetic and Potential Energy vs Time
plt.subplot(3, 1, 3)
plt.plot(time, kinetic_energy_values, label='Kinetic Energy')
plt.plot(time, potential_energy_values, label='Potential Energy')
plt.title('Energy vs Time')
plt.xlabel('t (s)')
plt.ylabel('Energy (J)')
plt.legend()

plt.subplots_adjust(hspace=2.0)
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

