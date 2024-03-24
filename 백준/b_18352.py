# 특정 거리의 도시 찾기 (다익스트라)

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b,1))

q = []
distance[x] = 0
heapq.heappush(q, (0, x))

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = distance[now] + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

count = 0
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        count += 1
if count == 0: print(-1)