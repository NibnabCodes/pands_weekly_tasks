# lab3.2_Extra.py
# This program takes in a float amount of dollars and returns it's absolute amount in cent
# author: Niamh Hogan

floatAmount = float(input("Enter an amount in dollars: "))
absoluteAmount = abs(floatAmount)

# float needs to be converted to an int to remove decimal point
centAmount = int(absoluteAmount * 100)

print ('${} is {} cents'.format(absoluteAmount, centAmount))