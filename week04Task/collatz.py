# collatz.py
# This program asks the user to input any positive integer 
# and outputs the successive values of the following calculation:
# Calculate the next value by taking the current value 
# and, if it is even, divide it by two, 
# if it is odd, multiply it by three and add one.
# The program ends if the current value is one
# and prints an error message if the input
# is not a positive integer.

# author: Niamh Hogan

# Create a variable that takes in a positive
# integer and stores it as an int 
number = int(input("Please enter a positive integer: "))

# Create a value error which checks to 
# ensure the input is a positive integer.
if number < 0:
    raise ValueError("Input must be a positive integer")

# The raise keyword is
# used to raise exceptions or errors
# See geeks for geeks for raise ValueError:
# https://www.geeksforgeeks.org/python-raise-keyword/


# Create a while loop that ends the program
# when the number = 1
# divides number by 2, if even
# and if odd, multiples it by 3
# and adds 1
while number != 1:
    if number % 2 == 0:
        number = number // 2
    else:
        number = number * 3 + 1

# While loops allow us to execute a set of statements
# as long as the condition is true
# See W3Schools for while loops:
# https://www.w3schools.com/python/python_while_loops.asp

# The if statement executes if the conditon is true,
# in this case, the number is divided by 2 if even.
# The else statement executes when the if statement is false,
# here, the number is multiplied by 3 & 1
# is added if it is an odd number.
# See geeks for geeks for if/else statement:
# https://www.geeksforgeeks.org/python-if-else/

# '!=' & '==' are comparison operators
# != means not equal to
# == means equal to
# See geeks for geeks for comparison operators:
# https://www.geeksforgeeks.org/relational-operators-in-python/

# The % operator is the modulus operator
# that returns the remainder of a division.
# The // operator is the floor division operator
# which divides the first number by the second
# and returns the largest whole number less than
# or equal to the result. 
# The * operator is the multiplication operator.
# The + operator is the addition operator.
# See geeks for geeks for arithmetic operators:
# https://www.geeksforgeeks.org/python-arithmetic-operators/


# Print the final values
# next to each other
    print(number, end=" ")

# The end parameter in the print() function
# specifies what to print at the end of output.
# See Python guides for end parameter:
# https://pythonguides.com/end-in-python/
# In this case, the end function 
# prints out the characters next to to each other
# See stack overflow:
# https://stackoverflow.com/questions/53345214/how-to-print-a-collection-of-characters-next-to-each-other/53345233#53345233