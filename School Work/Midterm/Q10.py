listOne = ["ABCD","EFG","HIJK","LMM"]
referenceLetters = "BGJM"

for i in range(len(listOne)):
    if listOne[i][2] in referenceLetters:
        print(listOne[i])

for i in range(len(listOne)):
    if listOne[i][1] in referenceLetters:
        listOne[i] = "XXXX"

print(listOne)