"""
Practice Problem: Display only those characters which are present at an even index number in given string.

Exercise Purpose: Understand how data is stored in memory using zero-based indexing. In most languages, the first character is at position 0, the second at 1, and so on. Mastering indexing is vital for data parsing.

Given Input: "pynative"
"""

givenInput = "pynative"

for index in range(len(givenInput)):
    if index % 2 == 0:
        print(givenInput[index])