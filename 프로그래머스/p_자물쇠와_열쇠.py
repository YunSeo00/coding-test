# 자물쇠와 열쇠

# 내 답변
# 풀이 과정
# 1. 열쇠 크기에 맞게 padding이 추가된 자물쇠 배열을 생성 (new_lock)
# 2. 채워야 할 부분이 포함되도록 fitter가 적용될 위치의 범위 계산 (row_s, row_e, col_s, col_e)
#    - 만약 채워야 할 0의 간격이 key의 크기를 넘어간다면 False 반환
# 3. key를 회전시키면서 뒤에서 저장한 filter에 맞추기

import copy

def isok(new_lock, n, m): # 자물쇠가 열리는 지 조건 검사
    total = 0
    for i in range(m-1, m+n-1):
        total += sum(new_lock[i][m-1:m+n-1])
    if total == n*n:
        return True
    else:
        return False
    return total

def find_range(new_lock, n, m): # filter를 적용할 범위 찾기
    min_row = n + (m-1)*2
    max_row = 0
    min_col = n + (m-1)*2
    max_col = 0
    
    for i in range(m-1, m+n-1):
        for j in range(m-1, m+n-1):
            if new_lock[i][j] == 0:
                min_row = min(min_row, i)
                max_row = max(max_row, i)
                min_col = min(min_col, j)
                max_col = max(max_col, j)
    return max_row, min_row, max_col, min_col

def turn_key(key, m):
    tmp_key = [[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            tmp_key[i][j] = key[j][m-1-i]
    return tmp_key
        
    
def solution(key, lock):
    answer = True
    m = len(key)
    n = len(lock)
    new_lock = [[0]*(n+2*m-2) for _ in range(m-1)] + [[0]*(m-1) + lock[i] + [0]*(m-1) for i in range(n)] +  [[0]*(n+2*m-2) for _ in range(m-1)] # add padding
    row_s, row_e, col_s, col_e = find_range(new_lock, n, m)
    # 만약 0의 간격이 key의 크기를 넘는다면 False 반환
    if (row_s - row_e) >= m or (col_s - col_e) >= m:
        return False
    # key를 90도씩 회전시키면서 검사 진행
    row_s -= m-1
    col_s -= m-1
    for k in range(4):
        key = turn_key(key, m)
        for i in range(row_s, row_e+1):
            for j in range(col_s, col_e+1):
                tmp_lock = copy.deepcopy(new_lock)
                for a in range(m):
                    for b in range(m):
                        tmp_lock[i+a][j+b] =  int(new_lock[i+a][j+b] != key[a][b])
                if isok(tmp_lock, n, m):
                    return True
    return False

# todo : 다른 사람 풀이 분석