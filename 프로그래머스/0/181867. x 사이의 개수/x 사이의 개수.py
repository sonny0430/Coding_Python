def solution(myString):
    temp_data = myString.split('x')
    result = []
    for s in temp_data:
        result.append(len(s))
        
    return result