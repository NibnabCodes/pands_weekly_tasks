# lab3.1.2_sub.py
# This program reads in two numbers and subtracts first number from the second
# author: Niamh Hogan

# input reads variables as a string so we need to convert the variables into ints
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
answer = x-y
print('{} minus {} is {}'.format(x, y, answer))

# Extra: when the program is running, try entering in something that is not an int
# This causes an error as the program is expecting an int and cannot convert the input to an int. 
# This is a common error in programming and is called a ValueError.