# 음식물 피하기
import sys
sys.setrecursionlimit(100000)

n, m, k = map(int, input().split())

matrix = [[0]*(m) for _ in range(n)]
visited = [[0]*(m) for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    matrix[r-1][c-1] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(r, c, size):
    visited[r][c] = 1
    for d in range(4):
        nx = r + dx[d]
        ny = c + dy[d]
        if nx >= 0 and nx < n and ny >= 0 and ny < m and visited[nx][ny] == 0 and matrix[nx][ny] == 1:
            size = dfs(nx, ny, size+1)
    return size

sizes = []

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1 and visited[i][j] == 0:
            sizes.append(dfs(i, j, 1))
print(max(sizes))