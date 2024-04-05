def solution(my_str, n):
    tmp = []
    for i in range(len(my_str)):
        if i % n == 0 and i != 0:
            tmp.append('.')
        tmp.append(my_str[i])
    
    return ''.join(tmp).split('.')