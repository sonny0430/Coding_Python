def solution(k, m, score):
    goods = sorted(score, reverse=True)
    
    temp_all = []
    temp = []
    
    for i in goods:
        if len(temp) == m-1:
            temp.append(i)
            temp_all.append(temp)
            temp = []
        else:
            temp.append(i)
            
    result = 0        
    for l in temp_all:
        result += min(l) * m
    
    return result
