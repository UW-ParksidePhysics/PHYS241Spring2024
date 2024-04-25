import math
import matplotlib.pyplot as plt
import numpy as np

# Experiment:    Date: April 15, 2024 
# 16oz of near to boiling water in a pyrex measuring cup.

# air and initial water temp (C)
T = 28.6  # ambient temperature (78 deg F) 
y0 = 81.0 # initial water temperature (177.8 deg F)
y_t = 50 #Median Water Temp From Data
t = 1.2 #Time of y(t)
k_actual = 0.0015

# t_data time data (Hours) 
t_data = np.array([0, 1, 2, 3, 4, 5])  # Time in hours

# T_data water temperature data (C) 
T_data = np.array([90, 80, 70, 60, 50, 40])  # Temperature in Celsius

# approximate k
def k_estimate(y0,T,y_t,t):
  return math.log((y0-T)/(y_t - T))/t
  
k_estimate_result = k_estimate(y0,T,y_t,t) #Estimate Newtons Cooling from experiement
print('K Estimate from our experiment is:', k_estimate_result)
print("\n" * 1)
print(f'The initial temperature of the water is: {y0} deg c')
print("\n" * 1)
print(f'The final temperature of the water is: {y_t} deg c')
print("\n" * 1)
print(f'The ambieant temperature is: {T} deg c')
print("\n" * 1)
print("Time (hours)\tTemperature (°C)") #Inserts Table with my experiment data
for t, T in zip(t_data, T_data):
  print(f"{t:^14}{T:^14}")

print("The actual Cooling Coefficient for water with similary temperatures is:", k_estimate_result)
def linear_regression(x, y):
  n = len(x)
  sum_x = np.sum(x)
  sum_y = np.sum(y)
  sum_xy = np.sum(x * y)
  sum_x_squared = np.sum(x ** 2)
  m = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2) #Slope
  c = (sum_y - m * sum_x) / n #Y-intercept
  return m, c

m, c = linear_regression(t_data, T_data - T)
regression_line = m * t_data + c

#Plot the data and the regression line
plt.scatter(t_data, T_data, label='Data')
plt.plot(t_data, regression_line, color='red', label='Linear Regression')
plt.xlabel('Time (hours)')
plt.ylabel('Temperature (°C)')
plt.title('Newton\'s Law of Cooling')

equation_text = f'y = {m:.2f}x + {c:.2f}'
plt.text(0.5, 85, equation_text, fontsize=12, color='blue')

plt.legend()
plt.grid(True)
plt.show()


plt.show()

########################################################################
# Reviewer Comments
########################################################################
#
# 1.
# The code runs without error.
#
# 2.
# The output of the code looks understandable,
# However, you have two variables t_data and T_data, it was confusing as I read the code.
#
# 3.
# PEP 8 is violated on many lines, read PyCharm to find out problematic lines.
# lines 10, 11, 12, 22, 23, 25, 34, 36, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 52, 102
# Also there are typos on lines 25, 32, 38.
#
# 4.
# line 11, I am unclear what median water temp by data means/does.
#
# 5.
# Again t_data and T_data are a bit similar/ confusing to tell apart, potential rename is t_hours and temp_data
# T and t could be renamed, however this isn't necessary since time(t) and temp(T) are commonly referred as such.
#
# 6
# I think your code uses an appropriate number of variables to convey Newton's Law of Cooling.
#
# 7.
# This code is fairly minimal, I don't have comments regarding how to make the modules work together more cohesively.
#
# 8.
# The graph shows a decreasing linear function, this graph appears to demonstrate Newton's
# Law of Cooling in a beautiful way. The domains/axes appear to be labeled and scaled in an appropriate manner.
#
########################################################################

