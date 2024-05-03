# 열혈강호

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [0] * n
matching = [-1] * m

for i in range(n):
    data = list(map(int, input().split()))
    graph[i] = data[1:]

def dfs(p):
    if visited[p] == 1:
        return False
    visited[p] = 1
    for t in graph[p]:
        if matching[t-1] == -1:
            matching[t-1] = p
            return True
        else:
            if dfs(matching[t-1]): # 만약 다른 일이 점유하고 있던 직원에게 배정된다면
                matching[t-1] = p # 현재의 일을 현재의 직원에게 배정
                return True

count = 0
for p in range(n):
    visited = [0] * n
    if dfs(p):
        count += 1
print(count)