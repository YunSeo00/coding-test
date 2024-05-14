# 숫자 카드2

import sys
input = sys.stdin.readline
n = int(input())
number_list = list(map(int, input().split()))

m = int(input())
find_list = list(map(int, input().split()))


# 이분 탐색 이용 방법
n_dic = {}
num_list = []
for n in number_list:
    if n in n_dic:
        n_dic[n] += 1
    else:
        num_list.append(n)
        n_dic[n] = 1
num_list.sort()

def binary(m, num_list, start, end):
    if start > end:
        return 0 
    mid = (start + end)//2
    if m == num_list[mid]:
        return n_dic[m]
    elif m < num_list[mid]:
        return binary(m, num_list, start, mid-1)
    else:
        return binary(m, num_list, mid+1, end)

for m in find_list:
    print(binary(m, num_list, 0, len(num_list)-1), end = ' ')
    
print()
# dictionary 자료형 이용
for m in find_list:
    if m in n_dic:
        print(n_dic[m], end = ' ')
    else:
        print(0, end = ' ')