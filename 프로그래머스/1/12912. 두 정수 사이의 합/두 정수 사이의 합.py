def solution(a, b):
    if a == b:
        return a
    else:
        return sum(list(range(min(a,b),max(a,b)+1)))