# 나이순 정렬
import heapq

n = int(input())
p = []

for i in range(n):
    age, name = input().split()
    heapq.heappush(p, [int(age), i, name])

for i in range(n):
    age, _, name = heapq.heappop(p)
    print(age, name)
