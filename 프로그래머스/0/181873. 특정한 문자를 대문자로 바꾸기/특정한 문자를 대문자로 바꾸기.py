def solution(my_string, alp):
    result = []
    
    for s in my_string:
        result.append(s.upper()) if s == alp else result.append(s)
        
    return ''.join(result)