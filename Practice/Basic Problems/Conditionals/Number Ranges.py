userInput = input("Enter a number: ")

ranges = ["0-50", "51-100", "101-150", "Above 150"]

if int(userInput) <= 50:
    print(userInput, "is in the range of", ranges[0])
elif int(userInput) <= 100:
    print(userInput, "is in the range of", ranges[1])
elif int(userInput) <= 150:
    print(userInput, "is in the range of", ranges[2])
else:
    print(userInput, "is in the range of", ranges[3])