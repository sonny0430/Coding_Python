def solution(strArr):
    tmp = []
    result = []

    for s in strArr:
        tmp.append(len(s))
    
    for i in range(len(set(tmp))):
        result.append(tmp.count(list(set(tmp))[i]))

    return max(result)