# 색종이 만들기 - 분할 정복
import heapq

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

blue = 0
white = 0

q = [(0, 0, -n)]
# heapq.heapify(q)
while q:
    x, y, length = heapq.heappop(q)
    length = -length
    # print(x, y, length)
    total = sum([sum(array[row][y:y+length]) for row in range(x, x+length)])
    if total == length*length:
        blue += 1
    elif total == 0:
        white += 1
    else:
        heapq.heappush(q, (x, y, -length//2))
        heapq.heappush(q, (x, y+length//2, -length//2))
        heapq.heappush(q, (x+length//2, y, -length//2))
        heapq.heappush(q, (x+length//2, y+length//2, -length//2))

print(white)
print(blue)