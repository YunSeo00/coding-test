# 1003, dp, silver3, fibonacci

# finbonacci(0) 과 fibonacci(1)이 몇번 호출되는지 출력하는 문제

T = int(input())
N = []

for t in range(T):
    N.append(int(input()))

list0 = [0] * 41
list1 = [0] * 41

list0[0] = 1; list1[0] = 0
list1[0] = 0; list1[1] = 1


for n in range(2,41):
    list0[n] = list0[n-1] + list0[n-2]
    list1[n] = list1[n-1] + list1[n-2]

string = ''

for n in N:
    string += str(list0[n]) + ' ' + str(list1[n]) + '\n'
    
print(string[:-1])