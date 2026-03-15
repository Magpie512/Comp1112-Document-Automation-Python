userInput = input("Enter a letter: ")
vowels = ["a", "e", "i", "o", "u"]

while len(userInput) != 1:
    print("Please enter a single letter.")
    userInput = input("Enter a letter: ")

if userInput in vowels:
    print(userInput, "is a vowel")
else:
    print(userInput, "is a consonant")