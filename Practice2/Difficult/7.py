score = 25

def processData(points):
    score = points // 2
    items = ["pen", "ink"]
    items.insert(1, "paper")
    items[0] = items[0].upper()
    return items

resultList = processData(15)
print("Score: " + str(score))
print("Result: " + resultList[1] + " " + resultList[0])