# 팰린드롬수

while True:
    number = input()
    if number == '0':
        break
    length = len(number)
    status = True
    for i in range(length//2):
        if number[i] != number[-i-1]:
            status = False
            break
    print('yes' if status else 'no')