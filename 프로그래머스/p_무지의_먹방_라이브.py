# 무지의 먹방 라이브

# 정확성 만점 코드
def solution(food_times, k):
    if k >= sum(food_times): return -1

    food_index = [i for i in range(1, len(food_times) + 1)]
    food_len = len(food_times)

    while True:
        min_times = min(food_times)
        min_index = list(filter(lambda x: food_times[x] == min_times, range(len(food_times))))
        
        if k > min_times * food_len:
            k -= min_times * food_len
            food_times = [time - min_times for time in food_times]
            for i in reversed(min_index): food_index.pop(i); food_times.pop(i)
            food_len = len(food_index)
        else:
            answer = food_index[k % food_len]
            break
    return answer

# 효율성 챙기기(우선 순위 큐를 이용)
import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1)) # (음식 시간, 음식 번호)
        
    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식의 개수
    
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length # 만약 같은 값을 가지는 음식이 뒤에 있다면 0이 되어 length만 줄어듦.
        length -= 1
        previous = now
    
    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_value) % length][1]
        
        
## test 용

food_times = list(map(int, input().split()))
k = int(input())

food_index = [i for i in range(1, len(food_times) + 1)]
food_len = len(food_times)

if k > sum(food_times): print(-1)

while True:
    min_times = min(food_times)
    min_index = list(filter(lambda x: food_times[x] == min_times, range(len(food_times))))
    if k > min_times * food_len:
        k -= min_times * food_len
        food_times = [time - min_times for time in food_times]
        for i in reversed(min_index): food_index.pop(i); food_times.pop(i)
        food_len = len(food_index)
        print(f'food_index: {food_index}, food_times: {food_times}, min_index: {min_index}')
        print(f'min_times: {min_times}, min_index: {min_index}')
    else:
        answer = food_index[k % food_len] 
        print(f'k%food_len: {k%food_len - 1}')
        print(f'food_index: {food_index}, food_times: {food_times}, min_index: {min_index}')
        print(f'min_times: {min_times}, min_index: {min_index}')
        break

print(answer)