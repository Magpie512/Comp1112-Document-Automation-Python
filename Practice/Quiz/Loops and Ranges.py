"""
Write a while loop that prints the first 5 natural numbers (1 through 5).

Use a for loop and the range() function to calculate the cumulative sum of all even numbers between 1 and 20 (inclusive).
"""

number = 0

while number < 5:
    number += 1
    print(number)

print(" ")

sum = 0
for i in range(1, 21):
    if i % 2 == 0:
        sum += i
    print("Cumulative sum of all even numbers between 1 and 20 (inclusive):", sum)