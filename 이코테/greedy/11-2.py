# 곱하기 혹은 더하기
# 풀이 : 0이 아닐 때는 모두 곱하는 것이 가장 큰 수임.

data = input()

result = int(data[0])
for i in data[1:]:
    if result == 0:
        result += int(i)
    else:
        result *= int(i)
        
print(result)