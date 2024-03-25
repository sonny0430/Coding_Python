def solution(arr, k):
    result = []

    for i in arr:
        if (len(result) < k) and (i not in result):
            result.append(i)
        elif len(result) == k:
            break
    
    while len(result) < k:
        result.append(-1)
    
    return result