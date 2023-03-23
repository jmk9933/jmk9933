a, b = map(int,input().split())

score = list(map(int,input().split()))
score.sort()
score.reverse()
print(score[b-1])