# lab3.2.1_round.py
# A program that takes in a float and outputs an int (rounded up or down)
# author: Niamh Hogan

# The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
# The default number of decimals is 0, meaning that the function will return the nearest integer.
# The round() function returns a floating point number if one parameter is passed, otherwise it returns an integer.
# The round() function returns the value of the number rounded to the nearest even integer.

numbertoRound = float(input("Enter a float number: "))
roundedNumber = round(numbertoRound)
print ('{} rounded is {}'.format(numbertoRound, roundedNumber))

