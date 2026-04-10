valA = "12"
valB = "5"
combined = str(int(valA) % int(valB))
text = "PythonProgramming"

if int(combined) > 0:
    part = text[0:int(combined)]
    finalText = part.swapcase() + combined
else:
    finalText = "NONE"

print(finalText)