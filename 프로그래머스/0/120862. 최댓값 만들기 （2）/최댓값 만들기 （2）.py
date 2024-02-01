def solution(numbers):
    temp_list_up = sorted(numbers, reverse=True)
    temp_list_down = sorted(numbers)
    
    if temp_list_up[0]*temp_list_up[1] >= temp_list_down[0]*temp_list_down[1]:
        return temp_list_up[0]*temp_list_up[1]
    else:
        return temp_list_down[0]*temp_list_down[1]