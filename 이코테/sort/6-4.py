# 두 배열의 원소 교체

n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)
print(sum(B[:k]) + sum(A[k:]))

