# 연결 요소의 개수
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [0] * (n+1)
q = []
count = 0
for i in range(1, n+1):
    if visited[i] == 0:
        visited[i] = 1
        count += 1
        q.append(i)
        while q:
            x = q.pop()
            for j in graph[x]:
                if visited[j] == 0:
                    visited[j] = 1
                    q.append(j)
                    
print(count)