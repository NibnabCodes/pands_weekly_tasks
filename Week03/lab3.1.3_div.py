# lab3.1.3_div.py
# This program reads in two numbers and divides the first number by the second number and gives the integer result and the remainder
# author: Niamh Hogan

# input reads variables as a string so we need to convert the variables into ints
x = int(input('Enter first number: '))
y = int(input('Enter the second number: '))

# outputs x divided by y and remainder

answer = x // y
remainder = x % y

print('{} divided by {} is {} with remainder {}'.format( x, y, answer, remainder))
