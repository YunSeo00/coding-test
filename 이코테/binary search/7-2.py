# 부품 찾기

# 이진 탐색
def binary_search(target):
    start = 0
    end = len(store) - 1
    while start <= end:
        mid = (start + end) // 2
        if store[mid] == target:
            print('yes', end = ' ')
            return
        elif store[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    print('no', end = ' ')

n = int(input())
store = list(map(int, input().split()))
m = int(input())
need = list(map(int, input().split()))

store.sort()
for i in need:
    binary_search(i)

# 계수 정렬
n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
        
# 집합 자료형
n = int(input())
array = set(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')