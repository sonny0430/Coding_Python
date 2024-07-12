def solution(name, yearning, photo):
    result = []

    for l1 in photo:
        temp = 0
        for l2 in l1:
            try:
                temp += yearning[name.index(l2)]
            except:
                pass
        
        result.append(temp)
        
    return result