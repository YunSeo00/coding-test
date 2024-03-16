# 만들 수 없는 금액
# 

N = int(input())
coins = map(int, input().split())

coins.sort()

target = 1

# [1,1,2,3,9]
for coin in coins:
    if target < coin:
        break
    target += coin

print(target)