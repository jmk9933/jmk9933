'''
input() 은 prompt message를 받을 수 있지만, sys.stdin.readline()은 그렇지 않다.
따라서 후자의 경우가 상대적으로 속도가 더 빠르다.
sys.stdin.readline()은 
1. 문자열로 입력을 받는다.
2. 개행문자(\n)가 기본으로 포함되어 있다.
'''

import sys

num = int(input())
list = [0] * 10001

for i in range(num):
    a = int(sys.stdin.readline())
    list[a] = list[a] + 1

for i in range(10001):
    if list[i] != 0:
        for j in range(list[i]):
            print(i)
