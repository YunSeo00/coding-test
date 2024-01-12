# 11055, dp, silver 2, 가장 큰 증가하는 부분 수열

N = int(input())
data = list(map(int, input().split()))

dp = [0] * N

dp[N-1] = data[N-1]

for i in range(N-1,-1,-1):
    tmp = 0
    for j in range(i+1,N):
        if data[i] < data[j] and tmp < dp[j]:
            tmp = dp[j]
    dp[i] = tmp + data[i]

print(max(dp))

        