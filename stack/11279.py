import sys
import heapq

num = int(sys.stdin.readline())

heap = []

for i in range(num):
    number = int(sys.stdin.readline())
    if number!= 0:
        heapq.heappush(heap, -number)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print((-1)*heapq.heappop(heap))