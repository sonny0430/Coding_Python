def solution(my_string):
    result = ''
    for i in my_string:
        if  ord(i) >= 97:
            result += i.upper()
        else:
            result += i.lower()
    return result