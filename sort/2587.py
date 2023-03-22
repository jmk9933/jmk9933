list = []
for i in range(5):
    a = int(input())
    list.append(a)
add = 0
for i in range(5):
    add += list[i]
ave = add/5

list.sort()
mid = list[2]

print(int(ave))
print(mid)
