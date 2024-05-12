# LCS

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
        if lcs_matrix[i+1][j+1] > result:
            result = lcs_matrix[i+1][j+1]

print(result)