# 문자열 재정렬
import heapq
import string

text = input()
alphabet = [i for i in string.ascii_uppercase]

q = []
total = 0
for i in text:
    if i in alphabet:
        heapq.heappush(q, i)
    else:
        total += int(i)

while q:
    print(heapq.heappop(q), end='')
print(total)        