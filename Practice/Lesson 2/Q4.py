word = input("Please input a word: ")

for i in word:
    print(i)
    if i in 'aeiouAEIOU':
        print(i + ' is a vowel.')