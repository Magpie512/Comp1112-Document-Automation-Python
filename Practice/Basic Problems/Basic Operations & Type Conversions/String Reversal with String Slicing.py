userInput = input("Enter a string: ")

# check for space
while " " not in userInput:
    print("The string does not contain a space.")
    userInput = input("Enter a string: ")

userInput.split(" ")

print(userInput[::-1])