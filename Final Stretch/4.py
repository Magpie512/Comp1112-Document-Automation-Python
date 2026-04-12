resultList = []
def mysteryFunc(n):
    if n <= 1:
        return 1
    
    resultList.append(n)
    return n + mysteryFunc(n - 2)

answer = mysteryFunc(7)
print(str(answer))
print(str(resultList))
print(str(len(resultList)))