data = ["sky", "sea"]
output = ""

for i in range(len(data)):
    word = data[i]
    if len(word) == 3:
        output = output + word[0:2].upper() + str(i)
    else:
        output = output + word.capitalize()

print(output)