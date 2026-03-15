year = input ("Enter a year: ")

if int(year) % 4 == 0: # check if the year is divisible by 4

    if int(year) % 100 == 0:
    
        if int(year) % 400 == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")

    else:
        print(year, "is a leap year")

else:
    print(year, "is not a leap year")