# 수들의 합

n = int(input())
tmp = 0

while n > tmp:
    tmp += 1
    n = n - tmp
    
print(tmp)