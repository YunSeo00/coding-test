# 팀 결성

n, m = map(int, input().split())

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        print(x, parent[x])
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

for _ in range(m):
    c, a, b = map(int, input().split())
    a = find_parent(parent, a)
    b = find_parent(parent, b) 
    if c == 0: # union
        if a > b:
            parent[a] = b
        else:
            parent[b] = a
    else: # find
        if a == b:
            print('YES')
        else:
            print('NO')


# 입력
# 7 8 
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1