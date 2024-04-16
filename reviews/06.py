import numpy as np
import matplotlib.pyplot as plt

# Define parameters
elevator_mass = 5000  # in kg
counterweight_mass = 5000  # in kg
g = 9.81  # acceleration due to gravity in m/s^2
cable_tension = 50000  # in N

# Define vectors for forces
elevator_force = np.array([0, elevator_mass * g])
counterweight_force = np.array([0, -counterweight_mass * g])
tension_force = np.array([0, -cable_tension])

# Create a figure and axis
fig, ax = plt.subplots()

# Plot elevator and forces
ax.arrow(0, 0, 0, elevator_mass * g, head_width=0.5, head_length=0.5, fc='b', ec='b', label='Elevator')
ax.arrow(0, 0, 0, -counterweight_mass * g, head_width=0.5, head_length=0.5, fc='r', ec='r', label='Counterweight')
ax.arrow(0, 0, 0, -cable_tension, head_width=0.5, head_length=0.5, fc='g', ec='g', label='Tension')

# Set axis limits
ax.set_xlim(-2, 2)
ax.set_ylim(-10000, 10000)

# Add labels and title
ax.set_xlabel('Horizontal Direction')
ax.set_ylabel('Vertical Direction')
ax.set_title('Forces Acting on Elevator System')

# Add legend
ax.legend()

# Show plot
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

