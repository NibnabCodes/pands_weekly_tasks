# plottask.py
# This program creates & displays a histogram of a normal distribution 
# with 1000 values that have a mean=5 and SD=2 
# and a plot of the function, h(x)=x3, 
# in the range 0 - 10, on the one set of axes. 
# Author: Niamh Hogan

# Import NumPy to generate random numbers, 
# to create the range of x & y values for the function h(x)=x3,
# and to calculate the mean and SD of the normal distribution
import numpy as np

# Import Matplotlib to plot data
import matplotlib.pyplot as plt


# Set the seed for reproducibility
# See Stack Overflow for explanation of np.random.seed:
# https://stackoverflow.com/questions/21494489/what-does-np-random-seed0-do
np.random.seed(1) 

# Generate 1000 random numbers, with a mean of 5 and standard deviation of 2, 
# for the normal distribution
# See Offical NumPy documentation for np.random.normal:
# https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html
normData = np.random.normal(loc=5, scale=2, size=1000)

# Define the colours for the histogram
# See Official Matplotlib documentation for colours:
# https://matplotlib.org/stable/users/explain/colors/colors.html
lilac = '#C8A2C8'
cyan = '#00FFFF'

# Create x values for h(x) = x^3 in the range 0 to 10
# See Official NumPy documentation for np.array: 
# https://numpy.org/doc/stable/reference/generated/numpy.array.html
x = np.array(range(0, 11))

# Create y values for h(x) = x^3
# See Official NumPy documentation for np.power:
#  https://numpy.org/doc/stable/reference/generated/numpy.power.html
y = x ** 3

# Create plot 
# See Official Matplotlib documentation: 
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
plt.figure(figsize=(8, 5))

# Create a histogram of the normal distribution
# See Official Matplotlib documentation: 
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
plt.hist(normData, bins=10, color=lilac, edgecolor=cyan)

# Plot function h(x) = x^3
# See Official Matplotlib documentation: 
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
plt.plot(x, y, 'r-', linewidth=2, label=r'$h(x) = x^3$')

# Add title to the plot
# See Official Matplotlib documentation: 
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html
plt.title('Histogram of Normal Distribution with $h(x) = x^3$', size = 14)

# Add ledgend
# See Official Matplotlib documentation: 
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
plt.legend()

# Save plot as PNG file
# See Official Matplotlib documentation: 
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
plt.savefig('plottask.png')

# Display the plot
# See Official Matplotlib documentation: 
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html  
plt.show()