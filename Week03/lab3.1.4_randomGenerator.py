# lab3.1.4_randomGenerator.py
# This program reads in two numbers and generates a random number between those two numbers
# author = Niamh Hogan

import random

number = random.randint(1, 50)
print("Here is a random number: {}".format(number))

# Extra: try modyfiyng the program to take in two numbers from the user and generate a random number between those two numbers

x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

number = random.randint(x, y)
print("Here is a random number between {} and {}: {}".format(x, y, number))