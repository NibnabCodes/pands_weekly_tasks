# bank.py
# This program asks the user to input 
# two amounts in cent. It then prints 
# out the sum of these with a euro sign 
# and decimal point between the euro
# and cent of the amount.

# author: Niamh Hogan 

# create two variables to store user input
# and convert them to integers (cent):
amount1 = int(input('Enter amount1 (in cent): ')) 
amount2 = int(input('Enter amount2 (in cent): '))

# Python input () function allows for 
# user input, stores it in a variable,
# and returns the value as a string.
# in this case, we want to take the 
# input as an integer (cents),
# therefore, we use typecasting 
# by using the int() function. 
# The int() function converts the 
# input to an integer
# See Geeks for Geeks for information on the int() & input() function:
# https://www.geeksforgeeks.org/python-input-function/


# create a new variable, which adds the two amounts
# and stores it as a float.
newAmount = float (amount1 + amount2)

# The float() function converts the input to float.
# See Geeks for Geeks for information on the float() function:
# https://www.w3schools.com/python/ref_func_float.asp
# The + operator adds the two amounts together.
# See W3 Schools for Python operators:
# https://www.w3schools.com/python/python_operators.asp


# print out the result of the two amounts added together
# and converted to euro by dividing by 100,
# with a euro sign and two decimal places.
print(f"The sum of these is €{newAmount/100:.2f}")

# The f-string is a way of formatting 
# strings in Python. It allows you to directly 
# include variables & expressions in the string
# and to perform calculations within the curly brakets.
# See geeks for Geeks for information on f-strings:
# https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/

# The / operator divides the newAmount 
# by 100 to convert cents to euro.
# See W3 Schools for Python operators:
# https://www.w3schools.com/python/python_operators.asp

# The : .2f formats the float amount 
# to two decimal places.
# See geeks for geeks for rounding to two decimal places:
# https://www.geeksforgeeks.org/how-to-get-two-decimal-places-in-python/