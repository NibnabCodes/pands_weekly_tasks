# squareroot.py
# This program creates a function that takes in
# a positive floating-point number (float) as input 
# and outputs an approximation of its square root 
# utilizing the Newton method.
# The program returns a ValueError if
# the input is a negative number.

# author: Niamh Hogan

# Create a variable that takes in &
# stores a positive floating point number
# typecast the input to a float
num = float(input("Please enter a positive floating point number: "))

# Return a ValueError if the input is a negative number
if num < 0:
    raise ValueError("Input must be a positive number")

# See geeks for geeks for float() function:
# https://www.geeksforgeeks.org/float-in-python/


# Define & create the function to calculate 
# the square root of the inputed number
def sqrt(num, tolerance=1e-6):
    
# To create a function the function 
# name must be defined using the def 
# function () keyword, followed 
# by the function name
# See w3Schools for def():
# https://www.w3schools.com/python/python_functions.asp

# Within the brackets a tolerance level 
# is added (1e-6 = 1 x 10-6)
# See calculeitor for info on 1e-6:
# https://calculeitor.com/1e-6-in-numbers

# The tolerance level is included to 
# ensure the the approximation is 
# close enough to the actual square root.
# The default value of the tolerance level
# is set to 1e-6, which is used as a common 
# default value in numberical methods.
# See ChatGpt Prompt: 
# "How do you create a python function that 
# takes a positive floating-point number (float) as input
# and outputs an approximation of its square root utilizing the Newton method.;
# What is the tolerance level used for?""
# https://chatgpt.com/share/67f14d10-47a0-8011-a3b0-91dfcb7395f1

# Set the initial guess as half of the input number.
    guess = num / 2

# Loop until the absolute difference between the guess and 
# the actual square root is less than the tolerance level
    while abs(num - guess ** 2) > tolerance:

        # Update the guess using the Newton method
        guess = (guess + num / guess) / 2 

# The abs() function returns the absolute value.
# See geeks for geeks for abs() function:
# https://www.geeksforgeeks.org/abs-in-python/

# The ** operator is the exponentiation operator
# which raises the number to the power of the exponent.
# In this case, guess is raised to the power of 2.
# See geeks for geeks for arithmetic operators:
# https://www.geeksforgeeks.org/python-arithmetic-operators/

# Return the approximate square root to one decimal place 
    return round(guess,1)

# return() function exits the function 
# & returns the value specified 
# See W3Schools for return():
# https://www.w3schools.com/python/ref_keyword_return.asp)

# round() function rounds the value to the nearest 
# decimal place specified in the second argument
# See W3Schools for round(): 
# https://www.w3schools.com/python/ref_func_round.asp)

# Print the result of the function
# and the input number
print (f"The square root of {num} is approx {sqrt(num)}")

# This program was partially developed using AI, CHATGPT.
# Prompt: 
# "How do you create a python function 
# that takes a positive floating-point number (float) 
# as input and outputs an approximation of 
# its square root utilizing the Newton method."
# See link:
# https://chatgpt.com/share/67f14d10-47a0-8011-a3b0-91dfcb7395f1
