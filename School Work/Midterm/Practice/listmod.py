listOne = ["ABCD","EFG","HIJK","LMM"]
referenceLetters = "BGJM"
vowels = "AEIOU"

# Find strings where the 3rd character is in referenceLetters AND the string length > 3
for i in range(len(listOne)):
    if len(listOne[i]) > 3 and listOne[i][2] in referenceLetters:
        print(listOne[i])

# Replace strings with 2nd character in referenceLetters OR contains a vowel
for i in range(len(listOne)):
    if listOne[i][1] in referenceLetters or any(vowel in listOne[i] for vowel in vowels):
        listOne[i] = "XXXX"

# Count and display how many strings were modified
modified_count = listOne.count("XXXX")
print(f"Modified {modified_count} strings")
print(listOne)