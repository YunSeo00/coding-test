# 01타일
# d_n = d_{n-2} + d_{n-1} = (00을 붙이는 경우) + (1을 붙이는 경우)

n = int(input())
dp = [0] * max(3, (n+1))
dp[1] = 1
dp[2] = 2

for k in range(3, n+1):
    dp[k] = (dp[k-1] + dp[k-2])%15746 # 반복문 안에서 나머지 연산을 해주어야 메모리 초과가 나지 x

print(dp[n])