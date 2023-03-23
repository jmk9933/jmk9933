a = int(input())
a = str(a)
list = []

for i in range(len(a)):
    list.append(a[i])
list.sort()
list.reverse()
for i in range(len(a)):
    print(list[i], end = '')
