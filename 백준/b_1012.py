# 유기농 배추
# 접근 : 처음에 dfs로 접근했다가 recursionerror 발생 -> sys.setrecursionlimit(10**6)으로 해결. (파이썬의 default 재귀 횟수는 1000임.)
# 접근2 : bfs로 접근

# DFS 풀이
import sys
sys.setrecursionlimit(10**6) 

def dfs(x, y):
    if x < 0 or y < 0 or x >= m or y >= n: return False
    if cells[x][y] == 1:
        cells[x][y] = 0
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False

t = int(input())

for _ in range(t):  
    m, n, k = list(map(int, input().split()))
    
    cells = [[0 for _ in range(n)] for _ in range(m)]
    points = []
    for _ in range(k):
        x, y = map(int, input().split())
        cells[x][y] = 1
        points.append((x, y))
        

    count = 0
    for x, y in points:
        if dfs(x, y) == True:
            count += 1
    print(count)
    
    
# BFS 풀이
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    cells[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx >= 0 and nx < m) and (ny >= 0 and ny < n):
                if cells[nx][ny] == 1:
                    queue.append((nx, ny))
                    cells[nx][ny] = 0
                    
t = int(input())
for _ in range(t):  
    m, n, k = list(map(int, input().split()))
    
    cells = [[0 for _ in range(n)] for _ in range(m)]
    points = []
    for _ in range(k):
        x, y = map(int, input().split())
        cells[x][y] = 1
        points.append((x, y))
    count = 0
    for x, y in points:
        if cells[x][y] == 1:
            bfs(x, y)
            count += 1
            
    print(count)