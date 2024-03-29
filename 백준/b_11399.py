# ATM

n = int(input())
times = list(map(int, input().split()))

times.sort()

tmp_t = 0
result = 0
for t in times:
    tmp_t += t
    result += tmp_t

print(result)