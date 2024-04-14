# 강의실 배정
# 강의실을 적게 사용하려면 시작시간과 종료시간 간격이 짧아야되서 시작시간을 기준으로 오름차순 해야함.
# ??? 왜 틀리지 (todo: 고치기)

from bisect import bisect_left
import heapq

n = int(input())
rooms = [0]
q = []
for _ in range(n):
    s, t = map(int, input().split())
    heapq.heappush(q, (s, t))

while q:
    s, t = heapq.heappop(q)
    if min(rooms) <= s:
        idx = bisect_left(rooms, s)
        rooms[idx-1] = t
    else:
        rooms.append(t)

print(len(rooms))