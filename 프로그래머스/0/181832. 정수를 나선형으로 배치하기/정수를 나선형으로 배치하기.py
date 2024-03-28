def solution(n):
    tmp = [[0 for _ in range(n)] for _ in range(n)]
    tmp2 = list(range(1, n**2 + 1))

    state = 0
    cnt = 0
    step = 0

    while cnt < n**2:
        for i in range(n):
            if state == 0 and tmp[0+step][i] == 0:
                tmp[0+step][i] = tmp2[cnt]
                cnt +=1 
            
            elif state == 1 and tmp[i][n-1-step] == 0:
                tmp[i][n-1-step] = tmp2[cnt]
                cnt += 1

            elif state == 2 and tmp[n-1-step][(-1)*(i+1)] == 0:
                tmp[n-1-step][(-1)*(i+1)] = tmp2[cnt]
                cnt += 1
            
            elif state == 3 and tmp[(-1)*(i+1)][0+step] == 0:
                tmp[(-1)*(i+1)][0+step] = tmp2[cnt]
                cnt += 1

        if state == 3:
            state = 0
            step += 1
        else:
            state += 1

    return tmp