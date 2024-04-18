import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Function to generate ellipse points


def generate_ellipse(center, x, y, angle, num_points=100):
    theta = np.linspace(0, 2*np.pi, num_points)
    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)
    ellipse_points = np.array([a * cos_theta, b * sin_theta])
    #rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
    #                            [np.sin(angle), np.cos(angle)]])
    rotation_matrix = np.array([[1,0], [0,1]])
    rotated_points = np.dot(rotation_matrix, ellipse_points)
    return rotated_points[0] + center[0], rotated_points[1] + center[1]
    return center[0], center[1]
# Function to update the plot


def update(frame):

    # Calculate new position of the moving point
    x = center[0] + np.cos(np.radians(frame)) * a
    y = center[0] + np.sin(np.radians(frame)) * b
    moving_point.set_data(x, y)

    # Update the ellipse
    ellipse.set_data(*generate_ellipse(center, x, y, np.radians(frame)))

    # Update the path of the moving point on the ellipse
    path_line.set_data([center[0], x], [center[0], y])

    return moving_point, ellipse, path_line

# Parameters


center = (0, 0)
a = 5  # Major axis
b = 3  # Minor axis
eccentricity = .206  # Eccentricity
radius = 1  # Radius of rotation

# Create initial plot
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
moving_point, = ax.plot([], [], 'ro')
ellipse, = ax.plot([], [], 'b')
path_line, = ax.plot([], [], 'r--')

# Create animation
ax.set_aspect("equal")
ani = FuncAnimation(fig, update, frames=np.linspace(0, 360, 360),
                    blit=True, interval=50)

plt.show()

plt.show()
########################################################################
# Reviewer Comments: Reviewed by Nicolas Garcia
########################################################################
#
# 1.
# Code runs smoothly without issue.
# No errors.
# 2.
# The output is well organized and explained through comments.
# Nothing stands out as difficult to understand.
# 3.
# The code is formatted well.
# PEP-8 violation appears on the rotational matrix line.
# 4.
# The comments do a good job explaining the process and function of the code that runs the output.
# The only comment I would add is something to describe the sin, cos np.array that is left as an example of how the final values were calculated. The example was left in the middle of the code without anything seperating it from the main code.
# 5.
# The variables are all labelled well in relation to the Ellipse.
# Nothing stood out as hard to understand.
# 6.
# The variables all properly explain how they relate to the Ellipse.
# Nothing to report.
# 7.
# The flow of the code does a good job at following a functional programming paradigm.
# The code was strictired fine as is.
# 8.
# The visualization works properly but some extra comments explaining the purpose of the output and its relation to the code would make it easier to understand what's being displayed.
# Only comments could make the visualization more ffective, the visualization itself works and looks great.
# 9.
#
########################################################################

