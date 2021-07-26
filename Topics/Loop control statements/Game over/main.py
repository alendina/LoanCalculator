user_answers = input()
c_count = 0
i_count = 0

for h in user_answers:
    if h == "C":
        c_count += 1
    elif h == "I":
        i_count += 1
    if i_count == 3:
        print(f'Game over\n{c_count}')
        break
else:
    print(f'You won\n{c_count}')
