def solution(rsp):
    temp_list = []
    for i in rsp:
        if i == '2':
            temp_list.append('0')
        elif i == '0':
            temp_list.append('5')
        else:
            temp_list.append('2')
    return ('').join(temp_list)
   
                     
# 다른 사람 코드 참고 // ++ 파이썬 문자열 덧셈 가능 (리스트 왜씀)
# def solution(rsp):
#     d = {'0':'5','2':'0','5':'2'}
#     return ''.join(d[i] for i in rsp)