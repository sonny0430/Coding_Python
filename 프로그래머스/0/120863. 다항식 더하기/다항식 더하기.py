def solution(polynomial):
    tmp = [0, 0]
    result = ''

    polynomial = polynomial.split(' + ')

    for s in polynomial:
        if s == 'x':
            tmp[0] += 1
        elif 'x' in s:
            s = s.replace('x', '')
            tmp[0] += int(s)
        else:
            tmp[1] += int(s)
    
    if tmp[0] == 1:
        result += 'x'
    elif tmp[0] != 0:
        result += str(tmp[0]) + 'x'

    if tmp[0] != 0 and tmp[1] != 0:
        result += ' + ' + str(tmp[1])
    elif tmp[0] == 0:
        result += str(tmp[1])
        
    return result