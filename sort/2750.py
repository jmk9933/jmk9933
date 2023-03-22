list = []

num = int(input())

for i in range(0,num):
    a = int(input())
    list.append(a)

list.sort()

for i in range(0,num):
    print(list[i])