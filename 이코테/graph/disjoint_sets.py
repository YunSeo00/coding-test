# 서로소 집합 이론

# 입력
# 6 4
# 1 4
# 2 3
# 2 4
# 5 6

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x]) # 루트 노드를 찾을 때까지 재귀적으로 호출
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드와 간선(union 연산)의 수 입력받기
v, e = map(int, input().split())
parent = [0] * (v+1)

# 부모 테이블에서 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i
    
# union 연산 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end = '')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')
    
print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')

print()

# 경로 압축 (find 연산 수정)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end = '')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')
    
print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')

print()

# 서로소 집합을 활용한 사이클 판별 (무향 그래프)
# 위에 작성한 find(경로 압축 버전)와 union 연산을 그대로 이용

# 입력
# 3 3
# 1 2
# 1 3
# 2 3

# 노드와 간선 입력
v, e = map(int, input().split())

# 정보 초기화 : 부모 테이블
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i
    
cycle = False

for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)
        
if cycle:
    print('사이클이 발생했습니다.')
else:
    print('사이클이 발생하지 않았습니다.')
    