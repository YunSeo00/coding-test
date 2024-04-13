# 수들의 합2 - 투포인터

n, m = map(int, input().split())
data = list(map(int, input().split()))

cum_sum = 0
end = 0
count = 0

for i in range(n): # start index
    while cum_sum < m:
        if end >= n: break
        cum_sum += data[end]
        end += 1
    
    if cum_sum == m:
        count += 1
    cum_sum -= data[i]

print(count)