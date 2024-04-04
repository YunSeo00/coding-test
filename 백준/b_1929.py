# 소수구하기 ***
# 에라토스테네스의 체를 적용하면 불필요한 탐색을 줄일 수 있음.

import math

def is_prime_num(n):
    if n == 1: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

m, n = map(int, input().split())

for i in range(m, n+1):
    if is_prime_num(i):
        print(i)