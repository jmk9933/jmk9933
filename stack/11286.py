import sys
import heapq

n = int(input())
queue = []

for i in range(n):
    num = int(sys.stdin.readline())
    if(num !=0 ):
        heapq.heappush(queue, (abs(num), num))
    else:
        if(len(queue) == 0):
            print(0)
        else:
            print(heapq.heappop(queue)[1])