# 도시 분할 계획 (크루스칼)
import sys
input = sys.stdin.readline

# find, union 함수 구현
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_set(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

# edge 입력
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b)) # cost, b

edges.sort()

# count = 0 # n-2가 되면 종료
# (첫 접근으로는 count가 n-2가 되면 종료하도록 했지만, 마을이 2개인 경우에는 이 조건이 만족되지 않으므로 현재 코드와 같이 가장 긴 간선을 삭제하는 것이 맞다.)
result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_set(parent, a, b)
        # count += 1
        result += cost
        last = cost 

print(result-last)

# 7 12
# 1 2 3
# 1 3 2
# 3 2 1
# 2 5 2
# 3 4 4
# 7 3 6
# 5 1 5
# 1 6 2
# 6 4 1
# 6 5 3
# 4 5 3
# 6 7 4