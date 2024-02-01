def solution(my_string):
    temp_string = sorted(filter(lambda x: x.isdigit(), my_string))
    for i in range(0, len(temp_string)):
        temp_string[i] = int(temp_string[i])
    return temp_string