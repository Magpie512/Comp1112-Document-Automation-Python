import random
def functionOne(stringOne):
    stringTwo = (stringOne *2)
    valueThree = (int(stringTwo) -2300)
    print(len(stringTwo))
    return (valueThree) 

def functionTwo(intOne):
    print(intOne%10)
    value = random.randint(1,5)
    while not (value == 2):
        value = random.randint(1,5)
    print(value)

print(functionOne("23"))
functionTwo(functionOne("23"))

# The output of the code will be:
# 4 because the string "23" is repeated twice to form "2323", which has a length of 4. 
# The value of functionOne("23") will be 23*2 - 2300 = 46 - 2300 = -2254. 

# The output of functionTwo will be the last digit of -2254, which is 4, and then it will print 
# random numbers between 1 and 5 until it gets a 2, at which point it will print 2.