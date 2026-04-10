vals = ["apple", "pear"]
vals.append("kiwi")
vals.insert(1, "mango")
vals[2] = vals[0].upper()
vals.insert(0, str(len(vals)))

print(vals)