#!/bin/python3

# Script: Ops 301d5 Ops Challenge: Class 09
# Author: Dean Weiss
# Date of latest revision: 12 Sept 2022
# Purpose: Create if statements using these logical conditionals below. Each statement should print information to the screen depending on if the condition is met.
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# Create an if statement using a logical conditional of your choice and include elif keyword that executes when other conditions are not met.

# Create an if statement that includes both elif and else to execute when both if and elif are not met.

# Assigned Variables
a = 12
b = 21

# Main
if a == b:
    print ("a and b are equal")

if a != b:
    print ("a does not equal b")

if a < b:
    print ("b is less than a")

if a <= b:
    print ("a is less than or equal to b")

if a > b:
    print ("a is greater than b")

if a >= b:
    print ("a is greater than or equal to b")

# Create an if statement using a logical conditional of your choice and include elif keyword that executes when other conditions are not met.
if a == b:
    print ("a and b are equal")
elif a != b:
    print ("a and b are not equal")

# Create an if statement that includes both elif and else to execute when both if and elif are not met.
if a > b:
    print ("a is greater than b")
elif a < b:
    print ("a is less than b")
else:
    print ("a and b are equal")

# End