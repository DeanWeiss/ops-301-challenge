#!/bin/python3

# Script: Ops 301d5 Ops Challenge: Class 08
# Author: Dean Weiss
# Date of latest revision: 09 Sept 2022
# Purpose: Create a Python script that includes the following:
# Assign to a variable a list of ten string elements.
# Print the fourth element of the list.
# Print the sixth through tenth element of the list.
# Change the value of the seventh element to “onion”.

# Main

# Assign to a variable a list of ten string elements
DBZ = ["Goku", "Gohan", "Vegeta", "Picollo", "Trunks", "Freeza", "Cell", "Krillin", "Dende", "Yamcha"]

# Print the fourth element of the list.
print(DBZ[3])

# Print the sixth through tenth element of the list.
print(DBZ[5:9])

# Change the value of the seventh element to onion.
DBZ[6] = "Onion"

# Printing at the end to verify it works.
print(DBZ)
#End