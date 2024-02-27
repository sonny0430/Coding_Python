def solution(myString):
    result = []
    myString = myString.lower()
    for s in myString:
        if s == 'a':
            result.append('A')
        else:
            result.append(s)
    return ''.join(result)