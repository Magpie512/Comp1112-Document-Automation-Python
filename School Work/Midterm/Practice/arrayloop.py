# Practice Program: Loops and Arrays Tracing

# Example 1: Simple array loop
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num    # += is a shorthand for total = total + num
print(f"Sum: {total}")

# Example 2: Nested loops with 2D array
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()

# Example 3: While loop with array indexing
arr = [5, 10, 15, 20, 25]
i = 0
while i < len(arr):
    arr[i] = arr[i] * 2
    i += 1
print(f"Doubled array: {arr}")

# Example 4: Loop with conditional
scores = [85, 92, 78, 95, 88]
count = 0
for score in scores:
    if score >= 90:
        count += 1
print(f"Scores >= 90: {count}")

# Example 5: Reverse loop
items = ['a', 'b', 'c', 'd']
for j in range(len(items) - 1, -1, -1):
    print(items[j], end=" ")