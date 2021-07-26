ls = []
while True:
    li = input()
    if li == ".":
        break
    ls.append(float(li))
print(min(ls))
