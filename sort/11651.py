import sys

num = int(input())
list = []

for i in range(num):
    a, b = map(int,sys.stdin.readline().split())
    list.append([b,a])

list.sort()

for i in range(num):
    print(list[i][1], list[i][0])