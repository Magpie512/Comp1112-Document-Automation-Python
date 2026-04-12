mainList = ['A', 'B', 'C', 'D']
refList = mainList # List with same reference
copyList = mainList[:]  # Shallow copy

mainList[1] = 'X'
refList.append('E')
copyList[0] = 'Z'
mainList.insert(2, 'Y')

print(str(mainList)) # ['A', 'X', 'Y', 'C', 'D', 'E']
print(str(refList)) # ['A', 'X', 'Y', 'C', 'D', 'E']
print(str(copyList)) # ['Z', 'B', 'C', 'D']
print(str(len(mainList) + len(refList) + len(copyList))) # 16