# 소수의 연속합
# 소수판별, 투포인터

import math

n = int(input())
array = [True for i in range(n+1)]

# 소수 찾기
for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i*j] = False
            j += 1

data = []
for i in range(2, len(array)):
    if array[i] == True:
        data.append(i)

# print(data)

# 투 포인터
end = 0
cum_sum = 0
count = 0

for i in range(len(data)):
    # print(i, end, cum_sum)
    while cum_sum < n:
        if end >= len(data): break
        cum_sum += data[end]
        end += 1
    if cum_sum == n:
        count += 1
    cum_sum -= data[i]

print(count)