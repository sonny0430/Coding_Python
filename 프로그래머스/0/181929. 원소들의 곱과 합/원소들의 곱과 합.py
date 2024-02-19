def solution(num_list):
    result_a = 1
    result_b = sum(num_list)**2
    
    for i in num_list:
        result_a *= i
        
    return (1 if result_a < result_b else 0)