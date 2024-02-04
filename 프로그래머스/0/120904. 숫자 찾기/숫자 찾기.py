def solution(num, k):
    for i in list(str(num)):
        if i == str(k):
            return list(str(num)).index(str(k))+1    
    return -1
        