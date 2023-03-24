'''
최빈값 구하는 방법??
Counter을 이용해야 한다.
Counter는 리스트의 각 숫자들의 등장횟수를 카운트하여 몇 회 등장했는지 딕셔너리로 표현한다.
Counter의 most_common(n)은 빈도수가 가장 많은 것 부터 n개의 수를 숫자의 형태로 반환한다.
'''

import sys

num = int(input()) 
list = []

for i in range(num):
    a = int(sys.stdin.readline())
    list.append(a)

list.sort()

ave = round(sum(list)/num)
mid = list[int((num+1)/2)-1]
most = 
diff = max(list) - min(list)

print(ave)
print(mid)
print(most)
print(diff)