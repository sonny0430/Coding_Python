def solution(my_string):
    result = ''
    for i in my_string:
        if  ord(i) >= 97: # 아스키코드 변환
            result += i.upper()
        else:
            result += i.lower()
    return result
