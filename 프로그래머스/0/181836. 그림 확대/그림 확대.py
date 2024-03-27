def solution(picture, k):
    tmp = ''
    tmp2 = []
    result = []

    for i in range(len(picture)):
        for j in picture[i]:
            tmp += j * k
        tmp2.append(tmp)
        tmp = ''

    for i in range(len(tmp2)):
        for j in range(k):
            result.append(tmp2[i])

    return result