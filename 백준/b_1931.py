# 회의실 배정
# 접근: 끝나는 시간이 가장 빠른 회의부터 배정하기

import heapq

n = int(input())
q = []
for _ in range(n):
    s, e = map(int, input().split())
    heapq.heappush(q, (e,s))

# print(q)

present = 0
count = 0 
while q:
    end, start = heapq.heappop(q)
    if present <= start:
        # print(start, end)
        present = end
        count += 1

print(count)