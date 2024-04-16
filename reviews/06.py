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
# 1. the code runs without error
#
#
# 2. The output is rough, it shows two lines one blue one green one of which is going up one is going down,
# however the bounds of the graph are not large enough to contain it
# I would fix this by changing the axis limits to be way higher like 20,000
#
# 3. The code is organized decently well, in some areas such as Show plot it is a little redundant to do plt.show
# and then follow it up with another plt.show
#
#
# 4. the comments and variables are sufficient for what is needed it describes what force is used for what.
#
#
# 5. Variable names are completely fine for what they represent, most are pretty simple such as g for gravity
# elevator mass for elevator mass, most just describe perfectly what they encompass
#
# 6. The variables capture the problem in a lackluster way, the biggest issue is how the data is outputted
# it just shows as two lines I have two major improvements i'd make, the first is increase the bounds of the data
# by increasing the range of data it shows, my second change would be to add more data as right now it shows that
# with a tension cable 5000kg is equal to a 5000kg counterweight, so if it were able to show what happens if one is
# off balanced what happens to the forces
# 7. The code follows a fine functional paradigm, what its trying to do is stated clearly and is completed within its
# area and is commented correctly
#
# 8. The visualizations do not show effectively the solutions to the problem, it is two lines and they dont fit into
# the box, not only that but on the X-axis there is almost nothing but blank space, so it would be fine to shrink that
# area. So as stated prior I would increase the range of the Y axis to be able to actually show the data
#
# 9.
#
########################################################################

