""" 
Mars Briggs
200561234
08/02/26

"""

def solveSeparater():
    print("-" * 30)

# Solve One
my_string = "Hello, World!"
print(my_string[0:5])  # Output: Hello
print(my_string[7:12]) # Output: World

# Note: The end index is exclusive, so it does not include the character at that index.

solveSeparater()

# Solve Two
my_string = "Python Programming"
print(my_string[0:6])  # Output: Python
print(my_string[7:18]) # Output: Programming

solveSeparater()

# Solve Three - Slicing reverse
my_string = "Hello, World!"
print(my_string[::-1])  # Output: !dlroW ,olleH

