def solution(score):
    tmp1 = []
    tmp2 = []
    result = []

    for i, j in score:
        tmp1.append((i+j)/2)        

    tmp2 = sorted(tmp1, reverse=True)

    for k in tmp1:
        result.append(tmp2.index(k)+1)
        
    return result