#!/bin/bash

# Script: Ops 301d5 Ops Challenge: Class 04
# Author: Dean Weiss
# Date of latest revision: 01 Sept 2022
# Purpose: Write a bash script to change file permission in a directory

#Main

# Create a bash script that launches a menu system with the following options:
# Hello world (prints “Hello world!” to the screen)
# Ping self (pings this computer’s loopback address)
# IP info (print the network adapter information for this computer)
# Exit
echo "CHOOSE YOUR DESTINY!!!"

function hello() {
    echo "Hello World!"
}

function loopping() {
    ping -c5 127.0.0.1
}

function info() {
    lshw -C network
}

function exit() {
    echo "Bye bye bye."
}

menu() {
    echo -ne "
    '1)' Hi.
    '2)' Loopback Ping
    '3)' IP Info
    '4)' Exit
    "
    read a
    case $a in
        1) hello ; menu ;;
        2) loopping ; menu ;;
        3) info ; menu ;;
        4) exit 0 ;;
        *) echo -e "Wrong Option." $clear; WrongCommand;;
    esac
}

menu

# Next, the user input should be requested.
# The program should next use a conditional statement to evaluate the user’s input, then act according to what the user selected.
# Use a loop to bring up the menu again after the request has been executed.


#End