def solution(s):
    temp_data = s.split(' ')
    result = 0
    pre_data = '0'

    for i in temp_data:
        if i == 'Z':
            result -= int(pre_data)
        else:
            result += int(i)
        pre_data = i
        
    return result