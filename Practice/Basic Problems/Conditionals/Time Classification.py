userInput = input("Enter a time in 24-hour format: ")
userInput = int(userInput)

if userInput < 12:
    print("Good Morning")
elif userInput < 17:
    print("Good Afternoon")
elif userInput < 20:
    print("Good Evening")
else:
    print("Good Night")