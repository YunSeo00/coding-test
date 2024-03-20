# 등수 매기기
# 접근1. 정렬 후 1부터 n까지 순위 주기 -> 시간 초과
# 접근2. 입력 받으면서 바로바로 순위 주기, 만약 본인이 입력한 값(expected)이 이미 선정되어 있다면 양 옆으로 동시에 한 칸씩 이동(bfs)하면서 적절한 순위 찾기

# 접근1 (시간 초과)
# n = int(input())
# expected = []
# for _ in range(n):
#     expected.append(int(input()))

# expected.sort()

# diff_value = [abs(a - b) for a, b in zip(expected, range(1,n+1))]

# result = sum(diff_value)
# print(result)

# 접근2 (시간 초과)
# n = int(input())

# counts = [0] * n
# queue = []
# result = 0
# for _ in range(n):
#     expected = int(input())
#     if counts[expected - 1] == 0:
#         counts[expected - 1] = 1
#     else:
#         i = 1
#         while True:
#             queue += [expected-i, expected+i]
#             value = queue.pop(0)
#             if value <= 1 or value > n: continue
#             if counts[value - 1] == 0:
#                 result += abs(value - expected)
#                 counts[value - 1] = 1
#                 break
#             i += 1

# print(result)

# 접근3
# 입력을 빠르게 받아야 함. (https://www.acmicpc.net/problem/15552)
import sys
n = int(sys.stdin.readline())
expected = [int(sys.stdin.readline()) for _ in range(n)]
expected.sort()

diff = [abs(a-b) for a, b in zip(expected, range(1, n+1))]

result = sum(diff)
print(result)