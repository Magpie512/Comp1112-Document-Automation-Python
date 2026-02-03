print("Provide three words of three differing lengths")
wordOne = input("Input word one: ")
wordTwo = input("Input word two: ")
wordThree = input("Input word three: ")

def lengthCheck(wordOne, wordTwo, wordThree):
    # Determine the longest word
    if len(wordOne) > len(wordTwo) and len(wordOne) > len(wordThree):
        longest = wordOne
    elif len(wordTwo) > len(wordOne) and len(wordTwo) > len(wordThree):
        longest = wordTwo
    else:
        longest = wordThree

    # Determine the shortest word
    if len(wordOne) < len(wordTwo) and len(wordOne) < len(wordThree):
        shortest = wordOne
    elif len(wordTwo) < len(wordOne) and len(wordTwo) < len(wordThree):
        shortest = wordTwo
    else:
        shortest = wordThree

    # Combine them
    combinedWords = shortest + longest

    # Sends combinedWords back to caller
    return combinedWords

# result holds combinedWords from lengthCheck function
result = lengthCheck(wordOne, wordTwo, wordThree)
print(result)

# Check if the combined length is even or odd
# Changed 'combinedWords' to 'result'
if len(result) % 2 == 0:
    print("Even.")
else:
    print("Odd.")