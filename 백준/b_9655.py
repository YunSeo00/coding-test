# 돌게임
# 해석 : 완벽하게 게임을 함 -> 돌을 남기지 않음. 최소 횟수로 가져감.

n = int(input())

d = [0] * (n+1)
d[1] = 1

for i in range(1, n+1):
    if i == 2: 
        d[2] = 2; continue
    if i == 3: 
        d[3] = 1; continue
    minimum = n
    if d[i-1] != 0: minimum = min(minimum, d[i-1]+1)
    if d[i-3] != 0: minimum = min(minimum, d[i-3]+1)
    d[i] = minimum

if d[i] % 2 == 1:
    print('SK')
else:
    print('CY')