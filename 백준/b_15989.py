# 1,2,3 더하기 4 (dp)
# b_2293과 비슷함.

# 접근1. 2293과 동일한 풀이 (시간초과)
# t= int(input())
# nums = [1, 2, 3]

# for _ in range(t):
#     n = int(input())
#     dp = [0] * (n+1)
#     dp[0] = 1

#     for num in nums:
#         for i in range(num, n+1):
#             dp[i] = dp[i] + dp[i-num]
    
#     print(dp[n])

# 접근2.
# 계산해서 수식을 구했어야 함. (https://www.acmicpc.net/board/view/69734)
t = int(input())
ns = [int(input()) for _ in range(t)]

for n in ns:
    print(int((n * (n+6) + 12) / 12))