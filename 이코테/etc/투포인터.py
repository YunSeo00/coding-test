# 투포인터

# 예제 : 특정한 합을 가지는 부분 연속 수열 찾기
# 1. 시작점(start)과 끝점(end)이 첫 번째 원소의 인덱스(0)를 가리키도록 한다.
# 2. 현재 부분합이 M과 같다면 카운트한다.
# 3. 현재 부분합이 M보다 작으면 end를 1 증가시킨다.
# 4. 현재 부분합이 M보다 크거나 같으면 start를 1 증가시킨다.
# 5. 모든 경우를 확인할 때까지 2번부터 4번까지의 과정을 반복한다.

n = 5
m = 5
data = [1,2,3,2,5]

count = 0
interval_sum = 0
end = 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]
    
print(count)

# 정렬된 두 리스트의 합집합
# 정렬된 2개의 리스트가 입력으로 주어질 때, 두 리스트의 모든 원소를 합쳐서 정렬한 결과를 계산
# 1. 정렬된 리스트 A와 B를 입력받는다.
# 2. 리스트 A에서 처리되지 않은 원소 중 가장 작은 원소를 i가 가리키도록 한다.
# 3. 리스트 B에서 처리되지 않은 원소 중 가장 작은 원소를 j가 가리키도록 한다.
# 4. A[i]와 B[j] 중에서 더 작은 원소를 결과 리스트에 담는다.
# 5. 리스트 A와 B에서 더 이상 처리할 원소가 없을 때까지 2 ~ 4번의 과정을 반복한다.

n, m = 3, 4
a = [1,3,5]
b = [2,4,6,8]

result = [0] * (n+m)
i = 0
j = 0
k = 0

while i < n or j < m:
    if j >= m or (i < n and a[i] <= b[j]):
        result[k] = a[i]
        i += 1
    else:
        result[k] = b[j]
        j += 1
    k += 1

for i in result:
    print(i, end = ' ')