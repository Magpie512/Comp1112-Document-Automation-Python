#Ask the user to input a number. Check if it's greater than 10. Print a message accordingly.

print("Enter a number:")
userInput = input()

if userInput > str(int(10)):
    print("The number is less than 10.")
else:
    print("The number is greater than 10.")