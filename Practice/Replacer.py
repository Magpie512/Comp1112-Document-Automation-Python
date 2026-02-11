# Goal to randomly replace odd elements from alphalist with random elements from numlist
import random

alphaList = ['a', 'b', 'c', 'd']
numList = ['1', '2', '3', '4']

for i in range(len(alphaList)):
    if not i % 2 == 0: # If the index is odd
        alphaList[i] = random.choice(numList) # Replace the element at the odd index with a random element from numList 
print(alphaList)

