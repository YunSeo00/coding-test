# 단어정렬 (heap 사용)
import heapq

n = int(input())
q = []

for _ in range(n):
    word = input()
    heapq.heappush(q, (len(word), word))

tmp = ''
for _ in range(n):
    present = heapq.heappop(q)[1]
    if present == tmp:
        continue
    print(present)
    tmp = present