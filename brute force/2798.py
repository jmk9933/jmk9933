n, m = map(int,input().split())

card = list(map(int,input().split()))
result = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            add = card[i] + card[j] + card[k]

            if(add <= m and m-add < m-result):
                result = add
print(result)