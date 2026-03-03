# All list functions and methods have been demonstrated in this code snippet, including 
animalList = ["cat", "dog", "rabbit", "hamster"]
# append, 
animalList.append("turtle")
print (animalList) # ['cat', 'dog', 'rabbit', 'hamster', 'turtle']
# insert, 
animalList.insert(1, "parrot")
print (animalList) # ['cat', 'parrot', 'dog', 'rabbit', 'hamster', 'turtle']
# remove, 
animalList.remove("rabbit")
print (animalList) # ['cat', 'parrot', 'dog', 'hamster', 'turtle']
# pop, 
animalList.pop(2)
print (animalList) # ['cat', 'parrot', 'hamster', 'turtle']
# sort, 
animalList.sort()
print (animalList) # ['cat', 'hamster', 'parrot', 'turtle']
# reverse, 
animalList.reverse()
print (animalList) # ['turtle', 'parrot', 'hamster', 'cat']
# clear, 
animalList.clear()
print (animalList) # []
animalList = ["Dragon", "Unicorn", "Phoenix", "Griffin", "dave","dave"]
# copy, 
copyList = animalList.copy()
print (copyList) # ['Dragon', 'Unicorn', 'Phoenix', 'Griffin', 'dave']
# count, 
print (copyList.count("dave")) # 2
# index, 
print (copyList.index("Phoenix")) # 2
# and extend.
copyList.extend(["Mermaid", "Centaur"])
print (copyList) # ['Dragon', 'Unicorn', 'Phoenix', 'Griffin', 'dave', 'dave', 'Mermaid', 'Centaur']

# Replacement of a value in a list
rList = [1, 2, 3, 4, 5]
rList[2] = 10
print (rList) # [1, 2, 10, 4, 5]

for i in range (len(rList)):
    if rList[i] % 2 == 0:
        rList[i] = i % 2 # if even
print (rList)


# separate string into a list
myString = "Hello World"
myList = myString.split()
print (myList) # ['Hello', 'World']

mystring = "HelloWorld"
mylist = list(mystring)
print (mylist) # ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']