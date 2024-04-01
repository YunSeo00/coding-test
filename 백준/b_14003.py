# 가장 긴 증가하는 부분 수열 2, 3, 4, 5 - 이진탐색 - lis algorithm ***

# dp - O(n^2)
# n = int(input())
# numbers = list(map(int, input().split()))

# dp = [0] * n

# for i in range(n):
#     dp[i] = 1
#     for j in range(i):
#         if numbers[j] < numbers[i]:
#             dp[i] = max(dp[i], dp[j] + 1)

# print(max(dp))

# binary search - O(n log n)
# 반례
# 13
# 3 4 5 6 2 3 1 7 4 3 5 6 7

from bisect import bisect_left
import copy
n = int(input())
numbers = list(map(int, input().split()))
orders = [0] * len(numbers)
lis = [numbers[0]]
j = 0
i = 1
idx = -1
while i < n:
    if lis[j] < numbers[i]:
        lis.append(numbers[i])
        j += 1
        orders[i] = j
    else:
        idx = bisect_left(lis, numbers[i])       
        lis[idx] = numbers[i]
        orders[i] = idx
    i += 1

# 역추적 **
order = len(lis) - 1
lis = []
for i in reversed(range(len(numbers))):
    if order == orders[i]:
        lis.append(numbers[i])
        order -= 1
print(len(lis))
for i in reversed(lis):
    print(i, end = ' ')
