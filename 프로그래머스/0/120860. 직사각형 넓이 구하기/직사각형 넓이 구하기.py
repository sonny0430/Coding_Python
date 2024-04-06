def solution(dots):
    tmp1 = []
    tmp2 = []

    for i, j in dots:
        if i not in tmp1:
            tmp1.append(i)
        if j not in tmp2:
            tmp2.append(j)
    
    return abs(tmp1[0] - tmp1[1]) * abs(tmp2[0] - tmp2[1])