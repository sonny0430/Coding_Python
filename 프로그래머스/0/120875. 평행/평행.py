def solution(dots):
    tmp1 = [(dots[1][1]-dots[0][1]) / (dots[1][0]-dots[0][0]),
             (dots[2][1]-dots[0][1]) / (dots[2][0]-dots[0][0]),
             (dots[3][1]-dots[0][1]) / (dots[3][0]-dots[0][0])]
    
    tmp2 = [(dots[3][1]-dots[2][1]) / (dots[3][0]-dots[2][0]),
             (dots[3][1]-dots[1][1]) / (dots[3][0]-dots[1][0]),
             (dots[2][1]-dots[1][1]) / (dots[2][0]-dots[1][0])]

    for i in range(len(tmp1)):
        if tmp1[i] == tmp2[i]:
            return 1

    return 0