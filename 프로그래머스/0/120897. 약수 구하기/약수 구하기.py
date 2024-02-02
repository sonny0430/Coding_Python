def solution(n):
    result = []
    for i in range(1, n+1):
        if (n % i) == 0:
            result.append(i)
    return result        

# 컴프리헨션 익히기 [i for i in range(1,n+1) if n%i == 0]