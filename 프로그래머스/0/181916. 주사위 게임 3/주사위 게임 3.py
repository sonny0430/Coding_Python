def solution(a, b, c, d):
    list_data = [a, b, c, d]
    set_data = list(set(list_data))

    if len(set_data) == 1:
        return 1111 * list_data[0]
    
    elif len(set_data) == 2:
        if list_data.count(set_data[0]) == 3:
            return (10 * set_data[0] + set_data[1])**2
        elif list_data.count(set_data[1]) == 3:
            return (10 * set_data[1] + set_data[0])**2
        elif list_data.count(set_data[0]) == 2:
            return ((set_data[0] + set_data[1]) * abs(set_data[0] - set_data[1]))
    
    elif len(set_data) == 3:
        if list_data.count(set_data[0]) == 2:
            return set_data[1] * set_data[2]
        elif list_data.count(set_data[1]) == 2:
            return set_data[0] * set_data[2]
        elif list_data.count(set_data[2]) == 2:
            return set_data[0] * set_data[1]

    elif len(set_data) == 4:
        return min(list_data)