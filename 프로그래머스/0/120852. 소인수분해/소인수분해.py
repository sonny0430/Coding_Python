def solution(n):
    result = []
    tmp = n
    i = 2
    cnt = 0

    while tmp != 1:
        if tmp % i == 0:
            result.append(i)
            tmp = tmp // i
            i = 2
        else:
            i += 1

    return sorted(list(set(result)))   