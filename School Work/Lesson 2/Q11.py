print("Welcome! Please enter a number greater than 5.")

number = int(input("Enter a number: "))

while not number > 5:
    print("The number is not greater than 5.")
    number = int(input("Enter a number: "))

print("Thank you! The number is greater than 5.")