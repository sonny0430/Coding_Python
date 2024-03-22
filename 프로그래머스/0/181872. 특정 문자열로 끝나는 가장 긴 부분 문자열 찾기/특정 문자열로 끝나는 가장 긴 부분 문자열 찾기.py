def solution(myString, pat):
    tmp = []
    tmp2 = myString
    result = []
    for i in range(len(myString)):
        for i in range(1, len(tmp2)):
            tmp.append(tmp2[:i+1])        
        tmp2 = tmp2[1:]

    for i in range(len(tmp)):
        if (tmp[i][(-1) * len(pat):]) == pat:
            result.append(tmp[i])

    return list(sorted(result, key = lambda x: len(x), reverse=True))[0]
