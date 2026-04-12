data = [
{'name': 'Alice', 'scores': [85, 90, 78]},
{'name': 'Bob', 'scores': [92, 88, 95]},
{'name': 'Charlie', 'scores': [70, 75, 80]}
]
output = ''
totalSum = 0
for item in data:
    avg = sum(item['scores']) // len(item['scores'])
if avg > 80:
    output = output + item['name'][0]
totalSum = totalSum + avg
print(output)
print(str(totalSum))