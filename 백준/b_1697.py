# 숨바꼭질
# bfs

from collections import deque

n, k = map(int, input().split())

count = 0
q = deque()
q.append(n)

visited = [0] * (100000+1)
visited[n] = 1
while q:
    x = q.popleft()
    if x == k: break
    for nx in [x-1, x+1, 2*x]:
        if nx >= 0 and nx <= 100000 and visited[nx] == 0:
            visited[nx] = visited[x] + 1
            q.append(nx)

print(visited[k]-1)
