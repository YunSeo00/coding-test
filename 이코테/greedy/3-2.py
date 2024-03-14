# 큰 수의 법칙

N, M, K = map(int, input().split())
int_list = list(map(int, input().split()))

# 1차 풀이
int_list.sort(reverse=True)
result = int_list[0] * (K * (M // K) + (M % K - M//K)) + int_list[1] * (M // K)
print(result)

# 답안
int_list.sort(reverse=True)
count = int(M / (K + 1)) * K + M % (K + 1)
result = int_list[0] * count + int_list[1] * (M - count)
print(result)