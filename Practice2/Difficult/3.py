import random

alphaList = ["A", "B", "C", "D"]
numList = [50, 100]

for i in range(len(alphaList)):
    if not i % 2 == 0:
        alphaList[i] = str(random.choice(numList))

print(alphaList)