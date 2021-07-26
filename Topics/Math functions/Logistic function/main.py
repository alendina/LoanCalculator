import math
x = int(input())
sigma = math.e ** x / (math.e ** x + 1)
print(round(sigma, 2))