# 모험가 길드

N = int(input())
data = list(map(int, input().split()))

data.sort()

group = []
result = 0

for i in data:
    group.append(i)
    if len(group) >= i: # 그룹의 길이가 새로 들어온 사람보다 크면 (이미 data를 정렬했기에 max(group)과 같은 결과를 냄.)
        result += 1
        group = []
        
print(result)
