# plottask.py
# This program creates & displays 
# a histogram of a normal distribution 
# with 1000 values that have a mean=5 
# and Standard deviation (SD)=2 
# and a plot of the function, h(x)=x3, 
# in the range 0 - 10, on the one set of axes. 

# Author: Niamh Hogan

# Import NumPy to generate random numbers, 
# create the range of x & y values 
# for the function h(x)=x3,
# and to calculate the mean & SD 
# of the normal distribution
import numpy as np

# Import Matplotlib to 
# plot the data
import matplotlib.pyplot as plt


# Set the seed for reproducibility
np.random.seed(1) 

# np.random.seed() is used to 
# reproduce the same random numbers
# every time the code is run.
# See Stack Overflow for explanation 
# on np.random.seed:
# https://stackoverflow.com/questions/21494489/what-does-np-random-seed0-do


# Create a variable that stores &
# generates 1000 random numbers, with 
# mean=5 and standard deviation=2 
# for the normal distribution
normData = np.random.normal(loc=5, scale=2, size=1000)

# np.random.normal() is used to generate 
# random numbers from a normal distibution.
# The loc parameter specifies the mean, 
# the scale parameter specifies the SD 
# & the size parameter specifies the number 
# of digits to generate.
# See Offical NumPy documentation for np.random.normal:
# https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html

# Create a variable that stores
# the x values for h(x) = x^3 
# in the range 0 to 10
x = np.arange(0, 11)

# x = np.array(range(0, 11))
# Can also be used

# np.arange() is used to create an 
# array of evenly spaced values
# within a specified range.
# The first parameter is the start value,
# the second paramter is the end value,
# & the third parameter is the step size 
# (the default is 1).
# See geeks for geeks for np.arange():
# https://www.geeksforgeeks.org/numpy-arrange-in-python/


# Create y values for h(x) = x^3
y = x ** 3

# ** is the exponent operator.
# in this case, x is raised
# to the power of 3.
# See geeks for geeks for arithmetic operators:
# https://www.geeksforgeeks.org/python-arithmetic-operators/


# Create plot & set figure size
plt.figure(figsize=(8, 5))

# plt.figure() is used to create a 
# new figure for the plot.
# The figsize parameter specifies the
# width/height of the figure in inches.
# See geeks for geeks for plt.figure():
# https://www.geeksforgeeks.org/matplotlib-pyplot-figure-in-python/


# Define the colours for the histogram
# See Official Matplotlib documentation 
# for colour ID's:
# https://matplotlib.org/stable/users/explain/colors/colors.html
lilac = '#C8A2C8'
cyan = '#00FFFF'

# Create a histogram of the normal distribution
plt.hist(normData, bins=10, color=lilac, edgecolor=cyan)

# plt.hist() is used to create a histogram.
# The first parameter contains the data 
# to be plotted, the second parameter
# specifies the number of bins, the 
# third parameter specifies the color of
# the bars & the fourth specifies the
# colour of the bar edges.
# See geeks for geeks for plt.hist():
# https://www.geeksforgeeks.org/matplotlib-pyplot-hist-in-python/


# Plot x & y values for
# function: h(x) = x^3
plt.plot(x, y, 'r-', linewidth=2, label=r'$h(x) = x^3$')

# plt.plot() is used to plot x & y values.
# The first parameter contains the x values,
# the second parameter contains the y values,
# the third parameter specifies the colour
# of the line, the fourth parameter specifies
# the line width & the fifth parameter specifies
# the label for the line.
# See geeks for geeks for plt.plot():
# https://www.geeksforgeeks.org/matplotlib-pyplot-plot-function-in-python/


# Create font specifications for title
font1 = {'family':'serif','color':'orange','size':14}

# Add title to the plot
plt.title('Histogram of Normal Distribution with $h(x) = x^3$', fontdict=font1)

# plt.title() adds a title to the plot.
# The first parameter is the title,
# the second parameter specifies the font 
# colour, size & syntax.
# See w3 schools for plt.title() & font1:
# https://www.w3schools.com/python/matplotlib_labels.asp

# Add ledgend
plt.legend()

# plt.ledgend() adds ledgend to plot
# See geeks for geeks for plt.ledgend():
# https://www.geeksforgeeks.org/matplotlib-pyplot-legend-in-python/

# Save plot as PNG file
plt.savefig('plottask.png')

# plt.savefig() saves the figure as an
# image file.
# The first parameter is the file name,
# the second parameter specifies the
# file format.
# See Official Matplotlib documentation: 
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html


# Display the plot
plt.show()

# plt.show() displays the plot.
# See Official Matplotlib documentation: 
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html  