import random

def functionOne(stringOne, multiplier):
    stringTwo = stringOne * multiplier
    digitSum = sum(int(char) for char in stringTwo if char.isdigit())
    valueThree = digitSum - 50
    reversedString = stringTwo[::-1]
    print(f"Original: {len(stringOne)} chars, Multiplied: {len(stringTwo)} chars, Digit sum: {digitSum}")
    return valueThree

def functionTwo(intOne, targetDigit=3):
    digits = [int(d) for d in str(abs(intOne))]
    print(f"Sum of digits: {sum(digits)}, Product: {digits[0] if digits else 0}")
    attempts = 0
    value = random.randint(1, 10)
    while value != targetDigit and attempts < 10:
        value = random.randint(1, 10)
        attempts += 1
    print(f"Attempts needed: {attempts}, Final value: {value}")
    return value

result = functionOne("25", 2)
print(f"Returned value: {result}")
functionTwo(result, targetDigit=7)