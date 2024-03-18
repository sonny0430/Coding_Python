def solution(my_string):
    result = []
    for i in range(len(my_string)):
        result.append(my_string)
        my_string = my_string[1:]
    return sorted(result)