"""
Mars Briggs
200561234
2026-02-17
Assignment 7: Write a function that will take a single argument of three words
(No test for the function). The function's purpose is to write the last letter
of each word to a text file. Once completed have the funcion return "1" to the
caller.
"""

# Required Imports
import pyinputplus as pyip  	# PyInputPlus library. pyip as shorthand 
import re                   		# Regex library for pattern matching

"""
Lecture 3: Function
Function to write the last three letters to a file named output in the same
directory
"""
def writeLastLetters(wordList):
    # Lecture 7: Opening a text file to write the data
    with open("output.txt", "w") as file: # a
        for word in wordList:
            # Lecture 4: String Manipulation
            # Takes the last index and rips the letter from it
            lastChar = word[-1]
            file.write("Last Letter for \"" + word + "\": " + lastChar + "\n")
    
    # Lab Requirement: Return "1" upon success
    return "1"

# --- Main Logic ---

# Lecture 6: Validating user input using pyinputplus
# Asks for three words and checks if theyre consisting of only letters
# via regular expression
print("Please enter three words consisting only of letters.")

w1 = pyip.inputRegex(r'^[A-Za-z]+$', prompt="Word 1: ")
w2 = pyip.inputRegex(r'^[A-Za-z]+$', prompt="Word 2: ")
w3 = pyip.inputRegex(r'^[A-Za-z]+$', prompt="Word 3: ")

# Lecture 5: Converting the individual strings into a list
userWordList = [w1, w2, w3]

# Calling the function and checking the return value
confirmation = writeLastLetters(userWordList)

# Lesson 7: Exception Handling while opening file
try:
    with open("output.txt", "r") as file:
        content = file.read()
    print("\nFile Contents: ")
    print(content)

# Incase the file is not found in the directory
except FileNotFoundError:
    print("File not found")

# Operational Check per lab requirements
if confirmation == "1":
    # Print the success message 
    print("File successfully written.")
else:
    print("Task Failed.")