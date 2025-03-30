# accounts.py
# A program that reads in a 10 character account number 
# and outputs the account number with only the last 4 digits showing 
# and the first 6 digits replaced with Xs.
# Extra: Modify the program to deal with account numbers of any length.
# author: Niamh Hogan

# Read in the account number
account_number = input("Please enter a 10 digit account number: ")

# The replace() function replaces the first 6 characters with Xs 
# and prints out the last 4 digits
# # Source: https://www.w3schools.com/python/ref_string_replace.asp
account_number = account_number.replace(account_number[0:6], "XXXXXX")

print(account_number)

# Read in account number of any length
account_number = input("Please enter an account number: ")

# The last four digits of the account number are stored in the 
# variable last_four using the slice method
# Source: https://www.w3schools.com/python/python_strings_slicing.asp
last_four = account_number[-4:]

# The first number digits of the account number are replaced with Xs 
# and stored in the variable first_part
x = len(account_number) - 4
first_part = "X" * x

print(first_part + last_four)