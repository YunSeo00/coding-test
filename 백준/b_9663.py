# N-Queen
# 접근1 : 2차원 배열을 이용하여 시도

# 백트래킹 ***
# 1. 조건 함수 생성: 현재 탐색이 조건에 맞는 지 확인할 수 있는 함수/조건 코드 작성
# 2. if 조건 만족 => 계속 탐색 
#    else 조건 만족 X => 다음 이어서 탐색
# 3. 종료 조건 적절히 배치

n = int(input())
row = [0] * n
cnt = 0

def isok(x):
    for i in range(x):
        # 같은 행에 퀸이 있거나 대각선에 퀸이 있음.
        # 만약 대각선에 퀸이 있다면, 행과 열의 차이가 동일함.
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
            return False
    return True

def dfs(start):
    global cnt
    if start == n:
        cnt += 1
    else:
        for i in range(n):
            row[start] = i
            if isok(start):
                dfs(start + 1)
dfs(0)

print(cnt)
