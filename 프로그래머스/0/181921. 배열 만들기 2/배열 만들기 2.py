def solution(l, r):
    temp = list(range(l, r+1))
    temp2 = []
    result = []
    for i in temp:
        temp2.append(str(i))

    temp2 = list(filter(lambda x: (('1' not in x) and ('2' not in x) and('3' not in x) and ('4' not in x) and 
                                   ('6' not in x) and ('7' not in x) and('8' not in x) and ('9' not in x)), temp2))
    for s in temp2:
        result.append(int(s))

    return ([-1] if result == [] else result)
