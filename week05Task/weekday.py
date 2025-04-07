# weekday.py
# This program outputs whether or not today is a weekday
# without user input.

# author: Niamh Hogan

# Import the datetime module
import datetime

# Create a variable that stores today's date
today = datetime.date.today()

# The date.today() function returns the current local date
# See Real Python for datetime module: 
# https://realpython.com/python-datetime/


# Create if/else statement that checks
# if today is a weekday or weekend
# & print the result
if today.weekday() < 5:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")

# The weekday() function returns the day of the 
# week as an integer (Mon = 0, Sun = 6)
# See geeks for geeks for weekday() function:
# https://www.geeksforgeeks.org/python-datetime-weekday-method-with-example/
# The if statement checks if today is a 
# weekday & prints result if it is correct.
# In this case, today is a weekday if it
# is less than 5 (Mon = 0, Sun = 6).
# The else statement executes when the if 
# statement is false.
# See w3schools for if/else statement:
# https://www.w3schools.com/python/python_conditions.asp 


# This program can also be adapted to assign 
# Friday as a weekday by changing the 
# weekday parameter to < 4:
#if today.weekday() < 4:
    #print("Yes, unfortunately today is a weekday.")
#else:
    #print("It is the weekend, yay!")

# This program was developed using AI, CHATGPT.
# Prompt: How do you create a python program 
# that outputs whether or not today is a weekday? 
# See link:
# https://chatgpt.com/share/67c48614-133c-8011-97f4-d427a4568b8a