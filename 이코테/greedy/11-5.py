# 볼링공 고르기

# 접근1: 2중 for문
N, M = map(int, input().split())
balls = list(map(int, input().split()))

balls.sort()

count = 0
for i in range(N):
    for j in range(i,N):
        if balls[i] != balls[j]:
            count += 1

print(count)

# 접근2 : 무게별 볼링공 개수
array = [0] * 10

for ball in balls:
    array[ball-1] += 1

count = 0
for m in range(M):
    count += array[m] * sum(array[m+1:])
    
print(count)