# 바이러스
# bfs, dfs

from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(n+1)
queue = deque()
queue.append(1)
visited[1] = 1
count = 0

while queue:
    a = queue.popleft()
    for i in graph[a]:
        if visited[i] == 0:
            count +=1
            visited[i] = 1
            queue.append(i)

print(count)