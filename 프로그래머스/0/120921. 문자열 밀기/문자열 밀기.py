def solution(A, B):
    tmp1 = A
    
    for i in range(len(A)):
        if tmp1 == B:
            break
        else:
            tmp1 = tmp1[-1] + tmp1[:-1]
    
    if tmp1 != B:
        return -1
    else:
        return i