import sys

deque = []

num = int(input())  

for i in range(num):
    enter = sys.stdin.readline().split()

    if enter[0] == 'push_front':
        deque.insert(0, enter[1])

    elif enter[0] == 'push_back':
        deque.append(enter[1])

    elif enter[0] == 'pop_front':
        if(len(deque) != 0):
            print(deque.pop(0))
        else:
            print(-1)

    elif enter[0] == 'pop_back':
        if (len(deque) != 0):
            print(deque.pop())
        else:
            print(-1)

    elif enter[0] == 'size':
        print(len(deque))
    
    elif enter[0] == 'empty':
        if (len(deque) == 0):
            print(1)
        else:
            print(0)

    elif enter[0] == 'front':
        if (len(deque) != 0):
            print(deque[0])
        else:
            print(-1)

    elif enter[0] == 'back':
        if (len(deque) != 0):
            print(deque[-1])
        else:
            print(-1)