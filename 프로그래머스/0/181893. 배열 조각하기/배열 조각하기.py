def solution(arr, query):
    result = arr

    for i in range(len(query)):
        if i % 2 == 0:
            result = result[:(query[i]+1)]
        elif i % 2 == 1:
            result = result[query[i]:]
    return result
