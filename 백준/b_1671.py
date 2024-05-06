# 상어의 저녁식사
import sys
input = sys.stdin.readline

n = int(input())
sharks = []
for _ in range(n):
    size, speed, intellect = map(int, input().split())
    sharks.append([size, speed, intellect])

matching = [-1] * n

def dfs(s):
    if visited[s] == 1:
        return False
    visited[s] = 1
    for i in range(n):
        if i == s: continue
        if sharks[i][0] <= sharks[s][0] and sharks[i][1] <= sharks[s][1] and sharks[i][2] <= sharks[s][2]:
            if sharks[i][0] == sharks[s][0] and sharks[i][1] == sharks[s][1] and sharks[i][2] == sharks[s][2] and s <= i:
                continue
            if matching[i] == -1 or dfs(matching[i]):
                matching[i] = s
                return True
    return False

count = 0
for i in range(n):
    for _ in range(2):
        visited = [0] * n
        if dfs(i):
            count += 1

# print(matching)
# print(count)
print(n - count)