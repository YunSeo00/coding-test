# 암호 만들기

l, c = map(int, input().split())
alphabet = list(map(str, input().split()))

# 조합
import itertools
import heapq

result = []
for x in itertools.combinations(alphabet, l):
    num = 0 # 모음의 수 
    data = list(x)
    for i in ['a', 'e', 'i', 'o', 'u']:
        if i in data:
            num +=1
    if num >= 1 and l - num >= 2:
        data.sort()
        heapq.heappush(result, ''.join(data))

while result:
    print(heapq.heappop(result))

# 이코테 답안

from itertools import combinations

vowels = ('a', 'e', 'i', 'o', 'u')
l, c = map(int, input().split(' '))

array = input().split(' ')
array.sort()

for password in combinations(array, l):
    count = 0
    for i in password:
        if i in vowels:
            count += 1
    if count >= 1 and count <= 1 - 2:
        print(''.join(password))