result = ''
counter = 0
for i in range(3): # occurs 3 times
    for j in range(2, 5): # occurs 3 times
        for k in range(1, 4): # occurs 3 times
            counter = counter + 1
            if (i + j + k) % 3 == 0: # if i + j + k is divisible by 3
                continue # skip the rest of the loop
            if counter > 12: # if counter is greater than 12
                break # break the loop
        result = result + str(i * j * k) # add if any 0 then 0
        if counter > 12:
            break

print(result)
print(str(counter))