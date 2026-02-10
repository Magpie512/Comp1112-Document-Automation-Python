sentence = "Millie maimed and disabled that MF bug."

# Split the sentence into words
wordList = sentence.split()

# Print the original list of words
print("Original list of words:", wordList, "\n")

# Loop through each word and print it
for i in range(len(wordList)): # Loop through each word in the list

    print("Word", i+1, "is", "'"+wordList[i]+"'") # Print the word and its position in the list

    for j in range(len(wordList[i])): # Loop through each letter in the current word

        print("Letter", j+1, "is", "'"+wordList[i][j]+"'") # Print the letter and its position in the word
        
    print()  # New line for better readability

# Make everything lowercase
lowercase_sentence = sentence.lower()
print("Lowercase sentence:", lowercase_sentence)

# Make everything uppercase
uppercase_sentence = sentence.upper()
print("Uppercase sentence:", uppercase_sentence)

#Make everything title case
titlecase_sentence = sentence.title()
print("Title case sentence:", titlecase_sentence)

# Make everything capitalized
capitalized_sentence = sentence.capitalize()
print("Capitalized sentence:", capitalized_sentence)

# Make everything swapcase
swapcase_sentence = sentence.swapcase()
print("Swapcase sentence:", swapcase_sentence)

# Make everything casefolded
casefolded_sentence = sentence.casefold()
print("Casefolded sentence:", casefolded_sentence)