# input : N x M

N, M = map(int, input().split())

data = list()

for i in range(N):
    data.append(list(input()))

min = 64
for i in range(N-7):
    for j in range(M-7):
        tmp1 = 0
        tmp2 = 0
    
        tmp_list = [y for x in data[i:i+8:2] for y in x[j:j+8]]
        tmp1 += sum([a != b for a , b in zip(tmp_list, list('WBWBWBWB')*4)])
        tmp_list = [y for x in data[i+1:i+9:2] for y in x[j:j+8]]
        tmp1 += sum([a != b for a , b in zip(tmp_list, list('BWBWBWBW')*4)])
        
        tmp_list = [y for x in data[i:i+8:2] for y in x[j:j+8]]
        tmp2 += sum([a != b for a , b in zip(tmp_list, list('BWBWBWBW')*4)])
        tmp_list = [y for x in data[i+1:i+9:2] for y in x[j:j+8]]
        tmp2 += sum([a != b for a , b in zip(tmp_list, list('WBWBWBWB')*4)])
        
        if tmp1 <= min: min = tmp1
        if tmp2 <= min: min = tmp2  
    
print(min)
        