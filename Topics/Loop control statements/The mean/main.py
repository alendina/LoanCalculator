list_ = []
while True:
    input_ = input()
    if input_ == '.':
        break
    list_.append(int(input_))
    # print(list_)
print(sum(list_) / len(list_))
