# 공통 부분 문자열

# 1. 원시적인 풀이
# string_a = input()
# string_b = input()

# common_string = ''
# common_string_list = ['']

# for i in range(len(string_a)):
#     k = 0
#     for j in range(len(string_b)):
#         if i+k >= len(string_a):
#             break
#         if string_a[i+k] == string_b[j]:
#             common_string += string_b[j]
#         else:
#             if common_string != '':
#                 common_string_list.append(common_string)
#                 common_string = ''
#         k+=1
#     if common_string != '':
#         common_string_list.append(common_string)
#         common_string = ''

# print(common_string_list)
# list_length = [len(string) for string in common_string_list]
# print(max(list_length))

# 2. LCS 알고리즘
import sys
inpuy = sys.stdin.readline

string_a = input()
string_b = input()

m = len(string_a)
n = len(string_b)

LCS_matrix = [[0]*(n+1) for _ in range(m+1)]
result = 0

for i in range(m):
    for j in range(n):
        if string_a[i] == string_b[j]:
            LCS_matrix[i+1][j+1] = LCS_matrix[i][j] + 1
        if LCS_matrix[i+1][j+1] > result:
            result = LCS_matrix[i+1][j+1]

print(result)

