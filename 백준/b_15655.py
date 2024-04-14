# N과 M(6)

import heapq

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

index_stack = []
stack = []
series = []

def dfs(x):
    stack.append(data[x])
    index_stack.append(x)
    # print(x, stack, len(stack) == m)
    if len(stack) == m:
        series.append(list(stack[:])) # 리스트 추가 시에 실제 리스트 객체의 참조를 추가함. -> 복사해서 추가해주어야 함.
        stack.pop()
        index_stack.pop()
        return
    for x in range(x+1, n):
        if x in index_stack:
            continue
        dfs(x)
    stack.pop()
    index_stack.pop()
    return

for i in range(n):
    dfs(i)

series.sort()
pre = ''
for x in series:
    current = ' '.join(map(str, x))
    if pre == current:
        continue
    print(current)
    pre = current