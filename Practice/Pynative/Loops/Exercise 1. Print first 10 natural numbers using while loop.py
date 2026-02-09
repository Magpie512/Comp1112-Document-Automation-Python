"""
Print first 10 natural numbers using while loop
"""

def solveSeparator():
    print("-" * 30)

# Solve One
number = 1 
while number > 10:
    print(number)
    number += 1

solveSeparator()

# Solve Two
number = 1 
while number <= 10:
    print(number)
    number += 1

solveSeparator()

# Solve Three
number = 10
while number > 0:
    print(11 - number)
    number -= 1

solveSeparator()

# Solve Four
number = 1
while not number > 10:
    print(number)
    number += 1

solveSeparator()

# Solve Five
i = 0
number = 1
while i < 10:
    print(number)
    number += 1
    i += 1  

solveSeparator()

# Solve Six
for n in range(1, 11):
    print(n)

solveSeparator()

# Solve Seven
for i in range(10):
    print(i + 1)