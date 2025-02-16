# lab3.3.2_normalise.py
# This program takes in a string and strips any leading or trailing spaces & converts the string to lower case.
# Additonally, the program outputs the length of the original string and the normalised string.
# author: Niamh Hogan

rawString = input("Please enter a string: ")
normalisedString = rawString.strip().lower()

lenghtOfrawString = len(rawString)
lengthOfnormalisedString = len(normalisedString)

print(f'That string normalised is :{normalisedString}')
print(f'We reduced the input string from {lenghtOfrawString} to {lengthOfnormalisedString} characters')