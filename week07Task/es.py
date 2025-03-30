# es.py
# A program that reads in a text file and outputs the number of 'e' & 'E's' it contains.
# The program reads the file in utf-8 encoding to avoid any encoding errors.
# The program takes the filename from an argument on the command line. 
# The program also deals with the following errors: 
# no argument, filename that does not exist, or is not a text file, and any other unexpected errors.
# Author: Niamh Hogan

import sys #import sys module to access command line arguments.
#See Offical Python Documentation: https://docs.python.org/3/library/sys.html

import os #import os module to check if file exists. 
# See Offical Python Documentation: https://docs.python.org/3/library/os.html

#define textfile as the name of the file to be read.
textfile = "Brave New World Full Text.txt"  

#Check if the file exists 
if not os.path.isfile(textfile):  #isfile() method returns True if the specified path is an existing file.
#See: https://www.w3schools.com/python/ref_file_isfile.asp
    raise FileNotFoundError(f"Error: File '{textfile}' does not exist.") #raise an error if the file does not exist.

#Check if the file is a text file
if not textfile.endswith('.txt'):  #endswith() method returns True if the string ends with the specified value.
#See: https://www.w3schools.com/python/ref_string_endswith.asp
    raise ValueError("Error: The file is not a text file.") #raise an error if the file is not a text file.

def count_e(textfile):
    try:
        # Open the file and count occurrences of 'e' and 'E'
        with open(textfile, 'r',  encoding='utf-8') as f: #need to encode the file to utf-8 to read it.
            #See: https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character
            read_data = f.read()

        #count() method returns the number of occurances of the specifed values.
        #See:https://www.w3schools.com/python/ref_list_count.asp
        e_count = read_data.lower().count('e')

        print(f"The file '{textfile}' contains {e_count} occurrences of 'e'.")

#catch the FileNotFoundError exception and print the error message.
    except FileNotFoundError as e: 
#See: https://docs.python.org/3/library/exceptions.html
        print(e)

#catch the ValueError exception and print the error message.    
    except ValueError as e: 
#See: https://docs.python.org/3/library/exceptions.html
        print(e)

#catch any other exceptions and print the error message.
    except Exception as e: 
#See: https://docs.python.org/3/library/exceptions.html
        print(f"An unexpected error occurred: {e}")

# Ensure there is exactly one command-line argument for the filename
# See: https://realpython.com/if-name-main-python/
if __name__ == "__main__": 
# https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/
    if len(sys.argv) != 2: #len() method returns the number of items in an object.
#See: https://www.w3schools.com/python/ref_func_len.asp
        print("Usage: python script.py <filename>") #print the usage message if there is not exactly one command-line argument.
    else: #if there is exactly one command-line argument, call the function count_e() with the filename as the argument.
        count_e(sys.argv[1]) #sys.argv[1] is the filename entered as the command-line argument. 