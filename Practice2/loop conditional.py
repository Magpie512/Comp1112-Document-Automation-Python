word = "Level"
output = ""
for i in range(len(word)):
    if i % 2 == 0:
        output += word[i].lower()
    else:
        output += word[i].upper()
print(output)