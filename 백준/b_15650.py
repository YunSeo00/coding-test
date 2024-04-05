# N과 M (2) (3) (4)

n, m = map(int, input().split())

stack = []
series = []

def dfs(x):
    stack.append(x)
    # print(x, stack, len(stack) == m)
    if len(stack) == m:
        series.append(list(stack[:])) # 리스트 추가 시에 실제 리스트 객체의 참조를 추가함. -> 복사해서 추가해주어야 함.
        stack.pop()
        return
    for x in range(x+1, n+1):  # (2)
    # for x in range(1, n+1): # (3)
    # for x in range(x, n+1): # (4)
        dfs(x)
    stack.pop()
    return


for i in range(1, n+2-m): # (2)
#for i in range(1, n+1): # (3) (4)
    dfs(i)

for x in series:
    print(*x)