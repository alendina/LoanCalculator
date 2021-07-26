sum_, sum_sq = 0, 0
while True:
    num = int(input())
    sum_ += num
    sum_sq += num ** 2
    if sum_ == 0:
        break
print(sum_sq)
