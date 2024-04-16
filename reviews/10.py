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

