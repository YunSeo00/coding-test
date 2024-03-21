# 공유기 설치
# 접근: 가장 멀리 떨어진 거리를 이분 탐색으로 찾기. 최소 mid 만큼 떨어지게 공유기를 설치하고 만약 설치할 수 없다면, 다음 값을 탐색.
# todo: 코드 좀 더 이쁘게 짜보기
import sys

n, c = map(int, sys.stdin.readline().split())
array = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
array.sort()
diff = [array[i+1] - array[i] for i in range(n - 1)]

start = 1
end = array[-1] - array[0]
while start <= end:
    mid = (start + end) // 2
    time = 0
    num = 1
    for _ in range(c-1):
        length = 0
        if time == n - 1: break
        while True:
            length += diff[time]
            time += 1
            if time == n-1 or length >= mid:
                if length >= mid: num += 1
                break
    if num < c:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
        
print(result)