# 트리의 부모 찾기
# todo) 다른 풀이 생각(or 찾아)보기
# 현재의 코드는 recursion limit이 100000일 때, recuresion error 발생함.

import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    s, e = map(int, input().split())
    graph[e].append(s)
    graph[s].append(e)

parents = [0] * (n+1)

def delete_parent(parent):
    node = graph[parent]
    for i in node:
        graph[i].pop(graph[i].index(parent))
        parents[i] = parent
        delete_parent(i)

delete_parent(1)

for i in range(2, n+1):
    print(parents[i])
