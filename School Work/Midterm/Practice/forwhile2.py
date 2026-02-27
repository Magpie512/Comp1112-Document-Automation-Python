a = 3
b = 2
y = 0

for x in range(1,5):
    if x % 2 == 0: 
        y = (a*y) + (b*x)
    else:
        y = y + (b*x)
    
    print(f"After iteration {x}:")
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"x = {x}")
    print(f"y = {y}")

print(y)

