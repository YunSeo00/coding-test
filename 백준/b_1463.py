# 1로 만들기

x = int(input())

d = [0] * (x+1)
for i in range(1, x+1):
    if i == 1: continue
    if i == 2: d[2] = 1
    if i == 3: d[3] = 1
    if d[i] != 0:
        continue
    minimum = d[i-1] + 1
    if i % 2 == 0:
        minimum = min(minimum, d[int(i/2)] + 1)
    if i % 3 == 0:
        minimum = min(minimum, d[int(i/3)] + 1)
    d[i] = minimum
    
print(d[x])