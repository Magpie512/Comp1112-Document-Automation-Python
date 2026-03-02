a1: int = 3
# another way to write is
# a1 = 3
a2: int = a1 + 9
a3: int = a1 + a2
a2 = a1 + a3 - 5
a1 = a1 + 1
a3 = a2 * 2 - a1
a1 = a1 + 1
print(str(a1) + " -> " + str(a2 + a3))
