# 동전 0 - 그리디
# 문제 포인트: 동전이 배수의 형태로 주어짐

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

count = 0
for c in reversed(coins):
    count += k//c
    k -= k//c * c
    if k == 0:
        break
print(count)