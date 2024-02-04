def solution(my_string):
    temp_list = []

    for i in my_string:
        if i in temp_list:
            pass
        else:
            temp_list.append(i)                   

    return ''.join(temp_list)
