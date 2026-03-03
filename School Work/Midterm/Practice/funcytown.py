def mystery(a, b):
    """ takes two numbers, a and b, and does something with them! """
    print(a, b)
    if a > b:
        c = a + 4
    elif b > a:
        c = b - 2
    else:
        c = -1
    return c

a = 3
b = 4
c = 5
b = mystery(c, a)
print(a, b, c)