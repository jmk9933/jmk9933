import sys
input = sys.stdin.readline

num = int(input())
dict = {}

a = list(map(int, input().split()))

new_a = sorted(set(a))

for i in range(len(new_a)):
    dict[new_a[i]] = i

for j in a:
    print(dict[j], end = " ")