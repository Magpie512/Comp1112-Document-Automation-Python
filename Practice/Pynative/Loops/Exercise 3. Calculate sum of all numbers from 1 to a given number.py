"""
Mars Briggs
200561234
09-02-26
Calculate sum of all numbers from 1 to a given number
Write a program to calculate the sum of all numbers from 1 to a given number.
"""

number = int(input("Enter a number: "))
total_sum = 0
for i in range(1, number + 1):
    total_sum += i
    # Showing all of the sumations until \number\
    print(str(i) + " + " + str(total_sum) + " = " + str(total_sum))
print("The sum of all numbers from 1 to", number, "is:", total_sum)