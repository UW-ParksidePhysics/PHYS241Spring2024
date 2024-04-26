###This code is designed to calculate the population change in a given year based on the population change of rabbits and foxes. This implements an equation called Lotka-Volterra function, and it takes an initial popukation, a growth rate, and a death rate as inputs. It then calculates the population change for the next year and returns the result.

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def lotka_volterra(y, parameters):
    alpha, beta, gamma, delta = parameters
    rabbit_pop, fox_pop = y
    rabbit_time_rate = alpha * rabbit_pop - beta * rabbit_pop * fox_pop
    fox_time_rate = delta * rabbit_pop * fox_pop - gamma * fox_pop
    return np.array([rabbit_time_rate, fox_time_rate])


# read in a file that contains yearly populations
data = np.loadtxt('population.txt', delimiter=".", skiprows=1)
years = data[:, 0]
rabbits = data[:, 1]
foxes = data[:, 2]

# defines parameters for the lotka-volterra equation
equation_parameters = [
    0.002,   # Rabbit birth rate (alpha)
    0.0002,  # Rabbit death rate (beta)
    0.001,  # Fox birth rate (gamma)
    0.0001,   # Fox death rate (delta)
]

initial_populations = [rabbits[0], foxes[0]]

plt.plot(years, rabbits, label="Rabbits")
plt.plot(years, foxes, label="Foxes")
plt.show()

initial_population = [rabbits[0], foxes[0]]
t = np.linspace(0, len(years), len(years)*10)
solution = odeint(lotka_volterra, initial_population, t, args=(alpha, beta, delta, gamma))
rabbit_solution, fox_solution = solution.T

plt.figure(figsize=(10,6))
plt.plot(years, rabbits, 'ro', label='Rabbits')
plt.plot(years, foxes, 'bo', label='Foxes')
plt.plot(years, rabbit_solution, 'r-', label='Rabbit Model')
plt.plot(years, fox_solution, 'b-', label='Fox Model')
plt.title('Population Dynamics of Rabbits and Foxes')
plt.xlabel('Year')
plt.ylabel('Population')
plt.legend()
plt.grid(True)

start_year, stop_year = 2023, 2040
number_of_years = stop_year - start_year
years = np.linspace(start_year, stop_year, number_of_years)

current_population = np.array(initial_populations)
populations_by_year = [current_population]

for year in years:
    #print(f'R_i, F_i = {current_population}')
    change_rates = lotka_volterra(current_population, equation_parameters)
    #print(f'dR/dt, dF/dt = {change_rates}')
    current_population = current_population + change_rates # * current_population
    #print(f'R_i+1, F_i+1 = {current_population}')
    populations_by_year.append(current_population)
    #print()



populations_by_year = np.array(populations_by_year)
years = np.append(years, years[-1]+1)
plt.plot(years, populations_by_year[:,0], years, populations_by_year[:,1])
plt.show()

########################################################################
# Reviewer Comments
########################################################################
#
# 1. Does the code run without error?
# 
# 2. How understandable is the output?
#
# 3. How readable is the code itself?
#
# 4. How clearly do the code docstrings and comments describe the problem it is trying to solve?
#
# 5. How clearly do the variable names relate to the concepts they concretize?
#
# 6. How well does the range of variables capture the problem described?
# 
# 7. To what degree does the script follow a functional programming paradigm, packaging components etc.
#
# 8. How clearly do the visualizations show the solutions to the problem?
#
########################################################################
