userGrade = input("Enter your grade in percentage: ")
userGrade = int(userGrade)

if userGrade >= 90:
    print ("You got an A+")

elif userGrade >= 80 and userGrade < 90:
    print ("You got an A")

elif userGrade >= 70 and userGrade < 80:
    print ("You got a B")

elif userGrade >= 60 and userGrade < 70:
    print ("You got a C")

elif userGrade >= 50 and userGrade < 60:
    print ("You got a D")

else:
    print ("You got an F")