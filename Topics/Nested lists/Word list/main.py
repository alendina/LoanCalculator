text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]
num = int(input())
total = []
for i in range(3):
    words = text[i]
    total.extend([w for w in words if len(w) <= num])
print(total)
