#goal is to create graphs the trajectory of a mass for a spring loaded projecile
#i have the initial velocity set so that you can just enter what that is.
#i need to set up a function to calculate the initial velocty using a mass and spring constant and using x as the displacement of the spring.
import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # acceleration due to gravity (m/s^2)
v0 = 20  # Enter your desired initial velocity in m/s

# Define a list of launch angles in degrees
theta_degrees = [30, 45, 60]

# Convert angles to radians
theta_radians = np.deg2rad(theta_degrees)

# Function to calculate y(x)
def calculate_y(x, theta):
    return np.tan(theta) * x - (g * x**2) / (2 * (v0 * np.cos(theta))**2)

# Calculate maximum horizontal distance for the largest angle
d_max = (v0**2 * np.sin(2*np.max(theta_radians))) / g

# Set the range of x-values
x_values = np.linspace(0, d_max * 1.2, 100)  # adjust the multiplier as needed for visibility

# Plotting
plt.figure(figsize=(8, 6))  # Set figure size
for theta_rad in theta_radians:
    y_values = calculate_y(x_values, theta_rad)
    plt.plot(x_values, y_values, label=f'{round(np.rad2deg(theta_rad))}°')  # Round the angle value to the nearest integer

plt.title('Trajectories of a Mass')
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')
plt.ylim(0, max(y_values) * 1.2)  # Set y-axis limits from 0 to maximum y-value
plt.legend(title='Launch Angle')
plt.grid(True)
plt.show()

########################################################################
# Reviewer Comments
########################################################################
#
# 1. The code runs without any errors maps it clearly.
#
#
# 2. The code is understandable straight forward no issues. It builds in order. A suggestion would be to print the values.
#
#
# 3. The code is readable following the PEP-8 regulations for the most part.
#
#
# 4. In the beginning they clearly state the intention of the code to graph the trejectory of a mass.
#
#
# 5. I recognized all the variables from previous knowledge and from the code comments.
#
#
# 6. The range of variables is perfect except I would add a table that shows both the x and y values.
#
#
# 7. The script follows all the major components gravity, initial velocity, etc
#
#
# 8. The visuals clearly show where the mass ends however a suggestion would be to include a point that calls out the x and y at the end.
#
#
# 9.
#
########################################################################

