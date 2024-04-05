# N과 M (5)

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

stack = []
series = []

def dfs(x):
    stack.append(data[x])
    # print(x, stack, len(stack) == m)
    if len(stack) == m:
        series.append(list(stack[:])) # 리스트 추가 시에 실제 리스트 객체의 참조를 추가함. -> 복사해서 추가해주어야 함.
        stack.pop()
        return
    for x in range(n):
        if data[x] in stack:
            continue
        dfs(x)
    stack.pop()
    return

for i in range(n):
    dfs(i)

for x in series:
    print(*x)