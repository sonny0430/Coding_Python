def solution(myStr):
    temp = myStr.split('a')
    temp2 = []
    temp3 = []
    for i in range(len(temp)):
        temp2 += temp[i].split('b')
    
    for i in range(len(temp2)):
        temp3 += temp2[i].split('c')

    if list(filter(lambda x: x != '', temp3)) == []:
        return ['EMPTY']
    else:
        return list(filter(lambda x: x != '', temp3))
    
# 참고   
# def solution(myStr):
#    answer = [x for x in myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split() if x]
#    return answer if answer else ['EMPTY']