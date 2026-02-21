j = 1
for i in range(12,6,-2):
    print(i-1)
    j = j + 1
    while not (j==3):
        print(j+1)
        if (j>1):
            break

# starts with i = 12 and j = 1
# 12 - 1 = 11 (prints 11)
# j = 1 + 1 = 2 (j is now 2)

# j is not equal to 3, so it enters the while loop
# 2 + 1 = 3 (prints 3)

# j is now 2, which is greater than 1, so it breaks out of the while loop
# i is now 10 (12 - 2), and j is still 2
# 10 - 1 = 9 (prints 9)

# j is not equal to 3, so it enters the while loop
# 2 + 1 = 3 (prints 3)
# j is now 2, which is greater than 1, so it breaks out of the while loop
# i is now 8 (10 - 2), and j is still 2
# 8 - 1 = 7 (prints 7)

# j is not equal to 3, so it enters the while loop
# 2 + 1 = 3 (prints 3)
# j is now 2, which is greater than 1, so it breaks out of the while loop
# i is now 6 (8 - 2), and j is still 2
# The loop ends because the range is from 12 to 6 (exclusive) with a step of -2, so it does not include 6.
# Final output:
# 11
# 3
# 9
# 7
# 5