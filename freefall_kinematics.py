import math


def velocity(time, initial_velocity, gravitational_acceleration):
    return initial_velocity - gravitational_acceleration * time


def height(time, initial_height, initial_velocity, gravitational_acceleration):
    return initial_height + initial_velocity * time - 0.5 * gravitational_acceleration * time **2


def velocity_square(height, initial_height, initial_velocity, gravitational_acceleration):
    return initial_velocity ** 2 - 2 * gravitational_acceleration * (height - initial_height)


def time(height, initial_height, initial_velocity, gravitational_acceleration):
  rise_time = initial_velocity / gravitational_acceleration
  discriminant = rise_time**2 - 2* (height - initial_height)/gravitational_acceleration
  if discriminant >= 0:
    return rise_time + math.sqrt(discriminant)
  else: 
    return None


if __name__ == '__main__':
  # Test velocity
  time = 2
  gravitational_acceleration = 9.8
  for initial_velocity in [1, 0, -1]:
    final_velocity = velocity(time, initial_velocity, gravitational_acceleration)
    print(f'Velocity at {time} seconds given an initial velocity of {initial_velocity:2} m/s is       {final_velocity} m/s')