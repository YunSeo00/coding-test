# 미로탈출
# 접근 : BFS
from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
queue.append((0,0))

while True:
    r, c = queue.popleft()
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if nx >= 0 and nx < n and ny >=0 and ny < m and graph[nx][ny] == 1:
            graph[nx][ny] += graph[r][c] # *
            queue.append((nx, ny))
    if r == n - 1 and c == m - 1:
        break
print(graph[r][c])