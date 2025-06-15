import json
import requests
import os
from datetime import datetime

print("="*60)
print("Part 1: File I/O Operations")
print("="*60)

def read_file():
    """
    Reads and prints the content of 'sample.txt'.
    Handles FileNotFoundError gracefully.
    """
    print("\n1.1 Basic File Reading")
    try:
        with open("sample.txt","r") as file:
            contents = file.read()
            print(f"The content in the file are:\n{contents}")
    except FileNotFoundError:
        print("The file 'sample.txt' is not found!")
        print("Please ensure the file exists or write to it first to create it.")
        return

def write_file():
    """
    Writes user-provided content and a timestamp to 'sample.txt'.
    Uses append mode ('a') to add content without overwriting existing data.
    If 'sample.txt' does not exist, it will be created.
    """
    print("\n1.2 Writing to File")
    try:
        # Open the file in append mode ('a').
        # If the file exists, content will be added to the end.
        # If the file does not exist, it will be created.
        with open("sample.txt","a") as file:
            # Get user input. .rstrip(" ").split() was removed as it converts
            # the input into a list of words then to its string representation.
            # Usually, you just want the plain input string.
            user_input = input("Enter the content to add: ")
            file.write(user_input + "\n") # Write user input, followed by a newline
            file.write(f"Added at: {datetime.now()}\n") # Append the timestamp with a newline

            print("✅ Content written and timestamp appended to 'sample.txt'.")

    except Exception as e:
        # Catch any general exceptions that might occur during file operations
        print(f"An error occurred: {e}")
        print("Could not write to 'sample.txt'.")

if __name__ == "__main__":
    # First, attempt to read the file.
    # If it doesn't exist, the 'read_file' function will print a message.
    read_file()

    # Then, write to the file. 'write_file' will create it if it doesn't exist
    # and append content.
    write_file()

    # Finally, read the file again to show the newly added content.
    read_file()
