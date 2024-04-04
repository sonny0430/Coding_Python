def solution(quiz):
    result = []
    tmp = []

    for i in range(len(quiz)):
        tmp = quiz[i].replace(' - ', ' -').replace('--', '').replace(' + ', ' ').replace(' = ', ' ').split(' ')
        
        if (int(tmp[0]) + int(tmp[1])) == int(tmp[2]):
            result.append('O')
        else:
            result.append('X')

    return result