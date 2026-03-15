list = [4,5,4,5,6,1]
average = 0
sum = 0

for i in range(len(list)):
    sum = sum + list[i]
    average = sum / len(list)

print(average)