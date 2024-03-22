# 왕실의 나이트

col = ['a','b','c','d','e','f','g','h']
# print(col.index('a') + 1)

dx = [-1, 1, -1, 1, -2, 2, -2, 2]
dy = [2, 2, -2, -2, 1, 1, -1, -1]

data = input()
y = int(col.index(data[0]) + 1)
x = int(data[1])

count = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
        count += 1

print(count)