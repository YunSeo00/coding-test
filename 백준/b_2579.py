# 계단 오르기 (todo: 해결 못 함.)

# 반례1 (거꾸로 하면 안 되고 앞에서부터 보면 됨.)
# 10
# 3 5 10 9 2 1 2 5 2 9
# 37 (3 10 9 1 5 9)

# 반례2 (앞에서부터 보면 안 되고 뒤에서부터 보면 됨.)
# -> 이건 시작 점을 2부터 할 수 있는 경우를 예외처리 안 시켜줘서 그런 것 같음.
# 7
# 1 8 7 3 7 3 8

# => 무조건 마지막 계단을 밟아야 하니까 뒤에서부터 보는게 맞을 것 같은데 왜 반례1이 안 되는 건지 생각이 안 남.



n = int(input())
stair = []
for _ in range(n):
    stair.append(int(input()))

dp = [0] * (n)
step1 = False
for i in reversed(range(len(stair))):
    print(dp)
    print(step1)
    if i == n-1:
        dp[n-1] = stair[n-1]
        continue
    if i == n-2:
        dp[n-2] = stair[n-1] + stair[n-2]
        step1= True
        continue
    
    if step1 == True:
        dp[i] = max(dp[i+1], dp[i+2]+stair[i])
        step1 = False
    else:
        if dp[i+1] > dp[i+2]:
            step1 = True
            dp[i] = dp[i+1] + stair[i]
        else: 
            # 만약 둘이 같다면 2칸 건너뛰어야 함. (둘의 값이 같다 = i+2에서 건너뛰었다.)
            dp[i] = dp[i+2] + stair[i]

print(dp[0])

# for i in range(len(stair)):
#     if i == 0:
#         dp[0] = stair[0]
#         continue
#     if i == 1:
#         dp[1] = stair[1] + stair[0]
#         step1= True
#         continue

#     if step1 == True:
#         dp[i] = max(dp[i-1], dp[i-2]+stair[i])
#         step1 = False
#         if i == n-1:
#             dp[i] = dp[i-2] + stair[i]
#     else:
#         if dp[i-1] > dp[i-2]:
#             step1 = True
#             dp[i] = dp[i-1] + stair[i]
#         else: 
#             # 만약 둘이 같다면 2칸 건너뛰어야 함. (둘의 값이 같다 = i+2에서 건너뛰었다.)
#             dp[i] = dp[i-2] + stair[i]
    
# print(dp[n-1])