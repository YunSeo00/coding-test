# 나는야 포켓몬 마스터 이다솜
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

num_dict = {}
name_dict = {}
for i in range(1, n+1):
    name = input().rstrip()
    num_dict[i] = name
    name_dict[name] = i

for _ in range(m):
    quest = input().rstrip()
    if quest in name_dict.keys():
        print(name_dict[quest])
    else:
        print(num_dict[int(quest)])