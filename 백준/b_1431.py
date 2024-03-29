# 시리얼 번호

import heapq
import string

alphabet = [i for i in string.ascii_uppercase]
n = int(input())
q = []

for _ in range(n):
    text = input()
    length = len(text)
    total = 0
    for i in text:
        if not i in alphabet:
            total += int(i)
    heapq.heappush(q, (length, total, text))

for _ in range(n):
    print(heapq.heappop(q)[2])