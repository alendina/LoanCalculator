import math

param = [int(input()) for x in range(3)]
p = sum(param) / 2
s = math.sqrt(p * (p - param[0]) * (p - param[1]) * (p - param[2]))
print(s)