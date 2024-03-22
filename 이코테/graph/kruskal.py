# 크루스칼 알고리즘 : 대표적인 최소 신장 트리 알고리즘(greedy)

# 신장트리(spanning tree)
# : 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프

# 1. 간선 데이터를 비용에 따라 오름차순으로 정렬
# 2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
#    - 사이클이 발생하지 않는 경우 최소 신장 트리에 포함
#    - 사이클이 발생하면 포함 X
# 3. 모든 간선에 대해 2의 과정 반복

# 입력
# 7 9
# 1 2 29
# 1 5 75
# 2 3 35
# 2 6 34
# 3 4 7
# 4 6 23
# 4 7 13
# 5 6 53
# 6 7 25

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
# 노드와 간선 개수 입력
v, e = map(int, input().split())
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

# 신장 트리에 포함한 간선의 정보
edges = []
result = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        
print(result)

