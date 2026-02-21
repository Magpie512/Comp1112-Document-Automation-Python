listOne = ["AB","BC","DF","mat"]
print (listOne[0]) # AB
print (listOne[-2]) # DF

for i in range (3):
    for j in range (len(listOne[i])):
        print (listOne[i][j]) # A, B, D, m  

# for every iteration in range 3,
# for every iteration in range of the length of the string at index i in listOne, 
# print the character at index j in the string at index i in listOne