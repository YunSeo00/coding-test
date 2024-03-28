# 영화감독 숌

number = int(input())

count = 0

for i in range(int(1e9)):
    if '666' in str(i):
        count += 1
    if count == number:
        print(i)
        break