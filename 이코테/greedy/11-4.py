# 만들 수 없는 금액
# 주요 아이디어
# 1. 코인을 크기 순으로 정렬했을 때, 현재의 값과 현재의 값 + 현재 코인의 값 사이의 값은 이전의 조합들과 현재 코인의 값으로 표현할 수 있음.
# 2. 위의 사실을 이용하여, target과 coin의 값을 비교하여 for 문을 종료시키고, target값을 변경하면 됨.

N = int(input())
coins = map(int, input().split())

coins.sort()

target = 1

for coin in coins:
    if target < coin:
        break
    target += coin

print(target)