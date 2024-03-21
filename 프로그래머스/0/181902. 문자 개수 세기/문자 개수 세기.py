def solution(my_string):
    temp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    result = [0 for _ in range(52)]

    for i in range(len(temp)):
        if temp[i] in my_string:
            result[i] = my_string.count(temp[i])

    return result