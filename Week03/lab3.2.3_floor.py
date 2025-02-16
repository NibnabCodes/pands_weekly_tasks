# lab3.2.3_floor.py
# This program takes in a float number and outputs an int that is rounded down.
# author: Niamh Hogan

import math

numberToFloor = float(input("Enter a float number: "))
flooredNumber = math.floor(numberToFloor)


print ('{} floored is {}'.format(numberToFloor, flooredNumber))