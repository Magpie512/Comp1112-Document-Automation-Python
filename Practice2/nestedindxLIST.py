data = [["Alice", 25], ["Bob", 30], ["Charlie", 35]]
result = ""
for person in data:
    if person[1] > 28:
        result += person[0][0]
print(result)