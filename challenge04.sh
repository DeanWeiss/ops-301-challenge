#!/bin/bash

# Script: Ops 301d5 Ops Challenge: Class 05
# Author: Dean Weiss
# Date of latest revision: 02 Sept 2022
# Purpose: Write a log clearing bash script.

# This script needs to be ran as root. (not sudo)

# Write a bash script that clears the contents of these logs:
# /var/log/syslog
# /var/log/wtmp
# Print to screen the before and after of the contents of each file.
# Add the below information as comments:
# Script Name
# Author
# Date of last revision
# Description of purpose
# Declaration of variables
# Declaration of functions

# Define Variables
syslogVar=/var/log/syslog
wtmpVar=/var/log/wtmp

# Define Functions
clearlog() {
    # This function takes the above filepaths as an argument and then prints the contents with cat. 
    # It then clears the contents with /dev/null and then prints the file # again, which is empty.
    echo "Printing the contents of $1"
    cat $1
    cat /dev/null > $1
    cat $1
}

# Main
clearlog $syslogVar
clearlog $wtmpVar

#End