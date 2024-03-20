def solution(my_string, queries):
    result = []
    temp = ''
    for s in my_string:
        result.append(s)
    
    for s, e in queries:
        temp = result[s:(e+1)]
        result[s:(e+1)] = list(reversed(temp))
    
    return ''.join(result)