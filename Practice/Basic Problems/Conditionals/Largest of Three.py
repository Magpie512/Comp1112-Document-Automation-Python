first = input ("Input first number: ")
second = input ("Input second number: ")
third = input ("Input third number: ")

if first > second and first > third:
    print(first, "is the largest number")
elif second > first and second > third:
    print(second, "is the largest number")
else:
    print(third, "is the largest number")