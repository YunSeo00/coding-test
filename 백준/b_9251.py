# LCS
# (수정): 연속된 수열을 찾는 것이 아닌 부분 수열을 찾는 것이기 때문에 이전의 matrix에서 max값을 가져옴.

a_text = input()
b_text = input()

m = len(a_text)
n = len(b_text)

lcs_matrix = [[0]*(n+1) for _ in range(m+1)]
result = 0

for i in range(m):
    for j in range(n):
        if a_text[i] == b_text[j]:
            lcs_matrix[i+1][j+1] = lcs_matrix[i][j] + 1
        else:
            lcs_matrix[i+1][j+1] = max(lcs_matrix[i+1][j], lcs_matrix[i][j+1])

print(lcs_matrix[m][n])