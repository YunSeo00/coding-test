# 위상 정렬
# 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것.

# 1. 진입차수가 0인 노드를 큐에 넣는다.
# 2. 큐가 빌 때까지 다음의 과정을 반복한다.
#    2-1. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
#    2-2. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
# * 만약 모든 노드를 꺼내기 전에 진입차수가 0인 노드가 없다면, 사이클이 존재하는 것임.

# 입력
# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4

from collections import deque

# 노드와 간선의 개수 입력
v, e = map(int, input().split())
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]

# 간선 정보 입력
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()
    
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end = ' ')

topology_sort()