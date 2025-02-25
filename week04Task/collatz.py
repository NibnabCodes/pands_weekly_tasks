# collatz.py
# Program that asks the user to input any positive integer and outputs the successive values of the following calculation:
# Calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# The program ends if the current value is one.

number = int(input("Please enter a positive integer: "))


while number != 1:
    if number % 2 == 0:
        number = number // 2
    else:
        number = number * 3 + 1

# Source: https://stackoverflow.com/questions/53345214/how-to-print-a-collection-of-characters-next-to-each-other/53345233#53345233
    print(number, end=" ")