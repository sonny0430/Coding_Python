def solution(code):
    mode = 0
    ret = ''
    for i in range(len(code)):
        if (code[i].isdigit() == True) and (mode == 0):
            mode = 1
        elif (code[i].isdigit() == True) and (mode == 1):
            mode = 0
        
        elif (code[i].isdigit() == False) and (mode == 0) and (i % 2 == 0):
            ret += code[i]
        elif (code[i].isdigit() == False) and (mode == 1) and (i % 2 == 1):
            ret += code[i]
    if ret == '':
        return "EMPTY"
    else:
        return ret