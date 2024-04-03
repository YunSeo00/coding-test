# 부분수열의 합 - 완전 탐색 ***
# 난 왜 완전 탐색이 어렵지..
# 1. 탐색을 시작할 범위를 작성한다.
# 2. 종료 조건을 지정한다.
# 3. 적절한 범위의 for 문을 돌면서 아래의 과정을 반복한다.
#      - append, visited 1, dfs -> 다음 depth를 탐색
#      - pop, visited 0 -> 다음 가치를 탐색하도록

n, s = map(int, input().split())
data = list(map(int, input().split()))

stack = []
visited = [0] * n
sets = []

def dfs(x, depth):
    # print(stack)
    if sum(stack) == s:
        sets.append(stack)
        if depth == n:
            return
    for i in range(x+1, n):
        if visited[i]:
            continue
        stack.append(data[i])
        visited[i] = 1
        dfs(i, depth+1)
        stack.pop()
        visited[i] = 0

for i in range(n):
    stack = []
    stack.append(data[i])
    visited[i] = 1
    dfs(i, 0)

print(len(sets))