valueOne = 7
def testFunction():
    valueOne = 56
    valueOne = 44
    print(valueOne)

testFunction() # prints the local variable valueOne, which is 44
print(valueOne) # prints the global variable valueOne, which is 7

# The function testFunction() is called,
# which assigns the value 56 to the local variable valueOne, 
# then reassigns it to 44, and finally prints it. So the output of testFunction() will be 44.
# After the function call, the global variable valueOne remains unchanged, so the output of print(valueOne) will be 7.