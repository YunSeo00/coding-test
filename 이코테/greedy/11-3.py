# 문자열 뒤집기
# 풀이: 가장 작은 세트를 뒤집는 방법은 가장 첫 번째 나온 숫자가 아닌 숫자의 세트를 뒤집는 것임.
# 이를 for문 없이 하기 위해 가장 첫 번째 나온 숫자를 이용해서 split을 하고 빈 문자열이 아닌 문자열의 개수를 셈.
# 근데 그냥 하나하나 비교하는게 더 빠름. (for문을 안 쓴다고 좋은 것이 아님.)

import time

# 내 풀이
data = input()
st = time.time()
start_str = data[0]
split_data = data.split(start_str)
result = len(split_data) - split_data.count('')
print(result)
print(f'time : {time.time() - st}')

# 기존 답안
data = input()
st = time.time()
count0 = 0
count1 = 0
if data[0] == '1':
    count0 += 1
else:
    count1 += 1
    
for i in range(len(data) - 1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))
print(f'time : {time.time() - st}')



