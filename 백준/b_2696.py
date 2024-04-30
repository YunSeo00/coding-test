# 중앙값 구하기
import sys
input = sys.stdin.readline

# # 시간 초과
# t = int(input())

# for _ in range(t):
#     n = int(input())
#     numbers = []
#     while len(numbers) < n:
#         numbers.extend(list(map(int, input().split())))
#     count = 0
#     mid_num = []
#     for i in range(n):
#         tmp = numbers[:i+1]
#         tmp.sort()
#         if i % 2 == 0:
#             count += 1
#             mid_num.append(tmp[i//2])
#     print(count)
#     k = 0
#     while k < len(mid_num):
#         if k > 1 and k % 10 == 0:
#             print()
#         print(mid_num[k], end = ' ')
#         k += 1
#     print()

# utils
def read_data():
    n = int(input())
    numbers = []
    while len(numbers) < n:
        numbers.extend(list(map(int, input().split())))
    return n, numbers

def print_results(count, mid_num):
    print(count)
    k = 0
    while k < len(mid_num):
        if k > 1 and k % 10 == 0:
            print()
        print(mid_num[k], end = ' ')
        k += 1
    print()

# 삽입 정렬
# t = int(input())

# for _ in range(t):
    
#     n, numbers = read_data()
    
#     # initial
#     sort_numbers = [numbers[0]] 
#     mid_num = [numbers[0]]
#     count = 1
    
#     for i in range(1, n):
#         # insertion sort - 삽입 정렬
#         j = i-1
#         if sort_numbers[j] <= numbers[i]:
#             sort_numbers.append(numbers[i])
#         else:
#             j -= 1
#             while j >= 0:
#                 if sort_numbers[j] <= numbers[i]:
#                     break
#                 j -= 1
#             sort_numbers.insert(j+1, numbers[i])
#         if i % 2 == 0:
#             count += 1
#             mid_num.append(sort_numbers[i//2])
            
#     print_results(count, mid_num)
    

# heap 이용
import heapq

t = int(input())


for _ in range(t):
    count = 0
    mid_num = []
    max_heap = []
    min_heap = []
    
    n, numbers = read_data()
    
    i = 0
    for num in numbers:
        if len(max_heap) == len(min_heap):
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)
        
        if len(min_heap) > 0 and -max_heap[0] > min_heap[0]:
            a = -heapq.heappop(max_heap)
            b = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -b)
            heapq.heappush(min_heap, a)
        if i % 2 == 0:
            count += 1
            mid_num.append(-max_heap[0])
        i+=1
            
    print_results(count, mid_num)