# lab3.1.6_randomFruit2.py
# This program prints out a random fruit using a tuple, not a list
# author: Niamh Hogan

import random

fruits = ('Strawberry', 'Mango', 'Lychee', 'Peach')

# get a random number between 0 and length-1 of the tuple
index = random.randint(0, len(fruits)-1)

fruit = fruits[index]
print("A random fruit: {}".format(fruit))
