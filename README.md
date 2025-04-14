# Programming and Scripting Weekly Tasks

![Alt text](images/HelloWorld.png)

Author: Niamh Hogan

## Overview

This repository contains my 8 weekly task submissions as part of the assessment for the Programming and Scripting module at Atlantic Technological University - Galway.

As a novice, the purpose of the weekly tasks was to increase my basic understanding of programming & scripting in Python by creating Python programs which grew in complexity each week.

## About this Repository

This repository is comprised of the following files and folders:

* A **README** file that contains
* An **images** folder that contains a .png file of a screenshot taken from my first Hello World program.
* **Week01Task** - **week08Task** Folders
    ** Each folder contains a .py file containing the weekly task.
    ** Each .py file contains a brief description of the program, python code, overcommenting & references. 
    ** The **week07Task** folder additionally contains a .txt file of the full novel **Brave New World*.
    ** The **week08Task** folder also contains a .png file of the generated histogram.
* A **requirements.txt** file containing all the Python packages that the programs depend on & their versions.

## Features

The programs located in this repo execute the following tasks:

**helloworld.py**
This program prints out 'Hello World!' when run.

**bank.py**
This program asks the user to input two amounts in cent. It then prints out the sum of these with a euro sign 
and decimal point between the euro and cent of the amount.

**accounts.py**
    ** The first program reads in a 10 character account number and outputs the account number with only the last 4 digits showing and the first 6 digits replaced with Xs.
    ** The second program deals with account numbers of any length and outputs the account number with the last 4 digits displayed and the rest replaced with Xs.

**collatz.py**
This program asks the user to input any positive integer and outputs the successive values of the following calculation:
    ** Calculate the next value by taking the current value and, if it is even, divide it by two, if it is odd, multiply it by three and add one. 
The program ends if the current value is one and prints an error message if the input is not a positive integer.

**weekday.py**
This program outputs whether or not today is a weekday without user input.

**squareroot.py**
This program creates a function that takes in a positive floating-point number (float) as input and outputs an approximation of its square root utilizing the Newton method. 
The program returns a ValueError if the input is a negative number.

**es.py**
A program that reads in a text file and outputs the amount of 'e' & 'E's' it contains. The program reads the file in utf-8 encoding to avoid any encoding errors. The program takes the filename from an argument on the command line. The program also deals with the following errors: 
no argument, filename that does not exist, or is not a text file, and any other unexpected errors.

**plottask.py**
This program creates & displays a histogram of a normal distribution with 1000 values that have a mean=5 and Standard deviation (SD)=2 and a plot of the function, h(x)=x3, in the range 0 - 10, on the one set of axes. 

## Dependencies

* Python==3.12.7
    ** os
    ** sys
    ** datetime
* matplotlib==3.9.2
* numpy==1.26.4

## Environment Setup

* GitHub
* Anaconda
* Visual Studio Code


## How to Download Repository



## How to Run the Code
* Week07Task 
how to run: 
enter: python es.py "Brave New World Full Text.txt" on command line

