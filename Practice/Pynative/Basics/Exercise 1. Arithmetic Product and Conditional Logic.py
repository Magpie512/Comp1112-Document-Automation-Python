"""
Practice Problem: Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.

Exercise Purpose: Learn basic control flow and the use of if-else statements. Understand how code decisions change output based on a mathematical threshold.
"""
import random

def productOrSum(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2
    
# Test case 1:
numTest1a = 20
numTest2b = 30

# Test case 2:
numTest1b = 40
numTest2a = 30

# Chose test case
testCase = random.choice([1, 2])
if testCase == 1:
    result = productOrSum(numTest1a, numTest2b)
    print("Test Case 1: Numbers (" + str(numTest1a) + ", " + str(numTest2b) + ") = Result: " + str(result))

else:
    result = productOrSum(numTest1b, numTest2a)
    print("Test Case 2: Numbers (" + str(numTest1b) + ", " + str(numTest2a) + ") = Result: " + str(result))