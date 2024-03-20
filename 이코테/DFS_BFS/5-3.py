# 음료수 얼려 먹기
# DFS 문제, 

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

print(graph)

# 답안 참고함.
def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m: return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True # * 
    return False

count = 0

# 이중 for 문을 사용해서 시작점 찾음.
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True: # * 
            count += 1
            
print(count)
