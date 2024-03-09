def solution(my_string, indices):
    temp_data = []
    for s in my_string:
        temp_data.append(s)
    
    for i in sorted(indices, reverse = True):
        temp_data.pop(i)     

    return ''.join(temp_data)