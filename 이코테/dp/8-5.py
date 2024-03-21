# 효율적인 화폐 구성
import sys

n, m = map(int, sys.stdin.readline().split())
array = [int(sys.stdin.readline().strip()) for _ in range(n)]

d = [0] * (m+1)

for i in range(min(array), m+1):
    if i in array: d[i] = 1
    minimum = 10001
    for j in array:
        if d[i - j] != 0: minimum = min(d[i-j] + 1, minimum)
    if minimum == 10001: d[i] = 0
    else: d[i] = minimum

if d[m] == 0:
    print(-1)
else:
    print(d[m])