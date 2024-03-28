# 평균

n = int(input())
number = list(map(int, input().split()))

maximum = 0

for i in number:
    maximum = max(maximum, i)

new_number = []

for i in number:
    new_number.append(i/maximum * 100)

print(sum(new_number)/len(new_number))