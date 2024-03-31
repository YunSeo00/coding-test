# 쉬운 최단거리 - bfs

from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    data = list(map(int, input().split()))
    if 2 in data:
        r = i
        c = data.index(2)
    graph.append(data)

graph[r][c] = 2
queue = deque()
queue.append((r, c))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    r, c = queue.popleft()
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < m and graph[nx][ny] == 1:
            graph[nx][ny] = graph[r][c] + 1
            queue.append((nx, ny))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            print(-1, end = ' ')
        elif graph[i][j] == 0:
            print(0, end = ' ')
        else:
            print(graph[i][j] - 2, end = ' ')
    print()