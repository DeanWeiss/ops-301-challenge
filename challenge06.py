#!/bin/python3

# Script: Ops 301d5 Ops Challenge: Class 06
# Author: Dean Weiss
# Date of latest revision: 06 Sept 2022
# Purpose: Make python that does the following.
# 1. The Python library “os” must be utilized
# 2. At least three variables must be declared in Python that contain bash operations
# 3. The Python function print() must be used at least three times

# Import the Operating System Library
import os

#Main

# Declaring the First Variable
declarevar1 = 'whoami'
print(declarevar1)

# Calling First Variable
os.system(declarevar1)

# Declaring the Second Variable
declarevar2 = 'ip a'
print(declarevar2)

# Calling Second Variable
os.system(declarevar2)

# Declaring the Third Variable
declarevar3 = 'lshw -short'
print(declarevar3)

# Calling the Third Variable
os.system(declarevar3)

# End