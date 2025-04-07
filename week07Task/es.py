# es.py
# A program that reads in a text file and 
# outputs the amount of 'e' & 'E's' it contains.
# The program reads the file in utf-8 encoding 
# to avoid any encoding errors.
# The program takes the filename from 
# an argument on the command line. 
# The program also deals with the following errors: 
# no argument, filename that does not exist, 
# or is not a text file, and any other unexpected errors.

# Author: Niamh Hogan

# import sys module to access 
# command line arguments.
# See Offical Python Documentation: 
# https://docs.python.org/3/library/sys.html
import sys 

# import os module to check if file exists. 
# See Offical Python Documentation: 
# https://docs.python.org/3/library/os.html
import os 


# insert the file & define textfile 
# as the name of the file to be read.
textfile = "Brave New World Full Text.txt"  

# Raise error if file does not exist
if not os.path.isfile(textfile):  
    raise FileNotFoundError(f"Error: File '{textfile}' does not exist.")

# if not is a logical operator that 
# returns true if the condition is false.
# See Python guides for Not operator:
# https://pythonguides.com/if-not-condition-in-python/ 

# os.path.isfile() method returns 
# Error raised if file does not exist.
# See geeks for geeks for isfile():
# https://www.geeksforgeeks.org/python-os-path-isfile-method/


# Raise error if file is not a textfile
if not textfile.endswith('.txt'):  
    raise ValueError("Error: The file is not a text file.") 

# endswith() method checks if the 
# string ends with the specified value.
# See geeks for geeks for .endswith():
# https://www.geeksforgeeks.org/python-string-endswith-method/


# Create function that opens
# the file in read mode
def count_e(textfile):
  try: 
        with open(textfile, 'r',  encoding='utf-8') as f: 
            read_data = f.read()

# The try: block lets you test a block of code for errors.
# The except block lets you handle the error.
# See W3 Schools for try/except:
# https://www.w3schools.com/python/python_try_except.asp

# The with open() function
# opens the file in read mode ('r')
# and automatically closes it when done.
# See free code camp for with open():
# https://www.freecodecamp.org/news/with-open-in-python-with-statement-syntax-example/

# The file needs to be encoded 
# to utf-8 to read it.
# See stack overflow for utf-8 encoding:
# https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character

# The read() method reads the file and returns the content.
# See w3 schools for read():
# https://www.w3schools.com/python/ref_file_read.asp


# Create a variable that
# counts the number of 
# 'e's & 'E's in the file
        e_count = read_data.count('e') + read_data.count('E')

#count() method returns the number of 
# e & E occurances within the file.
#See:https://www.w3schools.com/python/ref_list_count.asp


# Print the number of occurrences of 
# 'e' & 'E' in the file
        print(f"The file '{textfile}' contains {e_count} occurrences of 'e' and 'E'.")

# catch the FileNotFoundError exception
# and print the error message.
  except FileNotFoundError as e: 
        print(e)

# catch the ValueError exception
# and print the error message.    
  except ValueError as e: 
        print(e)

# catch any other exceptions 
# and print the error message.
  except Exception as e: 
        print(f"An unexpected error occurred: {e}")

# See W3 Schools for try/except:
# https://www.w3schools.com/python/python_try_except.asp
# See geeks for geeks for exception handling:
# https://www.geeksforgeeks.org/python-exception-handling/

# Ensure there is exactly one 
# command-line argument for the filename
if __name__ == "__main__": 
    if len(sys.argv) != 2: 
        print("Usage: python script.py <filename>") 
    else: 
        count_e(sys.argv[1]) 

# The __name__ variable is a built-in variable in Python.
# It is used to determine if a Python script 
# is being run directly or imported as a module.
# If the script is being run directly, 
# __name__ is set to "__main__".
# See: https://realpython.com/if-name-main-python/

# The len(sys.argv) counts the number of 
# command-line arguments passed to the script.
# Here we do not want to count the script name itself,
# so we check if the length is equal to 2.
# If the is not exactly one command-line argument,
# we print the usage message.
# If there is one command-line argument,
# we call the function count_e()
# with the filename as the argument.
# https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/

# Chat GPT, Prompt:
# "What is the purpose of a program that takes a filename 
# from an argument on the command line?"
# ChatGPT Response:
# "The purpose of a program that takes a filename from 
# an argument on the command line is to allow users to 
# specify which file the program should process without 
# modifying the program's code. 
# This approach provides flexibility and automation, 
# especially in command-line environments."
# Link:
# https://chatgpt.com/c/67e01176-aaac-8011-8e6a-a10c63cb4844

# This program was partially developed using AI, CHATGPT.
# Prompt:
# "How do you do the following in python: A program that 
# reads in a text file and outputs the number of e's it 
# contains. The program takes the filename from an 
# argument on the command line. The program also deals with 
# errors e.g., no argument, filename that does not exist, 
# or is not a text file."
# See Link:
# https://chatgpt.com/share/67f16c6a-818c-8011-ad3a-ca949ce09ebe
