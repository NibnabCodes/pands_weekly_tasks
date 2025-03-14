# es.py
# A program that reads in a text file and outputs the number of e's it contains.
# The program takes the filename from an argument on the command line.????
# Extra: The program also deals with errors eg no argument, filename that does not exist, or is not a text file.
# Author: Niamh Hogan


argument = "Brave New World Full Text.txt"
with open(argument, 'r',  encoding='utf-8') as f: #need to encode the file to utf-8 to read it.
#See: https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character
    read_data = f.read()
    print(read_data.count('e')) #count() method returns the number of occurances of the specifed values.
#See:https://www.w3schools.com/python/ref_list_count.asp
    