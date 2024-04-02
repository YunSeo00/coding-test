# 11055, dp, silver 2, 가장 큰 증가하는 부분 수열

# N = int(input())
# data = list(map(int, input().split()))

# dp = [0] * N

# dp[N-1] = data[N-1]

# for i in range(N-1,-1,-1):
#     tmp = 0
#     for j in range(i+1,N):
#         if data[i] < data[j] and tmp < dp[j]:
#             tmp = dp[j]
#     dp[i] = tmp + data[i]

# print(max(dp))


# 수정 -> b_14003 확인
n = int(input())
numbers = list(map(int, input().split()))

dp = [0] * n

for i in range(n):
    dp[i] = 1
    for j in range(i):
        if numbers[j] < numbers[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
        