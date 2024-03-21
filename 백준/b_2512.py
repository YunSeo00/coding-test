# 예산

n = int(input())
array = list(map(int, input().split()))
money = int(input())

start = 0
end = max(array)
while start <= end:
    mid = (start + end) // 2
    total = 0 
    for x in array:
        if x <= mid:
            total += x
        else:
            total += mid
    if total > money:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)