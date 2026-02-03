"""
Mara Briggs
200561234
02-02-2026
Demonstrates every function of a list in Python.
"""

# Creates a list with initial values
myList = [5, 10, 15, 20, 25]
print("myList =", myList, "\n")

# Appends a value to the end of the list
myList.append(30)
print("List after appending 30:", myList, "\n")

# Inserts a value at index 2
myList.insert(2, 12)

# Removes the value 15 from the list
myList.remove(15)

# Pops the last value from the list and stores it
poppedValue = myList.pop()
print("Popped Value:", poppedValue)

# Sorts the list in ascending order
myList.sort()
print("Sorted List:", myList)

# Reverses the list
myList.reverse()
print("Reversed List:", myList)

# Prints the length of the list
print("Length of List:", len(myList))

# Prints the final state of the list
print("Final List:", myList)

# Clears all elements from the list
myList.clear()

print("Cleared List:", myList)

# Demonstrates creating a new list after clearing
newList = [1, 2, 3]
print("New List:", newList)

# Demonstrates copying a list
copiedList = newList.copy()
print("Copied List:", copiedList)

# Demonstrates extending a list
newList.extend([4, 5, 6])
print("Extended List:", newList)

# Demonstrates counting occurrences of an element
countOfTwo = newList.count(2)
print("Count of 2 in New List:", countOfTwo)

# Demonstrates finding the index of an element
indexOfThree = newList.index(3)
print("Index of 3 in New List:", indexOfThree)

# Demonstrates slicing a list
slicedList = newList[1:4]
print("Sliced List (index 1 to 3):", slicedList)

# Demonstrates concatenating two lists
concatenatedList = newList + copiedList
print("Concatenated List:", concatenatedList)

# Demonstrates multiplying a list
multipliedList = newList * 2
print("Multiplied List:", multipliedList)
