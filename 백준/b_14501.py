# 퇴사

n = int(input())
time = [[]] + [list(map(int, input().split())) for _ in range(n)] # Time, Value

dp = [0] * (n+1)

for i in reversed(range(1, n+1)):
    if i + time[i][0] - 1 > n:
        dp[i] = max(dp)
        continue
    elif i + time[i][0] - 1 == n:
        dp[i] = time[i][1]
        dp[i] = max(dp)
    else:
        value = time[i][1] + dp[i+time[i][0]]
        for t in range(1, time[i][0]):
            if i + t <= n:
                value = max(value, dp[i + t])
        dp[i] = value

print(dp[1])