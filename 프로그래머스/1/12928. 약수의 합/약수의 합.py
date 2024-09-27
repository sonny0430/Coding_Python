def solution(n):
    tmp = [i for i in range(1, n+1)]
    return sum(filter(lambda x: (n % x) == 0, tmp))
