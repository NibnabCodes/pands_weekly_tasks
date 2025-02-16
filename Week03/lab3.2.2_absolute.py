# lab3.2.2_absolute.py
# A program that takes in a float and outputs an absolute int
# author = Niamh Hogan

# In the question, the number is ambigous but the output implies that the number is a float.
# Therefore, i am assigning the input to a float variable.

number = float(input("Enter a number: "))
absoluteNumber = abs(number)
print ('The absolute value of {} is {}'.format(number, absoluteNumber))
