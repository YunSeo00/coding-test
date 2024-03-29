# Z
# 분할정복, 재귀

n, r, c = map(int, input().split())

count = 0
standard_r = 0
standard_c = 0
for i in reversed(range(n)):
    tmp_length = 2**i
    # 1 사분면
    if r < standard_r + tmp_length and c >= standard_c + tmp_length:
        count += tmp_length * tmp_length
        standard_c += tmp_length
    # 2 사분면
    elif r < standard_r + tmp_length and c < standard_c + tmp_length:
        continue
    # 3 사분면
    elif r >= standard_r + tmp_length and c < standard_c + tmp_length:
        count += tmp_length * tmp_length * 2
        standard_r += tmp_length
    # 4 사분면
    else:
        count += tmp_length * tmp_length * 3
        standard_c += tmp_length
        standard_r += tmp_length

print(count)