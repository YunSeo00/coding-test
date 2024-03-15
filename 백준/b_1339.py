# 단어 수학
# 접근1: 가장 큰 자리수에 있는 알파벳에 큰 수가 들어가도록 (X)
# 접근2: 가장 큰 자리수, 가장 짧은 단어부터 살펴보면서 큰 수 할당 (X)
# 접근3: 각 자리수의 더해지는 것을 누적해서 정리하고 이를 이용해서 마지막에 숫자 할당.

# 접근2 코드
# N = int(input())
# words = []
# for _ in range(N):
#     words.append(input())

# alphabet_dict = {}
# words.sort(key=lambda x: len(x), reverse=True)
# for i in reversed(range(len(words[0]))):
#     for j in reversed(range(N)):
#         if i < len(words[j]):
#             if words[j][len(words[j])-i-1] in alphabet_dict:
#                 pass
#             else:
#                 alphabet_dict[words[j][len(words[j])-i-1]] = min(alphabet_dict.values(), default=10) - 1

# nums = []
# for word in words:
#     word_to_num = ''
#     for i in range(len(word)):
#         word_to_num += str(alphabet_dict[word[i]])
#     nums.append(int(word_to_num))

# result = sum(nums)
# print(result)
        
        
# 접근3 코드
N = int(input())
words = []
alphabet_dict = {}

for _ in range(N):
    word = input()
    words.append(word)
    digit = len(word) + 1
    for w in word:
        if w in alphabet_dict:
            alphabet_dict[w] += 10 ** (digit)
        else:
            alphabet_dict[w] = 10 ** (digit)
        digit -= 1

alphabet_dict = sorted(alphabet_dict.items(), key=lambda x : x[1], reverse=True)
num_dict = {alphabet_dict[i][0]: 9-i for i in range(len(alphabet_dict))}

nums = []
for word in words:
    word_to_num = ''
    for w in word:
        word_to_num += str(num_dict[w])
    nums.append(int(word_to_num))
    
result = sum(nums)
print(result)