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

# 효율성 챙기기


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