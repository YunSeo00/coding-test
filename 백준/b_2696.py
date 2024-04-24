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


# 삽입 정렬
t = int(input())

for _ in range(t):
    # input
    n = int(input())
    numbers = []
    while len(numbers) < n:
        numbers.extend(list(map(int, input().split())))
    
    # initial
    sort_numbers = [numbers[0]] 
    mid_num = [numbers[0]]
    count = 1
    
    for i in range(1, n):
        # insertion sort - 삽입 정렬
        j = i-1
        if sort_numbers[j] <= numbers[i]:
            sort_numbers.append(numbers[i])
        else:
            j -= 1
            while j >= 0:
                if sort_numbers[j] <= numbers[i]:
                    break
                j -= 1
            sort_numbers.insert(j+1, numbers[i])
        if i % 2 == 0:
            count += 1
            mid_num.append(sort_numbers[i//2])
            
    # print
    print(count)
    k = 0
    while k < len(mid_num):
        if k > 1 and k % 10 == 0:
            print()
        print(mid_num[k], end = ' ')
        k += 1
    print()