def solution(n):
    result = []
    for i in range(1000):
        result.append(n)
        if n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
        else: 
            return result
