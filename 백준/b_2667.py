# 단지번호붙이기

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(i, j):
    global num
    num += 1
    for a in range(4):
        nx = i + dx[a]
        ny = j + dy[a]
        if nx >= 0 and nx < n and ny >= 0 and ny < n and visited[nx][ny] == 0 and graph[nx][ny] == 1:
            visited[nx][ny] = 1
            dfs(nx, ny)
            
count = 0
nums = []
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and graph[i][j] == 1:
            num = 0
            count +=1
            visited[i][j] = 1
            dfs(i, j)
            nums.append(num)

print(count)
nums.sort()
for i in nums:
    print(i)
