listOne = ["ABCD","EFG","HIJK","LMM"]
referenceLetters = "BGJM"

for i in range(len(listOne)):
    if listOne[i][2] in referenceLetters:
        print(listOne[i]) 
        # this will print the strings that have the 3rd character in the referenceLetters string
# for every iteraion in range that is the length of listone,
# if the 3rd character of the string at index i in listOne is in the referenceLetters string,
# then print the string at index i in listOne

for i in range(len(listOne)):
    if listOne[i][1] in referenceLetters:
        listOne[i] = "XXXX"
        # this will replace the strings that have the 2nd character in the referenceLetters string with "XXXX"
# for every iteraion in range that is the length of listone,
# if the 2nd character of the string at index i in listOne is in the referenceLetters string,
# then replace the string at index i in listOne with "XXXX"

print(listOne)