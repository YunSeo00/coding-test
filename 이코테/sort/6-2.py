# 위에서 아래로

n = int(input())
numbers = [int(input()) for _ in range(n)]
numbers.sort(reverse=True)
print(*numbers)