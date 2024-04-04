# 피보나치 수 6

# 0. 기존의 방법 (시간 초과)
# n = int(input())
# prenum = 0
# num = 1
# for i in range(n-1):
#     prenum, num = num, prenum + num

# print(num % 1000000007)

# 1. 행렬 곱셈을 활용한 풀이 (시간초과) - todo
# n = int(input())

# def fibo(n):
#     size = 2
#     base_matrix = [[1, 1], [1, 0]]
    
#     def square_matrix_mul(a, b, size=size):
#         new = [[0 for _ in range(size)] for _ in range(size)]
#         new[0][0] = a[0][0] * b[0][0] + a[0][0] * b[1][0]
#         new[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1]
#         new[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
#         new[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1]      
#         return new
    
#     def get_nth(n): # 분할 정복
#         if n == 0:
#             return [[0, 0], [0, 0]]
#         if n == 1:
#             return base_matrix
        
#         half = get_nth(n//2)
#         square = square_matrix_mul(half, half)
#         if n % 2:
#             return square_matrix_mul(square, base_matrix)
#         else:
#             return square

#     return get_nth(n)[1][0]

# print(fibo(n) % 1000000007)


# 2. 도가뉴 항등식
# f_2n = f_n (f_n + 2 f_n-1)
# f_2n+1 = f_n^2 + f_n+1^2
from collections import defaultdict

n = int(input())
dp = defaultdict(int)

dp[0] = 0
dp[1] = 1
dp[2] = 1

def fibonacci(n):
    if not dp[n]:
        if n & 1: # 홀수면
            fn = fibonacci(n//2)
            fn_p1 = fibonacci(n//2 + 1)
            
            dp[n] = (fn ** 2 + fn_p1 ** 2) % 1000000007
        else:
            fn = fibonacci(n//2)
            fn_m1 = fibonacci(n//2 - 1)
            
            dp[n] = (fn * (fn + 2 * fn_m1)) % 1000000007
    return dp[n]

print(fibonacci(n))