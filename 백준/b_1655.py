# 가운데를 말해요

import heapq
import sys

input = sys.stdin.readline

n = int(input())
max_heap = []
min_heap = []
mid_num = []

for _ in range(n):
    num = int(input())
    
    if len(max_heap) == len(min_heap):
            heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)
    
    if len(min_heap) > 0 and -max_heap[0] > min_heap[0]:
        a = -heapq.heappop(max_heap)
        b = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -b)
        heapq.heappush(min_heap, a)
    print(-max_heap[0])
