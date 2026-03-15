sideOne = input("Enter the length of the first side: ")
sideTwo = input("Enter the length of the second side: ")
sideThree = input("Enter the length of the third side: ")

if sideOne == sideTwo == sideThree:
    print("The triangle is an equilateral triangle.")
elif sideOne == sideTwo or sideOne == sideThree or sideTwo == sideThree:
    print("The triangle is an isosceles triangle.")
else:
    print("The triangle is a scalene triangle.")