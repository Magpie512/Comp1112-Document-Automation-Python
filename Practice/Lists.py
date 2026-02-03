"""
Mara Briggs
200561234
02-02-2026
Demonstrates every function of a list in Python.
"""

# Creating a list from a sentence
sentence = "I am learning Python programming"
words = sentence.split()  # Splitting the sentence into words
print("Original list of words:", words, "\n")

#for each word
for i in range(len(words)):
    print("Word", i+1, "is", "'"+words[i]+"'\n")
    #for each letter
    for j in range(len(words[i])):
        print("Letter", j+1, "is", "'"+words[i][j]+"'")
    print()  # New line for better readability

# Demonstrating various list functions
print("Length of the list:", len(words))  # Length of the list

words.append("!")  # Adding an element to the end
print("List after appending '!':", words)
words.insert(2, "really")  # Inserting an element at index 2
print("List after inserting 'really' at index 2:", words)
