# 문자열 압축

# 내 풀이
def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2 + 1): # 문자열을 자르는 길이는 '길이//2'이다. (그 이후는 의미가 없음.)
        final_text = ""
        pre_text = ""
        text_count = 0
        for j in range(len(s)//i):
            text = s[j*i:(j+1)*(i)]
            if text == pre_text:
                text_count +=1
            else:
                if text_count >= 2:
                    final_text += str(text_count) + pre_text
                else:
                    final_text += pre_text
                text_count = 1
                pre_text = text
            if j == len(s)//i - 1:
                if text_count >= 2:
                    final_text += str(text_count) + pre_text
                else:
                    final_text += pre_text
        if (j+1)*i < len(s):
            final_text += s[(j+1)*i:]
        answer = min(answer, len(final_text))
    return answer

# 다른 사람 풀이
# 배울 점.
# 1. 문제를 풀면서 반복으로 조건을 검사하는 부분을 없앨 방법을 생각하지 못 했는데,
#    리스트 끝에 ['']을 추가해서 이를 해결함.
# 2. 단어를 사전에 짤라서 리스트로 저장해놓고, zip()을 이용해서 비교함.
#    두 개의 작업을 구분해서 간결함과 효율성을 높인 것이 좋았음.

def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",
    'aaaaaa',
]

for x in a:
    print(solution(x))
