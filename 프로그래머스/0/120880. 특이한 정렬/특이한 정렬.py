def solution(numlist, n):
    tmp = []
    result = []

    for i in numlist:
        tmp.append(i-n)
    tmp = sorted(tmp)
    result.extend(list(filter(lambda x: x >= 0, tmp)))

    for j in list(filter(lambda x: x < 0, tmp)):        
        for k in range(len(result)):
            if abs(j) < abs(result[k]):
                result.insert(k, j)
                break
            elif k == (len(result)-1):
                result.append(j)
                break

        if result == []:
            result.append(j)
    
    return [p+n for p in result]


# sorted 활용문제
#def solution(numlist, n):
#    answer = sorted(numlist,key = lambda x : (abs(x-n), n-x))
#    return answer