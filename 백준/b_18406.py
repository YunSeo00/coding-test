# 럭키 스트레이트

number = input()
length = len(number)

if sum(list(map(int, list(number[:int(length/2)])))) == sum(list(map(int, list(number[int(length/2):])))):
    print("LUCKY")
else:
    print("READY")