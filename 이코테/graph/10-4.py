# 커리큘럼

from collections import deque
import copy
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
time = [0] * (n+1)
need_time = [INF] * (n+1)

for i in range(1,n+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for j in data[1:-1]:
        indegree[i] += 1
        graph[j].append(i)

result = copy.deepcopy(time)
q = deque()

print(indegree)
for i in range(1, n+1):
    if indegree[i] == 0:
        print(i , end = ' ')
        result[i] = time[i]
        q.append(i)
    
while q:
    now = q.popleft()
    for i in graph[now]:
        indegree[i] -= 1
        result[i] += time[now]
        if indegree[i] == 0:
            q.append(i)

for i in range(1, n+1):
    print(result[i])


# 입력
# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1