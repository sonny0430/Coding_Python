def solution(num_list):
    result = []
    temp = 0
    cnt = 0
    for i in num_list:
        temp = i
        for j in range(i):
            if temp == 1:
                result.append(cnt)
                break
            elif temp % 2 == 1:
                cnt += 1
                temp = (temp - 1) // 2
            elif temp % 2 == 0:
                cnt += 1
                temp = temp // 2
        cnt = 0
    return sum(result)

#    for n in num_list:
#        while n != 1:
#            n //= 2
#            answer += 1