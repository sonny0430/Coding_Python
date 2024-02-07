def solution(array, n):
    temp_list = array
    temp_list.append(n)
    temp_list = sorted(temp_list)

    pre_index = temp_list.index(n)-1
    next_index = temp_list.index(n)+1

    if n != max(temp_list) and n!= min(temp_list):
        if abs(temp_list[pre_index]-n) - abs(temp_list[next_index]-n) == 0:
            return temp_list[pre_index]
        elif abs(temp_list[pre_index]-n) > abs(temp_list[next_index]-n):
            return temp_list[next_index]
        else:
            return temp_list[pre_index]
    elif n == max(temp_list):
        return temp_list[pre_index]
    else:
        return temp_list[next_index]