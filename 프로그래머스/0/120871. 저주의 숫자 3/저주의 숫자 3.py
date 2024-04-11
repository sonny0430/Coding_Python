def solution(n):
    tmp = list(range(1, 200))

    result = list(filter(lambda x: (x % 3 != 0) and ('3' not in str(x)), tmp))

    return result[n-1]