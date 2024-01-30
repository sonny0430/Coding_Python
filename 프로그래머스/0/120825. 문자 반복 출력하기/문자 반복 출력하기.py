def solution(my_string, n):
    temp_list = []
    for i in my_string:
        temp_list.append(i*n)
    return ''.join(temp_list)