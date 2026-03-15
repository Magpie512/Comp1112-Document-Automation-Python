userInput = int(input("Enter a number: "))

for i in range (1, userInput+1):
    print(str(i) + " x " + str(userInput) + " = " + str(i * userInput))