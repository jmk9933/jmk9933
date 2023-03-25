import sys

num = int(input())
list = []

for i in range(num):
    a, b = map(int,sys.stdin.readline().split())
    list.append([a,b])

list.sort()

for i in range(num):
    print(list[i][0], list[i][1])