import sys
num = int(sys.stdin.readline())

stack = []

for i in range (num):
    enter = sys.stdin.readline().split()

    if enter[0] == 'push':
        stack.append(enter[1])

    elif enter[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif enter[0] == 'size':
        print(len(stack))

    elif enter[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif enter[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])