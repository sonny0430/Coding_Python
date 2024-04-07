def solution(spell, dic):
    result = 0
    
    for s1 in dic:
        tmp = 0
        for s2 in spell:
            if s2 in s1:
                tmp += 1

        if tmp == len(spell):
            return 1
        
    return 2    