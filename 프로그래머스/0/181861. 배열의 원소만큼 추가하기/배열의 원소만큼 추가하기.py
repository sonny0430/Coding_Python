def solution(arr):
    result = []
    for i in arr:
        for count in range(i):
            result.append(i)
    return result
