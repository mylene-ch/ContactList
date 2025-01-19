Contact List Application

Introduction

This project is a Python-based Contact List program designed to manage a user’s contacts persistently. Users can add, delete, list, and search for contacts, with all data stored in a JSON file for persistent storage between sessions. The program ensures input validation for phone numbers and email addresses and provides a command-line interface for easy interaction.

Features

Persistent Storage:

Contacts are saved in a JSON file and persist across program runs.

CRUD Operations:

Add new contacts.

Delete existing contacts by name.

List all contacts in alphabetical order by first name.

Search for contacts by partial first and last names.

Validation:

Ensures unique first and last name combinations for contacts.

Validates phone numbers (10 digits, numeric).

Validates email addresses (e.g., contains @ and valid domain).

User-Friendly Interface:

Provides clear prompts and error messages.

Command-based interaction.

Commands

add: Adds a new contact.

delete: Deletes a contact using first and last name.

list: Lists all saved contacts alphabetically.

search: Searches for contacts by partial first and/or last names.

q: Quits the application and saves changes.

Sample Usage

Welcome to your contact list!

The following is a list of useable commands:  
"add": Adds a contact.
"delete": Deletes a contact.
"list": Lists all contacts.
"search": Searches for a contact by name.
"q": Quits the program and saves the contact list.

Type a command: add
First Name: John
Last Name: Doe
Mobile Phone Number: 123-456-7890
Home Phone Number:
Email Address: john.doe@example.com
Address: 123 Maple St.
Contact Added!

Type a command: list

1. John Doe
   Mobile: 123-456-7890
   Email: john.doe@example.com
   Address: 123 Maple St.

Type a command: search
First Name: John
Last Name:
Found 1 matching contacts.

1. John Doe
   Mobile: 123-456-7890
   Email: john.doe@example.com
   Address: 123 Maple St.

Type a command: delete
First Name: John
Last Name: Doe
Are you sure you would like to delete this contact (y/n)? y
Contact deleted.

Type a command: q
Contacts were saved successfully.

Code Structure

main.py:

Entry point for the program.

Manages user commands and program flow.

storage_1.py:

Handles reading and writing contacts to/from the JSON file.

tools.py:

Utility functions for validating email addresses, phone numbers, and retrieving contacts by name.

JSON File:

Stores contact data persistently in a structured format.

Requirements

Python 3.x

Future Improvements

Add support for additional contact fields.

Implement functionality to update existing contacts.

Add a graphical user interface (GUI) for improved usability.

Enhance search functionality with more advanced filters.
