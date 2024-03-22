# 상하좌우

N = int(input())
steps = list(input().split())

# 풀이
step_rule = {'R':[0, 1], 'L':[0,-1], 'U':[-1,0], 'D':[1, 0]}

result = [1,1]
tmp = result
for step in steps:
    tmp = [x + y for x, y in zip(result, step_rule[step])]
    if (tmp[0] == 0) | (tmp[0] == N+1) | (tmp[1] == 0) | (tmp[1] == N+1):
        continue
    result = tmp

print(result[0], result[1])

# 교재 답안
x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for step in steps:
    for i in range(len(move_types)):
        if step == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > N or nx > N:
        continue
    x, y = nx, ny

print(x, y)