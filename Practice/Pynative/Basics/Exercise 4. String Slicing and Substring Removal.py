"""
Practice Problem: Write a function to remove characters from a string starting from index 0 up to n and return a new string.

Exercise Purpose: This exercise demonstrates how to truncate data strings, a common data-cleaning task.
"""

givenString = "pynative"

def remove_chars(givenString, userInput):
    return givenString[userInput:]

userInput = int(input("Enter the number of characters to remove from the string: "))

print(remove_chars(givenString, userInput))