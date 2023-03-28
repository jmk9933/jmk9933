'''
컴파일 에러. 왜 컴파일 에러가 났는지 모르겠음
이진 탐색 이용
'''

import sys

n = int(input()) 
n_list = []
m_list = []
list_cnt = []

n_list.append(sys.stdin.readline().strip())

m = int(input()) 
m_list.append(sys.stdin.readline().strip())

for i in range(m):
    if m_list[i] in n_list:
        list_cnt.append(1)
    else:
        list_cnt.append(0)

for i in range(m):
    print(list_cnt[i], end = " ")