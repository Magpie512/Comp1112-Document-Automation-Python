result = ''
counter = 0
for i in range(3): # occurs 3 times
    for j in range(2, 5): # occurs 3 times
        for k in range(1, 4): # occurs 3 times
            counter = counter + 1
            if (i + j + k) % 3 == 0:
                continue
            if counter > 12:
                break
        result = result + str(i * j * k)
        if counter > 12:
            break

print(result)
print(str(counter))