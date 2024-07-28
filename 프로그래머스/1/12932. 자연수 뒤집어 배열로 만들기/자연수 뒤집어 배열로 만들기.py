def solution(n):
    n = str(n)
    result = [int(n[s]) for s in range(len(n)-1, -1, -1)]
    return result