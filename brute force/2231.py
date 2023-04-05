num = int(input())
x = 0

for i in range(num):
    a = list(map(int, str(i)))
    if num == sum(a) + i:
        x = i
        break
print(x)