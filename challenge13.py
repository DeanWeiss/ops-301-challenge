#!/bin/python3

# Script: Ops 301d5 Ops Challenge: Class 13
# Author: Dean Weiss
# Date of latest revision: 15 Sept 2022
# Purpose: Create a Python script that performs the following:

# Prompt the user to type a string input as the variable for your destination URL.

# Prompt the user to select a HTTP Method of the following options:
# GET
# POST
# PUT
# DELETE
# HEAD
# PATCH
# OPTIONS
# Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.

# Using the requests library, perform a GET request against your lab web server.

# For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.

# For the given URL, print response header information to the screen.

import requests

# Main
# Prompt the user to type a string input as the variable for your destination URL
website = input("Type Destination URL - Example: 'http://www.website.com' ")

# Prompt the user to select a HTTP Method of the following options:
# GET
# POST
# PUT
# DELETE
# HEAD
# PATCH
# OPTIONS
def menu():
    print("[1] GET")
    print("[2] POST")
    print("[3] PUT")
    print("[4] DELETE")
    print("[5] HEAD")
    print("[6] PATCH")
    print("[7] OPTIONS")
    print("[0] Exit Menu")

menu()
option = int(input("Enter your option: "))

while option != 0:
    if option == 1:
        print("The GET option has been chosen.")
        get1 = requests.get(website)
        if get1.status_code == 200:
                print("Your website has been found")
        elif get1.status_code == 400:
                print("Site Not Found")
        elif get1.status_code == 403:
                print("Forbidden")
        elif get1.status_code == 401:
                print("Unauthorized")
        elif get1.status_code == 405:
                print("Method Not Allowed")

    elif option == 2:
        print("The POST option been chosen." )
        post1 = requests.post(website)
        if post1.status_code == 200:
                print("Your website has been found")
        elif post1.status_code == 400:
                print("Site Not Found")
        elif post1.status_code == 403:
                print("Forbidden")
        elif post1.status_code == 401:
                print("Unauthorized")
        elif post1.status_code == 405:
                print("Method Not Allowed")

    elif option == 3:
        print("The PUT option has been chosen")
        put1 = requests.put(website)
        if put1.status_code == 200:
                print("Your website has been found")
        elif put1.status_code == 400:
                print("Site Not Found")
        elif put1.status_code == 403:
                print("Forbidden")
        elif put1.status_code == 401:
                print("Unauthorized")
        elif put1.status_code == 405:
                print("Method Not Allowed")


    elif option == 4:
        print("The DELETE option has been chosen")
        delete1 = requests.delete(website)
        if delete1.status_code == 200:
                print("Your website has been found")
        elif delete1.status_code == 400:
                print("Site Not Found")
        elif delete1.status_code == 403:
                print("Forbidden")
        elif delete1.status_code == 401:
                print("Unauthorized")
        elif delete1.status_code == 405:
                print("Method Not Allowed")

    elif option == 5:
        print("The HEAD option has been chosen")
        head1 = requests.head(website)
        if head1.status_code == 200:
                print("Your website has been found")
        elif head1.status_code == 400:
                print("Site Not Found")
        elif head1.status_code == 403:
                print("Forbidden")
        elif head1.status_code == 401:
                print("Unauthorized")
        elif head1.status_code == 405:
                print("Method Not Allowed")

    elif option == 6:
        print("The PATCH option has been chosen")
        patch1 = requests.patch(website)
        if patch1.status_code == 200:
                print("Your website has been found")
        elif patch1.status_code == 400:
                print("Site Not Found")
        elif patch1.status_code == 403:
                print("Forbidden")
        elif patch1.status_code == 401:
                print("Unauthorized")
        elif patch1.status_code == 405:
                print("Method Not Allowed")

    elif option == 7:
        print("The OPTIONS option has been chosen")
        options1 = requests.options(website)
        if options1.status_code == 200:
                print("Your website has been found")
        elif options1.status_code == 400:
                print("Site Not Found")
        elif options1.status_code == 403:
                print("Forbidden")
        elif options1.status_code == 401:
                print("Unauthorized")
        elif options1.status_code == 405:
                print("Method Not Allowed")

    else:
        print("Invalid Option.")
    break

# For the given URL, print response header information to the screen.
headera = requests.head(website)
print("Response Header")
print(headera.headers)

# End