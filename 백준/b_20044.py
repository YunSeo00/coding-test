# Project Teams
# 접근: 나열 후 i, -i-1 사람끼리 팀으로 합침.

n = int(input())
value = list(map(int, input().split()))

value.sort()

teams = [value[i] + value[-i-1] for i in range(n) ]
print(min(teams))