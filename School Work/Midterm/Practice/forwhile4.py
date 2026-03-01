y = 0
a = 4
b = 2
count = 0
square = 0
tri = 0
upt = 0
circle = 0

for x in range (16,1,-2):
    y += (b*3)
    tri = y
    while (y % b == 0):
        y = y//2
        square = y
    if (y % 5 == 0):
        y = x + 1
        upt = y
    elif not (y % b == 0):
        y -= b - 1
        circle = y
    else:
        continue
    count += 1

    print(f"a | b | x | tri |square| upt | circle | y")
    print(f"{a} | {b} | {x} |  {tri}  |   {square}  |  {upt}  |   {circle}    | {y} \n")

