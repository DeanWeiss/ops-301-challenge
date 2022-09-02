#!/bin/bash

# Script: Ops 301d5 Ops Challenge: Class 03
# Author: Dean Weiss
# Date of latest revision: 31 August 2022
# Purpose: Write a bash script to change file permission in a directory

#main
#Prompts user for input directory path.
echo Enter Directory Path
read path

#Prompts user for input permissions number
echo Enter permission numbers
read numbers

#Change the File Permissions
chmod -R $numbers $path

#Navigates to the directory input by the user and changes all files inside it to the input setting.
#for directory you'll want to use ". /Test" and for permissions I used "777", without quotations on both.

#Prints to the screen the directory contents and the new permissions settings of everything in the directory.
ls -l $path

#end