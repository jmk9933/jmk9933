import sys

num = int(input())  
list = []

for i in range(num):
    age, name = map(str, sys.stdin.readline().split())
    age = int(age)
    list.append([age, name])

list.sort(key = lambda x : x[0])

for i in range(num):
    print(list[i][0], list[i][1])