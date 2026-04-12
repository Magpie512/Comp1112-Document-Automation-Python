listOne = ['a', 'b', 'c', 'd', 'e', 'f']
listTwo = ['1', '2', '3', '4', '5', '6']
listThree = ['x', 'y', 'z', 'w', 'v', 'u']
# Result: ['A1X', 'YB', '22', 'D4W', 'VE', '55']
resultList = []

def advancedZipper(listOne, listTwo, listThree):
    tempItem = ''
    for index in range(len(listOne)):
        if index % 3 == 0:
            tempItem = str(listOne[index] + listTwo[index] + listThree[index])

        if index % 3 == 1:
            tempItem = str(listThree[index] + listOne[index])

        if index % 3 == 2:
            tempItem = str(listTwo[index-1]) * 2
        
        tempItem = tempItem.upper()
        resultList.append(tempItem)

    return resultList

print(advancedZipper(listOne, listTwo, listThree))