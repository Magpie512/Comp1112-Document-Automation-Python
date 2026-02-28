x = 0
y = 5

for i in range(3, 9, 2):
    x += 1

    for j in range(y, 0, -1):

        if j % 2 == 0:
            continue
        
        x += j
        print(x, end=" ")

        if x > 15:
            break

    y -= 1

    if x >= 20:
        break

    print("|", end=" ")
