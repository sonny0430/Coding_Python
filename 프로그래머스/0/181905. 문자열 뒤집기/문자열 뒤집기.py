def solution(my_string, s, e):
    temp_data = []
    result = []
    for i in range(len(my_string)):
        if i >= s and i < e:
            temp_data.append(my_string[i])
        elif i == e:
            temp_data.append(my_string[i])
            result.extend(reversed(temp_data))
        else:
            result.append(my_string[i])

    return ''.join(result)

# 헉
#def solution(my_string, s, e):
#    return my_string[:s] + my_string[s: e + 1][::-1] + my_string[e + 1:]