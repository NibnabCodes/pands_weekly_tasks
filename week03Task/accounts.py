# accounts.py
# The first program reads in a 10 character account number 
# and outputs the account number 
# with only the last 4 digits showing 
# and the first 6 digits replaced with Xs.

# The second program deals with account 
# numbers of any length
# and outputs the account number with the last 4 digits 
# displayed and the rest replaced with Xs.

# author: Niamh Hogan

# Ask the user to input a 10 digit account number
# which will be stored as a string
# in the variable account_number
account_number = input("Please enter a 10 digit account number: ")

# Create a variable 
# which converts the first 6 digits to Xs
account_number = account_number.replace(account_number[:6], "XXXXXX")

# The replace() function replaces 
# the first 6 characters with Xs 
# using the slice syntax. 
# See W3schools for replace() function: 
# https://www.w3schools.com/python/ref_string_replace.asp

# The slice syntax returns a specified amount of characters 
# from the string.
# See W3schools for string slicing: 
# https://www.w3schools.com/python/python_strings_slicing.asp

# Print account number 
print(account_number)


# Read in account number of any length
# which will be stored as a string
# in the variable account_number2
account_number2= input("Please enter an account number: ")

# Create a variable 
# that takes the lenght of the account number
# and subtracts 4 from it to get the required amount of Xs
x = len(account_number2) - 4

# The len () function returns amount of characters 
# in the string.
# See W3schools for len() function:
# https://www.w3schools.com/python/ref_func_len.asp

# The - operator subtracts 4 from the length 
# of the account number.
# See w3schools for subtraction operator:
# https://www.w3schools.com/python/python_operators.asp

# Create a new variable which converts the first
# part of the account number to Xs,
# using the multiplication operator to repeat the string
# the required amount of times
first_part = "X" * x

# See W3 Schools for multiplication operator:
# https://www.w3schools.com/python/python_operators.asp

# The last four digits of the account number are stored in the 
# variable last_four using the slice syntax.
last_four = account_number[-4:]

# using negative indexing (e.g., -4) allows us to extract the 
# last 4 digits of the account number.
# See W3schools for negative indexing:
# https://www.w3schools.com/python/python_strings_slicing.asp

# print out the first part 
# and last part of the account number
# concatenated together
print(first_part + last_four)

# String concatenation allows us two join two 
# or more strings together, 
# using the + operator 
# See W3schools for string concatenation:
# https://www.geeksforgeeks.org/python-string-concatenation/

