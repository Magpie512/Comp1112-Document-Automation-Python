# Assume the user types in the number 7

userValue = input()
# 7
print(userValue + "12")
# 7 + 12 = 712 (string concatenation)
print(len(userValue))
# len("7") = 1 (length of the string "7")
print((userValue * 2) + str(int(userValue) * 3)))
# Compile error: SyntaxError: unexpected EOF while parsing
# EOF stands for End Of File, which means that the Python interpreter reached the end of the file while it was still expecting more code to complete the statement. In this case, there is a missing closing parenthesis at the end of the line, which causes the syntax error.