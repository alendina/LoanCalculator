cafe_list = []
name = ()

while True:
    name = input().split()
    if name[0] == 'MEOW':
        break
    cafe_list.append(name)

max_num = 0
for i in range(len(cafe_list)):
    if max_num < int(cafe_list[i][1]):
        max_num = int(cafe_list[i][1])
        name = cafe_list[i]

print(name[0])
