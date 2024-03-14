# 2023, search, backtracking, 신기한 소수
import math

N = int(input())

# 소수 판별 함수
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

new_prime = []

stack = []

def backtracking(stack:list, N:int):
    for i in range(1,10):
        stack.append(str(i))
        if is_prime_number(int(''.join(stack))):
            if len(stack) == N:
                new_prime.append(int(''.join(stack)))
                stack.pop()
            else: stack = backtracking(stack, N)
        else: stack.pop()
    stack.pop()
    return stack


for j in range(2, 10):
    stack.append(str(j))
    if is_prime_number(int(''.join(stack))):
        if len(stack) == N:
            new_prime.append(int(''.join(stack)))
            stack.pop()
        else: stack = backtracking(stack, N)
    else: stack.pop()

for prime in sorted(new_prime):
    print(prime)