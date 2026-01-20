"""
Mars Briggs
200561234
01-20-2026
Checks if each succeeding input is longer than the last.
Caller then checks if total characters are odd or even.
"""

#Asks for user input
print("Input three words with increasing lengths")
wordOne = input("Word One: ")
wordTwo = input("Word Two: ")
wordThree = input("Word Three: ")

#Function to determin if word lengths are inreasing
def letterCountCheck(wordOne, wordTwo, wordThree):
    lengthOne = len(wordOne)
    lengthTwo = len(wordTwo)
    lengthThree = len(wordThree)

    # Only check increasing lengths
    if lengthTwo == lengthOne + 1 and lengthThree == lengthTwo + 1:
      return wordOne + wordTwo + wordThree
    else:
      return "NULL" #Stops

# CALLER | Checks if the concatenated length is odd or even
output = letterCountCheck(wordOne, wordTwo, wordThree)
print(output)

# Assigns the length of output to totalLength
totalLength = len(output)

# Checks if totalLength if odd or even
if totalLength % 2 == 0:
    print("Even")
else:
    print("Odd")