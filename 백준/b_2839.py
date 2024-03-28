# 설탕 배달

kg = int(input())

isok = False
for i in reversed(range(kg//5+1)):
    tmp = kg - 5 * i
    if tmp%3 == 0:
        isok = True
        print(i+tmp//3)
        break

if isok == False:
    print(-1)