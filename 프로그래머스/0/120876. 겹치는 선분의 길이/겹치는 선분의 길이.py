def solution(lines):
    tmp1 = []

    for i, j in list(sorted(lines)):
        tmp1.extend(list(range(i, j)))

    tmp2 = list(set(tmp1))
    
    for i in tmp2:
        tmp1.remove(i)

    return len(set(tmp1))