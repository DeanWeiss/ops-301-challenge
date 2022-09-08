#!/bin/python3

# Script: Ops 301d5 Ops Challenge: Class 07
# Author: Dean Weiss
# Date of latest revision: 07 Sept 2022
# Purpose:Create a Python script that generates all directories, sub-directories and files for a user-provided directory path.
# Script must ask the user for a file path and read a user input string into a variable.
# Script must use the os.walk() function from the os library.
# Script must enclose the os.walk() function within a python function that hands it the user input file path.

# Import libraries
import os

# Declaration of variables

### Read user input here into a variable
dirpath = input("Enter dirpath:") or "/home/dean/ops-301-challenge"
print("dirpath is: " + dirpath)
# Declaration of functions

### Declare a function here
def walkfunction(testdir):
    for (root, dirs, files) in os.walk(testdir):
        ### Add a print command here to print ==root==
        print(root)
        ### Add a print command here to print ==dirs==
        print(dirs)
        ### Add a print command here to print ==files==
        print(files)

# Main

### Pass the variable into the function here
walkfunction(dirpath)
# End
