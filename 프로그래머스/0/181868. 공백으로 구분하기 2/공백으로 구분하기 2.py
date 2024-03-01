def solution(my_string):
    result = []

    for i in my_string.split(' '):
        if i != '':
            result.append(i)

    return result