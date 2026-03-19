def solution(sizes):
    r = []
    c = []

    for box in sizes:
        temp = sorted(box)
        r.append(temp[0])
        c.append(temp[1])
        
    return sorted(r)[-1] * sorted(c)[-1]
    