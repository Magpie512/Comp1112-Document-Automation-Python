N = int(input("Enter a number: "))

total = 0

for i in range(1, N + 1):
    total += i
    print("Iteration", i, "\nCurrent total:", total)

print("The sum of the first", N, "natural numbers is:", total)