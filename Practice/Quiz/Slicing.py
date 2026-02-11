"""
Given the string text = "PythonProgramming", what is the result of the slice text[2:10:2]?

You have a string with leading and trailing whitespace, such as " hello world ". Which method would you use to remove that whitespace, and how would you remove only the whitespace on the right side?
"""

string = "PythonProgramming"

# Result of the slice text[2:10:2]
result = string[2:10:2]
print("Result of the slice text[2:10:2]:", result)

# The last index is exclusive, so it will not include the character at index 10. The slice will start at index 2 and go up to index 9, taking every second character. Therefore, the characters at indices 2, 4, 6, and 8 will be included in the result.