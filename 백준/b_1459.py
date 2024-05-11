# 걷기

x, y, w, s = map(int, input().split())

if 2 * w < s:
    print((x+y)*w)
else:
    if w < s:
        print(min(x, y) * s + abs(x-y) * w)
    else:
        print(min(x, y) * s + (abs(x-y)-abs(x-y)%2) * s + abs(x-y)%2 * w)
