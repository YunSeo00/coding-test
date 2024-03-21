# 동전 1


# 접근1 (시간초과)
# 가지고 있는 코인별로 list를 관리

# ex) coin : 1, 2, 5
#    i     1 2 3 4 5 6 7 8 9 10
# a_{1,i}  1 1 2 2 3 4 5 6 7 8
# a_{2,i}  0 1 0 1 0 1 1 1 1 1
# a_{5,i}  0 0 0 0 1 0 0 0 0 1
# 
# a_{j, i} = \sum_{m > j} a_{m, i-j}

# import sys

# n, k = map(int, sys.stdin.readline().split())
# coins = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
# coins.sort()

# d = {coin : [0] * (k+1) for coin in coins}

# for i in range(1, k+1):
#     if i in coins:
#         d[i][i] = 1
#     for j in range(len(coins)):
#         if i > coins[j]:
#             for m in range(j, len(coins)):
#                 d[coins[j]][i] += d[coins[m]][i-coins[j]]
# result = 0
# for coin in coins:
#     result += d[coin][k]

# print(result)

# 접근2
# 위의 코드를 더 효율적으로 만들기 (1개의 리스트로도 구현 가능함.)
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [0] * (k+1)
dp[0] = 1  # 금액 0을 만드는 방법은 아무것도 선택하지 않는 것 1가지

for coin in coins:
    for i in range(coin, k+1):
        if i >= coin:
            dp[i] += dp[i-coin]

print(dp[k])

