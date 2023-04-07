list = []
fake1 = 0
fake2 = 0

for i in range(9):
    num = int(input())
    list.append(num)

list.sort()

add_all = sum(list)

for i in range(8):
    for j in range(i+1, 9):
        if add_all - list[i] - list[j] == 100:
            fake1 = list[i]
            fake2 = list[j]

list.remove(fake1)
list.remove(fake2)
list.sort()

for i in list:
    print(i)