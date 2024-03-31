# 듣보잡

import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())

no_hear = set()
for _ in range(n):
    no_hear.add(input().rstrip())

no_hear_see = []
for _ in range(m):
    data = input().rstrip()
    if data in no_hear:
        heapq.heappush(no_hear_see, data)

print(len(no_hear_see))
for _ in range(len(no_hear_see)):
    print(heapq.heappop(no_hear_see))