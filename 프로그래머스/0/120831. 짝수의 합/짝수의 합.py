def solution(n):
    result = []
    for i in range(n+1):
        if i % 2 == 0:
            result.append(i)
    return sum(result)

# def solution(n):
#     return sum([i for i in range(2, n + 1, 2)])