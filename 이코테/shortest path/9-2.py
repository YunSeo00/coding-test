# 미래 도시
INF = 1e9

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
x, k = map(int, input().split())

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for a in range(1, n+1):
    for b in range(1, n+1):
        for c in range(1, n+1): # 양방향 그래프이므로
            graph[b][c] = min(graph[b][c], graph[b][a] + graph[a][c])

if graph[1][k] + graph[k][x] >= INF:
    print(-1)
else:
    print(graph[1][k] + graph[k][x])