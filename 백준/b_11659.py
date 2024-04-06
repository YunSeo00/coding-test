# 구간 합 구하기 4
# 누적 합 - 시간 초과
# 1차 시도: 단순히 sum()과 구간 인덱싱을 이용해서 구함 -> 시간 초과
#           - sum 계산 과정에서 O(n * (a-b))의 시간 복잡도가 생김
# 2차 시도: 누적합을 구한 list를 하나 만들고 두고, 이를 이용해서 구간 누적합을 계산.

# 참고 : 누적 합 알고리즘 (https://wikidocs.net/206294)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
cumulative_num = [0]

for i in range(n):
    cumulative_num.append(numbers[i] + cumulative_num[i])

for _ in range(m):
    i, j = map(int, input().split())
    print(cumulative_num[j] - cumulative_num[i-1])