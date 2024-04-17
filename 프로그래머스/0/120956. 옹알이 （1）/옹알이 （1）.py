def solution(babbling):
    tmp = ["aya", "ye", "woo", "ma"]
    result = []
    tmp2 = 0

    for s1 in babbling:
        for s2 in tmp:
            if s2 in s1:
                s1 = s1.replace(s2, ' ')
        
        result.append(s1)
    
    for s3 in result:
        if s3 == len(s3) * ' ':
            tmp2 += 1
    return tmp2