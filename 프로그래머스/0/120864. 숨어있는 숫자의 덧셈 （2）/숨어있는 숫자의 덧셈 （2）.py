def solution(my_string):
    tmp = '0'
    result = 0
    
    for i in range(len(my_string)):
        if my_string[i].isdigit() == True:
            tmp += my_string[i]
            print(9)

        else:
            result += int(tmp)
            tmp = '0'
        
        if i == len(my_string)-1:
            result += int(tmp)
            
    return result        