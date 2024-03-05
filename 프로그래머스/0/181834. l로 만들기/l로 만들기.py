def solution(myString):
    result = ''
    for s in myString:
        if ord(s) >= 97 and ord(s) < 108:
            result += 'l'
        else:
            result += s
    return result