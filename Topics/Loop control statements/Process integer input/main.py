num = []
while True:
    n = int(input())
    if n < 10:
        continue
    elif n > 100:
        break
    else:
        num.append(n)
for i in num:
    print(i)
