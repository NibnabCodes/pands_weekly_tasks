# lab3.1.5_randomfruit.py
# This program prints out a random fruit
# author: Niamh Hogan

import random

fruits = ['Strawberry', 'Mango', 'Lychee', 'Peach']

# get a random number between 0 and length-1 of the list
index = random.randint(0, len(fruits)-1)

fruit = fruits[index]
print ("A random fruit: {}".format(fruit))
