def solution(bin1, bin2):
    tmp1 = ''
    tmp2 = ''
    result = 0

    for i in range(len(bin1)-1,-1,-1):    
        tmp1 += bin1[i]
        
    for j in range(len(bin2)-1,-1,-1):
        tmp2 += bin2[j]


    for b1 in range(len(tmp1)):
        if tmp1[b1] == '1':
            result += 2**(b1)
    print(result)

    for b2 in range(len(tmp2)):
        if tmp2[b2] == '1':
            result += 2**(b2)
    print(result)

    return bin(result)[2:]