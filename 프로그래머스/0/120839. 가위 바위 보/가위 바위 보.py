def solution(rsp):
    temp_list = []
    for i in rsp:
        if i == '2':
            temp_list.append('0')
        elif i == '0':
            temp_list.append('5')
        else:
            temp_list.append('2')
    return ('').join(temp_list)