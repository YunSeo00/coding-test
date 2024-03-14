# 1이 될 때까지

N, K = map(int, input().split())

# 1차 답안
result = 0
while True:
    if N % K == 0:
        N = N / K
        result += 1
    else:
        N -= 1
        result += 1
    if N == 1:
        break
    
print(result)

# 답안 (좀 더 효율적인 코드, 일일히 1을 빼지 않음.)
N, K = map(int, input().split())
result = 0
while True:
    result += N % K
    N = (N // K) * K
    if N < K:
        break
    N = N // K
    result += 1

result += N - 1
print(result)