def solution(numbers):
    dic = {'one':'1',
           'two':'2',
           'three':'3',
           'four':'4',
           'five':'5',
           'six':'6',
           'seven':'7',
           'eight':'8',
           'nine':'9',
           'zero':'0'}
    
    result = ''
    tmp = ''

    for s in numbers:
        tmp += s

        if tmp in dic.keys():
            result += dic[tmp]
            tmp = ''

    return int(result)