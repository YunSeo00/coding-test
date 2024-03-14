# 숫자 카드 게임

n, m = map(int, input().split())

result = 0
for _ in range(n):
    data = list(map(int, input().split()))
    local_min = min(data)
    result = max(result, local_min)
    
print(result)