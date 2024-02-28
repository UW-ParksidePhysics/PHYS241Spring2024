import math
import numpy as np

starting_velocity = 5
standard_gravity = 9.81
ball_height = 0.2

discriminant = starting_velocity ** 2 - 2 * standard_gravity * ball_height
time_one = (starting_velocity - math.sqrt(discriminant)) / standard_gravity
time_two = (starting_velocity + math.sqrt(discriminant)) / standard_gravity

print('At t = {:.2f} s and {:.2f} s, the height is {:.1f} m'.format(time_one, time_two, ball_height))

# Example: Taking square root of -9
# result = np.sqrt(-9.+0j)
# print(result)  # Output: 3j

