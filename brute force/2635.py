n = int(input())
max_list = []

for i in range(1,n+1):
    list = [n]
    list.append(i)

    cnt = 1
    while True:
        next = list[cnt-1] - list[cnt]
        if next < 0:
            break
        list.append(next)
        cnt += 1

    if len(max_list) < len(list):
        max_list = list

print(len(max_list))
for i in max_list:
    print(i, end = " ")