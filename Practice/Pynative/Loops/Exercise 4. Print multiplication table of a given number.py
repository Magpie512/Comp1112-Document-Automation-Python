"""
Mars Briggs
200561234
09-02-26
Print multiplication table of a given number
"""

number = int(input("Enter a number: "))
for i in range (1, 11):
    result = number * i
    print(str(number) + " x " + str(i) + " = " + str(result))