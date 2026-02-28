import random
def functionOne(stringOne):
    stringTwo = (stringOne *2)
    valueThree = (int(stringTwo) -1500)
    print(len(stringTwo))
    return (valueThree) 

def functionTwo(intOne):
    print(intOne%10)
    value = random.randint(1,5)
    while not (value == 3):
        value = random.randint(1,5)
    print(value)

print(functionOne("17"))
functionTwo(functionOne("17"))
#