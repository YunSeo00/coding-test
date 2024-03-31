# 1, 2, 3 더하기

n = int(input())

numbers = []

for _ in range(n):
    numbers.append(int(input()))

dp = [0] * (max(numbers) + 1)

for i in range(max(numbers) + 1):
    if i == 0:
        pass
    elif i == 1:
        dp[i] = 1
    elif i == 2:
        dp[2] = 2
    elif i == 3:
        dp[3] = 4
    else:
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for n in numbers:
    print(dp[n])