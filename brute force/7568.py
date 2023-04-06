num = int(input())
list =[]

for i in range(num):
    w, h = map(int,input().split())
    list.append((w,h))

for i in list:
    rank = 1
    for j in list:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = " ")