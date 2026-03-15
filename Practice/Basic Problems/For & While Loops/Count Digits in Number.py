N = int(input("Enter a number: "))
count = 0
loop = N

while loop > 0:
    loop = loop // 10 # Removes the last digit
    count += 1

print("The number of digits in", N, "is", count)