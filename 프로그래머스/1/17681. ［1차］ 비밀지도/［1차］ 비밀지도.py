def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        x = bin(arr1[i] | arr2[i])[2:]
        
        if len(x) <= n:
            x = '0'*(n-len(x)) + x
                
        answer.append(x.replace('1', '#').replace('0', ' '))
    
    return answer