# 구간 합 구하기 5
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

# 각 칸 별로 누적합 구하기
cum_matrix = [[0]*(n+1) for _ in range(n+1)]
pre_cum_row_sum = [0] * (n+1)
for i in range(1, n+1):
    cum_sum = 0 
    for j in range(1, n+1):
        cum_matrix[i][j] = pre_cum_row_sum[j]
        cum_sum += matrix[i-1][j-1]
        pre_cum_row_sum[j] += cum_sum
        cum_matrix[i][j] += cum_sum

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(cum_matrix[x2][y2] - cum_matrix[x1-1][y2] - cum_matrix[x2][y1-1] + cum_matrix[x1-1][y1-1])