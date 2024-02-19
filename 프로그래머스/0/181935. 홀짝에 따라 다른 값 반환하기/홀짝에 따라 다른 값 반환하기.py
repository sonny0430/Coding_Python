def solution(n):
    temp_list = list(range(1,n+1))
    result = 0
    
    if n % 2 == 1:
        result = sum(filter(lambda x: x % 2 == 1, temp_list))        
    else:
        temp_list = list(filter(lambda x: x % 2 == 0, temp_list))
        for i in temp_list:
            result += i**2
    return result