# 랜선 자르기 - 이진 탐색

import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan = []

for _ in range(k):
    lan.append(int(input()))

start = 1
end = max(lan)

result = 1

def lan_number(length):
    count = 0
    for l in lan:
        count += l // length
    return count

while start <= end:
    median = (start + end) // 2
    count = lan_number(median)
    # print(start, end, median, count, result)
    if count >= n:
        result = median
        start = median + 1
    else:
        end = median - 1

print(result)