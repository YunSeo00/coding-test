# 뱀
# 접근: 뱀의 몸을 머리부터 1씩 감소하는 값으로 표현하고 이를 heap으로 관리
#       - 뱀의 머리는 항상 n*n이 됨.
#       - 뱀의 꼬리를 삭제해야 하는 경우 가장 작은 값을 가지는 칸을 0으로 만들 수 있음.

import heapq

n = int(input())
k = int(input())
apple = [[0]*n for _ in range(n)] # 사과의 위치
array = [[0]*n for _ in range(n)] # 뱀이 차지하는 영역
q = [] # 뱀의 몸
array[0][0] = 1
heapq.heappush(q, [n*n, [0,0]])

for _ in range(k):
    a, b = map(int, input().split())
    apple[a-1][b-1] = 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

i = 0 # 방향 (우회전: +1, 좌회전: -1)
count = 0 # 시간초
death = False # 생존 여부
x = 0; y = 0; # 머리의 위치
length = 1 # 뱀의 길이

l = int(input())
turn_info = {}
for _ in range(l):
    time, c = input().split()
    turn_info[int(time)] = c

while True:
    count += 1
    nx = x + dx[i]
    ny = y + dy[i]
    
    # 범위를 넘어가는지 확인
    if nx >= n or nx < 0 or ny >= n or ny < 0:
        death = True
        # print('넘어감')
        break
    
    # 몸에 부딪혔는지 확인 (꼬리가 이동하기 전에 검사해주어야 함.)
    if array[nx][ny] == 1:
        death = True
        # print('몸에 부딪힘')
        break
    
    q = [[q[i][0] - 1, q[i][1]] for i in range(len(q))]
    # 꼬리를 유지할 건지 말건지 확인
    if apple[nx][ny] == 1:
        length += 1
        apple[nx][ny] = 0
    else:
        tail_x, tail_y = heapq.heappop(q)[1]
        array[tail_x][tail_y] = 0
    
    x=nx; y=ny
    array[x][y] = 1
    heapq.heappush(q, [n*n, [x,y]])
    # print(f'count: {count}, q: {q}')
    
    # 방향 전환
    if len(turn_info.keys()) == 0: 
        continue
    if count in turn_info.keys():
        c = turn_info[count]
        if c == 'D':
            i += 1
            if i == 4: i = 0
        elif c == 'L':
            i -= 1
            if i == -1: i = 3

print(count)