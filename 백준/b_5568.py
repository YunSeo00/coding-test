# 카드 놓기
# *** 완전 탐색 (dfs)
# *** todo - 다시 풀어보기 + 내가 풀었던 풀이 다시보고 
# *** todo - 이어서 풀어보기 : 15566

n = int(input())
k = int(input())

cards = [int(input()) for _ in range(n)]

visited = [0] * n
stack = []
numbers = set()

def dfs(depth):
    if depth == k:
        numbers.add(''.join(map(str, stack)))
        return 
    for i in range(n):
        if visited[i]:
            continue
        stack.append(cards[i])
        visited[i] = 1
        dfs(depth+1)
        stack.pop()
        visited[i] = 0 

dfs(0)

print(len(numbers))


# 실패한 풀이 1
# def find_card(i, stack, visited):
#     print(stack, visited)
#     for i in range(n):
#         if visited[i] == 0:
#             stack.append(str(cards[i]))
#             if len(stack) == k:
#                 if int(''.join(stack)) not in numbers:
#                     numbers.append(int(''.join(stack)))
#                     print(numbers)
#                 stack.pop()
#                 continue
#             else:
#                 visited[i] = 1
#                 stack, visited = find_card(i, stack, visited)
#                 visited[i] = 0
#     return stack, visited

# for i in range(n):
#     print('i: ', i)
#     stack = []
#     visited = [0] * n
#     stack.append(str(cards[i]))
#     if len(stack) == k:
#         if int(''.join(stack) not in numbers):
#             numbers.append(int(''.join(stack)))
#         continue
#     else:
#         visited[i] = 1
#         stack, visited = find_card(i, stack, visited)

# print(len(numbers))


# 실패한 풀이 2

# def find_card(num, candidate, stack):
#     print(stack, candidate)
#     candidate.pop(candidate.index(num))
    
#     for p_num in candidate:
#         stack.append(str(p_num))
#         if len(stack) == k:
#             if int(''.join(stack)) not in numbers:
#                 numbers.append(int(''.join(stack)))
#                 print(numbers)
#             stack.pop()
#             continue
#         else:
#             candidate, stack = find_card(p_num, candidate, stack)
#     stack.pop()
#     return candidate, stack

        
# for num in cards:
#     print('i: ', num)
#     candidate = cards[:]
#     stack = []
#     stack.append(str(num))
#     if len(stack) == k:
#         if int(''.join(stack)) not in numbers:
#             numbers.append(''.join(stack))
#         continue
#     else:
#         candidate, stack = find_card(num, candidate, stack)


# print(len(numbers))

