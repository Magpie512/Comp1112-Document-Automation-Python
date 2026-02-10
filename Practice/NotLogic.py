example = 523

print(example) # prints the value of example

while example > 0: # while example is greater than 0
    print(example) # prints the value of example
    example = example - 1 # subtracts 1 from example and updates its value

while example not in [67,420,69]: # while example is not 0 or 1
    print("bruh")
    break
    example = 69
    if example in [67, 420, 69]:
        print("hit a special value")