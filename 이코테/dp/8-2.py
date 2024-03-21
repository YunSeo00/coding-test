# 1로 만들기

x = int(input())

d = [0] * (x+1)
d[2] = 1
d[3] = 1
d[5] = 1

for i in range(2, x+1):
    minimum = 30001
    if d[i] != 0:
        pass
    if i % 5 == 0:
        minimum = min(d[int(i/5)] + 1, minimum)
    if i % 3 == 0:
        minimum = min(d[int(i/3)] + 1, minimum)
    if i % 2 == 0:
        minimum = min(d[int(i/2)] + 1, minimum)
    minimum = min(d[int(i-1)] + 1, minimum)
    d[i] = minimum

print(d)
print(d[x])
