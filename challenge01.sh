#!/bin/bash

# Script: Ops 301d5 Ops Challenge: Class 02
# Author: Dean Weiss
# Date of latest revision: 30 August 2022 2022
# Purpose: Manipulate a variable in bash to apply today’s date to a log file.

# Current Date and Time
today=$(date +%D%T)
# copies file 
cp /var/log/syslog .
# moves file and add the date and time to it
mv syslog syslog$today
#End