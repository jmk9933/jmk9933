p = [0 for i in range(101)]
p[1] = 1
p[2] = 1
p[3] = 1

for i in range(98):
    p[i+3] = p[i] + p[i+1]
t = int(input())
for i in range(t):
    n = int(input())
    print(p[n])