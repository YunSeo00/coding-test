# 토마토
# 시간 초과

import copy
from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split()) # 열 행
array = [list(map(int, input().split())) for _ in range(n)]
day = copy.deepcopy(array)
final_day = [[n*m]*m for _ in range(n)]

q = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0] * m for _ in range(n)]

# 시간 초과 해결: 시작점을 모두 넣어두고 시작해야 함.
# bfs에서 최대 기간을 구하는 문제에서는 시작점을 모두 넣어야 한다.
for i in range(n):
    for j in range(m):
        if array[i][j] == 1:
            q.append([i, j])
            visited[i][j] = 1
            final_day[i][j] = 1
while q:
    r, c = q.popleft()
    for k in range(4):
        nx = r + dx[k]
        ny = c + dy[k]
        if nx >= 0 and nx < n and ny >= 0 and ny < m and \
            array[nx][ny] == 0 and visited[nx][ny] == 0 and final_day[nx][ny] > day[r][c] + 1:
            visited[nx][ny] = 1
            day[nx][ny] = day[r][c] + 1
            final_day[nx][ny] = min(final_day[nx][ny], day[nx][ny])
            q.append([nx, ny])

result = 0
for i in range(n):
    for j in range(m):
        if array[i][j] == -1:
            continue
        result = max(result, final_day[i][j] - 1)

print(-1 if result == m*n - 1 else result)