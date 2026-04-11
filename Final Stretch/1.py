globalVar = 10
localVar = 20
def outerFunc(x):
    globalVar = 30
    localVar = x * 2

    def innerFunc(y):
        global globalVar
        localVar = y + 5
        globalVar = globalVar + localVar
        return localVar
    
    result = innerFunc(3)
    return str(localVar) + str(result)
output = outerFunc(7)

print(output)
print(str(globalVar))