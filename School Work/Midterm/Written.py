# Write a function that takes a two list arguments of any equal legnth

# The purpose of the function is to create a new list which every odd CHARACTER corresponds to the odd CHARACTER of the first list ( counting the characters starts at 1) and every even CHARACTER is a random character from the second list.

# For example: if the first list was ['A','B','C','D'] AND THE SECOND LIST WAS ['1','2','3','4'] thenew list could be ['A', '3', 'C', '1']

import random

alphaList = ['A','B','C','D']
numList = ['1','2','3','4']

def listScrambler(alphaList, numList):
    newList = [] # create an empty list to store the new list
    for i in range(len(alphaList)):
        if (i+1) % 2 == 1:
            newList.append(alphaList[i])
        else:
            newList.append(random.choice(numList))
    return newList