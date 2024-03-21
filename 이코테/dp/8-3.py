# 개미 전사

n = int(input())
array = list(map(int, input().split()))

d = [0] * n
d[0] = array[0]
d[1] = array[1]

for i in range(2, n):
    d[i] = max(d[i-2], d[i-3]) + array[i]

print(max(d))

# 교재: max(d_{i-1}, d_{i-2} + array[i])
d = [0] * n
d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])
    
print(d[n-1])