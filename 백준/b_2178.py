# 미로 탐색 - bfs

from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
# print(graph)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
queue.append((0,0))

while True:
    r, c = queue.popleft()
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        # print(r, c, nx, ny)
        if nx >= 0 and ny >= 0 and nx < n and ny < m:
            if graph[nx][ny] == 1:
                graph[nx][ny] += graph[r][c]
                queue.append((nx, ny))
    # print(r, c, queue)
    if r == n-1 and c == m-1:
        break
print(graph[r][c])