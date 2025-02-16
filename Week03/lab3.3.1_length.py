# lab3.3.1_length.py
# This program takes in a string and outputs the length of the string
# author: Niamh Hogan

# The len() function returns the number of items in an object.
# This includes spaces within the string.

inputString = input("Enter a string: ")
lenghtOfString = len(inputString)
print(f'The lenght of {inputString} is {lenghtOfString} characters')

# Question 2:
# How would you output:
# John said     "hi"
# I said        "bye"

# second line contains two tabs
# Therefore, I included two \t within the second line of the print statement

message = 'John said\t"hi"\nI said\t\t"bye"'
print(message)