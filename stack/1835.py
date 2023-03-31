from collections import deque

num = int(input())

queue = deque()

queue.append(num)

for i in range(num-1, 0 , -1):
    queue.appendleft(i)
    for j in range(i):
        queue.appendleft(queue.pop())
print(*queue)