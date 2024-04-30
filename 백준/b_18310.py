# 안테나 - 중간값이 정답이다.

n = int(input())
house = list(map(int, input().split()))
house.sort()

print(house[(n-1)//2])