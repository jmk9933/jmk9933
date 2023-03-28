import sys

num = int(input())
list_num = []

for i in range(num):
    a = int(sys.stdin.readline())
    list_num.append(a)

b = (list(set(list_num))).sort()

for i in range(len(b)):
    print(b[i])