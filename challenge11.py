#!/bin/python3

# Script: Ops 301d5 Ops Challenge: Class 10
# Author: Dean Weiss
# Date of latest revision: 13 Sept 2022
# Purpose:Using file handling commands, create a Python script that creates a new .txt file, appends three lines, prints to the screen the first line, then deletes the .# txt file.

# Import the Operating System Library
import os

# Main

# Create a Python script that creates a new .txt file
myfile = open("challenge11.txt", "w")

# Appends three lines
myfile.write("Obi-Wan: Hello there.\n")
myfile.write("General Grievous: General Kenobi. You are a bold one. Kill him.\n")
myfile.write("General Grievous: Back away! I will deal with this Jedi slime myself.\n")

# Closing the File
myfile.close()

# Open file to read
madefile = open("challenge11.txt", "r")

# Using readline method to read a line from the document I created.
content = madefile.readlines()

# Prints to the screen the first line.
print(content[0])

# Delete Text File
os.remove("challenge11.txt")

# End

# Source: https://www.guru99.com/python-file-readline.html
# Source: https://www.geeksforgeeks.org/how-to-read-specific-lines-from-a-file-in-python/