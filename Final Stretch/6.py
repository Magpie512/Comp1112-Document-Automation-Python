text = 'PyThOn_CoDeR'
step1 = text[::2].lower() # every two
step2 = step1[::-1].upper() # going reverse
step3 = step2.replace('O', '0').replace('E', '3') # replace O with 0 and E with 3
step4 = step3[1:4] + step3[-3:] # first three and last three
finalResult = str(len(step4)) + step4 + str(step4.count('R'))

print(step1)
print(step2)
print(step3)
print(step4)
print(finalResult)