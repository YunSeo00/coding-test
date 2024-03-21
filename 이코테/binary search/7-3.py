# 떡볶이 떡 만들기

n, m = map(int, input().split())
x = list(map(int, input().split()))

start = 0
end = max(x)

# 풀이 : 아래의 경우 딱 나눠떨어지지 않을 때 오류가 날 수 있음.
def isok(mid):
    length = 0
    for i in x:
        if i > mid:
            length += i - mid
    return length

while start <= end:
    mid = (start + end) // 2
    if isok(mid) == m:
        break
    elif isok(mid) < m:
        end = mid - 1
    else:
        start = mid + 1
print(mid)

# 교재 정답
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in x:
        if i > mid:
            total += i - mid
    if total < m:
        end = mid - 1
    else:
        result = mid # * total >= m 일 때 한 번 저장해준다.
        start = mid + 1
        
print(result)