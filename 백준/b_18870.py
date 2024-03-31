# 좌표 압축
import sys
import heapq

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

dict = {}
count = 0
q = []
for i in data:
    heapq.heappush(q, i)    

for _ in range(n):
    i = heapq.heappop(q)
    if i not in dict:
        dict[i] = count
        count += 1

for i in data:
    print(dict[i], end = ' ')