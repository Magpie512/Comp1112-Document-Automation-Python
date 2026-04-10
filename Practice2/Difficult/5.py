level = 10
status = ["low", "mid"]

def update(val):
    level = val * 2
    status[0] = "high"
    status.insert(1, "max")
    return level // 3

print("Return: " + str(update(5)))
print("Level: " + str(level))
print("Status: " + str(status))