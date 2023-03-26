import sys

num = int(input())
list = []
new_list = []

for i in range(num):
    word = sys.stdin.readline().strip()
    if [len(word), word] not in new_list:
        new_list.append([len(word), word])

new_list.sort()

for i in range(len(new_list)):
    print(new_list[i][1])