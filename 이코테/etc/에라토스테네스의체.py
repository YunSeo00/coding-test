# 에라토스테네스의 체
# 후보가 여러 개가 있을 때, 그 중에서 소수들을 찾는 방법
# 후보군 중 가장 작은 수부터 돌아가면서, 배수인 수는 삭제하고, 소수이면 소수 리스트에 넣는다.

import math

n = 1000 # 2부터 1000까지의 모든 수에 대하여 소수 판별
array = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i*j] = False
            j += 1

for i in range(2, n+1):
    if array[i]:
        print(i, end = ' ')