# squareroot.py
# This program creates a function that takes a positive floating-point number (float) as input 
# and outputs an approximation of its square root utilizing the Newton method.
# author: Niamh Hogan

# Set the input as float
num = float(input("Please enter a positive floating point number: "))

# Define & Create the function to calculate the square root of the inputed number
def sqrt(num, tolerance=1e-6): # function is defined with def keyword (See W3Schools: https://www.w3schools.com/python/python_functions.asp)
    if num < 0: # Value error check to ensure the input is a positive number. (See ChatGPT: https://chatgpt.com/share/67d300bd-1bc4-8011-983a-ea145d9632af
        raise ValueError("Input must be a positive number:")
    
    # Set the initial guess as half of the input number. (See ChatGPT: https://chatgpt.com/share/67d300bd-1bc4-8011-983a-ea145d9632af)
    guess = num / 2

    # Loop until the absolute difference between the guess and the actual square root is less than the tolerance level
    # (See ChatGPT: https://chatgpt.com/share/67d300bd-1bc4-8011-983a-ea145d9632af)
    while abs(num - guess ** 2) > tolerance:

        # Update the guess using the Newton method
        # (See ChatGPT: https://chatgpt.com/share/67d300bd-1bc4-8011-983a-ea145d9632af)
        guess = (guess + num / guess) / 2 

    # Return the approximate square root to one decimal place 
    # return() function exits the function & retruns the value specified 
    # (See W3Schools: https://www.w3schools.com/python/ref_keyword_return.asp)
    # round() function rounds the value to the nearest decimal place specified in the second argument
    # (See W3Schools: https://www.w3schools.com/python/ref_func_round.asp)
    
    return round(guess,1)

print (f"The square root of {num} is approx {sqrt(num)}")