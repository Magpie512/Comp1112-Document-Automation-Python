valA = "25"
valB = 4

def process(s, n):
    result = int(s) // n
    if result % 2 == 1:
        return str(result) + " odd"
    return str(result) + " even"

final = process(valA, valB)
print("Final: " + final) 