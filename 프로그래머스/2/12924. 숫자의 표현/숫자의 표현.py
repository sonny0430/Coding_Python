def solution(n):
    result = 0
    
    for i in range(1, n+1):
        temp = 0
        
        for j in range(i, n+1):
            temp += j
            if temp > n:
                break
            elif temp == n:
                result += 1
            else:
                None

    return result