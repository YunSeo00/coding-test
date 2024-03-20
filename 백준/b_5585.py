# 거스름돈

money = 1000 - int(input())

result = 0
for i in [500,100,50,10,5,1]:
    result += money // i
    money -= (money // i) * i

print(result)