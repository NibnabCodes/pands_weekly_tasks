# Extra: Why does the below expression cause an error? How can you fix it?

# message = 'I have eaten ' + 99 + ' burritos.'
#print(message)

#   Answer: The above expression causes an error because you cannot concatenate a string with an integer.
#   To fix this, you can convert the integer to a string using the str() function.

message = 'I have eaten ' + str(99) + ' burritos.'
print(message)

# Why is eggs a valid variable name while 100 is invalid?
#   Answer: Variable names must start with a letter or an underscore. They cannot start with a number.
#   This ensures that variables names are distinct & easily distinguishable from numbers and other elements in the code.
#   This makes the code more readable and maintainable. 
#   Therefore, eggs is a valid variable name while 100 is invalid.

# What three functions can be used to get the integer, floating-point number, or string version of a value?
# The three functions that can be used to get the integer, floating-point number, or string version of a value are:
#   Answer: int() - converts a value to an integer
#   float() - converts a value to a floating-point number
#   str() - converts a value to a string