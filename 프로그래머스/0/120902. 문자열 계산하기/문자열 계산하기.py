def solution(my_string):
    tmp1 = 0
    op = ''
    
    tmp = my_string.split(' ')
    result = int(tmp[0])
    
    for i in range(1,len(tmp)):
        if i % 2 == 1:
            op = tmp[i]
        else:
            tmp1 = tmp[i]

            if op == '+':
                result += int(tmp1)
            elif op == '-':
                result -= int(tmp1)
        
    return result